Adjusting Timing Belt Tension
=============================


[Index](index.md) -- [operation](operation.md) | belts | [optics](optics_setup.md)

Timing belts work most reliably when their tension is well adjusted. Incorrect tension can cause the belt to jump teeth and can make the gantry cart loose its origin. In case of the Lasersaur it is also possible to have the y-cart rotate out of alignment because the angular constraint is achieved by the the two y-drive belts.

Adjustment works by sliding the idler along the aluminium extrusion. With one hand firmly push the idler (at the base) into the belt while tightening the shaft screw with the other one. It requires about the force that can be applied with one finger.

Check Belt Tension (Movement/Listening)
---------------------------

By doing a simple movement/listening check many belt problems can quickly be identified. With a bit of experience this is usually a sufficient test.

  - With the steppers off, manually move the cart through the full range.
  - Belts should run smooth with a constant purr.
  - A noise like a creaking  door or wooden staircase means the belt needs adjustment and may sporadically jump teeth.
  - The speed of the manual movement should be pretty fast (up to ~6000mm/min) but not so fast as to cause the steppers to break from self-induction.


Check Belt Tension (Pluck/Frequency)
------------------------------

For this test, pluck the belt (the side running free, not attached to cart) and measure the dominant frequency. Since the frequency is dependant on length and tension (like a violin string) this is a good measure for tension.

- x-belt: ~40Hz
- y-belts: ~60Hz

Here is an easy way to measure the dominant frequency. You will need the following:

- [Audacity](http://audacity.sourceforge.net/) (cross-platform, open source)
- microphone (iPod headphones work fine)

Then hold the mic close to the belt, pluck it (so it swings free), and record this in Audacity. Select about one second of the sound wave at about 0.5 seconds after the attack. Click "Analyze/Plot Spectrum" and look for the tallest peak. This is your dominant frequency.
 
![pluck wave](http://farm9.staticflickr.com/8233/8471494065_44e036ea0d_z.jpg)
![spectrum](http://farm9.staticflickr.com/8104/8471493931_618d57bff2_z.jpg) 

