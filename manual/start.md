How to get a Lasersaur
===============

[Index](index.md) -- 

Welcome to the Lasersaur project!

If you want to build your own laser cutter, understand it from ground up, and want to maintain such a system yourself you have come to the right place. This project is about empowering you with knowledge, robotics, and things that make things. We think of it as both open source hardware and the infrastructure that enables more open source hardware. Most importantly it is also a place to exchange ideas about personal fabrication and promoting technology that is open and shared. The Lasersaur project is currently in **pre-release phase**. Please understand that the documentation is still subject to completion. Nonetheless, many have built one already and we have a good record of addressing open questions on the mailing list.

<table>
<tr><td>
<strong>DISCLAIMER:</strong>
</td></tr>
<tr><td>
Please be aware that operating a self-built laser cutter can be dangerous and requires full awareness of the risks involved. NORTD Labs does not warrant for any contents of the manual and does not assume any risks whatsoever with regard to the contents of this manual or the machine assembled by you. NORTD Labs further does not warrant for and does not assume any risks whatsoever with regard to any parts of the machine contained in this manual which are provided by third parties. You need to have the necessary experience in handling high-voltage electrical devices and class 4 laser beams to build the machine described in this manual. Otherwise you should seek professional advice for building the machine.
</td></tr>
</table>

Still excited? This is how you go after building your own Lasersaur:

1. Understand the Prerequisites
2. Understand the Risks
3. Order Parts
4. Assemble System
5. Run and Maintain


Understand Prerequisites
------------------------

You need some simple tools and some basic understanding of mechanical and electrical systems as well as some understanding of basic software development. We tried our best not to require any advanced tools or advanced craftsmanship to complete the build. For the most part the system is assembled by mounting and connecting parts with socket cap screws. The control board requires some through-hole soldering and running wires to sensors, motors, and the laser.



Understand Risks
------------------

The primary risks come from operating a CO2 laser tube. Please operate your first system with a laser source within your level of expertise, even if this is a laser pointer. From there work yourself up until you can safely run a high-powered system.

CO2 lasers involve high-energy infrared beams that may be reflected or scattered and can cause fire on many materials. Most importantly lasers may cause permanent damage to the eye. The best way to manage these kinds of risk is wearing protection glasses certified for CO2 wavelength and having proper fire extinguishers available at all times (see [Accessories](accessories.md)).

The second danger is high-voltage. Depending on the tube, you are looking at 25000-40000 volts. The power supplies are rated in the 50mA range which puts any electric shocks into lethal territory. One might be able to survive such a shock but depending on things like physical condition, length of shock, and the fact that the power supply may actually supply more amps temporarily puts this into the avoid-at-all-costs category. Also note that electricity at these voltages jumps through the air for several inches and be aware that the power supplies stay charged after disconnecting them from the outlet for quite some time.

Most countries have specific regulation for laser radiation that is typically dependent on the class of laser. Any laser that is suitable for cutting is class 4. Only after proper encasement and applying specifically regulated safety measures will a laser cutter be class 1.


Ordering Parts
------------

Sourcing all components is straight forward if you are located in North America or Europe. We provide specific lists with suggested suppliers for both areas. However, if you are looking to cut down on the cost rather then time, we suggest you use our list as a guide to source the materials cheaper locally or online. In other parts of the world we have less experience, and it might take some extra work to get all the parts but it should be possible. Most suppliers ship worldwide and alternatives can be found quite easily in our experience.

The budget you need to allocate if using our suggested suppliers is around USD 7000 for the 100W system (same for EUR as sourcing in Europe is a bit more expensive). Please refer to the part lists for exact numbers. These lists are optimized for hassle-free ordering rather then cheapest option. There is plenty of opportunities to push the costs further down. For example, cutting the case panels yourself and sourcing the polycarbonate sheets locally would save you up to USD 800. Many standardized parts can also be sourced cheaper, like ball bearings, fasteners, and tubing.

* [Bill of Materials](bom.md)


Assemble System
---------------

We are compiling comprehensive instructions during the beta phase. This means until the project goes fully open source the manual needs to be complemented with the CAD model and the mailing list. After that we aim for a complete step-by-step instructional guide.

* [Build Instructions](assembly.md)
* [Time-Lapse of the Build](http://www.flickr.com/photos/stfnix/5721014861/)

We think the assembly process is fairly enjoyable (think Lego Technik on steroids). Assembly does not include any difficult steps, like drilling precision holes or cutting pieces to size. On average, it should take about a week to put a Lasersaur together and we have seen people do it in substantially less time (the best time is at 3 days).



Run and Maintain
---------------

Our mailing list is an extensive resource for this. Also, as time passes we are moving the essential information to the manual for easy reference.

