
Howto Create the LasaurBBB Image
================================

[Index](index.md) -- 

### Create SD Card
- Get BBB ubuntu Image from elinux.org and follow instructions.
  - http://elinux.org/BeagleBoardUbuntu#BeagleBone_Black
- Before booting it on the BBB edit the network settings files and configure the name. We will be using 'lasersaur' in the host files so the zeroconf will use lasersaur.local as its domain name.
  - `/etc/network/interfaces`
  - `/etc/host`
  - `/etc/hosts`

### Boot SD Card
- insert into BBB
- power up while S2 button pressed (release when all 4 leds light up)

### Setup Ubuntu
- ssh into BBB
  - `ssh ubuntu@lasersaur.local`
    - default password is: temppwd
  - alternatively figure out the IP address like this:
    - `nmap -sP $(ip -o addr show | grep inet\  | grep wlan0 | cut -d\  -f 7)`
- root login
  - `sudo passwd root`
  - `sudo vi /etc/ssh/sshd_config`
    - set *PermitRootLogin* to *yes*
    - `reboot`
- lock user account
  - make sure ssh login works with root first
  - passwd -l ubuntu
- update software
  - apt-get update
  - apt-get upgrade
- add packages
  - avahi-daemon
  - arduino-core
  - git
  - screen
  - ipython
  - pypy
  - python-serial
  - python-pip
  - nodejs
  - npm
  - pv
- install LasaurApp
  - git clone git://github.com/stefanix/LasaurApp.git
  - install startup script

#### Startup Script
```bash
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
```
