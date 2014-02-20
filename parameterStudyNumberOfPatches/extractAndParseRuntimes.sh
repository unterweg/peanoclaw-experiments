#!/bin/bash

if [ -z $1 ]
then
  PATTERN="*"
else
  PATTERN="*$1*"
fi

grep -Ho "SolveTimestep [^|]*|[^|]*|[^|]*|[^|]*|" output/$PATTERN | egrep -o "output[0-9]+Processes.*" | sed "s/output/ /g" | sed "s/Processes/ /g" | sed "s/GridSize/ /g" | sed "s/SubdivisionFactor/ /g" | sed "s/HeapCompression/ /g" | sed "s/ReducedReductions/ /g" | sed "s/bdz.txt/bdz /g" | sed "s/.txt/snb /g" | sed "s/|//g"


