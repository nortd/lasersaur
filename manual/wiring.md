Wiring the Lasersaur
=====================

DEPRECATED: The electronics wiring on this page does not apply to the newer DriveBoard. For this see the [DriveBoard Page](driveboard.md).

The electronics subsystem consists of the Controller (Arduino Shield, Arduino Uno), two stepper drivers, two stepper motors, 24V DC power supply, a relay, an e-stop, four limit sensors, two door sensor (one redundant), and the laser system. The depicted wiring to the laser power supply is based on the products from [cncoletech](http://cncoletech.com/). Please double check the data sheets for your specific laser system or consult the mailing list when in doubt.


### Laser System

The high-voltage (positive) wire of the power supply **requires proper insulation**. The voltage is in excess of 25kV and poses a **lethal risk**. Also be aware that the voltage supplied can easily arc for 15cm (multiple inches) and the cable stays charged for a considerable time after the AC power is disconnected (when in doubt use an AC ground wire on a chicken stick to discharge the high-voltage cables).

### Howto

1. See [BOM](bom.md) by subsystem for part details.
2. Mount the DIN rail in the back of the Lasersaur.
3. Clip PSU, relay, and screw terminals onto the DIN rail.
4. Connect LasaurShield to stepper drivers.
5. Mount the Arduino, LasaurShield, and stepper drivers onto the electronics mount panel. 
6. Then mount the panel onto the DIN rail.
7. Run all the cables by mounting in T-slots with hotglue (for AC wiring us one of the excessive power cords).
8. Connect all the cables using heat shrink tubing liberally to insulate and reduce wire stress at tight turns.
9. Secure all cables with zip ties making sure to reduce tension on connectors.
10. Double-check with schematic, go through checklist, then turn on machine carefully.


[SVG](http://dl.dropbox.com/u/9430160/lasersaur/diagram_wiring.svg) | [High-res PNG](http://farm8.staticflickr.com/7082/7227014208_9a265cf881_o_d.png)


<a href="http://dl.dropbox.com/u/9430160/lasersaur/diagram_wiring.svg"><img src="http://farm8.staticflickr.com/7082/7227014208_e0bf0daf68_z.jpg"></a>


### Checklist

1. Are the high-voltage wires properly insulated? (positive laser pole).
2. Are the AC wires properly insulated and is the Lasersaur frame grounded?
3. Does the E-Stop turn off the machine?
4. Has the chiller's water circulations been properly tested and is the tubing mounted in ways not to cause stress on the inlet and outlet ducts.
5. Are all the signal wires shielded and grounded? Wires for limit switches, door switch, chiller, power relay, and laser PSU need to be shielded and the shield needs to be connected to the logic ground of the LasaurShield.
6. Is the disable pin on the Gecko drivers left disconnected?
7. Have all the wires been secured with zip ties?
8. Has the second redundant door switch been installed (connect in parallel).



<br>



![controller wiring](http://farm9.staticflickr.com/8003/6973305936_af7b60f56d_z.jpg)

![laser wiring](http://farm8.staticflickr.com/7186/7119387413_024fb3852c_n.jpg)![laser wiring](http://farm8.staticflickr.com/7185/7119387815_761fce44db_n.jpg)

![laser wiring](http://farm8.staticflickr.com/7248/6973306754_f7a790b3ab_n.jpg)![laser wiring](http://farm8.staticflickr.com/7111/6973306624_cc9549da00_n.jpg)



