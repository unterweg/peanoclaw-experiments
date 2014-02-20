#!/bin/bash
#
#@ wall_clock_limit = 02:00:00
#@ job_name = peanoclaw.scalability.regular.__PROCESSES__processes
#@ job_type = parallel
#@ class = __CLASS__
#@ node = __NODE__
#@ total_tasks = __PROCESSES__
#@ node_usage = not_shared
#@ island_count = 1
#@ output = output/job$(jobid).out
#@ error = output/job$(jobid).err
#@ queue
. /etc/profile
. /etc/profile.d/modules.sh

#Paths and modules
module unload python

export PYTHONPATH=~/workspace/peanoclaw/src:~/workspace/clawpack:$PYTHONPATH
export PATH=~/programme/Python-2.7.5/bin:$PATH
export LD_LIBRARY_PATH=~/programme/Python-2.7.5/lib:$LD_LIBRARY_PATH

#Output file
outputFile=output/output__PROCESSES__Processes__GRID_SIZE__GridSize__SUBDIVISION_FACTOR__SubdivisionFactor__HEAP_COMPRESSION_TEXT____REDUCE_REDUCTIONS_TEXT__.txt
echo $outputFile
echo "$outputFile" >/dev/stderr
echo -n "__PROCESSES__: " > time__PROCESSES__.txt

#MPI Settings
#export MP_EAGER_LIMIT=__EAGER_LIMIT__
#export MP_TIMEOUT=36000
#export MP_PULSE=0
#export MP_DEBUG_COMM_TIMEOUT=yes
#export MP_DEBUG_NOTIMEOUT=yes

#Run
/usr/bin/time -f %e -ao time__PROCESSES__.txt poe python shallowCustomPatchGridSizeAndEndTime.py __GRID_SIZE__ __SUBDIVISION_FACTOR__ __T_FINAL__ 1 __USE_HEAP_COMPRESSION__ __FORK_LEVEL_INCREMENT__ __REDUCE_REDUCTIONS__ > $outputFile


