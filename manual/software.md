
Lasersaur Software
==================

[Index](index.md) -- Lasersaur Software | [BeagleBone Setup](bbb_setup.md) | [LasaurApp Setup](lasaurapp_setup.md) | [Firmware Setup](firmware_setup.md)

**A Lasersaur is fully controllable by web browser.** Simply go to: [http://lasersaur.local](http://lasersaur.local) and Lasersaur's user interface will show up. This is a local web connection to the Lasersaur on the same network, no cloud necessary. There is no software or driver installation required on the controlling computer which, btw, can be even beyond the world of mainstream operating systems. Consequently there is no dedicated, typically neglected, Windows workstation in the mix. Everybody just uses their laptop/desktop/tablet directly. Now go play ... or read on if you are interested in the multifaceted details.


### The Software Stack

The entire software stack comprises a Linux OS, the LasaurApp, and a firmware. Linux runs off the DriveBoard's BeagleBone (BBB). LasaurApp runs partly on this Linux platform and partly in the browser. The firmware runs on a dedicated real-time chip (Atmega328) on the DriveBoard. All in all this is a setup with great modularity and hackability yet runs out of the box with minimal setup (if there was a box).

### LasaurApp

- send vector files to the Lasersaur
- import files and optimize
- convert file formats (SVG, G-Code ([subset](gcode.md)), DXF ([subset](dxf_import.md))
- GUI for moving/jogging the laser head
- stopping/pausing/continuing jobs
- firmware flashing
- handy G-code programs for the optics calibration process

![LasaurApp v13.04](http://farm9.staticflickr.com/8101/8645800331_8c4350fd2c_z.jpg)


### Software Setup

On the Lasersaur's [DriveBoard](driveboard.md) runs a certain software stack that needs to be installed once. You have the option to skip these steps by getting the Assembled DriveBoard from the [Lasersaur Store](http://store.lasersaur.com/). To install the software yourself do the following:

- [Setup Linux on BeagleBone Black (BBB)](bbb_setup.md)
- [Setup LasaurApp on BBB](lasaurapp_setup.md)
- [Setup LasaurApp firmware](firmware_setup.md)


### Prerequisites

- A modern web browser with HTML5 support
- A local network connection between user and Lasersaur
- A [zeroconf](https://en.wikipedia.org/wiki/Zero-configuration_networking) client to resolve `lasersaur.local`.
  - On OSX this is called Bonjour and part of the OS.
  - On Linux this is typically part of the OS and named Avahi.
  - Windows does not have this out of the box but many popular apps (Skype, iTunes and Adobe Photoshop) install one. You can also install [Bonjour Print Services for Windows](http://support.apple.com/kb/DL999) to make the local domain names work.


### Developers

Run LasaurApp directly on your computer. For details see: [LasaurApp Dev Setup](dev_setup.md)
