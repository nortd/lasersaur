[Index](index.md) -- [bom](bom.md) | revisions

This is the place to keep track of all the revisions and future plans to hardware, software, BOM, and documentation. Version numbers also mean the following: `v[year].[month]`. For further details also check out the [LasaurApp Commit Log](https://github.com/stefanix/LasaurApp/commits/master). For even more details strike up a conversation on the mailing list.


Roadmap
--------
  - raster engraving

Revisions
---------
### Minor Model/Bom update
  - changed y-drive shaft coupling MCKSC20-6-6 to MCSSC20-6-6
  - readded a missing FWS-D19-V15.0-T1.0 to the BOM

### LasaurApp v14.11b
  - Improved compatibility with various SVG authoring apps.
    Especially Inkscape v0.91 is fully supported.
  - Fixed circle, ellipse, rounded rect issues.
  - Fixed g-code name postfix, so same files can also be imported again, duh!
  - Improved seek optimization.
    LasaurApp can now process any path in both directions and
    seek optimization also looks for closest end points.
    This reduces a lot of weird movement artifacts.

### v14.03
  - x/y-drive idlers slightly optimized
    - slide washer removed, third ball bearing added
    - pre tslot nut instead of post tslot nut
  - LED light strip for bed illumination added to BOM
  - usb entry module removed from BOM
    - (new WiFi module has good reception from inside the machine)
    - entry panel hole cover added

### v14.03-rc3
  - BOM, different cover panel (old panels increased in price signifficantly)
    - HFPAL-3 instead of PDSPHC4H
    - PAAL 2mm instead of PDSPHC4H for bottom panels
  - BOM, minor change to washers for limit switch magnets
    - now only one G-Form washers between magnet and extrusion
  - slit panels slightly increased in length to reduce center gap (minor)

### v14.03-rc2
  - BOM corrections
     - HFS5-2040-55-TPW instead of HFS5-2040-55-LTP
     - one HFS5-2040-1620 was missing

### v14.03-rc1
The main change here is a new lens/nozzle assembly based on a
sliding design. It's easier to adjust, can handle lenses down to
25mm focal length and has 40mm range. The other changes are
non-functional but simplify the build process and make aligning
much easier. Along with this we also switched to standard ball
bearings on M5 screws for all the cart rollers.

  - frame-bottom
    - made cable carrier base extrusion symmetric, added one left
      (allows for second cable carrier to run cameras, etc. to head)
    - outer separation panels part of Mount Pack, custom-cut
    - custom-cut cable/air tube passage holes in outer right separation
      panel. Passage holes allow pre-assembled cables to run through.
      Cover part to close extra space.
  - frame-top
    - four separation panels analog to frame-bottom. Outer panels
      are custom-cut and part of Panel Pack.
  - x-cart (build simplifications)
    - aluminum plates mount now to the end of the extrusions
      to eliminate alinment steps
    - rollers are now standard 5x14x5 ball bearings on M5 screws
    - adjustment ball bearing shaft screws are now supposed to touch
      t-slot base and reverse nut is not necessary anymore
    - additional mount plate for cable carrier
    - washers under limit sensors
  - y-cart (build simplifications)
    - rollers are now standard 5x14x5 ball bearings on M5 screws
    - adjustment ball bearing shaft screws are now supposed to touch
      t-slot base and reverse nut is not necessary anymore
    - washers under limit sensors
  - optics-laser
    - mirror mount one
      - angle mount extrusion shortened to align with mirror mount
      - vertical mount extrusion extended to align with angled extrusion
    - mirror mount two
      - angles mount extrusion shortened to align with mirror mount
    - nozzle lens assembly (improved focusing mechanism)
      - 2" lens tube held by Thorlabs CP12 part
      - nozzle friction-fit into 2" lens tube
      - MechParts mount plate modified to hold a sliding lens tube
  - electronics
    - e-stop moved to top panel
  - frame-panels
    - door front panel minimal overlap to reduce chopping danger
  - reorganized subsystems
    - frame-outer split up into frame-bottom and frame-top
    - frame-panels split up into frame-panels and door-panels
    - optimized build order of subsystems
    - columns of frame-table moved to frame-bottom
    - moved limit switch magnets to x-cart, y-cart
    - moved belt attachment screws to x-cart, y-cart
    - moved door sensors to frame-door
    - moved entry panel to frame-bottom
  - reorganized BOM
    - ThorLabs items available through Lasersaur store
      as "Mirror Mount Pack" and "Optics Accessory Pack"
    - DriveBoard peripherials available through Lasersaur store
      (mostly wired with DriveBoard-compatible modular plugs)
      - "Stepper X-Drive" and "Stepper Y-Drive"
      - "DriveBoard DIY Pack" and "DriveBoard Assembled"
      - "Stepper Driver Pack"
      - "E-Valve Assembly"
      - "Door Sensor Pack"
      - "Limit Sensor Pack"
      - "E-Stop Assembly"
      - "DriveBoard Wiring Pack"
      - "Power Supply Pack"
      - "Zip Ties"
      - "Rubber Tape"


### v14.01b
- magnetic limit switches moved slightly
 - mount holes for y1, y2 moved 2mm closer towards y-cart (now 14mm from edge)
- lock screws for top bearing in x-drive gear moved to overlap bearing 0.5mm more
- lens tube hole on x-cart reduced in diameter slightly (had 1mm of play)
- screws in outer idlers of y-drive flipped
- CAD model cleaned up
- 1" SM1 lens tube now part of Lasersaur Nozzle (BOM shuffled around a bit)

### v14.01

- improved drive system for higher precision and easier maintenance
- magnetic limit switches for easier cleaning

For details see [revision v14.01 plans](rev14.01.md).

### v13.06
- BeagleBone Black in BOM, preconfigured option
- entry panel now from 3mm tinted acrylic, sealed with rubber inserts
- acrylic mount panels now available in Nortd Labs store for convenience
  - this includes entry panel, DriveBoard bottom hull, and top hull
- Minor DriveBoard adaptation for BeagleBone Black compatibility
  - moved avr reset control from GPIO2_7 to GPIO2_9 because BBB does not boot otherwise

### v13.04 - BOM
- minor, moved a few components between subsystems
- added power entry module filtered, Mouser 5110.1033.1 (for good measure)
- magnetic limit switch mount screws (optional)

### v13.04 - Driveboard Image
- New Linux image for the Driveboard, see [BeagleBone Setup](beaglebone_setup.md)

### v13.02 - BOM update
- switched back to higher-amp motors (low-amp motors were a bit noisy)
  - Nanotec ST5918M3008-B (instead of ST5918M1008-B)
  - LinE WO-5718M-02ED (instead of WO-5718M-04ED) and WO-4118S-01F (instead of WO-4118S-04E)
- custom nozzle added
  - removed 4 Thorlabs items: SM1V05, SM1V10, SM1CP2M, SPW602
  - added: lock ring, Thorlabs SM1NT
- optics pack added: lens, 3x mirrors
- moved beam axis 1mm to left, optimize for 3mm (thickness) mirrors
  - mirror1 2mm to left, laser orifice 2mm to left
  - optics tube 1mm to right
- removed optics cleaning system from bom
  - Reason is that compressed air typically contains oils which
    causes more problems than is solves.
- added optics cleaning wipes and swabs (to be used with acetone)
- capacitors added to bom for v13.03 DriveBoard update



### v13.02 - LasaurApp
- stop button (formerly cancel, works now always immediately)
- pause/continue button
- ready state to prevent  disturbing a running job
- basic DXF file support
- new firmware v13.02b
  - beam dynamics conservatively activated
  - lower acceleration to reduce ripples resulting from tight junctions
- chiller and door status now in the header bar, not filling up the log
- job time estimations tweaked, mostly correct +/- 20%
- bugfix: bottleneck related to DNS request when running over a LAN
- various smaller bugfixes


### v13.01 - LasaurApp, the DriveBoard Update
- Tested with new DriveBoard hardware
- Firmware flashing from GUI
  - DriveBoard v13.01 firmware
  - LasaurShield v13.01 firmware (need testers!)
  - LasaurShield v12.08f firmware (for easy downgrading after testing)
- LaserTags - save cutting parameters in SVG files
  - see: [LaserTags](lasertags.md)
- Up to 32 passes
- Generates air assist control gcode (M80/M81).
- Control buttons for air assist.
- Gcode support (M82/M83) for aux1 output (e.g gas assist)
- rough cutting time estimation
- improved log view
- auto-connect on startup
- some bugfixes in svg parser (maybe added some other bugs ;)
- flashing directly from beaglebone if avrdude package is installed


### v12.11
This revision is primarily about the new DriveBoard. This replaces the LasaurShield/Arduino setup. Secondly we have upgraded the custom parts from acrylic to aluminum.

- DriveBoard
  - fully integrated LasaurApp server and network interface
  - all control and sensor wiring with shielded Cat5 patch cables
  - z-axis ready, for setups with a movable cutting table
  - low-voltage interlocks (for e-stop and optional keyswitch)
  - solid state relay switching of AC loads
  - two outputs for heavy inductive loads (solenoid air valves)
  - improvements to hard-logic safety system
  - built from common, easy to source components
- MechParts
  - the custom parts made from 6mm aluminum
  - no cracking from over-tightening
  - mostly identical to acrylic parts
  - simpler x-stepper mount
  - threaded mount M2.5 mount holes for limit switches
- Minor other updates
  - frame-table slat direction changed from front-to-rear to left-to-right
  - y-bar 2mm longer
  - y-cable carrier, 23 links, one more
  - x-cable carrier, 40 links, two less
  - added air valve M3 mount screw and tslot nut

### bom v12.08b
  - added parts for optics cleaning system; small tubing of compressed air to all optics parts to keep them reliably clean and prevent burn-ins.

### v12.08a
  - power sensor cable changed to shielded
  - power/chiller sensor cable shield pins changed in wiring schematic
  - BOM supplier change: mirror optics now from ColeTech instead of Thorlabs
  - BOM addition: nozzle end cap, Thorlabs SM1CP2M


### v12.08
This revision introduces a new improved gantry, a simplified frame, and many small optimizations. It was made possible through generous support by Hyperwerk.ch and Studio for Creative Inquiry at Carnegie Mellon University. For details on changes see the CAD models and [BOM](/lasersaur/manual/bom).

  - simplified frame
    - larger door, better access to work area
    - separate compartment for laser system and electronics
    - more mount space for alternative laser systems (Synrad Firestar f201 anybody)
    - more rigidity
    - one (recessed) entry panel for all connections
    - no more foam tape
    - rear door slit fully sealed
  - improved gantry
    - more elegant integration of air assist
    - more rigidity
    - easier maintenance (replacing rollers, rails)
    - adjustable rails (for compensating frame imprecisions)
    - less custom parts
    - adjustable rollers and belt tensioners take advantage of tslots
  - optics
    - three times the same mirror mount
    - focus adjustment tube at the top so air assist nozzle can stay in place
    - using 75mm focus lens by default for better performace with thick materials
    - air assist tubing included in BOM
    - rubber tape for laser tube attachment points
  - electronics
    - Lin Engineering Steppers for North America BOM
    - "x-current" resistor for NA BOM to 12.7K (instead of 6.5K)
  - general
    - post assembly tslot nuts for most connections -> simple nut loading
    - all M5 tslot nuts with threadlocking resin to omit lock washers
    - all fasteners from Misumi
    - bigger e-stop button

### v12.06 (aka LasaurApp under the Hood)
  - LasaurApp
    - path optimizations using the fine Ramer–Douglas–Peucker algorithm
    - line joining of segmented pseudo-polylines
    - automatic unit conversion using the page size
    - seek time optimizations by sorting geometry based on a greedy, lowest distance algorithm


### v12.05 (aka LasaurApp new UI)
  - LasaurApp
    - new user interface
    - persistent job queue
    - boundary box indication
    - svg import of line colors
    - multiple passes
    - color/geometry assignment to any of the passes
    - new laser intensity range 0-100%
    - direct control including jog buttons
    - offset support
  - LasaurGrbl
    - slightly better error reporting
    - instead of "Error: stopped" it indicates any of the following
      - "Error: Power Off"
      - "Error: Chiller Off"
      - "Error: Limit Hit"

### v12.02 (aka "zero")
  - opto-isolated stepper drivers to reduce noise in electronics
    - Geckodrive G203V (instead of G251X)
    - this changes the pin configuration on the LasaurShield
      - Pin 1 to 12 is: power-, power+, A, /A, B, /B, dis, dir, step, logic-, currset, currset
      - instead of: power-, power+, currset, currset, A, /A, B, /B, dir, step, dis, logic-
      - also the current set resistors are different on this driver
  - stepper motors that are easier to source and cheaper
    - Nanotec ST4118M1206-A (instead of LinEngineering WO-4118S-0
