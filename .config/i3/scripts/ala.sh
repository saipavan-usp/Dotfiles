i3-msg 'workspace 1; append_layout ~/.config/i3/workspace-1.json;'
alacritty --config-file=/home/pawan-i3/alacritty.yml -e "htop" &
sleep 0.5;
alacritty --config-file=/home/pawan-i3/alacritty.yml -e tail -F ~/i3logs/log-$(date +'%F') &
sleep 0.5;
alacritty --config-file=/home/pawan-i3/alacritty.yml --working-directory "/run/media/PAWAN" &


