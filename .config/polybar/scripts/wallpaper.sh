WALL=$(ls -t ~/Walls | grep 'jpg\|png\|jpeg' | rofi -dmenu -p "Select Wallpaper: ")
[[ -z $WALL ]] && exit
feh --bg-scale ~/Walls/"$WALL"
