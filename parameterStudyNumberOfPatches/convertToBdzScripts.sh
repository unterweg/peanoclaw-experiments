#!/bin/bash

for line in $(ls -1 runScripts/*.sh)
do
  echo $line
  sed -i "s/partition=snb/partition=bdz/g" $line
  sed -i "s/\.txt/bdz.txt/g" $line
done
