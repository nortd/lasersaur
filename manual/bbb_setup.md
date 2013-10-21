BeagleBone Black Setup
=======================

[Index](index.md) -- [LasaurApp](lasaurapp.md) | [DriveBoard](driveboard.md) | BeagleBoneBlack

For ease of setup we have created a pre-configured disk image. It's Ubuntu 13.10 with UART1 enabled in the device tree and all Lasersaur-related software installed.

If you know what you are doing you can skip the rest and simply clone [lasersaur-BBB-image-v13.06.img.xz](http://file.lasersaur.com/driveboard/lasersaur-BBB-image-v13.06.img.xz) to the the BBB. This is a well documented procedure with lots of guides online. To read up on this you may want to start at the [BeagleBone mailing list](https://groups.google.com/forum/#!forum/beagleboard).

### Installing the System Image

- Get [lasersaur-BBB-flasher-v13.06.img.xz](http://file.lasersaur.com/driveboard/lasersaur-BBB-flasher-v13.06.img.xz)
- Clone to a micro sd-card.
  - `xz -dc lasersaur-BBB-flasher-v13.06.img.xz | pv -s 2G -peta | sudo dd of=/dev/sdx bs=1M`
  - IMPORTANT: make sure `/dev/sdx` is the sd-card, eg. by running `sudo fdisk -l`
- Boot BBB from this card.
  - The BBB will automatically boot from the sd-card if inserted. (If not, hold S2 button when connecting power until the four blue LEDs illuminate.)
- At this point you should already have a usable BBB. Continue if you want to make this boot image permanent by cloning it to the internal emmc.
- Clone disk image to internal memory:
  - ssh to BBB: `ssh root@lasersaur.local`
  - clone to emmc by running: ./clone2emmc
    - IMPORTANT: do not abort the cloning as it may semi-brick your BBB


### BBB on DriveBoard v13.03 and earlier

We had to make a minor change to the DriveBoard after we realized that the BBB does not boot when pin P8:46 is connected to the AVR reset pin. On DriveBoard v13.06 or later this function will be on P8:44. This means that a v13.03 DriveBoard needs to be adapted for use with a BBB.

- cut pin P8:46 on the BeagleBone headers on the DriveBoard. This is the most top-left pin.
- on the rear of the board create a solder bridge between P8:46 and P8:44 (the pin right to it).

This effectively moves the AVR reset line one pin over. The latest LasaurApp already supports both setups.
