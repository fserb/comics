#!/bin/bash
# Run on cron

./gencomics.rb
#./gencomics.py
rsync -vr --partial --progress newfeed.xml fserb.com.br:www/comics.xml
