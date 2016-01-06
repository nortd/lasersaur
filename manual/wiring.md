Lasersaur Guide
=====================

[Index](index.md) -- [DriveBoard](driveboard.md)

The electronics subsystem consists of the [DriveBoard](driveboard.md) and its sensing and control peripherials: **laser** system, **gantry** steppers, **limit** switches, **door** switches, **chiller**. Additonally it implements a reliable **stop** mechanism.

**WARNING**: The laser PSU supplies the laser tube with roughtly 25kV. This poses a **lethal risk**. Take special care when dealing with the red power cable (rear side of the laser tube) and make sure **proper insulation** is in place before flipping the on switch. Also be informed that the capacitors inside the PSU may possibly stay charged after disconnecting from grid power.

Schematic
---------

[svg](img/wiring-lasersaur-control.svg) | [high-res bitmap](img/wiring-lasersaur-control.jpg)

![Wiring Schematic](img/wiring-lasersaur-control.jpg)


Assembly of Control and Sensor Wires
------------------------------------
The Driveboard makes extensive use of standard Ethernet patch cables. Laser control, stepper control, e-stop, and all the sensors use them.

Please make sure to use standard patch cables with the following properties: Cat5 , **shielded** (FTP, STP, SFTP), **stranded**, 26 or 25 AWG. Cables with solid leads, cables without a shield, or 27+ AWG cross-section are not suitable. (also see: [Cat5](https://en.wikipedia.org/wiki/Category_5_cable))

### Limit and Door Switches

![switches 01](img/wiring-switches-01.jpg)
![switches 01](img/wiring-switches-02.jpg)
![switches 01](img/wiring-switches-03.jpg)
![switches 01](img/wiring-switches-04.jpg)
![switches 01](img/wiring-switches-05.jpg)
![switches 01](img/wiring-switches-06.jpg)


Checklist
---------

1. Is the high-voltage wire (red wire to backside of tube) properly insulated with the insulation cover?
2. Are the AC wires properly insulated and is the Lasersaur frame grounded?
3. Does the E-Stop turn off the machine?
4. Has the chiller's water circulations been properly tested and is the tubing mounted in ways not to cause stress on the inlet and outlet ducts.
