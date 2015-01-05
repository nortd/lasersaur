Lasersaur Software
==================

[Index](index.md) -- [Lasersaur Software](software.md) | [BeagleBone Setup](bbb_setup.md) | [LasaurApp Setup](lasaurapp_setup.md) | Firmware Setup



### Flashing the Firmware

The Lasersaur hardware also needs to be loaded with firmware. This has already been done if you got yourself an assembled DriveBoard. In all other cases LasaurApp can flash the firmware for you. In the header menu go to Admin/Flash Firmware. This works as long as you are connected and the Atmega328 has an [Arduino bootloader](http://arduino.cc/en/Hacking/Bootloader) on it.


### Compiling Custom Firmware

LasaurApp (starting with v13.06b) makes it easy to run custom firmwares. For small changes (e.g. in the config.h file) one click on `Admin/Build and Flash from Source` builds a new firmware and asks if it should be flash-uploaded. The firmware source code from which it gets build is in `LasaurApp/firmware/src`. These files can even be directly edited through an ssh session with `vi` or `nano`. Happy Hacking!
