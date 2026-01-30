#!/usr/bin/env bash

export DISPLAY=:1
export XAUTHORITY=/home/matthewyang/.Xauthority

dbus-monitor --system "type='signal',interface='org.freedesktop.login1.Manager',member='PrepareForSleep'" |
while read line; do
    if echo "$line" | grep -q "boolean true"; then
        /usr/bin/i3lock
    fi
done

