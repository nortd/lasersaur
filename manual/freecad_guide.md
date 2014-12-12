FreeCAD Survival Guide
=======================

![freecad](http://farm9.staticflickr.com/8187/8128015105_9ebf3c334a_z.jpg)

[FreeCAD](www.freecadweb.org/) is an open source 3D CAD program with a promising future. The technology behind FreeCad is very solid (OpenCascade, Coin3D, QT, and Python) and the UI, while still very uncooperative, is getting better with every release. As it matures, the Lasersaur project aims to support it more and more. While the Lasersaur CAD files are more efficiently edited with Rhino, FreeCAD is already quite usable for assisting the assembly process. 

During assembly the CAD model can fill in most of the gaps of the build instructions. It's very helpful for clarifying parts placements and taking measurements. With this guide we hope to provide an easy start with FreeCAD v0.13 and up. For later versions some of these difficulties may already be more intuitive, so we hope.

- [Getting FreeCAD](http://www.freecadweb.org/wiki/index.php?title=Installing)


Setting up the UI
-----------------
First free yourself from interface clutter. In the "View" menu towards the bottom you can find "Workbench", "Toolbars", "Views". Set these to "Inspection", "View", and "Tree View", respectively.

![ui](http://farm9.staticflickr.com/8191/8128014841_8d2d7665f8_n.jpg)
![ui](http://farm9.staticflickr.com/8189/8128042446_d079457a90_n.jpg)
![ui](http://farm9.staticflickr.com/8334/8128042382_2cc7c116a9_n.jpg)


Getting Used to Scene Navigation
--------------------------------
The essential scene navigation operations are orbiting, translating, zooming and setting the center of orbiting. In addition a tree view/layers in which to organize geometry is very useful.

FreeCAD allows for [different ways of navigation](http://www.freecadweb.org/wiki/index.php?title=Mouse_Model). Which one to choose depends on what you are familiar with, what platform you are using, and if you have a mouse with multiple buttons. Personally I like "Touchpad navigation".

![ui](http://farm9.staticflickr.com/8189/8128042582_fb28710d44_n.jpg)

- orbit -> `alt-drag`
- translate -> `shift-drag`
- zoom -> `PgUp` and `PgDn`

The only way to set the center of orbiting I could find is with the "Box Zoom" command. By pressing `Ctrl-B` it allows you to set a zoom box which then also sets the orbiting center.

The standard views are on the numbers 0-5. Also `shift-F` saves the current view which is then available through `ctrl-1` (the next freez-view will be accessible through `ctrl-2` and so on). 

Under View/Standard views there is also the "Fit All" command. Unfortunately it is not associated with a keyboard shortcut by default but you can do this through Tools/Customize/Keyboard. I added the shortcut `ctrl-F` to it.

![ui](http://farm9.staticflickr.com/8054/8128015015_fc92afc455.jpg)

### Tree View
The tree view is a list of all geometries in the scene. It allows for easy selection and modification/deletion (via context menu). Most importantly though, it allows for showing/hiding certain geometry by pressing `SPACE`. This speeds up the workflow tremendously.


Measuring Parts
---------------
FreeCAD has a measurement tool accessible from the View menu or the toolbar. You can also assign it to something like `ctrl-M` (see Tools/Customize/Keyboard). You basically have to select two points and it will add the measurement. The length is best seen in the Tree View (as it is notorious to be placed far away from the geometry). It can also be deleted from there.

![ui](http://farm9.staticflickr.com/8336/8128015157_5077ec0d4f_m.jpg)


Exporting to other Formats
---------------------------
FreeCAD's OpenCascade kernel has great support for [IGES](http://en.wikipedia.org/wiki/IGES) and [STEP](http://en.wikipedia.org/wiki/ISO_10303) file formats. It can also export to [STL](http://en.wikipedia.org/wiki/STL_%28file_format%29) and [VRML](en.wikipedia.org/wiki/Vrml). In the Tree View simply select the geometry to export then click on File/Export (or `ctrl-E`). Then simply choose a filename with .igs, .step,  .stl, or .vrml extension. All selected geometry will be exported.

To preserve the various colors of the subsystems I usually export each subsystem separately. Then I assign colors (rgb or hex) accordingly (see [colors page](colors.md)).


