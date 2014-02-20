import math

class ParameterSet:
  def __init__(self, processes=None, tasks_per_node=None, gridSize=None, patchSize=None, tFinal=None, useHeapCompression=None, forkLevelIncrement=None, reduceReductions=None):
    self.processes = processes
    self.tasks_per_node = tasks_per_node
    self.gridSize = gridSize
    self.patchSize = patchSize
    self.tFinal = tFinal
    self.useHeapCompression = useHeapCompression
    self.forkLevelIncrement = forkLevelIncrement
    self.reduceReductions = reduceReductions
    
  def derive(self, processes=None, tasks_per_node=None, gridSize=None, patchSize=None, tFinal=None, useHeapCompression=None, forkLevelIncrement=None, reduceReductions=None):
    return ParameterSet(
      self.processes if processes==None else processes,
      self.tasks_per_node if tasks_per_node==None else tasks_per_node,
      self.gridSize if gridSize==None else gridSize,
      self.patchSize if patchSize==None else patchSize,
      self.tFinal if tFinal==None else tFinal,
      self.useHeapCompression if useHeapCompression==None else useHeapCompression,
      self.forkLevelIncrement if forkLevelIncrement==None else forkLevelIncrement,
      self.reduceReductions if reduceReductions==None else reduceReductions
    )

  def generateJobScript(self, templateFileName):
    if(self.processes==None or self.tasks_per_node==None or self.gridSize==None or self.patchSize==None or self.tFinal==None or self.useHeapCompression==None or self.forkLevelIncrement==None or self.reduceReductions==None):
      raise Exception("ParameterSet not fully specified! " + str(self))
  
    print "Generating job script for", self.processes, "processes and a grid of", (self.gridSize), "cells divided into subgrids of size", self.patchSize
    
    heapCompressionText = "With" + ("" if self.useHeapCompression else "out") + "HeapCompression"
    reductionText = "With" + ("" if self.reduceReductions else "out") + "ReducedReductions"
    nodes = int(math.ceil(float(self.processes) / self.tasks_per_node))
  
    inputFileName = templateFileName
    outputFileName = "runScripts/runPeanoClaw" + str(self.processes) + "Processes" \
      + str(self.gridSize) + "Cells" + str(self.patchSize) + "PatchSize" + heapCompressionText + reductionText + ".sh"
    
    with open(inputFileName, "r") as inputFile:
      with open(outputFileName, "w") as outputFile:
        for line in inputFile:
          newLine = line
          newLine = newLine.replace("__NODE__", str(max(1, nodes)))
          newLine = newLine.replace("__TASKS_PER_NODE__", str(self.tasks_per_node))
          newLine = newLine.replace("__PROCESSES__", str(self.processes))
          newLine = newLine.replace("__GRID_SIZE__", str(self.gridSize))
          newLine = newLine.replace("__SUBDIVISION_FACTOR__", str(self.patchSize))
          #newLine = newLine.replace("__EAGER_LIMIT__", str(eagerLimit))
          newLine = newLine.replace("__T_FINAL__", str(self.tFinal))
          newLine = newLine.replace("__USE_HEAP_COMPRESSION__", str(self.useHeapCompression))
          newLine = newLine.replace("__HEAP_COMPRESSION_TEXT__", heapCompressionText)
          newLine = newLine.replace("__CLASS__", "test" if nodes <= 32 else "general")
          newLine = newLine.replace("__FORK_LEVEL_INCREMENT__", str(self.forkLevelIncrement))
          newLine = newLine.replace("__REDUCE_REDUCTIONS__", str(self.reduceReductions))
          newLine = newLine.replace("__REDUCE_REDUCTIONS_TEXT__", reductionText)
          outputFile.write(newLine)
    
    return outputFileName

  def __str__(self):
    return "processes=" + str(self.processes) + ", tasks_per_node=" + str(self.tasks_per_node) + ", gridSize=" + str(self.gridSize) + ", patchSize=" + str(self.patchSize) + ", tFinal=" + str(self.tFinal) + ", useHeapCompression=" + str(self.useHeapCompression) + ", forkLevelIncrement=" + str(self.forkLevelIncrement) + ", reduceReductions=" + str(self.reduceReductions)

class ParameterSpace:

  def __init__(self):
    self.parameterSets = []
    
  def addParameterSet(self, parameterSet):
    self.parameterSets.append(parameterSet)
    
  def generateJobScripts(self, templateFileName):
    startlines = []
    for parameterSet in self.parameterSets:
      startlines.append(parameterSet.generateJobScript(templateFileName))
      
    return startlines
    
    
    
