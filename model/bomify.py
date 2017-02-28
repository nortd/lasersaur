import re
import rhinoscriptsyntax as rs

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

obj_hash = {}
for layer in get_step_children(rs.CurrentLayer()):
    objs = rs.ObjectsByLayer(layer, False)
    for obj in objs:
        obj_name = rs.ObjectName(obj)
        if not obj_hash.has_key(obj_name):
            obj_hash[obj_name] = 1
        else:
            obj_hash[obj_name] += 1
for k in sorted(obj_hash.keys()):
    print str(obj_hash[k]) + " : " + k
print "item count: " + str(len(obj_hash))