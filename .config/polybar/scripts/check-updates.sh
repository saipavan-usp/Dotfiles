#!/bin/sh

PACMAN_UPDATES=$(checkupdates 2> /dev/null | wc -l )
YAY_UPDATES=$(yay -Qum 2> /dev/null | wc -l )

UPDATES=$(("$PACMAN_UPDATES" + "$YAY_UPDATES"))

echo " $UPDATES"
