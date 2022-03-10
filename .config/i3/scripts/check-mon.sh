if xrandr --listactivemonitors | grep "HDMI"; then
    sh ~/Scripts/monitor.sh 2
else
    sh ~/Scripts/monitor.sh 1
fi