Lasersaur System Overview
=========================

[Index](index.md) --

![lasersaur dark](http://farm9.staticflickr.com/8233/8464050599_c02f553c27_m.jpg)
![lasersaur open](http://farm9.staticflickr.com/8510/8464041087_d23416e7dc_m.jpg)

Laser cutters are systems for applying electromagnetic radiation to a work piece. When done like a boss this will cause the material to disintegrate in the area of application. The challenge is doing this in a controlled manner and gaining full control of the energy density at any point in time. So, apart from safety,  energy density over dt is our major concern here.

To accomplish this control the Lasersaur uses a combination of robotic actuators and sensors, laser resonator, optical beam delivery, and control software. All of these subsystems need to work together to get good results. Additionally the project's nature requires a level of simplicity that allows for home building.

### Specs:
- overall dimensions: 1700x1170x360mm (67x46x14.2")
- work area: 1220x610mm (48x24")
- resolution: 0.1-0.03mm (240-840dpi)
- maximum seek rate: 12000mm/min
- maximum feed rate: 8000mm/min


Mechanics
---------

![mechimage](http://farm9.staticflickr.com/8528/8464053217_fac4bf454e_m.jpg)
![mechclose](http://farm9.staticflickr.com/8074/8414185536_c9090070b1_m.jpg)

The mechanics comprise both stationary and dynamic parts. The primary building blocks of both the frame and the gantry are T-slot aluminum extrusions. They are widely used in the automation industry and many suppliers offer them. The Lasersaur is designed around extrusions with 20mm side lengths. All the mount assemblies are built from angle brackets and custom-cut alumiunm pieces.

The linear motion assemblies for the x- and y-axis roll directly on the aluminum extrusions. Unlike many gantry designs, no proprietary rails and carriage assemblies are used. The Lasersaur carriages are build from standard-sized ball bearings (with nylon coating), cap screws and custom-cut acrylic pieces. Both axes are minimally constraint and are quite forgiving in terms of imprecisions of the frame.

The drive mechanisms are based on timing belts and stepper motors. We use 12-tooths pulleys, 5.08mm XL belts and 2000 microsteps steppers/drivers. This results in a theoretical resolution of 0.03mm/step.


Electronics
-----------

![stepper](http://farm9.staticflickr.com/8090/8414187450_ef48c676c7_m.jpg)
![electroimage](http://farm9.staticflickr.com/8081/8414619512_190b059209_m.jpg)

The system is controlled by the Lasersaur DriveBoard in conjunction with two GeckoDrive G203Vs. Each of the Geckos drive a Nanotec (EU BOM) or LinEngineering (US BOM) stepper motor. For the x-axis we use a lightweight Nema 17 and for the y-axis a Nema 23 with rear shaft. For network connectivity the DriveBoard supports one of two embedded Linux computers: BeagleBone and RaspberryPi. They plug right into the board and serve the control interface via http.

The DriveBoard also controls the laser intensity via a digital PWM line and monitors limit switches, door sensors, and water chiller. All critical laser shutdown functions are implemented software-independently with logic gates. Optionally the board can control air and gas assist with optically isolated relays. At the lowest level the firmware understands a subset of [gcode](gcode.md).

* [DriveBoard](driveboard.md)
* [GeckoDrive G203V](geckodrives.md)
* [Stepper Motors](steppers.md)

Looking for deprecated [LasaurShield](LasaurShield.md)?


Optics and Laser
----------------

![closeoptics](http://farm8.staticflickr.com/7185/7119387815_761fce44db_m.jpg)
![opticsimage](http://farm8.staticflickr.com/7054/6973307346_0674b570aa_m.jpg)

The Lasersaur uses a stationary laser resonator and flying optics for beam delivery. Three mirrors and one lens plus the various mounts make up the optics subsystem. The optics components are from a modular system (Thorlabs). This makes it easy to experiment with further improvements like different laser sources and beam expanders. Mirrors and lenses have a 1" diameter and can adapt well to stronger lasers.

The system is designed with a DC-excited CO2 laser tube in mind but can be adapted for other sources relatively easily. The space dedicate to the tube can accommodate up to 1.4m tubes which makes it compatible with typical  low-budget CO2 lasers up to 100W.

A typical low-budget CO2 laser system (like the one listed in the BOM) consists of 3 components: laser tube, power supply and water chiller. We have a dedicated space for the power supply inside the Lasersaur. The water chiller is external to the box.

* [Laser and PSU](lasersystem.md)
* [Water Chiller](chiller.md)


Control Software
----------------

The Lasersaur is generally controlled through the [LasaurApp](software.md) web application that runs on the Lasersaur (it can also run locally on the user's computer). It's typically accessible via LAN at at http://lasersaur.local. The main interface can be used with any modern web browser. LasaurApp then streams G-code to the controller's low-level firmware which then does all the time sensitive motor control. [The subset of G-code](gcode.md) which is understood by the firmware is a fairly simple control language which can also be used directly.

While it can be useful to understand some G-code this is not necessary when using LasaurApp. For most usage scenarios knowing how to save an .svg file in Illustrator or Inkscape and importing it in LasaurApp is all that is necessary to start cutting.

- [Software Setup Page](software.md)


Accessory Subsystems
--------------------

A Lasersaur needs a couple of additional subsystems for operation: air exhaust, air assist, cutting surface, fire extinguisher, hand vacuum cleaner, ...

- [Accessories Page](accessories.md)
