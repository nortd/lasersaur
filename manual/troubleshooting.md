

Lack of Precision
-----------------
We have seen some common problems causing a lack of precision in the cutting accuracy.
- optical mis-alignment
- gantry carts loose on rails
- y-cart not perpenticular
- slip of shaft couplings
- loosing steps



Lasersaur is Losing Steps
--------------------------
Loosing steps is a fairly common issue with stepper motor systems. It is caused by either the gantry having too much resistance (rail or belt) or the stepper too little torque. You fix it by making sure the gantry is aligned and clean and the motors are functioning properly.

### Rail Resistance
Generally speaking the gantry is fine if there is no noticable mis-alignment and/or visible dirt build-up on the rails. Technically one of the ball bearing rollers can also fail but this is unusual. Test the carts with the stepper belt disconnected because the motors self-induce and cause friciton that oddly feels like a rail problem. Align all the rollers so they grab the rail. Tilt the cart in all directions and make sure this still holds true. Every roller should be in contact but no so hard that you cannot manually rotate it any more. Also when you manually rotate them (while in light contact with the rail) they should all have about the same resistance. This give you a sense how hard the press against the rail. If a roller presses onto the rail too hard you are just unecessarily wearing down your rail.

### Belt Resistance

### Stepper Motor Torque
Stepper motors are fairly fragil and do not take impact well. Dropping them on the floor may break them and may require replacing them. That being said, a lack of torque is usually caused by an electrical problem. Firstly, check the wiring. A loose connection is typical for weak and jerky steppers (This may also cause increased noice in the electronics and possibly even sudden stops and reboots).

  - Are all the 24V PSU wires well connected?
  - Are all the terminal connector screws of the stepper driver well tightened?
  - Is the patch cable form DriveBoard to Stepper sound?
  - Is the socket of the stepper well connected to the stepper wires?

Secondly make sure the current set resistors are correct. They are located next to the stepper drivers. In v14.03 there should be a 6.49K resistor next to the x-axis stepper driver and a 11.5K resistor next to the y-axis driver. If in doubt you can also cut these resistor off the board and set the current trough dip switches on the stepper drivers. See the [Geckodrive G201X manual](http://www.geckodrive.com/g201x-g210x-rev-6) for this (use x-axis: 0.8A, y-axis: 2A). 
