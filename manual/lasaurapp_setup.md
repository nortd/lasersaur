LasaurApp Setup
===============

[Index](index.md) -- [Lasersaur Software](software.md) | [BeagleBone Setup](bbb_setup.md) | LasaurApp Setup | [Firmware Setup](firmware_setup.md)

**LasaurApp does not have to be installed separately.** After the [BeagleBone Setup](bbb_setup.md) you should have a working LasaurApp setup. The same applies for an *Assembled DriveBoard*. Nonetheless, to get the most out of this Software you should keep LasaurApp up to date.

Bigger updates are usually announced on the Lasersaur mailing list. For all the development details check out [LasaurApp on Github](https://github.com/stefanix/LasaurApp/). We have three important branches: *master*, *beta*, *alpha*. The *master* branch is stable and for production. The *beta* branch is for testing release candidates and *alpha* is for current development work.



Updating
------------

LasaurApp can be updated over the network. For this, ssh into the Lasersaur and pull the latest version from our repository. Bt default this will be the latest code off LasaurApp's *master* branch. Check out the [commit log](https://github.com/stefanix/LasaurApp/commits/master) for details on changes.

- `ssh root@lasersaur.local`
- `cd LasaurApp`
- `git pull`

Default ssh password is *bone*. For details on how to connect see [Lasersaur networking](networking.md).


The *beta* Branch
-----------------

We first post new software features and other changes to the *beta* branch. This is a form of quality assurance for the *master* branch. If you want to try out this more advanced (potentially less stable) LasaurApp here is how you do it:

- `ssh root@lasersaur.local`
- `cd LasaurApp`
- `git checkout beta`
- `git pull`
- `reboot`

To revert back to the *master* branch do:

- `ssh root@lasersaur.local`
- `cd LasaurApp`
- `git checkout master`
- `git pull`
- `reboot`


Firmware Update
---------------

The firmware is a low-level software component on one of the DriveBoard's chips (Atmega328). Some LasaurApp changes also comprise a change to the firmware. If this is the case the firmware needs to be flashed as well. This can easily be done from the web interface's menu:

- `Admin/Flash Firmware`
