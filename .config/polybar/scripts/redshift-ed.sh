STATUS=`pgrep -c redshift`
if [[ $STATUS -eq 1 ]]; then
    killall redshift
else
    redshift -l 16.5433519:81.4811212
fi