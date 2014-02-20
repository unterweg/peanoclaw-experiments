#!/usr/bin/python

global lastID
lastID = -1

def callback(id, parameters, gridSize):
  processes = parameters[0]
  patchSize = parameters[1]
  eagerLimit = parameters[2]
  
  t_final = 1000
  
  global CSV
  global lastID
  if lastID != id:
    CSV.write("\nAxis " + str(id) + ": ")
    lastID = id

  print "Extracting data for", processes, "processes and a grid of", gridSize, "cells divided into subgrids of size", patchSize
  
  inputFileName = "output/output" + str(processes) + "Processes" + str(gridSize) + "GridSize" + str(patchSize) + "SubdivisionFactor" + str(t_final) + "TFinal.txt"
  
  with open(inputFileName, "r") as inputFile:
    foundLine = False
    for line in inputFile:
      if " SolveTimestep " in line:
        CSV.write(str(processes) + " " + str(patchSize) + " ")
        CSV.write(line.split()[7])
        CSV.write(" ")
        foundLine = True
        break
    if not foundLine:
      print "Error: File does not contain statistics line for SolveTimestep"


with open("data.csv", "w") as csv:
  global CSV
  CSV = csv

  from traversal import PlaneTraversal
  from traversal import LineTraversal
  from traversal import ParameterSpace
  t = LineTraversal(callback)
  ps = ParameterSpace(t)
  ps.traverse()
  
  csv.write("\n")

