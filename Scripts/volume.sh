#!/bin/bash

dunst_progress () {
    dunstify "Volume" -h string:x-dunst-stack-tag:test "" -h int:value:"$(pamixer --get-volume)" -t 2000 2> /dev/null
}

inc () {
    pamixer -i $1 && dunst_progress
}

dec () {
    pamixer -d $1 && dunst_progress
}

toggle_mute () {
    pamixer -t
}

case $1 in
    "inc")
        inc $2
        ;;
    "dec")
        dec $2
        ;;
    "mute")
        toggle_mute
        ;;
esac