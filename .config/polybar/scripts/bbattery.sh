devices=$(bluetoothctl paired-devices | wc -l)
if [ $devices -gt 0 ]; then
    mac=$(bluetoothctl info | grep "Device" | cut -d ' ' -f 2) 
    battery=$(/home/pa1/.local/bin/bluetooth_battery $mac | cut -d ' ' -f 6)
    echo $battery
fi