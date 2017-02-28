"""
Generate build manual images.

1. set last view tab to the wanted rendering mode
   (as ViewDisplayMode is not implemented in Python)
2. make Rhino viewport square for ZoomExtents to work best

"""

import os
import shutil
import rhinoscriptsyntax as rs

import utils
reload(utils)

import config
reload(config)
conf = config.conf


# docpath = rs.DocumentPath()
# docdir, docname = os.path.split(docpath)

thislocation = os.path.dirname(os.path.realpath(__file__))
outputdir = os.path.join(conf['outputdir'], 'img')

views = rs.ViewNames()   # ['Left', 'Front', 'Top', 'Perspective']



def clear_img_dir():
    print "clearing: %s" % (outputdir)
    if os.path.exists(outputdir):
        shutil.rmtree(outputdir)


def create_view_image(name, w=1600, h=900):
    imgfile = os.path.join(outputdir, name)
    if not os.path.exists(outputdir):
        os.makedirs(outputdir)
    rs.Command("_-ViewCaptureToFile " + imgfile + " Width="+str(w)+" Height="+str(h)+" Scale=1 DrawingGrid=No DrawWorldAxes=No DrawCPlaneAxes=No TransparentBackground=Yes _Enter")
    # was unable to generate shaded view with CreatePreviewImage
    # rs.CreatePreviewImage(imgfile, view="Perspective", size=[1000,2000], flags=0, wireframe=False)
    print "Image generated: " + imgfile


def create_image_set(stepnumeral, w,h):
    rs.RestoreNamedView(conf['persp_view'])
    rs.ZoomExtents()
    create_view_image(conf['step_img_persp'] % stepnumeral, w,h)
    rs.RestoreNamedView(conf['top_view'])
    rs.ZoomExtents()
    create_view_image(conf['step_img_top'] % stepnumeral, w,h)
    rs.RestoreNamedView(conf['front_view'])
    rs.ZoomExtents()
    create_view_image(conf['step_img_front'] % stepnumeral, w,h)
    rs.RestoreNamedView(conf['right_view'])
    rs.ZoomExtents()
    create_view_image(conf['step_img_right'] % stepnumeral, w,h)


def get_manual_named_views():
    views = rs.NamedViews()
    for view in views:
        if len(view) > 2 and view[1] == '.':
            print view
    # rs.RestoreNamedView(views[0])





def generate_step_images(structure):
    global view_aspect
    w_l = conf['step_img_width']
    h_l = int(w_l/view_aspect)
    rs.CurrentLayer("Default")
    utils.show_blocks()
    utils.show_subsystems()
    rs.ZoomExtents()
    utils.hide_subsystems()
    utils.hide_non_subsystems()

    for iSub in xrange(len(structure)):
        subsystem = structure.keys()[iSub]
        v = structure[subsystem]
        if subsystem in conf['build_apart']:
            utils.hide_subsystems()
        rs.LayerVisible(subsystem, True)
        # utils.hide_non_subsystems()
        utils.hide_children(subsystem)
        for iStep in xrange(len(v)):
            step = v.keys()[iStep]
            vv = v[step]
            stepnumeral = str(iSub+1)+'.'+str(iStep+1)
            rs.LayerVisible(step, True)
            rs.UnselectAllObjects()
            rs.ObjectsByLayer(step, True)
            # create images
            create_image_set(stepnumeral, w_l,h_l)
        if subsystem in conf['build_apart']:
            # show all previous subsystems again
            rs.UnselectAllObjects()
            rs.InvertSelectedObjects()
            for sub in structure.keys():
                rs.LayerVisible(sub, True)
                if sub == subsystem:
                    break
            # images for subsystem installed
            finnumeral = str(iSub+1)+'.'+str(len(v)+1)
            create_image_set(finnumeral, w_l,h_l)
    # subsystem overview images
    for iSub in xrange(len(structure)):
        subsystem = structure.keys()[iSub]
        rs.UnselectAllObjects()
        # select subsystem and its step layers
        for child in rs.LayerChildren(subsystem):
            rs.ObjectsByLayer(child, True)
        finnumeral = str(iSub+1)+'.0'
        create_image_set(finnumeral, w_l,h_l)



def generate_part_images(structure):
    global view_aspect
    w_l = conf['part_img_width']
    h_l = int(w_l/view_aspect)

    for iSub in xrange(len(structure)):
        subsystem = structure.keys()[iSub]
        v = structure[subsystem]
        utils.show_only(subsystem)
        utils.hide_children(subsystem)
        for iStep in xrange(len(v)):
            step = v.keys()[iStep]
            vv = v[step]
            stepnumeral = str(iSub+1)+'.'+str(iStep+1)
            rs.LayerVisible(step, True)
            for partkind,vvv in vv.items():
                rs.HideObjects(vvv)
            for partkind,vvv in vv.items():
                if len(vvv) >= 1:
                    part = vvv[0]
                    rs.ShowObject(part)
                    # create images
                    rs.RestoreNamedView(conf['persp_view'])
                    rs.ZoomExtents()
                    create_view_image(conf['part_img_persp'] % (stepnumeral,partkind), w_l,h_l)
                    rs.RestoreNamedView(conf['top_view'])
                    rs.ZoomExtents()
                    create_view_image(conf['part_img_top'] % (stepnumeral,partkind), w_l,h_l)
                    rs.RestoreNamedView(conf['front_view'])
                    rs.ZoomExtents()
                    create_view_image(conf['part_img_front'] % (stepnumeral,partkind), w_l,h_l)
                    rs.RestoreNamedView(conf['right_view'])
                    rs.ZoomExtents()
                    create_view_image(conf['part_img_right'] % (stepnumeral,partkind), w_l,h_l)
                    #
                    rs.HideObject(part)
            for partkind,vvv in vv.items():
                rs.ShowObject(vvv)
            rs.LayerVisible(step, False)
        # utils.show_children(subsystem)
        utils.show_step_children(subsystem)
    utils.show_blocks()
    utils.show_subsystems()
    rs.ZoomExtents()



clear_img_dir()
# get CAD file structure
structure = utils.get_structure()
utils.structure_to_file(structure)
# set up view
rs.CurrentView(rs.ViewNames()[-1])  # typ "Perspective" on 4th tab
view_to_restore = rs.CurrentView()
size = rs.ViewSize()
view_aspect = size[0]/float(size[1])
# generate images
generate_part_images(structure)
generate_step_images(structure)
# restore view
rs.CurrentView(view_to_restore)
