Revision 14.01 (testing)
=======================

[Index](index.md) -- [bom](bom.md) | [revisions](revisions.md)

This revision features an improved drive system with the following features/changes:

  - gear reduction
    - ~2.7 on x-drive
    - ~2.8 on y-drive
  - more rigid y-drive coupling, 12mm shafts
  - GT (or HTD) 3M belts, 9mm wide
  - compatible with a wider selection of stepper motors
    - no rear shaft required
    - no motor length restriction
    - space for optional encoder
  - magnetic limit switches
  - full width cable carrier base

This revision will be fully tested in Nov and become the master branch most likely Jan 2014. Please drop us a line if you want to build this revision ahead of time.

 - CAD Model v14.01
   - [model (Rhino4)](http://file.lasersaur.com/model/model-lasersaur-v14.01.3dm)
   - [model (FreeCAD)](http://file.lasersaur.com/model/model-lasersaur-v14.01.FCStd)
   - [model (IGES)](http://file.lasersaur.com/model/model-lasersaur-v14.01-iges.zip)
 - Job Files
   - [MechParts v14.01 (dxf)](http://file.lasersaur.com/job-files/MechParts-v14.01.dxf)
 - Bill of Materials 
   - [BOM v14.01 (EU)](http://labs.nortd.com/lasersaur/bom-1401-subsystems-eur)
   - [BOM v14.01 (US)](http://labs.nortd.com/lasersaur/bom-1401-subsystems-usd)

<br>

![top](http://farm4.staticflickr.com/3817/10155720676_31429845b9_b.jpg)
![front](http://farm4.staticflickr.com/3746/10155632635_1b3c04c3b9_b.jpg)
![x-drive](http://farm8.staticflickr.com/7343/10155548564_ffdeb0deca_b.jpg)
![y-drive](http://farm8.staticflickr.com/7401/10155631215_44c762519e_z.jpg)

All these changes address precision and ease of maintenance. We expect to have an easier time with adjusting belt tension and generally make the system more tolerant to non-optimally adjusted belts. Similarly the magnetic limit switches are more reliable when a cleaning schedule is not always followed.

The gearing will push up the resolution and positioning accuracy and also help with stepper resonance issues. In terms of resonance we previously got a 0.4mm ripple at a narrow speed band on the y-axis. In the line test pattern it shows on the 9th line from the top: [line test](http://www.flickr.com/photos/stfnix/8627632165/). On the test card it shows as slight perforation under 1500mm/min and ripples at higher speeds. See [1500mm/min](http://www.flickr.com/photos/stfnix/8627624247/) versus [2000mm/min](http://www.flickr.com/photos/stfnix/8600930123/). Here also an example how the ripples look in a normal job at speeds above 2000mm/min: [pic](http://www.flickr.com/photos/stfnix/8494039023/). Gearing and torque adjustment can significantly improve on this as some tests have shown. This way we can reduce and bring down the stepper resonance (currently at 450Hz).

  
