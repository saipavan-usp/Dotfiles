#! /bin/bash

if [ `ping -c 1 -q google.com >&/dev/null; echo $?` -eq 0 ]; then
	echo ""
else
	echo "睊"
fi

