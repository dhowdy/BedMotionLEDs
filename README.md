# BedMotionLEDs

Ever get out of bed in the middle of the night to go to the bathroom and *didn't* want to break your toe on the dresser?  Good.  This is for you.  When you put your feet on the floor a motion detector senses that and turns on a strip of LEDs under your bed so you can see where you are going.

This repo is software to use a Raspberry Pi, Neopixels, PIR sensors, and logic in order to turn on LEDs mounted underneath a bed when motion is detected AND it is dark outside.  The software does the following:

  - Calculates the civil twilight values based on latitude and longitude
  - Detects motion using PIR sensors
  - Turns the LEDs on when it is dark outside
  - Turns the LEDs off after a specified time with no movement detected
  - Allows push buttons to override the behavior

### More Information

Please find more information on the hardware on [my blog](http://dhowdy.blogspot.com).

### Installation

This project assumes the use of a Raspbian-based distro.
Install the necessary dependencies.

```sh
cd
sudo apt-get update
sudo apt-get install build-essential python-dev git scons swig python-pip python-setuptools
git clone https://github.com/jgarff/rpi_ws281x.git
cd rpi_ws281x
scons
sudo easy_install pytz
sudo pip install astral
cd
git clone https://github.com/dhowdy/BedMotionLEDs.git

```

Add a line to the autostart shell script file in your /etc/rc.local script.

### Hardware Schematic
![wiring diagram](https://raw.githubusercontent.com/dhowdy/BedMotionLEDs/master/MotionDetectedBedLEDs.png)

### Adjustments

You will likely have to adjust the GPIO pins in the software to reflect the actual GPIO pins that you use.

You will need to adjust the Lat/Long coordinates to your home town in the software.

You will need to adjust the color multipliers to achieve the color that you would like.  For example:
Red is ```Color(int(round(fadeLoop * 0)), fadeLoop, int(round(fadeLoop * 0)))```
Blue is ```Color(int(round(fadeLoop * 0)), int(round(fadeLoop * 0)), fadeLoop)```
A warm yellowish color is ```Color(int(round(fadeLoop * .5)), fadeLoop, int(round(fadeLoop * .1)))```

Basically, you'll need to move the 'fadeLoop' variable to your brightest RGB (this implementation uses GRB ordering) color and adjust the proportion of the other two colors.  In the last example, G will be 1/2 or R while B will be 1/10 of R.  This was a simple and fast implementation that worked for 99% of my uses.  


### Updates

This code is not very polished. There are still a lot of references and variables that are not used. I probably won't be cleaning these up.  But I'm happy to accept pull requests for anyone that wants to improve on this idea.
