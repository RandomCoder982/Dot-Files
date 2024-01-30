#!/bin/bash

age=17

if [ "$age" -not 18]; then
    echo "you can vote"
else
    echo "you can not vote"
fi