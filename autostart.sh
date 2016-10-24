#!/bin/bash
#
# This script acts as a watchdog in the event that our program crashes.

until /usr/bin/python ./bed_leds.py; do
  echo "Bed Lights exited with code $?.  Restarting..." >&2
  sleep 10
done
