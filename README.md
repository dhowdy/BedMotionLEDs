# BedMotionLEDs

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
![wiring diagram]
