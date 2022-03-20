function DualMonitor {
	echo "Activating both Monitors"
	xrandr --output HDMI-1 --auto --same-as LVDS-1
	xrandr --output HDMI-1 --mode 1366x768
}

function SingleHDMI1 {
	echo "Switching to HDMI1"
	xrandr --output LVDS-1 --off --output HDMI-1 --auto
	xrandr --output HDMI-1 --mode 1366x768
}

function SingleLVDS1 {
	echo "Switching to LVDS-1"
        xrandr --output HDMI-1 --off --output LVDS-1 --auto
}

DEFAULT=$1
HDMIACTIVE=`xrandr --listactivemonitors | grep -c HDMI-1`
HDMICONNECTED=`xrandr -q | grep -c "HDMI-1 connected"`
HDMIDISCONNECTED=`xrandr -q | grep -c "HDMI-1 disconnected"`

while true; do
    if [ $HDMICONNECTED -gt 0 ]; then
        SingleHDMI1
        while [ $HDMIDISCONNECTED -gt 0 ]; do
            sleep 1
            
done

trap MonitorFix SIGINIT
trap MonitorFix EXIT