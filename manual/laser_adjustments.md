Laser Adjustments
=================

Laser systems are typically already adjusted. Sometimes this is not the case (either they forgot or the tube and PSU was bought separately) so it's usually a good idea to double-check this.

For the 100W Reci W4 tube the output current of the DY13 laser PSU needs to be adjusted to 24-28mA. To achieve this do the following:

  - Be cautious:
    1. Make sure to wear laser protection glasses when dealing with an open Lasersaur.
    2. Make yourself aware of high voltage circuitry and avoid contact.
  - Measure the tube current at maximum power:
    1. Turn the laser PSU off and let it fully discharge a couple of minutes. Disconnect from power.
    2. Connect an amp-meter at the cathode side (the side where the laser beam exits). For this disconnect the thin, non-high-voltage wire and place the amp-meter in between the wire and the tube (Most DMMs will work since the tube drops the voltage way down).
    3. Make sure non of the connections can touch anything and power up the Lasersaur.
    4. Read amp-meter when lasing at 100% power.
    5. If current is not approximately 26mA proceed with adjustments.
  - Adjusting the output current.
    1. Locate the trim-pot at the side of the laser PSU
    2. Adjust (with insulated screw driver) until you get the desired output current.

![trim-pot](http://farm8.staticflickr.com/7044/6987014326_2eca395e36_z.jpg)


### Output Power Control

<pre>
| 1 | 2 | 3 | 4 | 5 | 6 |    |trim pot|
| 5V| TH| TL| WP|GND| IN|
</pre>

The DY13 laser PSU has various ways to control the output power. The logic is like this: TH and TL fire the laser. You can choose if a high signal or a low signal does this (you only use one of them). The voltage on IN optionally allows you to cap the output power. Typically 0-5V is mapped to 0-24mA by the factory. A disconnected IN also produces an output, typically about 9mA. The trim pot allows for adjustment of this mapping.

For the Lasersaur we modulate the laser intensity by PWM-pulsing on the TH pin and wiring the IN pin to the 5V pin. If the intensity is low and the laser cuts out at under 50% power it's most likely the IN is not connected to 5V.

