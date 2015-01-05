LasaurApp Developer Setup
=========================

LasaurApp is quite flexible software and can also be run on any Windows, OSX, and Linux computer. This is not the recommended way but useful for developers working on the code. It's also useful for taking a look at the interface or setting up a laser cutter without a DriveBoard (e.g: with a USB-to-serial converter). In this case the LasaurApp backend runs on the computer and the browser connects locally.

- Open the command line.
- Make sure you have Python 2.7, run `python --version`
  - If not, get 2.7.x installers from the [Python Website](http://python.org/download/).
  - On Windows we recommend using the [ActiveState distribution](http://downloads.activestate.com/ActivePython/releases/2.7.2.5/ActivePython-2.7.2.5-win32-x86.msi) as it sets all the PATH shortcuts.
- Download the latest [stable LasaurApp](https://github.com/stefanix/LasaurApp/zipball/master) and unzip to a convenient location.
  - For advanced users we recommend using `git clone git://github.com/stefanix/LasaurApp.git` instead. This way you can easily update with `git pull`
- Go to that location in the command line and run `python backend/app.py`

At this point your default browser should open at [http://localhost:4444](http://localhost:4444). LasaurApp runs in any current Firefox or Chrome (Safari and IE may work too). Congrats!

On Windows you may have to specifically tell the program which COM-port to use by typing "python backend/app.py COM7" where COM7 is the actual port the Lasersaur is connected to. One of the easiest ways to figure this out is to run the Arduino IDE and look under "Tools/Serial Port".

On Linux you may have to set proper r/w permissions for the serial port.
