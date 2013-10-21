Optics Calculations
===================

Lasers are awesome because their output light can be focused into a very small area. This leads to a very high energy density that annihilates the material under it. Still there is an optical limit to how tiny the focus area can be. It  follows this formula (assuming perfect beam shape and 10600nm CO2 laser):

minFocusDia (in mm) = 0.013 * focusLength / beamDiameterAtLens

Basically high energy density results from large beam diameter and short focal length. Sounds easy to optimize but the tricky part is how the depth of focus is inversely related:

depthOfFocus (in mm) = 0.0265 * (focusLength/beamDiameterAtLens)^2

While optimizing for small focal diameter the depth of focus goes down too. This is unfavorable. Although it's important to remember that focus diameter is an absolute value while depth of focus is relative to the focus diameter (typically defined as the distance where the focus diameter is less than 1.4 times the minimal focus diameter).

For more details see [paralax faq](http://www.parallax-tech.com/faq.htm#f_size) and [buildlog calculator](http://www.buildlog.net/cnc_laser/laser_calcs.htm).

<h2>50mm Focal Length</h2>

<div style="width:250px; float:left">
<img src="http://farm8.staticflickr.com/7181/6893222279_80865855cf_m.jpg">
Minimal focus diameter (y-axis, in mm) for beam diameter at lens (x-axis).
</div>
<div style="width:250px; float:left; padding-left:30px">
<img src="http://farm8.staticflickr.com/7185/6893222189_0a1f98c513_m.jpg">
Depth of focus (y-axis, in mm) for beam diameter at lens (x-axis).
</div>
<div style="clear:both"></div>


<h2>75mm Focal Length</h2>

<div style="width:250px; float:left">
<img src="http://farm8.staticflickr.com/7039/6893222397_f9a1d5e095_m.jpg">
Minimal focus diameter (y-axis, in mm) for beam diameter at lens (x-axis).
</div>
<div style="width:250px; float:left; padding-left:30px; padding-top:4px">
<img src="http://farm8.staticflickr.com/7042/6893222059_d95ab13cf2_m.jpg">
Depth of focus (y-axis, in mm) for beam diameter at lens (x-axis).
</div>
<div style="clear:both"></div>

<h2>100mm Focal Length</h2>

<div style="width:250px; float:left">
<img src="http://farm8.staticflickr.com/7036/6893222503_54c2dc1a35_m.jpg">
Minimal focus diameter (y-axis, in mm) for beam diameter at lens (x-axis).
</div>
<div style="width:250px; float:left; padding-left:30px; padding-top:4px">
<img src="http://farm8.staticflickr.com/7056/6893222629_2465b47d41_m.jpg">
Depth of focus (y-axis, in mm) for beam diameter at lens (x-axis).
</div>
<div style="clear:both"></div>


<h2>Focal Length along x (beamDiameter=8mm)</h2>

<div style="width:250px; float:left">
<img src="http://farm8.staticflickr.com/7061/6893867929_a40f1c2b87_m.jpg">
Minimal focus diameter (y-axis, in mm) for focal length (x-axis).
</div>
<div style="width:250px; float:left; padding-left:30px; padding-top:4px">
<img src="http://farm8.staticflickr.com/7043/6893867845_e1a78c6994_m.jpg
">
Depth of focus (y-axis, in mm) for focal length (x-axis).
</div>
<div style="clear:both"></div>



