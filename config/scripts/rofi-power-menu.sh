#! /bin/sh

chosen=$(printf "Power Off\nRestart\nLock" | rofi -dmenu -i -theme-str '@theme "/usr/share/rofi/themes/Adapta-Nokto.rasi"')

case "$chosen" in
	"Power Off") poweroff ;;
	"Restart") reboot ;;
	"Lock") hyprlock ;;
	*) exit 1 ;;
esac
