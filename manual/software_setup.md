Setting up the Software
=======================

<span style="color:#ff0000">DEPRECATED PAGE!</span> please see [LasaurApp Page](lasaurapp)

![lasaurapp2](http://farm8.staticflickr.com/7077/7179166822_a647dc6d8f_m.jpg)
![lasaurapp1](http://farm8.staticflickr.com/7237/7179166690_8e15760c8e_m.jpg)

We provide LasaurApp binaries (OSX, Windows) which contain all Lasersaur software. If you run into problems or limitations please proceed to the [Software Setup for Developers](software_setup#dev) section. Also let us know on the mailing list of any problems so we can efficiently smoothify things.

<div class="wire">
<ul>
<li>
<a href="https://github.com/downloads/stefanix/LasaurApp/LasaurApp-v12.08f-osx.zip">LasaurApp v12.08f for OSX 10.6+</a>
</li>
<li>
<a href="https://github.com/downloads/stefanix/LasaurApp/lasaurapp-v12.08f-win.zip">LasaurApp v12.08f for Windows</a>
</li>
<li>
<a href="#dev">LasaurApp for Linux</a> - Please use the sources.
</li>
</ul>
</div>

Simply unzip and double click the LasaurApp executable. There is no installation necessary. This will start the backend and open the GUI in your default browser. Supported browsers are recent Firefox/Chrome, and future Safari 6/IE 10. Optionally copy the executable to your Applications/Programms directory.

### Flashing the Arduino
To turn an Arduino Uno into a Lasersaur controller you need to upload the LasaurGrbl firmware. LasaurApp can do this by normally running it and then opening [http://127.0.0.1:4444/flash_firmware](http://127.0.0.1:4444/flash_firmware) in your browser. Flashing is only necessary the first time or when updating the firmware but also does generally not cause problems when done repeatedly.


<a name="dev"></a>
Software Setup for Developers
-----------------------------

The Lasersaur software stack consists of LasaurApp (client app) and LasaurGrbl (firmware). They work in concert to generate low-level motion control from high-level design files (SVG). LasaurApp is a CommanLine/Terminal program with a browser-based GUI. It runs on OSX, Linux, and Windows and allows for very flexible setups.

- [LasaurApp](https://github.com/stefanix/LasaurApp) - app
- [LasaurGrbl](https://github.com/stefanix/LasaurGrbl) - firmware


### Prerequisites
Both programs depend on Python 2.7 (that's the version we test against). Make sure you can run python from the Terminal/Shell/CommandLine. If you are on Linux or OSX chances are you already have Python. On Windows we recommend installing it from the [ActiveState distribution](http://downloads.activestate.com/ActivePython/releases/2.7.2.5/ActivePython-2.7.2.5-win32-x86.msi) as it automatically sets up all the environment variables and comes with package managers like easy_install, pip, and pypm.



### LasaurApp

LaserApp runs mostly in a browser and comes in the form of a small dedicated python server. You start the server and then use your browser of choice to control the Lasersaur.

- open the Terminal/Shell/CommandLine
- make sure you have Python 2.7, run "python --version"
- download the latest [stable LasaurApp](https://github.com/stefanix/LasaurApp/zipball/master) and unzip to a convenient location
- go to that location in the Terminal/Shell/CommandLine
- upload firmware to the controller, run "python backend/app.py -f" (only the first time or when updating firmware)
- open LasaurApp, run "python backend/app.py"

At this point your default browser should open at [http://localhost:4444](http://localhost:4444). LasaurApp runs in any current Firefox or Chrome, and future Safari 6 or IE 10. Inside LasaurApp you should see a big "connect" button. If all went smooth this button should turn green upon pressing. Congrats!

On Windows you may have to specifically tell the program which com port to use by typing "python backend/app.py COM7" where COM7 is the actual port the Arduino is connected to. One of the easiest ways to figure this out is to run the Arduino IDE and look under "Tools/Serial Port".

On Linux you may have to set proper r/w permissions for the serial port. For quickly testing and bypassing this issue you can also run LasaurApp as root by typing "sudo python backend/app.py".


### LasaurGrbl

You only need to install the LasaurGrbl sources if you want to hack on the firmware. For normal use simple use the precompiled firmware that is distributed with LasaurApp.

Download LaserGrbl, compile, and upload it to the Arduino Uno:

- make sure you have Python 2.7
- make sure you have the [Arduino IDE](http://www.arduino.cc/en/Main/software) installed (we only need the avr toolchain)
- download the latest [stable LaserGrbl](https://github.com/stefanix/LasaurGrbl/zipball/master) and unzip to a convenient location
- open the Terminal/Shell/CommandLine and go to this location
- connect the Arduino via USB
- run "python flash.py"
- You should see some progress bars and "avrdude done. Thank you." at the end.

If this fails open the flash.py file in an editor and follow the instructions inside. On Windows you will have to specifically tell the program which com port to use by typing "python flash.py COM7" where COM7 is the actual port the Arduino is connected to. One of the easiest ways to figure this out is to run the Arduino IDE and look under "Tools/Serial Port".

If things don't work with the Arduino it's a good idea to test the tool chain and hardware by running a simple "Hello World" program. Go through the [Arduino Getting Started Guide](http://arduino.cc/en/Guide/HomePage) and make sure the LED is blinking at the end.

If all went smooth you have converted an Arduino to a Lasersaur controller. Congrats!


