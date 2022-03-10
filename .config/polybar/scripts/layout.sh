LAYOUT=$(qtile cmd-obj -o layout -f info | grep "'name'" | sed 's/}//' | cut -d ":" -f 2 | sed 's/'\''//g')
qtile cmd-obj -o layout -f info
echo $LAYOUT