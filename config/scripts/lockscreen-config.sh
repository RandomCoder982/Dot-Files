#!/bin/bash

xhost +
waybar_pid=$(pgrep -x waybar)
lockscreen=true


#Kill waybar if it's active
if [ !  -f ~/.config/scripts/lockscreen-condition ];
then
	if [ $waybar_pid ];
	then
		pkill '^waybar$'
	fi
	hyprlock
	touch ~/.config/scripts/lockscreen-condition
fi

if [ -f ~/.config/scripts/lockscreen-condition ];
then
	nohup waybar &
	rm ~/.config/scripts/lockscreen-condition
fi


