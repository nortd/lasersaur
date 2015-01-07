BeagleBone Setup
=================

[Index](index.md) -- [Lasersaur Software](software.md) | BeagleBone Setup | [LasaurApp Setup](lasaurapp_setup.md) | [Firmware Setup](firmware_setup.md)


To setup the BeagleBone Black (BBB) **install the following disk image on the EMMC**. If you know how to do this go ahead and skip the rest of this document. Otherwise find detailed instruction below.

<table>
<tr><td>
<a href="http://file.lasersaur.com/driveboard/lasersaur-BBB-image-v15.01.img.xz">Lasersaur BBB Image v15.01</a>
<br> (md5sum: 65203a255b38fa7abe50913be698253e)
</td>
</tr>
</table>

Looking for older files:
[lasersaur-BBB-image-v13.06.img.xz](http://file.lasersaur.com/driveboard/lasersaur-BBB-image-v13.06.img.xz)

This image is a modified <a href"http://elinux.org/Beagleboard:Ubuntu_On_BeagleBone_Black">elinux.com image</a> based on Ubuntu 14.04 LTS. It has UART1, WiFi, and GPIOs enabled as needed. For details how to roll one from scratch see [Howto Create LasaurBBB Image](bbb_ubuntu.md).


Detailed Setup Instructions
---------------------------

The following steps are quite Linux-specific but should work on OSX too. In either way some [command line skills](http://www.linuxcommand.org/) do help. To get this working on Windows some decent amount of web-searching may be required.

- Get [lasersaur-BBB-image-v15.01.img.xz](http://file.lasersaur.com/driveboard/lasersaur-BBB-image-v15.01.img.xz)
- Clone to a micro sd-card.
  - This sd-card must be 2gb or bigger.
  - `xz -dc lasersaur-BBB-flasher-v15.01.img.xz | pv -s 2G -peta | sudo dd of=/dev/mmcblk0 bs=1M`
  - **IMPORTANT:** Make sure `/dev/mmcblk0` is the sd-card, eg. by running `sudo fdisk -l` before and after you insert the card.
  - Also, you can drop the `| pv -s 2G -peta` if you don't have it on your system. You won't get a progress indicator so give it some 30min at least.
  - Mount the sd-card and copy the same `lasersaur-BBB-image-v15.01.img.xz` to `/root` on the system partition.
    - Make sure to unmount cleanly. For good measure you can call `sync` before unmounting.
- [Connect BBB to your local network.](networking.md)
- Boot BBB from this card.
  - The BBB should automatically boot from the sd-card if inserted. (If not, hold S2 button when connecting power until the four blue LEDs illuminate.)
- At this point you should already have a usable BBB. Continue to install the image on the EMMC (internal flash memory). This will make it boot faster.
- Install disk image to EMMC:
  - ssh to BBB: `ssh root@lasersaur.local`
    - default password is: `bone`
  - The disk image you copied earlier should be in your home directory. If not you can also `scp` it there.
  - `xz -dc lasersaur-BBB-image-v15.01.img.xz | pv -s 2G -peta | dd of=/dev/mmcblk1 bs=1M`
    - **IMPORTANT:** Do not abort the copy process as it may semi-brick your BBB.
  - call `sync`
  - Depower, remove sd-card, and boot up again.
  - **Done!**
  - Open [http://lasersaur.local](http://lasersaur.local)



Special Case: BBB on DriveBoard v13.03
-------------------------------------

We had to make a minor change to the DriveBoard v13.06 and later after we realized that the BBB does not boot when pin P8:46 is connected to the AVR reset pin. On DriveBoard v13.06 or later this function will be on P8:44. This means that a v13.03 DriveBoard needs to be adapted for use with a BBB.

- cut pin P8:46 on the BeagleBone headers on the DriveBoard. This is the most top-left pin.
- on the rear of the board create a solder bridge between P8:46 and P8:44 (the pin right to it).


Deprecated Guides
-----------------

- [BeagleBone](beaglebone_setup.md)
- [RaspberryPi](raspberrypi_setup.md)
