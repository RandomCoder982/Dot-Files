#!/bin/bash
ACTIVE_WIN=$(xdotool getactivewindow 2>/dev/null)
if [ -z "$ACTIVE_WIN" ]; then
    # protected window that can't be analyzed, e.g. gnome-terminal
    echo "Failed to get active win"
    exit 1
fi
WINDOW=$(echo $(xwininfo -id $ACTIVE_WIN -stats | \
                egrep '(Width|Height):' | \
                awk '{print $NF}') | \
         sed -e 's/ /x/')
SCREEN=$(xdpyinfo | grep -m1 dimensions | awk '{print $2}')
if [ "$WINDOW" = "$SCREEN" ]; then
    exit 0
else
    exit 1
fi
