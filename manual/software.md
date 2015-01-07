
Lasersaur Software
==================

[Index](index.md) -- Lasersaur Software | [BeagleBone Setup](bbb_setup.md) | [LasaurApp Setup](lasaurapp_setup.md) | [Firmware Setup](firmware_setup.md)

**The Lasersaur is fully controllable by web browser.** Simply go to: [http://lasersaur.local](http://lasersaur.local) and Lasersaur's user interface will show up. This is a local web connection to the Lasersaur in the same network, no cloud necessary. There is no software or driver installation required on the controlling computer. Consequently there is no dedicated, neglected, virus-ridden Windows workstation in the mix. Everybody just uses their laptop/desktop/tablet directly.

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
