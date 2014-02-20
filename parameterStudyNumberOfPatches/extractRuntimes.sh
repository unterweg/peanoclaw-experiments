#!/bin/bash

if [ -z $1 ]
then
  PATTERN="*"
else
  PATTERN="*$1*"
fi

grep -o "SolveTimestep [^|]*|[^|]*|[^|]*|[^|]*|" output/$PATTERN
