import os
import json
import collections
import rhinoscriptsyntax as rs

import utils
reload(utils)


docpath = rs.DocumentPath()
docdir, docname = os.path.split(docpath)
# outdir = os.path.join(docdir, "export_step")
outdir = os.path.join("E:\lasersaur_stuff", "export_step")
                   

def structure_to_file(structure):
    struc = collections.OrderedDict()
    for subsystem,v in structure.items():
        struc[subsystem] = collections.OrderedDict()
        for step,vv in v.items():
            struc[subsystem][step] = collections.OrderedDict()
            for partkind,vvv in vv.items():
                struc[subsystem][step][partkind] = len(vvv)

    with open(os.path.join(outdir,"structure.json"), 'w') as fp:
        json.dump(struc,fp)
        

def export(structure):
    # create output dir if not exists
    if not os.path.exists(outdir):
        print "creating output dir: " + outdir
        os.makedirs(outdir)

    rs.CurrentLayer("Default")
    utils.show_blocks()
    utils.show_subsystems()
    rs.ZoomExtents()
    utils.hide_subsystems()
    utils.hide_non_subsystems()                        
    for subsystem,v in structure.items():
        utils.show_only(subsystem)
        for step,vv in v.items():
            for partkind,vvv in vv.items():
                rs.UnselectAllObjects()
                rs.SelectObjects(vvv)
                filename = utils.get_part_filename(subsystem,utils.get_layer_tail(step),partkind)
                outpath = os.path.join(outdir, filename)
                print "exporting step file: " + outpath
                rs.Command("_-Export " + outpath + " Schema=AP214AutomotiveDesign ExportParameterSpaceCurves=Yes LetImportingApplicationSetColorForBlackObjects=Yes _Enter")


structure = utils.get_structure()
export(structure)
# write file with structure
structure_to_file(structure)
