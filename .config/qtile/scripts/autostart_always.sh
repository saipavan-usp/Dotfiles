#!/bin/bash

polybar -c ~/.config/polybar/normal.ini qtile &
# polybar -c ~/.config/polybar/rounded.ini qtile &
picom --experimental-backends &
dunst &
nm-applet &
blueman-applet &
sh ~/Scripts/monitor.sh 2
feh --bg-fill ~/Walls/magenta-cat.png &