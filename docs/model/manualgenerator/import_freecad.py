
import os
import json
import collections
import ImportGui


thislocation = os.path.dirname(os.path.realpath(__file__))
# step_dir = os.path.join(thislocation, 'lasersaur-model-v14.03-step')
# step_dir = os.path.join(thislocation, 'test-step')
step_dir = os.path.join("/home/noema/Shared/lasersaur_stuff", 'export_step')


def structure_from_file(path):
    fp = open(path)
    return json.load(fp, object_pairs_hook=collections.OrderedDict)

def get_layer_tail(layer):
    parts = layer.split('::')
    return parts[-1]

def get_part_filename(subsystem, step, partkind):
    return "%s#%s#%s.step" % (subsystem, step,partkind)


doc = FreeCAD.newDocument()
structure = structure_from_file(os.path.join(step_dir,"structure.json"))

for subsystem,v in structure.items():
    subsystem_grp = doc.addObject("App::DocumentObjectGroup", subsystem)
    subsystem_grp.Label = subsystem
    for step,vv in v.items():
        step_name = get_layer_tail(step)
        step_grp = doc.addObject("App::DocumentObjectGroup", step_name)
        step_grp.Label = step_name
        subsystem_grp.addObject(step_grp)
        for partkind,vvv in vv.items():
            partkind_name = "%s::%s" % (step_name,partkind)
            partkind_grp = doc.addObject("App::DocumentObjectGroup", partkind_name)
            partkind_grp.Label = partkind_name
            step_grp.addObject(partkind_grp)

            filename = get_part_filename(subsystem, step_name, partkind)
            FreeCAD.Console.PrintMessage(filename + "\n")
            preimport_obj_count = len(doc.Objects)
            ImportGui.insert(os.path.join(step_dir, filename), doc.Name)
            # group new objects
            for i in range(preimport_obj_count, len(doc.Objects)):
                obj = doc.Objects[i]
                if obj.TypeId == 'Part::Feature':
                    partkind_grp.addObject(obj)


    FreeCAD.Gui.SendMsgToActiveView("ViewFit")
    if not subsystem == "1.frame-bottom":
        subsystem_grp.ViewObject.Visibility=False

    doc.recompute()

