b=`cat /sys/class/backlight/intel_backlight/brightness`
echo `expr $1 + $b` > /sys/class/backlight/intel_backlight/brightness
