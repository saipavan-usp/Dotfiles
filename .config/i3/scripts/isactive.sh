function Fox {
	while [[ `wmctrl -lx | grep Navigator.firefox | grep -vc grep` -eq 0 ]]
        do
                sleep 1
        done
}


function Term {
	while [[ `wmctrl -lx | grep terminator.Terminator | grep -vc grep` -eq 0 ]]
	do
                sleep 1
        done
}

if [ "$1" -eq 1 ]; then
	Fox
elif [ "$1" -eq 2 ]; then
	Term
fi
