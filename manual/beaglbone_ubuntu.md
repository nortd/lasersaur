Configure Ubuntu for Lasersaur
================================

**DEPRECATED**

The following guide is to be used on a Linux computer (may also work on OSX). These instruction were partially extracted from the following resources:

- http://www.elinux.org/BeagleBoardUbuntu
- http://embeddedprogrammer.blogspot.co.at/2012/10/beaglebone-installing-ubuntu-1210.html


Preparation of the BeagleBone SD-Card
-----------------------------------
- download Ubuntu 12.04 (arm, minimal) image
  - `wget http://rcn-ee.net/deb/rootfs/precise/ubuntu-12.04-r9-minimal-armhf-2012-11-29.tar.xz`
  - `tar xJf ubuntu-12.04-r9-minimal-armhf-2012-11-29.tar.xz`
  - `cd ubuntu-12.04-r9-minimal-armhf-2012-11-29`
- clone image to sd-card (must be 4gb)
  - make sure /dev/sdb is actually your sd-card (!)
  - `sudo ./setup_sdcard.sh --mmc /dev/sdb --uboot bone`

Configuration on BeagleBone
----------------------------
- connect BeagleBone to router and ssh into it
  - `ssh ubuntu@xxx.xxx.xxx.xxx`
  - password is: temppwd
- enable root, become root
  - `sudo passwd root`
  - `su`
- change name in /etc/hostname and /etc/hosts
  - replace arm with lasersaur
- install/remove packages
  - `sudo apt-get update`
  - `apt-get install avahi-daemon`
  - `apt-get install arduino-core`
  - `apt-get install git`
  - `apt-get install screen`
  - `apt-get purge apache2; apt-get autoremove`
- install LasaurApp
  - `git clone git://github.com/stefanix/LasaurApp.git`
  - in the future, simply update with `cd ~/LasaurApp; git pull`
  - place script in: `/etc/init.d/lasaurapp.sh`
  - make executable: `sudo chmod 755 /etc/init.d/lasaurapp.sh`
  - activate with: `sudo update-rc.d lasaurapp.sh defaults`

### lasaurapp.sh

    #!/bin/bash
    # place in: /etc/init.d/lasaurapp.sh
    # make executable: sudo chmod 755 /etc/init.d/lasaurapp.sh
    # activate with: sudo update-rc.d lasaurapp.sh defaults
    # deactivate with: sudo update-rc.d -f lasaurapp.sh remove

    if test "$1" = "start"
    then
        echo "Starting LasaurApp ..."
        /usr/bin/python /root/LasaurApp/backend/app.py -p --beaglebone
    fi


Wifi Configuration
--------------------
You can Wifi-enable the system by adding a usb wifi dongle and doing the following. This works with dongles that use the rtl8192cu chipset, for example the Edimax EW-7811Un or the [OurLink](http://www.adafruit.com/products/814).

- edit /etc/network/interfaces
  - for wpa-ssid and wpa-psk, enter you access point name and passphrase
- restart BeagleBone


Deactivate Root Account
-----------------------
This is useful to add some more security. For admin tasks you would then use the sudo command.

- rename ubuntu user to pi
  - `usermod -l pi ubuntu`
  - `usermod -c "lasersaur user" pi`
  - `usermod -md /home/pi pi`
  - `groupmod -n pi ubuntu`
- lock root account (optionally)
  - `sudo passwd -l root`


Other
------
- check what service are listening for connections
  -  `netstat -plnt`
- backup sd-card
  - `sudo dd if=/dev/<sdx> | gzip > /path/to/image.gz`
- restoresd-card
  - `gzip -dc /path/to/image.gz | sudo dd of=/dev/<sdx>`
- backup/restore with progress
  - `sudo dd if=/dev/<sdx> | pv -s 4G -peta | gzip -1 > /path/to/image.gz`
  - `gzip -dc /path/to/image.gz | pv -s 4G -peta | sudo dd of=/dev/<sdx>`


