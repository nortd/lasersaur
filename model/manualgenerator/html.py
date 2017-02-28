import os
import json
import glob
import shutil
import collections

import config
reload(config)
conf = config.conf


thislocation = os.path.dirname(os.path.abspath(__file__))

# hack
conf['outputdir'] = '/home/noema/Shared/lasersaur_stuff/manual'


def get_text_index():
    tfile = 'text/index.html'
    if os.path.exists(tfile):
        with open(tfile) as fp:
            template = fp.read()
        return template
    else:
        return ''

def get_text_subsystem(subsystem):
    tfile = 'text/%s.html' % subsystem
    if os.path.exists(tfile):
        with open(tfile) as fp:
            template = fp.read()
        return template
    else:
        return ''

def get_text_step(stepnumeral):
    tfile = 'text/%s.html' % stepnumeral
    if os.path.exists(tfile):
        with open(tfile) as fp:
            template = fp.read()
        return template
    else:
        return ''


def index(structure):
    html = []
    html.append('<ul class="list-inline">')
    for iSub in xrange(len(structure)):
        subsystem = structure.keys()[iSub]
        v = structure[subsystem]
        # html.append('<div class="container-fluid" style="width:340px">')
        html.append('<li>')
        html.append('<div class="panel panel-default">')
        html.append('<div class="panel-heading">')
        html.append('<h3 class="panel-title">%s</h3>' % (subsystem))
        html.append('</div>')
        html.append('<div class="panel-body">')
        sub_file = subsystem+'.html'
        img_persp = conf['step_img_persp_low'] % (str(iSub+1)+'.0')
        html.append('<a href="%s"><img src="img/%s" width="%spx"></a>' % (sub_file, img_persp, conf['step_img_width_low']))
        html.append('</div>')
        html.append('</div>')
        # html.append('</div>')
        # html.append('<ul class="list-inline">')
        # for iStep in xrange(len(v)):
        #     step = v.keys()[iStep]
        #     vv = v[step]
        #     stepnumeral = str(iSub+1)+'.'+str(iStep+1)
        #     step_file = conf['step_file_pat'] % stepnumeral
        #     html.append('<li><a href="%s" class="btn btn-info btn-xs">%s</a></li>' % (step_file,stepnumeral))
        # if subsystem in conf['build_apart']:
        #     stepnumeral = str(iSub+1)+'.'+str(len(v)+1)
        #     step_file = conf['step_file_pat'] % stepnumeral
        #     html.append('<li><a href="%s" class="btn btn-info btn-xs">%s</a></li>' % (step_file,stepnumeral))
        # html.append('</ul>')
        html.append('</li>')
    html.append('</ul>')
    text = get_text_index()
    if text:
        html.append('<div class="row"><div class="col-md-6" style="padding-bottom:50px">')
        html.append(text)
        html.append('</div></div>')
    # apply template
    with open('template.html') as fp:
        template = fp.read()
    first_step_file = conf['step_file_pat'] % ('1.1')
    header = '<h1><a href="%s" class="btn btn-primary btn-lg">Start building your Lasersaur</a> <button type="button" class="btn btn-xs btn-default" disabled="disabled">%s</button></h1>' % (first_step_file, conf['version'])
    html = template % {'title':conf['main_header'],
                       'header':header,
                       'content':"".join(html),
                       'footer':conf['main_header'],
                       'container_style':''}
    # write file
    with open(os.path.join(conf['outputdir'], 'index.html'), 'w') as fp:
        fp.write("".join(html))



def subsystems(structure):
    def sub_page(stepnumeral):
        step_file = conf['step_file_pat'] % stepnumeral
        img_persp = conf['step_img_persp_thumb'] % stepnumeral
        content.append('<li>')
        content.append('<div class="panel panel-default">')
        content.append('<div class="panel-heading">')
        content.append('<h3 class="panel-title">step %s</h3>' % (stepnumeral))
        content.append('</div>')
        content.append('<div class="panel-body">')
        content.append('<a href="%s"><img src="img/%s" width="%spx"></a>' % (step_file, img_persp, conf['step_img_width_thumb']))
        content.append('</div>')
        content.append('</div>')
        content.append('</li>')

    for iSub in xrange(len(structure)):
        subsystem = structure.keys()[iSub]
        v = structure[subsystem]
        prevlink = 'dummy'
        nextlink = 'dummy'
        nav = []
        nav.append('<ul class="list-inline">')
        nav.append('<li style="margin-right:40px; padding-right:0"><a href="index.html" class="btn btn-default btn-lg">index</a></li>')
        nav.append('<li><a class="btn btn-default btn-lg" disabled="disabled">%s</a></li>' % (subsystem.split('.')[-1]))
        firststep_link = conf['step_file_pat'] % (str(iSub+1)+'.1')
        nav.append('<li><a href="%s" class="btn btn-primary btn-lg">start</a></li>' % (firststep_link))
        nav.append('</ul>')
        content = []
        content.append('<ul class="list-inline">')
        for iStep in xrange(len(v)):
            step = v.keys()[iStep]
            vv = v[step]
            stepnumeral = str(iSub+1)+'.'+str(iStep+1)
            sub_page(stepnumeral)
        if subsystem in conf['build_apart']:
            # subassembly installation step
            stepnumeral = str(iSub+1)+'.'+str(len(v)+1)
            sub_page(stepnumeral)
        content.append('</ul>')
        content.append(get_text_subsystem(subsystem))
        # apply template
        with open('template.html') as fp:
            template = fp.read()
        html = template % {'title':conf['main_header'],
                           'header':"".join(nav),
                           'content':"".join(content),
                           'footer':conf['main_header'],
                           'container_style':''}
        # write file
        with open(os.path.join(conf['outputdir'], subsystem+'.html'), 'w') as fp:
            fp.write(html)



def steps(structure):
    """Generate steps pages from structure.

    The structure is a hierarchy with the subystems on top.
    Dictionaries are ordered.
    struct = {
        subsystem1 = {
            buildstep1 = {
                partkind1 = [obj1, obj2, ...]
                partkind2 = []
            },
            buildstep2 = {}
        },
        subsystem2 = {}
    }
    """
    def step_page(structure, iSub, iStep, vv=None):
        stepnumeral = str(iSub+1)+'.'+str(iStep+1)
        # prev link
        if iStep > 0:
            prevfile = conf['step_file_pat'] % (str(iSub+1)+'.'+str(iStep))
        else:
            if iSub > 0:
                prevsubsystem = structure.keys()[iSub-1]
                if prevsubsystem in conf['build_apart']:
                    steps_prev_sub = len(structure[structure.keys()[iSub-1]])+1
                else:
                    steps_prev_sub = len(structure[structure.keys()[iSub-1]])
                prevfile = conf['step_file_pat'] % (str(iSub)+'.'+str(steps_prev_sub))
                # subsystem = structure.keys()[iSub]
                # prevfile = subsystem+'.html'
            else:
                prevfile = 'index.html'
        prevlink = '<a href="%s" class="btn btn-default btn-lg"><span class="glyphicon glyphicon-arrow-left" aria-hidden="true"></span></a>' % (prevfile)
        # next link
        subsystem = structure.keys()[iSub]
        if subsystem in conf['build_apart']: nSteps = len(v)+1
        else: nSteps = len(v)
        #
        if iStep+1 < nSteps:
            nextfile = conf['step_file_pat'] % (str(iSub+1)+'.'+str(iStep+2))
        else:
            if iSub+1 < len(structure):
                nextfile = conf['step_file_pat'] % (str(iSub+2)+'.1')
                # nextsubsystem = structure.keys()[iSub+1]
                # nextfile = nextsubsystem+'.html'
            else:
                nextfile = 'index.html'
        nextlink = '<a href="%s" class="btn btn-default btn-lg"><span class="glyphicon glyphicon-arrow-right" aria-hidden="true"></span></a>' % (nextfile)
        # assemble nav buttons
        nav = []
        nav.append('<ul class="list-inline" style="margin-left:10px">')
        nav.append('<li style="margin-right:40px"><a href="%s.html" class="btn btn-default btn-lg">%s</a></li>' % (subsystem, subsystem.split('.')[-1]))
        nav.append('<li>%s</li>' % (prevlink))
        nav.append('<li><a class="btn btn-default btn-lg" disabled="disabled">step %s</a></li>' % (stepnumeral))
        nav.append('<li>%s</li>' % (nextlink))
        nav.append('</ul>')
        content = []
        with open('carousel.html') as fp:
            carousel = fp.read()
        carousel = carousel % {'imgurl1':'img/%s' % conf['step_img_persp'] % (stepnumeral),
                               'imgurl2':'img/%s' % conf['step_img_top'] % (stepnumeral),
                               'imgurl3':'img/%s' % conf['step_img_front'] % (stepnumeral),
                               'imgurl4':'img/%s' % conf['step_img_right'] % (stepnumeral)}
        content.append(carousel)
        content.append('<div class="row" style="margin:0">')
        content.append('<div class="col-md-6" style="padding:0">')
        if vv is not None:
            content.append('<table class="table table-striped">')
            for partkind,vvv in vv.items():
                content.append('<tr>')
                content.append('<td>%sx</td>' % (vvv))
                partimg = conf['part_img_persp_thumb'] % (stepnumeral,partkind)
                content.append('<td><img src="img/%s" width="%s"></td>' % (partimg, conf['part_img_width_thumb']))
                content.append('<td>%s</td>' % (partkind))
                content.append('</tr>')
            content.append('</table>')
        content.append('</div>')
        text = get_text_step(stepnumeral)
        if text:
            content.append('<div class="col-md-6">')
            # content.append('<h2>Concerning the entire subsystem:</h2>')
            content.append(text)
            content.append('</div>')
        content.append('</div>')
        step_file = conf['step_file_pat'] % stepnumeral
        # apply template
        with open('template.html') as fp:
            template = fp.read()
        html = template % {'title':conf['main_header'],
                           'header':"".join(nav),
                           'content':"".join(content),
                           'footer':conf['main_header'],
                           'container_style':'padding-left:0; padding-right:0'}
        # write output
        with open(os.path.join(conf['outputdir'], step_file), 'w') as fp:
            fp.write(html)

    for iSub in xrange(len(structure)):
        subsystem = structure.keys()[iSub]
        v = structure[subsystem]
        for iStep in xrange(len(v)):
            step = v.keys()[iStep]
            vv = v[step]
            # nav buttons
            # prev link
            step_page(structure, iSub, iStep, vv)
        if subsystem in conf['build_apart']:
            # subassembly installation step
            step_page(structure, iSub, len(v))



def resize_images():
    import Image
    def _imgresize(src, w, suffix='_thumb'):
        # dst to match part_img_persp_thumb
        image = Image.open(src)
        h = int((float(w)/image.size[0])*image.size[1])
        image = image.resize((w,h), Image.ANTIALIAS)
        dst = src[:src.rfind('.')]+suffix+src[src.rfind('.'):]
        image.save(dst)
        print "image resized: %s" % dst

    cwd_temp = os.getcwd()
    os.chdir(os.path.join(conf['outputdir'], 'img'))

    ### part image tumbs
    width = conf['part_img_width_thumb']
    # persp
    file_list = glob.glob(conf['part_img_persp'] % ('*.*', '*'))
    for src in  file_list:
        _imgresize(src, width)
    # # top
    # file_list = glob.glob(conf['part_img_top'] % ('*.*', '*'))
    # for src in  file_list:
    #     _imgresize(src, width)
    # # front
    # file_list = glob.glob(conf['part_img_front'] % ('*.*', '*'))
    # for src in  file_list:
    #     _imgresize(src, width)
    # # right
    # file_list = glob.glob(conf['part_img_right'] % ('*.*', '*'))
    # for src in  file_list:
    #     _imgresize(src, width)

    ### step image tumbs
    width = conf['step_img_width_thumb']
    # persp
    file_list = glob.glob(conf['step_img_persp'] % ('*.*'))
    for src in  file_list:
        _imgresize(src, width)
    # # top
    # file_list = glob.glob(conf['step_img_top'] % ('*.*'))
    # for src in  file_list:
    #     _imgresize(src, width)
    # # front
    # file_list = glob.glob(conf['step_img_front'] % ('*.*'))
    # for src in  file_list:
    #     _imgresize(src, width)
    # # right
    # file_list = glob.glob(conf['step_img_right'] % ('*.*'))
    # for src in  file_list:
    #     _imgresize(src, width)

    ### step image low
    width = conf['step_img_width_low']
    # persp
    file_list = glob.glob(conf['step_img_persp'] % ('*.0'))
    for src in  file_list:
        _imgresize(src, width, '_low')  # match step_img_persp_low

    # restore cwd
    os.chdir(cwd_temp)



def copy_static_files():
    src_js = os.path.join(thislocation, 'js')
    src_css = os.path.join(thislocation, 'css')
    src_img = os.path.join(thislocation, 'img')
    dst_js = os.path.join(conf['outputdir'], 'js')
    dst_css = os.path.join(conf['outputdir'], 'css')
    dst_img = os.path.join(conf['outputdir'], 'img')
    print "js: %s \n\t-> %s" % (src_js, dst_js)
    print "css: %s \n\t-> %s" % (src_css, dst_css)
    if os.path.exists(dst_js):
        shutil.rmtree(dst_js)
    if os.path.exists(dst_css):
        shutil.rmtree(dst_css)
    shutil.copytree(src_js, dst_js)
    shutil.copytree(src_css, dst_css)
    shutil.copy(os.path.join(src_img, 'logo.png'), dst_img)


with open(os.path.join(conf['outputdir'], conf['struct_file'])) as fp:
    struct = json.load(fp, object_pairs_hook=collections.OrderedDict)

index(struct)
subsystems(struct)
steps(struct)
resize_images()
copy_static_files()
