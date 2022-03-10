i3-msg 'workspace 1; append_layout ~/.config/i3/workspace-1.json;'
terminator -e "htop" &
sleep 0.5;
terminator --working-directory=/run/media/PAWAN &
sleep 0.5;
terminator &

firefox &
thunar &
