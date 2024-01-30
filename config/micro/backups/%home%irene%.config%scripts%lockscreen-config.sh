#!/bin/bash

xhost +
waybar_pid=$(pgrep -x waybar)
slock_pid=$(pgrep -x slock)


	
#Kill waybar if it's active
if [ !  -f ~/.config/scripts/lockscreen-condition ];
then
	if [ $waybar_pid ];
	then
		pkill '^waybar$'
	fi
	slock
	touch ~/.config/scripts/lockscreen-condition
fi

if [ -f ~/.config/scripts/lockscreen-condition ];
then
	nohup waybar &
	rm ~/.config/scripts/lockscreen-condition
fi


