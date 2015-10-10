
Troubleshooting Common Problems
===============================

Complex systems can fail in prolific ways. This page serves as a collection of common problems and how to solve them. Alternatively search our [mailing list](https://groups.google.com/forum/#!forum/lasersaur) archive and also do not hessitate to post yourself.


Cutting Precision and Sporadic Offsets
--------------------------------------
The following deals with some common problems regarding cutting accuracy. Accuracy issues below 1mm are very often related to adjustment shortcomings at the belts, rollers, and/or optics. Accuracy issues above 1mm are evidence for deeper mechanical or electrical problems. For details see [Stepper Motors Losing Steps](#stepper-motors-losing-steps). 

#### Low Belt Tension
This is probably the number one cause for small offsets (sub-mm). Due to a loose belt the cart has some wiggle room. Cuts in opposite direction will be offset to whatever range the loose belt allows. To fix, make sure to increase the belt tension by repositioning the idler. Loosen the idler screw, push the idler screw outwards at its base with the help of a thin screw driver (which you slide in between extrusion and ball bearing), tighten firmly in new position.

#### Belt/Y-Cart Alignment
The y-cart has two belts which assure the perpendicularity of this cart. The lack of alignment rotates the cart along its vertical center axis. Always make sure this cart is perpendicular to the rails. Especially adjusting y-belt tension can cause misalignment. To adjust, loosen one shaft coupling's set screw, push the y-cart all way back gainst its end stops, and retighten the set screw.

#### Shaft Slippage
All the shaft couplings and pulleys which transfer the motor torque to the belt can potentially slip under heavy load. Make sure all the set screws are firmly tightened (without breaking their threading). Also make sure the shafts did not inadvertently get lubricated. To check, draw a line across coupling/pulley and shaft.

#### Cart/Rail Misalignment
Play between the rollers of the x-cart/y-cart and the rail can cause accuracy problems. In very bad cases this can even max-out the stepper motors and cause them to loose steps (see: [Stepper Motors Losing Steps](#stepper-motors-losing-steps)). In minor cases it may reduces positioning accuracy. Generally make sure non of the carts can tilt around and firmly grab the rails with their roller ball bearings. The pressure on the rollers should be evenly distributed. This can be checked by manually rotating the rollers while they touch the rail. Resistance should be equal. Specifically check if the entire y-cart has left/right wiggle room. If yes, adjust the corresponding rollers.

#### Optical Misalignment
In a perfectly built and adjusted Lasersaur the laser beam is always in the center of all mirrors and perpendicular/parallele to the gantry. This results in a perfectly vertical and centric last laser beam leg through the lens and nozzle. Misalignments in the mechanics and mirrors can cause the laser beam to wander around on the mirrors. This decreases absolute positioning accuracy. In bad cases it will even cause the laser to hit the inside of the nozzle and lead to reflections and defocusing. Since this may only happen in certain places of the cutting area you should always be testing proper alignment throughout the entire cutting area.




Stepper Motors Losing Steps
---------------------------
Losing steps is a fairly common issue with stepper motor systems. It is caused by either the gantry having too much resistance (rail or belt) or the stepper too little torque. You fix it by making sure the gantry is aligned and clean and the motors are functioning properly.

#### Rail Resistance
Generally speaking the gantry is fine if there is no noticable misalignment and/or visible dirt build-up on the rails. Technically one of the ball bearing rollers can also fail but this is unusual. Test the carts with the stepper belt disconnected because the motors self-induce and cause friciton that oddly feels like a rail problem. Align all the rollers so they grab the rail nicely. Tilt the cart in all directions and make sure this still holds true. Every roller should be in contact but not so hard that you cannot manually rotate it any more. Also when you manually rotate them (while in light contact with the rail) they should all have about the same resistance. This gives you a sense how hard they press against the rail. If a roller presses onto the rail too hard you are just unecessarily wearing down your rail.

#### Belt Resistance
The v14.03 system is quite tolerant about belt tension. Still the belts can be over-tensioned. Basically when the tension reaches levels that causes shafts, idlers, and pulleys to bend you may introduce unecesary friction into the system.

#### Stepper Motor Torque
Stepper motors are fairly fragil and do not take impact well. Dropping them on the floor may break them and may require replacing them. That being said, a lack of torque is usually caused by an electrical problem. Firstly, check the wiring. A loose connection is typical for weak and jerky steppers (This may also cause increased noice in the electronics and possibly even sudden stops and reboots).

  - Is the 24V PSU supplying enough Volts/Amps?
  - Are all the 24V PSU wires well connected?
  - Are all the terminal connector screws of the stepper driver well tightened?
  - Is the patch cable form the DriveBoard to the Stepper sound?
  - Is the socket of the stepper well connected to the stepper wires?

Secondly make sure the current set resistors are correct. They are located next to the stepper drivers on the DriveBoard. In v14.03 there should be a 6.49K resistor next to the x-axis stepper driver and a 11.5K resistor next to the y-axis driver. If in doubt you can also cut these resistor off the board and set the stepper current through dip switches on the stepper drivers. See the [Geckodrive G201X manual](http://www.geckodrive.com/g201x-g210x-rev-6) for this (use x-axis: 0.8A, y-axis: 2A). 
