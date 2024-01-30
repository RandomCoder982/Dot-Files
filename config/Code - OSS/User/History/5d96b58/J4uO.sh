#!/bin/bash

read input

if [ $input -ge 1 ]; then
    nmcli d wifi
else
    nmcli -f "CHAN,BARS,SIGNAL,SSID" d wifi list ifname wlx10feed21ae1d  | sort -n
fi