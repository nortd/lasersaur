Lasersaur Firmware
==================

[Index](index.md) -- [Lasersaur Software](software.md) | [BeagleBone Setup](bbb_setup.md) | [LasaurApp Setup](lasaurapp_setup.md) | Firmware Setup

The firmware is a low-level software component on one of the DriveBoard's chips (Atmega328). It is responsible for all the real-time stepper pulsing. It communicates with the BBB by UART. Initially, when setting up the DriveBoard, the firmware needs to be flashed onto this chip. Some LasaurApp updates also comprise a change to the firmware. If this is the case the firmware needs to be flashed as well. This can easily be done from the web interface's menu:

- `Admin/Flash Firmware`

**NOTE:** This works as long as the Atmega328 has an [Arduino bootloader](http://arduino.cc/en/Hacking/Bootloader) on it. The chips from the Lasersaur Store always have one. If you source this chip elsewhere you will have to upload this bootloader with a programmer.


### Compiling Custom Firmwares

LasaurApp makes it easy to run custom firmwares. For small changes (e.g. in the config.h file) one click on `Admin/Build and Flash from Source` builds a new firmware and asks if it should be flash-uploaded. The firmware source code from which it gets built is in `LasaurApp/firmware/src`. These files can even be directly edited through an ssh session with `vi` or `nano`. If you want to get fancy you can also use git to track your source changes directly on the BBB. Happy Hacking!
