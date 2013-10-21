LaserTag Presets
==================

[LasaurApp](lasaurapp) | LaserTags | [DXF Support](dxf_import)

LasaurApp looks for special tags in an SVG file and uses these to preset cutting parameters (feedrate, intensity, pass-color-assignments). This way cutting parameters can easily be saved with the SVG file. These tags can be added to the file by simply adding graphical text of a specific format to the file.

![lasertags](http://farm9.staticflickr.com/8378/8423980589_436253c688.jpg)

LaserTag Format
---------------

The format is a column-separated list of parameters that starts and ends with an equal sign:

<span style="color:#ff0000">=</span>pass<span style="color:#0000ff">num</span><span style="color:#ff0000">:</span><span style="color:#0000ff">feedrate</span>mm/min<span style="color:#ff0000">:</span><span style="color:#0000ff">intensity</span>%<span style="color:#ff0000">:</span><span style="color:#0000ff">hexcolor1</span><span style="color:#ff0000">=</span>

The `hexcolor` field is optional. So are the units for feedrate and intensity. Up to six hexcolors can be assigned (separated by columns).

### Examples

- =pass1:550mm/min:90%:#ff0000=
- =pass2:550:90:#00ff00:#ffff00:#000000=
- =pass3:1200mm/min:80%:#00000=
- =pass4:1200mm/min:80%=
- =pass5:4000mm/min:100%=
- =pass6:4000:100=
