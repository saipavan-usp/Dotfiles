#!/usr/bin/env bash

interval=0

# load colors
. ~/.config/bin/bar_themes/catpuccin

cpu() {
	cpu_val=$(grep -o "^[^ ]*" /proc/loadavg)

	printf "CPU"
	printf "$cpu_val"
}

pkg_updates() {
	updates=$(checkupdates | wc -l)   # arch , needs pacman contrib

	if [ -z "$updates" ]; then
		printf "  Fully Updated"
	else
		printf "  $updates"" Updates"
	fi
}

battery() {
	get_capacity="$(cat /sys/class/power_supply/BAT1/capacity)"
	printf "^  $get_capacity"
}

brightness() {
	printf "  "
	printf "%.0f\n" $(cat /sys/class/backlight/*/brightness)
}

mem() {
	printf " "
	printf "$(free -h | awk '/^Mem/ { print $3 }' | sed s/i//g)"
}

wlan() {
	case "$(cat /sys/class/net/wl*/operstate 2>/dev/null)" in
	up) printf "󰤨 ^%s" " $blue^Connected" ;;
	down) printf "^c$black^ ^b$blue^ 󰤭 ^d^%s" " ^c$blue^Disconnected" ;;
	esac
}

clock() {
	printf "^c$black^ ^b$darkblue^ 󱑆 "
	printf "^c$black^^b$blue^ $(date '+%I:%M %p')  "
}

while true; do
	[ $interval = 0 ] || [ $(($interval % 3600)) = 0 ] && updates=$(pkg_updates)
	interval=$((interval + 1))
	sleep 1 && xsetroot -name "$(pkg_updates)"
done
