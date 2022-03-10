NOMONITORS=$(xrandr --listactivemonitors | grep -c 'HDMI-1\|LVDS-1')
ACTIVEMONITOR=$(xrandr --listactivemonitors | grep 'HDMI-1\|LVDS-1' | cut -d ' ' -f 6)

if [ $NOMONITORS -eq 2 ]; then
    echo ""
elif [ $ACTIVEMONITOR = "HDMI-1" ]; then
    echo ""
else
    echo ""
fi


function LVDS1 {
    echo "Activating LVDS-1"
    xrandr --output HDMI-1 --off --output LVDS-1 --auto
}

function HDMI1 {
    echo "Activating HDMI-1"
    xrandr --output LVDS-1 --off --output HDMI-1 --mode 1366x768
}

function DualMonitor {
    if [ $NOMONITORS -eq 1 ]; then
        if [[ $ACTIVEMONITOR = "HDMI-1" ]]; then
        	xrandr --output LVDS-1 --auto --same-as HDMI-1
        else
            xrandr --output HDMI-1 --mode 1366x768 --same-as LVDS-1
        fi
    fi
}

SELECTED=$(echo "1. LVDS-1
2. HDMI-1
3. DualMonitor" | rofi -dmenu)

SELECTED=`echo $SELECTED | sed "s/\-//" | cut -d " " -f 2`

$SELECTED