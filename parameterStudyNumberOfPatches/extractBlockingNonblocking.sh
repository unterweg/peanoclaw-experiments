#!/bin/bash

grep -H "SolveTimestep " output/output92Processes39366GridSize54SubdivisionFactorWithHeapCompressionWithReducedReductions*.txt | sed "s/.txt.*Statistics\(\)//g" | sed "s/output\/output.*Processes.*GridSize.*SubdivisionFactorWithHeapCompressionWithReducedReductions//g" | sed "s/#.*//g" | sed "s/()//g" | sort -n


grep -H "SolveTimestep " output/output92Processes39366GridSize54SubdivisionFactorWithHeapCompressionWithReducedReductions*.txt | wc -l
