DriveBoard
==========

[Index](index.md) -- DriveBoard | [BeagleBoneBlack](bbb_setup.md) | [BeagleBone](beaglebone_setup.md) | [RaspberryPi](raspberrypi_setup.md)

The DriveBoard is the main electronics board of the Lasersaur (successor of [LasaurShield](LasaurShield.md)). It interfaces all the electronics components and allows full control over LAN (ethernet). The board runs the real-time firmware (LasaurGrbl) on its Atmege328 chip and the web-based UI (LasaurApp) on a BeagleBone embedded Linux computer. This separation allows for simple hacking and modding. For example, alternative (experimental) headers for the RaspberryPi are provided. The board is z-axis ready but is typically only operated with the x- and y-axis stepper drivers and motors.

Features
--------
- three stepper drivers (x,y,z)
- two limit sensors per axis
- two door sensors (one redundant) 
- one chiller sensor
- two (emergency) interlocks (e-stop, keylock) via solid state relay
- interlocks double as system on/off
- two 24V, 1A, opto-isolated outputs (e-valve, solenoid actuators)
- all sensor and control wiring with shielded Cat5 patch cables
- hard-logic laser safety system (laser is switched of reliably by the following events: door open, chiller failure, limits hit)
- driver-less solution, full control with any modern browser (embedded web app)
- build for easy hacking and modding in mind (minimal real-time firmware, powerful Linux-based UI programing, future expandability like camera, wifi, etc ...)


![driveboard assembled](http://farm9.staticflickr.com/8072/8271614212_43813ff101_z.jpg)

![driveboard](http://farm6.staticflickr.com/5473/9455690694_955cb9333e_z.jpg)


Required Parts
---------------
The following parts are required to get the DriveBoard working. All of these items are in the Lasersaur BOM:

- Two GeckoDrive G203V stepper drivers
  - GeckoDrive G201X are also fully compatible.
  - Experimental headers for Nanotec SMC11 stepper drivers are also provided.
- A BeagleBone
  - loaded with LasaurApp
  - Experimental headers for the RaspberryPi are also provided.
- Two PSUs
  - 24V, 3A
  - 5V, 3A
- 11x Cat5 Patch cables, shielded, 26-24AWG, 3m
  - these are used for most of the wiring
- standard insulated wires, 18AWG
  - these are for the PSU wiring (screw terminals)
  - the BOM has an extra power cord to salvage for this
- (optionally) e-stop switch and keylock switch (both rated for 2A)
  - the DriveBoard has two interlocks which need to be connected for operation
  - both interlocks can also be connected with a jumper
- (optionally) e-valve, 24V
- (optionally) acrylic mount/cover sheets

![driveboard case](http://farm9.staticflickr.com/8349/8270542701_dfae76ef4f_z.jpg)



Power Wiring
-------------
The power wiring involves AC input, 24V PSU, 5V PSU, laser PSU, and frame. This is all about the screw terminals on the left side of the DriveBoard. The recommended wire gauge is 18AWG (standard power cord gauge). All three PSUs are powered through the board.

1. AC input connects to `AC_in_1`, `AC_in_2`, and `GND_in`
2. The laser PSU connects to `AC_laser_psu_1`, `AC_laser_psu_2`, and `GND_laser_psu`
3. The 24V PSU connects to `AC_24V_psu_1`, `AC_24V_psu_2`, and `GND_24V_psu`. The 24V output connects to `DC_in_24V+`, and `DC_in_24V-`.
4. The 5V PSU connects to `AC_5V_psu_1`, `AC_5V_psu_2`, and `GND_5V_psu`. The 5V output connects to `DC_in_5V+`, and `DC_in_5V-`.
5. The Lasersaur frame connects to `GND_frame`. Be aware that the aluminum extrusions have a non-conductive coating. Either sand or connect to an angle bracket. Alternatively if the laser PSU casing has connectivity to the frame (sanding may be required), the DriveBoard will be grounded too.

The screw terminals labeled `air_assist+`, `air_assist-`, `aux1_assist+`, `aux1_assist-` are optional and redundant to the `assists` jack. Typically the assists are wired with a Cat5 patch cable.


Sensor and Control Wiring
-------------------------
Most of the sensor and control wiring is done with shielded [Cat5 patch cables](http://en.wikipedia.org/wiki/Category_5_cable) (ethernet cables). This has the advantage of not having to assemble plugs while still being affordable and highly available. We recommend using 3m patch cables and cutting them to the appropriate lengths. The wiring is as follows (for both TIA/EIA-568-A and TIA/EIA-568-B style cables, also the shorthands `wgr,wor,gr,or,bl,br,wbr,wbl` are the colors of the leads):

- x1
  - cable length: 2900mm
  - wgr,wor      -> red        (=vcc =1,3)
  - gr,bl,wbl,or -> black      (=sig =2,4,5,6)
  - not used   -> blue
  - wbr,br       -> not used (=gnd =7,8)
- x2
  - cable length: 1500mm
  - (connect same as x1)
- stepper_x
  - cable length: 1500mm
  - Nanotec
    - wgr, wor  ->  orange (=A =1,3)
    - gr,or     ->  brown  (=A' =2,6)
    - bl,br     ->  red    (=B =4,8)
    - wbr,wbl   ->  yellow (=B' =7,5)
  - LinEngineering
    - gr, or    ->  black  (=A =1,3)
    - wgr, wor  ->  green  (=A' =2,6)
    - bl,br     ->  red    (=B =4,8)
    - wbr,wbl   ->  blue   (=B' =7,5)
- y1
  - cable length: 650mm
  - (connect same as x1)
- y2
  - cable length: 1350mm
  - (connect same as x1)
- stepper_y
  - cable length: 650mm
  - Nanotec
    - wgr, wor  ->  green (=A =1,3)
    - gr,or     ->  black (=A' =2,6)
    - bl,br     ->  red   (=B =4,8)
    - wbr,wbl   ->  blue  (=B' =7,5)
    - red-white -> blue-white
    - black-white -> green-white
  - LinEngineering
    - gr, or    ->  blue-white  (=A =1,3)
    - wgr, wor  ->  red         (=A' =2,6)
    - bl,br     ->  green-white (=B =4,8)
    - wbr,wbl   ->  black       (=B' =7,5)
    - red-white ->  blue
    - black-white -> green
- door1
  - cable length: 2500mm
  - wgr,wor      -> blue       (=vcc =1,3)
  - gr,bl,wbl,or -> black      (=sig =2,4,5,6)
  - not used   -> red
  - wbr,br       -> not used (=gnd =7,8)
- door2
  - cable length: 1700mm
  - (connect same as door1)
- laser
  - cable length: 750mm
  - gr,or   -> P or WP         (=dis =2,6)
  - bl      -> H or TH         (=pwm =4)
  - wbr,br  -> G or GND        (=gnd =7,8)
  - wgr,wor -> not used (=vcc =1,3)
  - wbl     -> not used (=aux2 =5)
  - Also on the laser PSU connector: 5V(pin1) -> IN(pin6)
  - See [Laser Adjustment](laser_adjustments.md) page for output calibration.
- chiller
  - cable length: 2900mm
  - wgr,wor -> H3 (=vcc =1,3)
  - gr,bl,wbl,or -> H1 (=sig =2,4,5,6)
  - wbr,br -> not used (=gnd =7,8)
- assists
  - cable length: 500mm
  - wgr,wor -> air_assist+ (=1,3)
  - gr,or -> gnd (=2,6)
  - bl,br -> gnd (=4,8)
  - wbr,wbl -> aux1_assist+ (=7,5)
- e-stop interlock
  - cable length: 1700mm
  - wgr, wor -> e-stop_1 (=1,3)
  - gr,or -> e-stop_2 (=2,6)
- keylock interlock
  - cable length: 30mm
  - bl,br (=4,8) -> wbr,wbl (=7,5)
- z1, z2, stepper_z (optional)
  - (analogous to x- and -y-axis)


Current Set Resistors
---------------------
The DriveBoard (assembled version) comes with current set resistors that match the stepper motors of the current BOM. If you are upgrading an older build or using alternative stepper motors for some other reasons make sure to adapt these resistors. The resistors are located right to the stepper drivers. Their value is calculated as follows, "I" being the current rating of the motor in Ampere:

- `R (kOhm) = 47*I/(7-I)`


Software Installation
---------------------
The DriveBoard runs the LasaurGrbl firmware on the Atmega328 chip and LasaurApp on the BeagleBone. For the assembled version of the DriveBoard follow the [LasaurApp setup](lasaurapp.md). When building from scratch you will also have to get the Arduino bootloader onto the Atmega chip. This can be done with an Arduino and the Arduino IDE. The actual flashing of the firmware and continuous updates can then be done from LasaurApp.


Safety Systems
--------------

During operation the Lasersaur hardware (hard-logic safety) and firmware monitor various sensor events and make sure safe operation is maintained.

- hardware safety functions (DriveBoard logic):
  - the laser is disabled via the "laser:dis" pin when any of the following happens
    - any limit interlock is open
    - chiller interlock is open
    - any door interlock is open 
- firmware safety functions (LasaurGrbl):
  - the controller is put into "stop mode" when any of the following happens:
    - any of the limit interlocks opens
    - serial data contains a '!' character
  - the controller resumes from "stop mode" when serial data contains a '~' character. LasaurApp sends this character when pressing 'Cancel' or  'Homing Cycle'.
- e-stop/keylock interlock
 - both need to be closed for operation
 - when open the following subsystems are turned off:
   - 5V board power
   - Laser PSU AC line (via SSR)
   - 24V PSU AC line (via SSR)



Various Mods (optionally)
-------------------------

### Using an Arduino instead of a BeagleBone

Usually the BeagleBone runs LasaurApp and sends G-code to the DriveBoard's Atmega chip. If no BeagleBone is available you can also run LasaurApp on your computer. An Arduino's USB-to-Serial converter can then be used for connectivity (in fact pretty much any USB-to-serial converter can be used).

For this to work you need to remove the Atmega chip from the Arduino and connect three pins to the DriveBoard: TX, RX, and GND. You can find these pins on the DriveBoard's "serial" header (v13.03 and newer). Connect as such: Arduino:TX -> DriveBoard:RX, Arduino:RX -> DriveBoard:TX, Arduino:GND -> DriveBoard:GND. (If you want to power through the Arduino, also connect 5V pins)

Then start LasaurApp on your computer by running `python backend/app.py`. The browser-based GUI should then open automatically.




 
