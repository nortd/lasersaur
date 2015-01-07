DXF Support in LasaurApp
========================

[Index](index.md) -- [LasaurApp](software.md#lasaurapp) | [LaserTags](lasertags.md) | DXF Support

With v13.02 LasaurApp supports a subset of the DXF file format. This is very useful to go straight from CAD modeller to Lasersaur. Most 3D apps can export geometry as DXFs and it is often the lowest common denominator when moving between apps.

Since DXF is a nasty proprietary format with a gazillion versions and bad standardization LasaurApp can only import the file when it is saved as version R14 with lines, arcs, and lwpolylines.

In most pro 3D apps this is easy to do. Here is how this looks in Rhino:

![rhino dxf](http://farm8.staticflickr.com/7199/6960279403_0caea51a58_z.jpg)

The tessellation parameters are not crucial as LasaurApp optimizes curves for the Lasersaur hardware. Although if the tessellation resolution is very high the import may take longer. A tolerance of 0.05mm is usually more than enough.
