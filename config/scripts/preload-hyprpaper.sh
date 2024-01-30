#!/bin/bash

search_dir=/home/irene/Pictures/wallpapers
echo starting 

for preloader_wallpaper in "$(cat ~/.config/hypr/hyprpaper.conf)"
	for wallpaper in "$search_dir"/*;
	if 
	do
		echo "preload = $wallpaper" >>~/.config/hypr/hyprpaper.conf
	done
