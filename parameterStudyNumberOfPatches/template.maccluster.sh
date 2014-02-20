#!/bin/bash

#SBATCH -o output/job.__PROCESSES__Processes__GRID_SIZE__GridSize__SUBDIVISION_FACTOR__SubdivisionFactor__HEAP_COMPRESSION_TEXT____REDUCE_REDUCTIONS_TEXT__.out
#SBATCH -e output/job.__PROCESSES__Processes__GRID_SIZE__GridSize__SUBDIVISION_FACTOR__SubdivisionFactor__HEAP_COMPRESSION_TEXT____REDUCE_REDUCTIONS_TEXT__.err
#SBATCH -D /home/hpc/pr63so/lu26his2/workspace/diss/experiments/parameterStudyNumberOfPatches
#SBATCH -J peanoclaw.scalability.regular.__PROCESSES__processes
#SBATCH --get-user-env
#SBATCH --partition=snb
#SBATCH --ntasks=__PROCESSES__
#SBATCH --nodes=__NODE__
#SBATCH --mail-type=end
#SBATCH --mail-user=unterweg@in.tum.de
#SBATCH --export=NONE
#SBATCH --time=02:00:00

source /etc/profile.d/modules.sh

export PYTHONPATH=~/workspace/peanoclaw/src/python:~/workspace/peanoclaw/src/python:$PYTHONPATH
export LD_LIBRARY_PATH=~/programme/Python-2.7.5/lib:$LD_LIBRARY_PATH

#Output file
outputFile=output/output__PROCESSES__Processes__GRID_SIZE__GridSize__SUBDIVISION_FACTOR__SubdivisionFactor__HEAP_COMPRESSION_TEXT____REDUCE_REDUCTIONS_TEXT__.txt
echo $outputFile
echo "$outputFile" >/dev/stderr

mpiexec.hydra -n __PROCESSES__ python shallowCustomPatchGridSizeAndEndTime.py __GRID_SIZE__ __SUBDIVISION_FACTOR__ __T_FINAL__ 1 __USE_HEAP_COMPRESSION__ __FORK_LEVEL_INCREMENT__ __REDUCE_REDUCTIONS__ > $outputFile

