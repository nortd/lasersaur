BeagleBone Setup
================

**DEPRECATED**

Note: There are two different kinds of BeagleBones on the market now: Please see [BeagleBone Black setup](bbb_setup.md) for the latest board.

While the [BeagleBone](http://beagleboard.org/bone) comes with [Angstrom Linux](http://www.angstrom-distribution.org/) pre-installed we use [Ubuntu](http://elinux.org/BeagleBoardUbuntu) for the Lasersaur. It plays better with usb peripherals like wifi dongles.  The following shows how to get the fully pre-configured *lasersaur-beaglebone-image* onto the BeagleBone. 

Alternatively you can [configure a stock Ubuntu/Debian image from scratch](beaglbone_ubuntu.md). Or use the pre-installed Angstrom Linux (see [old setup instruction](beaglebone_angstrom.md)).

Before you start be informed that some command line skills are helpful. If you need to brush up, here is a great [command line tutorial](http://www.linuxcommand.org), well worth the time.

### Setup Steps
1. Download [lasersaur-beaglebone-image-v13.06.img.gz](http://file.lasersaur.com/driveboard/lasersaur-beaglebone-image-v13.06.img.gz)
  - md5sum: 0f17bedc61421bb3fbd98f7d6583c6ad
2. Clone image to BeagleBone SD-card
3. Configure Wifi (optionally)
4. Set new root password
5. Update LasaurApp


On Linux
---------
1. Download lasersaur-beaglebone-image
2. Clone image to BeagleBone SD-card
  - Insert card in computer's sd-card reader.
  - Figure out sd-card device name by running `df -l` and substitute for `/dev/sdx` in the following.
  - `gzip -dc lasersaur-beaglebone-image.gz | pv -s 4G -peta | sudo dd of=/dev/sdx bs=1M`
      - if you don't have `pv`, the following works too but you won't get a progress bar
      - `gzip -dc lasersaur-beaglebone-image.gz | sudo dd of=/dev/sdx bs=1M`
3. Configure Wifi (optionally)
  - edit `/etc/network/interfaces` on the sd-card
    - replace "your access point name" and "your passphrase" with your wireless credentials (this assumes wpa or wpa2 encryption)
  - Add a usb wifi dongle to BeagleBone. Make sure it uses the rtl8192cu chipset like the Edimax EW-7811Un or the [OurLink](http://www.adafruit.com/products/814)
  - Boot BeagleBone with newly created sd-card
  - If the wifi is spotty use a short usb extension cable. [More info here.](https://groups.google.com/forum/?fromgroups=#!topic/beaglebone/UPERscSdoEk)
4. Set new root password
  - Make sure you are on the same network/router as the BeagleBone and give it about two minutes to boot up.
  - connect to the BeagleBone with `ssh root@lasersaur.local`
  - default password is: `bone`
  - run `passwd`
5. Update LasaurApp
  - Connect to the BeagleBone with `ssh root@lasersaur.local`
  - `cd LasaurApp; git pull`
  - Alternatively you can also manually copy the latest sources to `~/LasaurApp`
  - reboot
  - Open `lasersaur.local` in a web browser.
  - In web interface flash firmware via *Admin/Flash Firmware (latest)*


On OSX
-------
1. Download lasersaur-beaglebone-image
2. Clone image to BeagleBone SD-card
  - Insert card in computer's sd-card reader.
  - Unmount partitions on sd-card
    - Use `diskutil list` to figure out exact names and substitute in the following two steps.
    - `diskutil umountDisk /dev/diskX`
  - Copy image data. This may take more than 10 minutes.
    - `gzip -dc lasersaur-beaglebone-image.gz | sudo dd of=/dev/diskX`
3. Configure Wifi (optionally)
  - edit `/etc/network/interfaces` on the sd-card
    - replace "your access point name" and "your passphrase" with your wireless credentials (this assumes wpa or wpa2 encryption)
  - Add a usb wifi dongle to BeagleBone. Make sure it uses the rtl8192cu chipset like the Edimax EW-7811Un or the [OurLink](http://www.adafruit.com/products/814)
  - Boot BeagleBone with newly created sd-card
  - If the wifi is spotty use a short usb extension cable. [More info here.](https://groups.google.com/forum/?fromgroups=#!topic/beaglebone/UPERscSdoEk)
4. Set new root password
  - Make sure you are on the same network/router as the BeagleBone and give it about two minutes to boot up.
  - connect to the BeagleBone with `ssh root@lasersaur.local`
  - default password is: `bone`
  - run `passwd`
5. Update LasaurApp
  - Connect to the BeagleBone with `ssh root@lasersaur.local`
  - `cd LasaurApp; git pull`
  - Alternatively you can also manually copy the latest sources to `~/LasaurApp`
  - reboot
  - Open `lasersaur.local` in a web browser.
  - In web interface flash firmware via *Admin/Flash Firmware (latest)*


On Windows
-----------
1. Download lasersaur-beaglebone-image
2. Clone image to BeagleBone SD-card
  - Extract image with [7-zip](http://www.7-zip.org/download.html)
  - Block-copy image to sd-card with [Image Writer for Windows](http://sourceforge.net/projects/win32diskimager/?source=dlp)
  - more info about this on [BeagleBone page](http://beagleboard.org/static/beaglebone/latest/README.htm) under *Program an SD Card with Latest Software*
3. Configure Wifi (optionally)
  - edit `/etc/network/interfaces` on the sd-card
    - replace "your access point name" and "your passphrase" with your wireless credentials (this assumes wpa or wpa2 encryption)
  - Add a usb wifi dongle to BeagleBone. Make sure it uses the rtl8192cu chipset like the Edimax EW-7811Un or the [OurLink](http://www.adafruit.com/products/814)
  - Boot BeagleBone with newly created sd-card
  - If the wifi is spotty use a short usb extension cable. [More info here.](https://groups.google.com/forum/?fromgroups=#!topic/beaglebone/UPERscSdoEk)
4. Set new root password
  - Make sure you are on the same network/router as the BeagleBone and give it about two minutes to boot up.
  - connect to the BeagleBone at `lasersaur.local` with [Putty](https://en.wikipedia.org/wiki/PuTTY)
  - user: `root`
  - default password is: `bone`
  - run `passwd`
5. Update LasaurApp
  - Connect to the BeagleBone again.
  - `cd LasaurApp; git pull`
  - Alternatively you can also manually copy the latest sources to `~/LasaurApp`
  - reboot
  - Open `lasersaur.local` in a web browser.
  - In web interface flash firmware via *Admin/Flash Firmware (latest)*
