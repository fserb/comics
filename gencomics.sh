#!/bin/bash
# Run on cron

./gencomics.py -
rsync -vr --partial --progress comics.xml fserb.com.br:www/comics.xml
