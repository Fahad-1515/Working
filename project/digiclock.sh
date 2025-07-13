#!/bin/bash
while true
do
    clear
    currenttime=$(date "+%T")
    color=$((RANDOM % 7 + 1))
    fontsize="\e[7m"
    case $color in
        1) textcolor="\e[91m";;  # Red
        2) textcolor="\e[92m";;  # Green
        3) textcolor="\e[93m";;  # Yellow
        4) textcolor="\e[94m";;  # Blue
        5) textcolor="\e[95m";;  # Purple
        6) textcolor="\e[96m";;  # Cyan
        7) textcolor="\e[97m";;  # White
        *) textcolor="\e[97m";;  # Default
    esac

    echo -e "${fontsize}${textcolor}    ${currenttime}    "
    sleep 1
done
