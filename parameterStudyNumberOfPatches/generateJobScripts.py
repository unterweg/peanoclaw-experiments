#!/usr/bin/python
from parameters import ParameterSpace, ParameterSet


if __name__=='__main__':
  from argparse import ArgumentParser
  parser = ArgumentParser()
  parser.add_argument('template', nargs='?', default='template.sh')
  parser.add_argument('tasksPerNode', nargs='?', default=16, type=int)
  arguments = parser.parse_args()

  #Set up parameter space
  parameterSpace = ParameterSpace()

  f=5

  for reduceReductions in [0, 1]:
    for processes in [1, 10, 11, 82, 83, 11+81, 730, 11+81+729 ]: #, 6562]:
      forkLevelIncrement = 1
      if(processes == 82 or processes == 83 or processes == 730):
        forkLevelIncrement = 2


      psProcesses = ParameterSet(processes=processes, tasks_per_node=arguments.tasksPerNode, forkLevelIncrement=forkLevelIncrement, reduceReductions=reduceReductions)

      #6x6 Patches
      ps6x6PatchSize = psProcesses.derive(patchSize=6)
      parameterSpace.addParameterSet(ps6x6PatchSize.derive(gridSize=162, tFinal=1, useHeapCompression=1))
      parameterSpace.addParameterSet(ps6x6PatchSize.derive(gridSize=486, tFinal=f, useHeapCompression=1))
      parameterSpace.addParameterSet(ps6x6PatchSize.derive(gridSize=1458, tFinal=f*f, useHeapCompression=1))
      parameterSpace.addParameterSet(ps6x6PatchSize.derive(gridSize=4374, tFinal=f*f*f, useHeapCompression=1))
      parameterSpace.addParameterSet(ps6x6PatchSize.derive(gridSize=13122, tFinal=f*f*f*f, useHeapCompression=1))
      parameterSpace.addParameterSet(ps6x6PatchSize.derive(gridSize=13122*3, tFinal=f*f*f*f*f, useHeapCompression=1))
      parameterSpace.addParameterSet(ps6x6PatchSize.derive(gridSize=162, tFinal=1, useHeapCompression=0))
      parameterSpace.addParameterSet(ps6x6PatchSize.derive(gridSize=486, tFinal=f, useHeapCompression=0))
      parameterSpace.addParameterSet(ps6x6PatchSize.derive(gridSize=1458, tFinal=f*f, useHeapCompression=0))
      parameterSpace.addParameterSet(ps6x6PatchSize.derive(gridSize=4374, tFinal=f*f*f, useHeapCompression=0))
      parameterSpace.addParameterSet(ps6x6PatchSize.derive(gridSize=13122, tFinal=f*f*f*f, useHeapCompression=0))
      parameterSpace.addParameterSet(ps6x6PatchSize.derive(gridSize=13122*3, tFinal=f*f*f*f*f, useHeapCompression=0))

      #18x18 Patches
      ps18x18PatchSize = psProcesses.derive(patchSize=18)
      parameterSpace.addParameterSet(ps18x18PatchSize.derive(gridSize=486, tFinal=f, useHeapCompression=0))
      parameterSpace.addParameterSet(ps18x18PatchSize.derive(gridSize=1458, tFinal=f*f, useHeapCompression=0))
      parameterSpace.addParameterSet(ps18x18PatchSize.derive(gridSize=4374, tFinal=f*f*f, useHeapCompression=0))
      parameterSpace.addParameterSet(ps18x18PatchSize.derive(gridSize=13122, tFinal=f*f*f*f, useHeapCompression=0))
      parameterSpace.addParameterSet(ps18x18PatchSize.derive(gridSize=13122*3, tFinal=f*f*f*f*f, useHeapCompression=0))
      parameterSpace.addParameterSet(ps18x18PatchSize.derive(gridSize=486, tFinal=f, useHeapCompression=1))
      parameterSpace.addParameterSet(ps18x18PatchSize.derive(gridSize=1458, tFinal=f*f, useHeapCompression=1))
      parameterSpace.addParameterSet(ps18x18PatchSize.derive(gridSize=4374, tFinal=f*f*f, useHeapCompression=1))
      parameterSpace.addParameterSet(ps18x18PatchSize.derive(gridSize=13122, tFinal=f*f*f*f, useHeapCompression=1))
      parameterSpace.addParameterSet(ps18x18PatchSize.derive(gridSize=13122*3, tFinal=f*f*f*f*f, useHeapCompression=1))

      #54x54 Patches
      ps54x54PatchSize = psProcesses.derive(patchSize=54)
      parameterSpace.addParameterSet(ps54x54PatchSize.derive(gridSize=486, tFinal=f, useHeapCompression=1))
      parameterSpace.addParameterSet(ps54x54PatchSize.derive(gridSize=1458, tFinal=f*f, useHeapCompression=1))
      parameterSpace.addParameterSet(ps54x54PatchSize.derive(gridSize=4374, tFinal=f*f*f, useHeapCompression=1))
      parameterSpace.addParameterSet(ps54x54PatchSize.derive(gridSize=13122, tFinal=f*f*f*f, useHeapCompression=1))
      parameterSpace.addParameterSet(ps54x54PatchSize.derive(gridSize=13122*3, tFinal=f*f*f*f*f, useHeapCompression=1))
      parameterSpace.addParameterSet(ps54x54PatchSize.derive(gridSize=13122*9, tFinal=f*f*f*f*f*f, useHeapCompression=1))
      parameterSpace.addParameterSet(ps54x54PatchSize.derive(gridSize=486, tFinal=f, useHeapCompression=0))
      parameterSpace.addParameterSet(ps54x54PatchSize.derive(gridSize=1458, tFinal=f*f, useHeapCompression=0))
      parameterSpace.addParameterSet(ps54x54PatchSize.derive(gridSize=4374, tFinal=f*f*f, useHeapCompression=0))
      parameterSpace.addParameterSet(ps54x54PatchSize.derive(gridSize=13122, tFinal=f*f*f*f, useHeapCompression=0))
      parameterSpace.addParameterSet(ps54x54PatchSize.derive(gridSize=13122*3, tFinal=f*f*f*f*f, useHeapCompression=0))
      parameterSpace.addParameterSet(ps54x54PatchSize.derive(gridSize=13122*9, tFinal=f*f*f*f*f*f, useHeapCompression=0))

      #162x162 Patches
      ps162x162PatchSize = psProcesses.derive(patchSize=162)
      parameterSpace.addParameterSet(ps162x162PatchSize.derive(gridSize=486, tFinal=f, useHeapCompression=1))
      parameterSpace.addParameterSet(ps162x162PatchSize.derive(gridSize=1458, tFinal=f*f, useHeapCompression=1))
      parameterSpace.addParameterSet(ps162x162PatchSize.derive(gridSize=4374, tFinal=f*f*f, useHeapCompression=1))
      parameterSpace.addParameterSet(ps162x162PatchSize.derive(gridSize=13122, tFinal=f*f*f*f, useHeapCompression=1))
      parameterSpace.addParameterSet(ps162x162PatchSize.derive(gridSize=13122*3, tFinal=f*f*f*f*f, useHeapCompression=1))
      parameterSpace.addParameterSet(ps162x162PatchSize.derive(gridSize=13122*9, tFinal=f*f*f*f*f*f, useHeapCompression=1))
      parameterSpace.addParameterSet(ps162x162PatchSize.derive(gridSize=486, tFinal=f, useHeapCompression=0))
      parameterSpace.addParameterSet(ps162x162PatchSize.derive(gridSize=1458, tFinal=f*f, useHeapCompression=0))
      parameterSpace.addParameterSet(ps162x162PatchSize.derive(gridSize=4374, tFinal=f*f*f, useHeapCompression=0))
      parameterSpace.addParameterSet(ps162x162PatchSize.derive(gridSize=13122, tFinal=f*f*f*f, useHeapCompression=0))
      parameterSpace.addParameterSet(ps162x162PatchSize.derive(gridSize=13122*3, tFinal=f*f*f*f*f, useHeapCompression=0))
      parameterSpace.addParameterSet(ps162x162PatchSize.derive(gridSize=13122*9, tFinal=f*f*f*f*f*f, useHeapCompression=0))

  startlines = parameterSpace.generateJobScripts(arguments.template)


