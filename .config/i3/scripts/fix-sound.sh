#!/bin/bash

CURR_MONITOR=`xrandr --listactivemonitors | sed -n '2p' | cut -d " " -f 6`

if [ "$CURR_MONITOR" = "HDMI1" ]; then
	notify-send "Switched To External Audio"
	pactl set-card-profile 0 output:hdmi-stereo
else
	notify-send "Switched To Laptop Audio"
	pactl set-card-profile 0 output:analog-stereo
fi
