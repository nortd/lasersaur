---
title: Document Center
---

LasaurApp
=========

LasaurApp | [DriveBoard](driveboard) | [BeagleBoneBlack](bbb_setup) | [LaserTags](lasertags) | [DXF Support](dxf_import)

LasaurApp is the main control app for the Lasersaur. It is installed on the Lasersaur and accessed over the local network (ethernet or wifi) with a web browser. A Lasersaur typically does not require any software or driver installation on the user's computer and is conveniently access via [http://lasersaur.local](http://lasersaur.local).

The main features are as follows:

- send vector files to the Lasersaur
- import files and optimize
- supported file formats are: SVG, G-Code ([subset](gcode)), DXF ([subset](dxf_import)) 
- GUI for moving/jogging the laser head
- stopping/pausing/continuing jobs
- firmware flashing
- handy G-code programs for the optics calibration process

![LasaurApp v13.04](http://farm9.staticflickr.com/8101/8645800331_8c4350fd2c_z.jpg)


LasersaurBBB Configuration
--------------------------

[LasersaurBBB](/lasersaur/store#la-bbb) is our pre-configured BeagleBone Black with wifi module. It's ready to serve the Lasersaur GUI to your Firefox/Safari/Chrome/IE browser. For this to work your computer and the BeagleBone need to be on the same network.

### Ethernet
- Simply plug the BeagleBone into the same access point as your computer.
- Open  [http://lasersaur.local](http://lasersaur.local)
- Done!

On most access points this will work without complications. The most common reasons it may fail are: (1) AP does not route between ethernet and wifi. Try plugging computer also into ethernet. (2) AP does not run a DHCP server or the DHCP server fails to provide a lease to the BeagleBone. If you have access to the AP control panel take a look at the settings. Maybe the leases are limited and they are all handed out already.

### Wifi
- ssh to the BeagleBone and edit the `/etc/network/interfaces` file to match your wifi access point name and password (replace "the internets" and "itpinthehouse").
- Reboot and connect your computer to the same wifi AP
- Open  [http://lasersaur.local](http://lasersaur.local)
- Done!

You may have a few question at this point.

- What's ssh?
  - Secure SHell gives you full control of the BeagleBone.
  - On Linux and OSX you run it like this from the Terminal: `ssh root@lasersaur.local`
  - On Windows you use a program called Putty, among others.
  - Default password is: bone
- How to connect if the wifi is not configured?
  - Connect by ethernet or configure your wifi access point to the LasersaurBBB defaults.
  - By default the LasersaurBBB will try to connect to:
    - SSID: "the internets"
    - pass: "itpinthehouse"
    - encryption: WPA
  - BTW: most Android phones can be configured as a WiFi AP.

If you run into problems feel free to ask on the mailing list. Make sure to provide a detailed description of the issue at hand. Better questions naturally get better answers.

### Network Security

Please make sure to use the default Wifi configuration only initially to configure your own AP name and password. Also make sure to change the default ssh password on the BeagleBone:

- ssh into the Lasersaur: `ssh root@lasersaur.local`
- set new root password: `passwd`


Updating
------------

LasaurApp can be automatically updated over the network. For this log into the Lasersaur with your favorite secure shell program and pull the latest version from our [git repository](https://github.com/stefanix/LasaurApp).

- ssh into the Lasersaur: `ssh root@lasersaur.local`
- pull latest LasaurApp: `cd LasaurApp; git pull`



Advanced Topics
---------------

### Installation on Vanilla BeagleBone

If you want to use a vanilla BeagleBone (Black) on the DriveBoard you can also set it up yourself by following these guides:

- [Setup BeagleBone Black](bbb_setup)
- [Setup BeagleBone](beaglebone_setup)
 


### Flashing the Firmware

The Lasersaur hardware also needs to be loaded with firmware. This has already been done if you got yourself an assembled DriveBoard. In all other cases LasaurApp can flash the firmware for you. In the header menu go to Admin/Flash Firmware. This works as long as you are connected and the Atmega328 has an [Arduino bootloader](http://arduino.cc/en/Hacking/Bootloader) on it.


### Compiling Custom Firmware

LasaurApp (starting with v13.06b) makes it easy to run custom firmware. For small changes (e.g. in the config.h file) one click on `Admin/Build and Flash from Source` builds a new firmware and asks if it should be flash-uploaded. The firmware source code from which it gets build is in `LasaurApp/firmware/src`. These files can even be directly edited through an ssh session with `vi` or `nano`. Happy Hacking!


### Developer Setup

Use this if you want to take a quick peak at the interface or you are a developer hacking on the code.

LasaurApp is quite flexible software and can also be run on any Windows, OSX, and Linux computer. This is not the recommended way but useful for developers working on the code. It's also useful for taking a look at the interface or setting up a laser cutter without a DriveBoard (e.g: with a USB-to-serial converter). In this case the LasaurApp backend runs on the computer and the browser connects locally.

- Open the Terminal/CommandLine.
- Make sure you have Python 2.7, run `python --version`
  - If not, get 2.7.x installers from the [Python Website](http://python.org/download/).
  - On Windows we recommend using the [ActiveState distribution](http://downloads.activestate.com/ActivePython/releases/2.7.2.5/ActivePython-2.7.2.5-win32-x86.msi) as it sets all the PATH shortcuts.
- Download the latest [stable LasaurApp](https://github.com/stefanix/LasaurApp/zipball/master) and unzip to a convenient location.
  - For advanced users we recommend using `git clone git://github.com/stefanix/LasaurApp.git` instead. This way you can easily update with `git pull`
- Go to that location in the Terminal/CommandLine and run `python backend/app.py`

At this point your default browser should open at [http://localhost:4444](http://localhost:4444). LasaurApp runs in any current Firefox or Chrome, and future Safari 6 or IE 10. Congrats!

On Windows you may have to specifically tell the program which COM-port to use by typing "python backend/app.py COM7" where COM7 is the actual port the Lasersaur is connected to. One of the easiest ways to figure this out is to run the Arduino IDE and look under "Tools/Serial Port".

On Linux you may have to set proper r/w permissions for the serial port. For quickly testing and bypassing this issue you can also run LasaurApp as root by typing "sudo python backend/app.py".



