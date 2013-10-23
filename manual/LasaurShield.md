LasaurShield
============

[Index](index.md) --

The LasaurShield connects Arduino, stepper drivers, and wires. In addition it also implements a strictly hardwired safety subsystem (logic gates). The laser is forced off when any of the following occurs: door opens, chiller off or malfunctions, a limit switch triggers.

- size is 80x70mm (3.15x2.76")
- double layer pcb
- Immersion Silver (ROHS)
- [Also see the Lasersaur wiring diagram](wiring)


The relevant parts from the [BOM](bom.md) are:

- 1x   36 pin header 2.54mm pitch   538-22-28-4360
- 2x   nand logic ICs   863-MC74AC20NG
- 7x   resistor 10 KOhm   271-10K-RC
- 5x  resistor 100 Ohm   271-100-RC
- 10x   screw terminal, 2.54mm pitch   651-1725672
- 2x   screw terminal, 3.5mm pitch   1984714
- 1x   screw terminal, 5.08mm pitch   571-2828414
- 1x   resistor 20 KOhm   271-20K-RC
- 1x   resistor 6.5 KOhm   271-6.49K-RC

### Matching Stepper Motors and Drivers

The board uses two resistors to set the maximum current of the stepper motors. If your motors or drivers differ from the latest [BOM](bom.md) make sure you use the correct resistors (named x-current, y-current; some boards also say x-set and y-set).

<table style="width:640px; border: solid 1px #000000; padding:5px; margin-bottom:20px">
<tr>
<td style="border-right:solid 1px #000000; border-bottom:solid 1px #000000"></td><td style="border-bottom:solid 1px #000000">x-current-set</td><td style="border-bottom:solid 1px #000000">y-current-set</td>
</tr>
<tr>
<td style="border-right:solid 1px #000000">Nanotec/G203V (standard as of v12.02)</td><td>6.5 KOhm (271-6.49K-RC)</td><td>20 KOhm (271-20K-RC)</td>
</tr>
<tr>
<td style="border-right:solid 1px #000000">Lin Engineering/G203V</td><td>12.7 KOhm (271-12.7K-RC)</td><td>20 KOhm (271-20K-RC)</td>
</tr>
<tr>
<td style="border-right:solid 1px #000000">Lin Engineering/G251X</td><td>1.5 KOhm (271-1.5K-RC)</td><td>2.1 KOhm (271-2.1K-RC)</td>
</tr>
</table>


### Wiring Motors to LasaurShield 

<table style="width:640px; border: solid 1px #000000; padding:5px; margin-bottom:20px">
<tr>
<td style="border-right:solid 1px #000000; border-bottom:solid 1px #000000">stepper motor</td>
<td style="border-bottom:solid 1px #000000">x-terminal</td>
<td style="border-bottom:solid 1px #000000">y-terminal</td>
</tr>
<tr>
<td style="border-right:solid 1px #000000">Lin Engineering WO-4118S-01</td>
<td>black -> A; green -> /A; red -> B; blue -> /B</td>
<td></td>
</tr>
<tr>
<td style="border-right:solid 1px #000000">Lin Engineering WO-5718M-02ED</td>
<td></td>
<td>blue-white -> A; red -> /A; green-white -> B; black -> /B; blue -> red-white; green -> black-white</td>
</tr>
<tr>
<td style="border-right:solid 1px #000000">Nanotec ST4118M1206-A</td>
<td>yellow -> A; red -> /A; brown -> B; orange -> /B</td>
<td></td>
</tr>
<tr>
<td style="border-right:solid 1px #000000">Nanotec ST5918M3008-B</td>
<td></td>
<td>black -> A; green -> /A; red -> B; blue -> /B; red-white -> blue-white; black-white -> green-white</td>
</tr>
</table>


### Wiring Air Assist Control Valves

The LasaurShield has a couple of IO-pins to control air and nitrogen valves. They can be controlled directly via [G-Code](gcode.md) (M7, M8, M9). The air valve should be connected to A4 and is turned high with M7. Nitrogen should be connected to A5 and is turned high with M8. G-code M9 turns both low. To switch a solenoid valve please use a 5V micro-relay that draws less than 40mA.

NOTE: Unfortunately some of the v12.02 boards have incorrect or missing labels for the air assist pins. The following are the correct pin outs. When unsure about this drop us a line on the mailing list.

![air assist](http://farm8.staticflickr.com/7117/7504187678_40c852ffc9_z.jpg)



### Images

![wired lasaurshield](http://farm8.staticflickr.com/7066/6840859946_d5a5db514a_z.jpg)

<iframe src="http://player.vimeo.com/video/38388132" width="640" height="360" frameborder="0">video</iframe>

![laa-shld schematic](http://farm8.staticflickr.com/7065/6977189781_5cf08461ff_z.jpg)

![laa-shld schematic](http://farm8.staticflickr.com/7159/6831326821_7dd01a9b88_z.jpg)
