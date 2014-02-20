import sys
import time
import shutil
from subprocess import call
from subprocess import Popen
from subprocess import PIPE
import os
from os.path import join

peanoclawPath=join(os.getenv("HOME"), "workspace/peanoclaw")
peano3Path=join(os.getenv("HOME"), "workspace/peano3")

mask = 0
flags = ['SendWorkerMasterMessagesBlocking', 'SendMasterWorkerMessagesBlocking', 'ReceiveMasterMessagesBlocking', 'SendAndReceiveLoadBalancingMessagesBlocking', 'ReceiveIterationControlMessagesBlocking', 'BroadcastToIdleNodesBlocking', 'BroadcastToWorkingNodesBlocking', 'SendAndReceiveHeapMetaDataBlocking']

startDirectory = os.getcwd()


#Job configuration
processes = 92
gridSize = 13122*3
subgridSize = 54


while mask < 2**len(flags):
  print "Running mask ", mask
   
  for i in xrange(len(flags)):
    enabled = (mask & (1<<i)) != 0

    os.chdir(peanoclawPath)

    #SED
    command = ['sed', '-i', 's/.*#define .*' + flags[i] + '.*/#define ' + flags[i] + ' ' + str(enabled).lower() + '/g ', join(peano3Path, 'src/tarch/compiler/LinuxIntel.h')]
    #print command
    call(command)


  #Scons
  command = ['scons', 'build=release', 'dim=2', 'parallel=yes', 'compiler=icc', '-j32']
  call(command)

  #Submit
  os.chdir(startDirectory)
  command = ['sbatch', 'runScripts/runPeanoClaw' + str(processes) + 'Processes' + str(gridSize) + 'Cells' + str(subgridSize) + 'PatchSizeWithHeapCompressionWithReducedReductions.sh']
  call(command)

  #Wait until job has finished
  running = True
  while running:
    p = Popen([join(os.getenv("HOME"), "tools/showJobs.sh")], stdout=PIPE)
    out, err = p.communicate()
    #print out
    print "lu26his2" in out
    running = "lu26his2" in out
    time.sleep(1)

  outputFile="output/output" + str(processes) + "Processes" + str(gridSize) + "GridSize" + str(subgridSize) + "SubdivisionFactorWithHeapCompressionWithReducedReductions.txt"
  print "Copying to", outputFile.replace(".txt", "{0:b}".format(10) + ".txt")
  shutil.copyfile(outputFile, outputFile.replace(".txt", "{0:b}".format(mask) + ".txt"))

  print ""
  mask+=1
