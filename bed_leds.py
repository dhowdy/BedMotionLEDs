#!/usr/bin/python
# this script turns on leds for bed when motion is detected between dusk and dawn

import time
import RPi.GPIO as GPIO
from neopixel import *

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# Time in seconds to turn off after last motion detection
time_on = 15

# Time to wait between motion checks
sleep_sec = .9

# LED strip configuration:
LED_COUNT      = 6      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 5       # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)

# Define functions which animate LEDs in various ways.
def colorWipe(strip, color, wait_ms=50):
   """Wipe color across display a pixel at a time."""
   for i in range(strip.numPixels()):
      strip.setPixelColor(i, color)
      strip.show()
      time.sleep(wait_ms/200.0)




if __name__ == '__main__':
   # Create NeoPixel object with appropriate configuration.
   strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
   # Intialize the library (must be called once before other functions).
   strip.begin()

   print "turning strip off" 
   colorWipe(strip, Color(0, 0, 0))

   waiting_sec = 0
   leds_on = 0


   while True:               # G, R, B

      if GPIO.input(4):
         print "motion detected"
         waiting_sec = 0
         
         if leds_on == 0:
            print "turning strip on"
            colorWipe(strip, Color(0, 0, 255))
            leds_on = 1

      
         time.sleep(sleep_sec)
   
      else:
         print "no motion detected in " + str(waiting_sec) + " seconds."
         waiting_sec += 1
         time.sleep(sleep_sec)
 
      
      if ( waiting_sec > time_on and leds_on == 1):
         leds_on = 0
         print "turning strip off" 
         colorWipe(strip, Color(0, 0, 0))    
  
   
