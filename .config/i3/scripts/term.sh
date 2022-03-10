function term {
	i3-msg workspace 1
	sleep 1
	i3-msg split h
	sleep 1
	i3-msg "exec terminator -e htop"
	sleep 1
	i3-msg "exec echo 9 | terminator -e topgrade"
	sleep 1
	i3-msg split v
	sleep 1
	i3-msg "exec terminator --working-directory=/run/media/PAWAN"
}

term
