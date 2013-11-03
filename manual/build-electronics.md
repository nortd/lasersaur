build <span style="background-color:#ccb17f">electronics</span>
============================

[&#xAB; x-drive](build-x-drive.md) | [overview](assembly.md) | [optics-laser &#xBB;](build-optics-laser.md)

![electronics](http://farm9.staticflickr.com/8397/8700215178_6b84d671e4_z.jpg)


The electronics subsystem consists of the [Driveboard](driveboard.md), two stepper drivers, two stepper motors, 5V and 24V DC power supplies, an e-stop, four limit sensors, two door sensor (one redundant), and the laser system. Most of the wiring is done with shielded cat5 patch cables. One side has to be soldered to the sensor or actuator while the other side plugs straight into the Driveboard.

**HIGH VOLTAGE DANGER!** Wiring the laser system has to be done with the utmost care and certainty. Messing up this part of the assembly can result in significant personal injury. The high-voltage (positive) wire of the power supply **requires proper insulation**. The voltage is in excess of 25kV and can spark several inches (some 150mm). Also the cable stays charged for a considerable time after the AC power is disconnected (when in doubt use an AC ground wire on a chicken stick to discharge the high-voltage cable).


1. Prepare parts for this subsystem (See [BOM](bom.md) by subsystem)
2. Assembeg and mount Driveboard
  - Solder Driveboard
  - Mount onto acrylic carrier panel together with 5V and 24V PSUs.
  - If you plan on cutting the carrier panel yourself improvise with cardboard.
  - Mount unit in rear compartment.
3. Wire Sensors and E-stop
  - For details see "Sensor and Control Wiring" on [Driveboard page](driveboard.md).
  - Drill holes as necessary to run cables through the separation wall.
  - Door switches and E-stop cables can be run inside the extrusion. This requires drilling an M5 hole in the approximate area of the switch/E-stop (see images).
  - Take shielded cat5 patch cable and cut to approximate length.
  - Plug into Driveboard and run cable to sensor. Cut to exact length.
  - Solder sensor by splicing the cables in a way they still fit into the t-slot.
  - Test electrical functions before actually hot-gluing into the t-slots.
4. Wire Steppers
  - For details see "Sensor and Control Wiring" on [Driveboard page](driveboard.md).
  - Drill holes as necessary to run cables through the separation wall.
5. Wire Power/AC
  - For details see "Power Wiring" on [Driveboard page](driveboard.md).
  - Two of the three C-14 power cords are intended for wiring inside the machine. Cut these up as needed.
6. Wire Laser System
  - For details see "Power Wiring" and "Sensor and Control Wiring" on [Driveboard page](driveboard.md).
  - The laser PSU connects to the tube by two wires. The high-voltage (thick, red) wire connects to the rear of the tube while the thin blue wire connects to the front. Before operation make sure the high-voltage side is properly insulated with the insulation cap in place.
  - The laser PSU also connects to the AC through the Driveboard
  - Finally the PSU connects to the laser control output of the Driveboard.


### Checklist

1. Is BeagleBone plugged into the Driveboard correctly? Connectors have to align on the left side! If aligned on the right side the BeagleBone does not properly boot.
2. Are the z-axis limit switches short-wired (if not used). On a two axis system the z-axis limit switches still need to be closed otherwise you get "Limit Hit" errors.
3. Does the E-Stop turn off the Driveboard, laser PSU, Stepper PSU? (5V PSU should stay on)
4. Is the Lasersaur frame grounded? The aluminum extrusions' finish can sometimes prevent this.
5. Are the high-voltage wires properly insulated? (positive laser pole).
6. Are the AC wires properly insulated?
7. Has the chiller's water circulations been properly tested and is the tubing mounted in ways not to cause stress on the inlet and outlet ducts?
8. Have all the wires been secured with zip ties? 


### Troubleshooting

- The BeagleBoane does not power up.
  - Two interlocks are used to control power to the DriveBoard: `e-stop` and `keylock`. Make sure both are closed. See the "interlocks" section in the wiring instructions for details.


### Images

![driveboard](http://farm9.staticflickr.com/8047/8413082007_eb5a234e96_z.jpg)
![driveboard](http://farm9.staticflickr.com/8507/8413520569_4c927e1133_z.jpg)
(image of prototype, driveboard cover panel may vary)

![driveboard](http://farm9.staticflickr.com/8185/8413519529_7ec6882104_z.jpg)
(image of prototype, driveboard cover panel may vary)

![driveboard](http://farm9.staticflickr.com/8081/8414619512_190b059209_z.jpg)
(image of prototype, driveboard cover panel may vary)

![tube](http://farm9.staticflickr.com/8369/8414620484_a230ea38f5_z.jpg)
![entry](http://farm9.staticflickr.com/8216/8414618344_a45a4550b7_z.jpg)
![power c14](http://farm9.staticflickr.com/8517/8413084587_a4d6002e58_z.jpg)

![door switch](http://farm9.staticflickr.com/8336/8414182364_505c9d48b5_z.jpg)
![door switch](http://farm9.staticflickr.com/8194/8414182126_9e9fd85f48_z.jpg)
![door switch](http://farm9.staticflickr.com/8232/8413082741_7128161894_z.jpg)
![splicing](http://farm9.staticflickr.com/8377/8414180946_74fde066d8_z.jpg)
![splicing](http://farm9.staticflickr.com/8183/8413072681_8495e575bf_z.jpg)

![stepper](http://farm9.staticflickr.com/8365/8413083945_7d396cbd4a_z.jpg)
![window](http://farm9.staticflickr.com/8473/8413083729_79fc695741_z.jpg)

![stepper](http://farm9.staticflickr.com/8365/8413083945_7d396cbd4a_z.jpg)
![stepper](http://farm9.staticflickr.com/8043/8413082299_d28b659f07_z.jpg)

![e-valve](http://farm9.staticflickr.com/8238/8414177622_c73c4bfdae_z.jpg)
