BeagleBone Angstrom Setup 
==========================

[LasaurApp](lasaurapp.md) | [DriveBoard](driveboard.md) | [BeagleBone](beaglebone_setup.md) | [RaspberryPi](raspberrypi_setup.md)

[Angstrom Linux](http://www.angstrom-distribution.org/) is pre-installed on the BeagleBone and it's possible to use it for the Lasersaur. Nonetheless we recommend using Ubuntu as it's easier to configure (especially WiFi). For setting up the BeagleBone with Ubuntu please checkout the main [BeagleBone Setup](beaglebone_setup.md) page.


### (DEPRECATED)

For this some command line skills are helpful. Need to brush up? Here is a great [command line tutorial](http://www.linuxcommand.org), well worth the time.

- [BeagleBone Guide](http://beagleboard.org/static/beaglebone/latest/README.htm)
- [Angstrom Manual](http://www.linuxtogo.org/gowiki/AngstromManual)
- [A BeagleBone Linux 101](http://www.gigamegablog.com/2012/01/29/beaglebone-linux-101-configuring-angstrom-linux/)


Connecting
----------

To do anything we need to have shell access. This is done by [ssh](http://en.wikipedia.org/wiki/SSH_client)'ing into the BeagleBone. The following will show how this is done with the ssh command that is standard on Linux and MacOS. On windows this can be done with [Putty](https://en.wikipedia.org/wiki/PuTTY).

The BeagleBone can establish a network connection over Ethernet, USB, and WiFi (given a usb dongle is installed). This guide focuses on Ethernet as it works out-of-the-box on all major operating systems. Connecting via USB also works without driver installation on Linux and MacOS and is useful for quick testing (connect via mini usb cable, then *unmount* the BEAGLEBONE drive).

- Connect BeagleBone to Ethernet port (either directly or via switch).
- Run: `ssh root@beaglebone.local` (use empty password)

On windows you would use Putty to connect to 'root@beaglebone.local'. On Linux (Ubuntu) you may have to configure your wired Ethernet manually. Set the "IPv4 Settings" to "Link-Local only".
 

Setup Overview
---------------
- Set password
- Set hostname, make available at `lasersaur.loacal`
- Deactivate unnecessary services
- Install software packages
- Install LasaurApp


Setup Step-by-Step
------------------
- Set a root password:
  - Run `passwd`
- Deactivate default services:
  - `systemctl disable bone101.service`
  - `systemctl disable cloud9.service`
  - `systemctl disable gateone.service`
- Change hostname from `beaglebone` to `lasersaur`:
  - Change name in `/etc/hostname` from "beaglebone" to "lasersaur".
  - Also add "127.0.0.1 lasersaur" to `/etc/hosts`.
  - Restart (command is `reboot`).
  - After rebooting it will make itself known as "lasersaur.local" so your ssh command will have to be changed to `ssh root@lasersaur.local`
- Install packages:
  - Specifically we need "avrdude" for firmware flashing and "git" for easily downloading/updating LasaurApp.
  - If the BeagleBone has access to the internet package installation can be done exclusively with the `opkg` command. (Otherwise the packages have to be manually copied to the BeagleBone from the [Angstrom repository](http://www.angstrom-distribution.org/repo/).)
  - Update package index (takes a while): `opkg update`
  - Install any updates: `opkg upgrade`
  - Install avrdude: `opkg install avrdude`
  - Install git: `opgk install git`

Finally Install LasaurApp
-------------------------

- Download LasaurApp sources with git:
  - in root directory run: `git clone git://github.com/stefanix/LasaurApp.git` 
  - you now should have a directory called "LasaurApp"
- Test-run by typing: `python LasaurApp/backend/app.py -p --beaglebone`
  - point browser at [lasersaur.local](http://lasersaur.local)
  - ctrl-C to exit
- If you every need to update LasaurApp run: `git pull` from within the LasaurApp directory and restart.

### Register LasaurApp as a Service at Boot Time
Go to `/lib/systemd/system` and create `lasaurapp.service` with the following content:
  -----
<pre>
[Unit]
Description=LasaurApp Web Server
ConditionPathExists=|/usr/bin/python

[Service]
ExecStart=/usr/bin/python /home/root/LasaurApp/backend/app.py -p --beaglebone

[Install]
WantedBy=multi-user.target
</pre>
  -----

Then enable the service with `systemctl enable lasaurapp.service` and restart (command is `reboot`).


