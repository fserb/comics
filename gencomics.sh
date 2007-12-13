#!/bin/sh

export LD_LIBRARY_PATH="/home/fserb/run/lib:"
export LD_RUN_PATH="/home/fserb/run/lib:"
export PATH="$PATH:/home/fserb/run/bin"
export PYTHONPATH="/home/fserb/.python"
./gencomics.py
