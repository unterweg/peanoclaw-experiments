#!/bin/bash

if [ -z $1 ]
then
  PATTERN=".*"
else
  PATTERN=$1
fi

for runScript in `ls -1 runScripts | grep "$PATTERN"` 
do
  llsubmit runScripts/$runScript
done
