STATUS=`pgrep -c redshift`
[[ $STATUS -eq 1 ]] && echo ""; 
[[ $STATUS -eq 0 ]] && echo ""; 