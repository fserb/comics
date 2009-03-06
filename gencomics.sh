#!/bin/sh
#
# For various ridiculous reasons, we can't run a cron job on the current machine.
# This script is run on a screen instance

while [ 1 ]; do
  ./gencomics.py -
  echo "done"
  sleep 10800
done