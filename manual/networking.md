
Lasersaur Networking
--------------------

To ssh into the BBB some networking needs to take place.

By default the BBB will try to connect to a WiFi network named `the internets` with `itpinthehouse` as its password, and `WPA2` encryption. If you have a quick way to set this up (like an Android phone) this is the easiest option.

Alternatively you can connect the BBB by Ethernet wire to your access point. This will work if there is a DHCP server handing out IP addresses.

Once you have ssh access you can always edit the `/etc/network/interfaces` file to reconfigure the network settings like WiFi credentials or make the Ethernet IP address static. Be careful not create an invalid interfaces files as this may lock you out.


For this to work your computer and the BeagleBone need to be on the same network.

### Ethernet
- Simply plug the BeagleBone into the same access point as your computer.
- Open  [http://lasersaur.local](http://lasersaur.local)
- Done!

On most access points this will work without complications. The most common reasons it may fail are: (1) AP does not route between ethernet and wifi. Try plugging computer also into ethernet. (2) AP does not run a DHCP server or the DHCP server fails to provide a lease to the BeagleBone. If you have access to the AP control panel take a look at the settings. Maybe the leases are limited and they are all handed out already.

### Wifi
- ssh to the BeagleBone and edit the `/etc/network/interfaces` file to match your wifi access point name and password (replace "the internets" and "itpinthehouse").
- Reboot and connect your computer to the same wifi AP
- Open  [http://lasersaur.local](http://lasersaur.local)
- Done!

You may have a few question at this point.

- What's ssh?
  - Secure SHell gives you full control of the BeagleBone.
  - On Linux and OSX you run it like this from the Terminal: `ssh root@lasersaur.local`
  - On Windows you use a program called Putty, among others.
  - Default password is: bone
- How to connect if the wifi is not configured?
  - Connect by ethernet or configure your wifi access point to the LasersaurBBB defaults.
  - By default the LasersaurBBB will try to connect to:
    - SSID: "the internets"
    - pass: "itpinthehouse"
    - encryption: WPA
  - BTW: most Android phones can be configured as a WiFi AP.

If you run into problems feel free to ask on the mailing list. Make sure to provide a detailed description of the issue at hand. Better questions naturally get better answers.

### Network Security

Please make sure to use the default Wifi configuration only initially to configure your own AP name and password. Also make sure to change the default ssh password on the BeagleBone:

- ssh into the Lasersaur: `ssh root@lasersaur.local`
- set new root password: `passwd`
