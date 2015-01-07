RaspberryPi Setup
==================
**DEPRECATED**

- http://blog.makezine.com/2012/12/25/ten-raspberry-pi-tips/
- http://interlockroc.org/2012/12/06/raspberry-pi-macgyver/


HowTo
------

- hook up router with dhcp server
- alternatively hook up directly, configure internet sharing 
  (local dhcp, nat), find IP
  - osx: cat /private/var/db/dhcpd_leases
  - ubuntu: cat /var/lib/misc/dnsmasq.leases
- ssh pi@xxx.xxx.xxx.xxx
  - default password is raspberry
- change password with: passwd


WiFi
------

type `sudo vi /etc/network/interfaces` to edit

    auto lo
    iface lo inet loopback
    iface eth0 inet dhcp

    auto wlan0
    allow-hotplug wlan0
    iface wlan0 inet dhcp
            wpa-ssid "name of wifi network"
            wpa-psk "password"


Zero-Configuration
-------------------

- sudo apt-get update
- sudo apt-get install avahi-daemon
- edit /etc/hostname to:
lasersaur
- new network name will be: lasersaur.local


Apps
-------

- sudo apt-get install git-core
- git clone git://github.com/stefanix/LasaurApp.git
- (whenever you want to update to the latest: cd LasaurApp; git pull)
- sudo apt-get install avrdude
- sudo apt-get install arduino-core


Serial Port
------------

By default the serial port runs a terminal. This first needs to 
be deactivated before the serial port can be used from user space.
- http://www.irrational.net/2012/04/19/using-the-raspberry-pis-serial-port/

sudo vi /boot/cmdline.txt
and remove the following parameters:
"console=ttyAMA0,115200 kgdboc=ttyAMA0,115200"

sudo vi /etc/inittab
and comment out 
"2:23:respawn:/sbin/getty -L ttyAMA0 115200 vt100"


Starting LasaurApp at Boot Time
-------------------------------

- place the following script in /etc/init.d/lasaurapp.sh
- make executable: sudo chmod 755 /etc/init.d/lasaurapp.sh
- activate with: sudo update-rc.d lasaurapp.sh defaults

<pre>
#!/bin/bash
# place in: /etc/init.d/lasaurapp.sh
# make executable: sudo chmod 755 /etc/init.d/lasaurapp.sh
# activate with: sudo update-rc.d lasaurapp.sh defaults
# deactivate with: sudo update-rc.d -f lasaurapp.sh remove

if test "$1" = "start"
then
    echo "Starting LasaurApp ..."
    /usr/bin/python /home/pi/LasaurApp/backend/app.py -p --raspberrypi	
fi
</pre>

