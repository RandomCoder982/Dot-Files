#!/bin/bash

echo "Working"

spotify-launcher &
sleep 0.8
wmctrl -r spotify-launcher -t
