temp_path=~/.config/dunst/dunstrc.template
norm_path=~/.config/dunst/dunstrc


bg=$(cat ~/.Xresources | grep background | cut -d " " -f 2)
fg=$(cat ~/.Xresources | grep foreground | cut -d " " -f 2)
cbg=$(cat ~/.Xresources | grep color9 | tr -s " " | cut -d " " -f 2)
fc=$(cat ~/.Xresources | grep color5 | tr -s " " | cut -d " " -f 2)
cfg=$(cat ~/.Xresources | grep foreground | cut -d " " -f 2)

sed "s/urgency_low_background/\"$bg\"/g;s/urgency_low_foreground/\"$fg\"/g;s/urgency_critical_background/\"$cbg\"/g;s/urgency_critical_foreground/\"$cfg\"/g;s/dunst_frame_color/\"$fc\"/g" $temp_path > $norm_path 

killall dunst;
dunst &