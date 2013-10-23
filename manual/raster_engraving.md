Raster Engraving Ideas
======================

LasaurApp/SVG parser additions
------------------------------

In LasaurApp we need to write additons to the svg parser. It needs to look for embedded images and vector fills. These need to be converted to lines of pixels which are then converted to the following G-code format.

### Raster Data

svg_tag_reader.py already looks for image tags in the SVG but currently doesn do anything with it. This needs to be extended so we get G-code raster lines from the image data.

### Vector Data

Similarly to an image we need G-code raster lines. This should be fairly simple with solid fills and non-overlapping shapes.


Firmware/G-code additions
-------------------------

<pre>
G8 P0.1
G8 X50
G8 N
G8 D&lt;data&gt;
G8 D&lt;raster data encoded in ascii&gt;
G8 N
G8 D&lt;data&gt;
...
</pre>

G8 P0.1 sets the dimensions of one 'dot'. It's the space reserved for
one data pixel, one character in the raster data. The technical minimum
is 0.034mm (based on the minimum step distance) but for best results
this should reflect the focus diameter of the setup.

G8 X50 defines the direction of the raster data and the offset. So 'X'
means data will be interpreted as x-axis lines. The offset is necessary
to achieve constant speed during engraving. It's the distance used for
accelerating the head (and also decelerating).

G8 D&lt;data&gt; sends the actual data. Likewise lines will be concatenated
until a 'G8 N' arrives. Currently line length is limited to 80
characters. The actual data is encoded into the extended ascii range
(`[128,255]`). Each character is a dot. The new raster line marker also
resets the head to the next line which is 0.1mm (or whatever was defined
with G8 Px) under the next.
