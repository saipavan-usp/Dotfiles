xsetroot -cursor_name left_ptr

sh ~/Scripts/check-mon.sh
sh ~/Scripts/fix-sound.sh

killall -9 picom xfce4-power-manager dunst nm-applet polybar

dunst &
xfce4-power-manager &
nm-applet &
picom --experimental-backends &
/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &
feh --bg-scale Walls/magic-windmills-jo.jpg
sh ~/.config/polybar/launch.sh &
/usr/lib/kdeconnectd &