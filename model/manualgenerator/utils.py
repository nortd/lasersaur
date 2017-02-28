import os
import re
import json
import collections
import rhinoscriptsyntax as rs

from config import conf



def show_blocks():
    for layer in conf['blocks']:
        rs.LayerVisible(layer, True)
        for child in rs.LayerChildren(layer):
            rs.LayerVisible(child, True)

def hide_non_subsystems():
    for layer in conf['non_subsystems']:
        rs.LayerVisible(layer, False)

def hide_subsystems():
    for layer in conf['subsystems']:
        rs.LayerVisible(layer, False)

def show_subsystems():
    for layer in conf['subsystems']:
        rs.LayerVisible(layer, True)

def hide_children(layer):
    rs.LayerVisible(layer, True)
    for child in rs.LayerChildren(layer):
        rs.LayerVisible(child, False)

def show_children(layer):
    rs.LayerVisible(layer, True)
    for child in rs.LayerChildren(layer):
        rs.LayerVisible(child, True)


def show_only(layer):
    rs.LayerVisible("Default", True)
    rs.CurrentLayer("Default")
    for sub in rs.LayerNames():
        if sub == "Default":
            continue
        if sub in conf['blocks']:
            rs.LayerVisible(sub, True)
            continue
        rs.LayerVisible(sub, False)

    for block in conf['blocks']:
        for blockchild in rs.LayerChildren(block):
            rs.LayerVisible(blockchild, True)

    # show parent layers, if nested (two up, max)
    p_layer = rs.ParentLayer(layer)
    if p_layer:
        pp_layer = rs.ParentLayer(p_layer)
        if pp_layer:
            rs.LayerVisible(pp_layer, True)
        rs.LayerVisible(p_layer, True)

    # show the target layer
    rs.LayerVisible(layer, True)
    rs.CurrentLayer(layer)
    rs.LayerVisible("Default", False)



def get_step_children(layer):
    # Get steps layers sorted by step number.
    # That is the num after the period: subsystemnum.stepnum
    sublayerdict = {}
    for child in rs.LayerChildren(layer):
        sublayermatch = re.match(layer+"::([0-9]{1,3})\.([0-9]{1,3})", child)
        if sublayermatch:
            step = int(sublayermatch.groups()[1])
            if sublayerdict.has_key(step):
                raise Exception("dublicated step number")
            sublayerdict[step] = child
    sublayers = []
    for k in sorted(sublayerdict):
        sublayers.append(sublayerdict[k])
    return sublayers



def get_layer_tail(layer):
    parts = layer.split('::')
    return parts[-1]

def get_part_filename(subsystem, step, partkind):
    return "%s#%s#%s.step" % (subsystem, step,partkind)



def get_structure(debug=False):
    """Get the structure of the CAD file.

    The structure is a hierarchy with the subystems on top:
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
    # subsystems{ steps { objects { uuids [] } } }
    structure = collections.OrderedDict()
    for layer in conf['subsystems']:
        structure[layer] = collections.OrderedDict()
        if debug:
            print "---[%s]---" % (layer)
        for sublayer in get_step_children(layer):
            structure[layer][sublayer] = collections.OrderedDict()
            if debug:
                print "    %s" % (get_layer_tail(sublayer))
            objs = rs.ObjectsByLayer(sublayer, False)
            objnamedict = {}
            for obj in objs:
                name = rs.ObjectName(obj)
                if not objnamedict.has_key(name):
                    objnamedict[name] = [obj]
                else:
                    objnamedict[name].append(obj)
            for name in sorted(objnamedict):
                structure[layer][sublayer][name] = objnamedict[name]
                if debug:
                    print "        %sx %s" % (len(objnamedict[name]), name)
    return structure


def structure_to_file(structure):
    struc = collections.OrderedDict()
    for subsystem,v in structure.items():
        struc[subsystem] = collections.OrderedDict()
        for step,vv in v.items():
            struc[subsystem][step] = collections.OrderedDict()
            for partkind,vvv in vv.items():
                struc[subsystem][step][partkind] = len(vvv)

    with open(os.path.join(conf['outputdir'], conf['struct_file']), 'w') as fp:
        json.dump(struc,fp)


def structure_from_file():
    with open(os.path.join(conf['outputdir'], conf['struct_file'])) as fp:
        struct = json.load(fp, object_pairs_hook=collections.OrderedDict)
    return struct