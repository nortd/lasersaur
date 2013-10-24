LasaurGrbl G-code Protocol
===========================

[Index](index.md) -- 

LasaurGrbl uses a small subset of G-code ([rs274/ngc](http://linuxcnc.org/docs/html/gcode.html), [ISO6983](https://en.wikipedia.org/wiki/G-code)) for operation (see [Mode of Operation page](operation) for details). This support is intentionally reduced to the essentials to allow for a very lightweight and agile code base. Usually generated and streamed by LasaurApp, G-code can also be sent directly and manually with the Arduino Serial Monitor. 

This is very useful for debugging. For example, by sending a '?' the Lasersaur will reply with an extended status string, giving information on all sensor inputs, current gantry location, and firmware version. (More information on the return format can be found further down.)

![arduino serial monitor](http://farm9.staticflickr.com/8300/7746226640_6bb538a627.jpg)

### Low-level Serial on DriveBoard

You can manually send and test G-code on the DriveBoard as well. For this do the following:

  1. Press Disconnect button in LasaurApp
  2. ssh into BeagleBone
  3. Run "screen /dev/ttyO1 57600"
  4. Type "?" followed by `<ctrl>-<enter>`

Note that `<enter>` alone may not send the line, use `<ctrl>-<enter>`. Also exiting screen is not exactly obvious, type: `<ctrl>-a k`



G-code Commands
---------------

### G0, G1 - seek, feed
- G0 X120 Y150 - moves the head to 120,150 without lasing
- G0 F2000 - sets the seek rate to 2000mm/min
- G1 X120 Y150 - lase to 120,150
- G1 F2000 - sets the lasing rate to 2000mm/min

### S - laser intensity
- S0 - sets the laser intensity to 0%
- S255 - sets the laser intensity to 100%

### G4 - pierce (not implemented yet)
- G4 P0.5 - lase in location for 0.5 seconds

### G10 - set offsets
- G10 L20 P0 - set table offset (G54) to current location
- G10 L20 P1 - set custom offset (G55) to current location
- G10 L2 P0 X20 Y20 - set table offset (G54) to 20,20
- G10 L2 P1 X220 Y140 - set custom offset (G55) to 220,140

### G30 - homing cycle
- G30 - find physical home and reset the origin
- (the table origin will be set to the offset defined by `CONFIG_X_ORIGIN_OFFSET` and `CONFIG_Y_ORIGIN_OFFSET` in config.h) 

### G54, G55 - switch offsets
- G54 - use table offset
- G55 - use custom offset

### G90, G91 - absolute, relative mode
- G90 - following coordinates are absolute
- G91 - following coordinates are relative

### M80, M81, M82, M83 - air, aux1, aux2 control
- M80 - air assist enable
- M81 - air assist disable
- M82 - aux1 enable
- M83 - aux1 disable
- M84 - aux2 enable
- M85 - aux2 disable

### '!' and '~' are special control characters (non-G-code)
- ! - stop operation immediately and put machine in stop mode
- ~ - continue, exit stop mode

### '?' is a special query character (non-G-code)
- ? - get full status string


Return Format
-------------
LasaurGrbl returns a newline-terminated string for each line it receives. It consists of uppercase letters that are either flags or markers for a value. Parsing the flags is simply done by looking if a certain character is in the return line. A typical reply looks like this:

- "DCP" ... door is open (D), chiller is off (C), power is off (P)
- "!L"  ... the hardware is in stop mode (!) because a limit was hit (L)


### Flag Characters:
- ! ... hardware is in stop mode
- P ... stop: power off
- L ... stop: limit hit
- L1 ... stop: limit x1 hit
- L2 ... stop: limit x2 hit
- L3 ... stop: limit y1 hit
- L4 ... stop: limit y2 hit
- R ... stop: requested by serial
- B ... stop: serial rx buffer overflow
- I ... stop: line buffer overflow
- T ... stop: transmission error
- O ... stop: other reason
- D ... warning: door open
- C ... warning: chiller off
- N ... warning: bad number format
- E ... warning: expected command letter
- U ... warning: unsupported statement
- W ... warning: other reason

### Value Characters
An extended status string can be queried by sending a '?' and will also include current location and version number (e.g: DCPL1L2L3L4X0.000Y0.000V12.08).

- X ... current absolute x pos
- Y ... current absolute y pos
- V ... version number


Checksum and Error Correction
-----------------------------
In addition to plain G-code lines LasaurGrbl also supports extended lines for basic transmission error correction. This is accomplished by prepending two bytes to every line. Byte one can be either a `'^'` or a `'*'` and byte two is an 8-bit checksum between `[128, 255]`  (effectively just 7-bit, it uses the extended ascii range).

The sending side can choose how much redundancy to use by sending zero or more lines identified by a leading `'^'` followed by a final line identified by a leading `'*'`. Redundant lines will be used for automatic error correction. If no redundant lines (only `'*'` lines) are sent no automatic correction can be done but transmission errors will be reported.

```
^ + checksum + line     <- redundant line 1 (optional)
^ + checksum + line     <- redundant line 2 (optional)
* + checksum + line     <- final line
```

Any line starting with a `'^'` is a redundant line and LasaurGrbl expects another redundant line or the final line afterwards. As soon as a line matches the checksum it will skip all following lines until the end of the final line. If non are matching the checksum including the final it reports a transmission error.

### Calculating the Checksum
This is done super light-weight (no CRCs at the moment).

```c
char *itr = line_string;
uint16_t checksum = 0;
while (*itr) {  // all chars without 0-termination
    checksum += (uint8_t)*itr++;
    if (checksum >= 128) {
        checksum -= 128;
    }          
}
checksum = (checksum >> 1) + 128;
```
