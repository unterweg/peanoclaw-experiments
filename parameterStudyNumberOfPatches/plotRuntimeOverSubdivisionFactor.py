from numpy import *
import Gnuplot, Gnuplot.funcutils

def plotTimePerIteration(gnuplot, processes, gridSize):
  gnuplot('set terminal pdf dashed enhanced font "arial, 14" size 14cm,10cm')
  gnuplot('set output "figures/runtimePerIterationOverSubdivisionFactor' + str(processes) + 'Processes' + str(gridSize) + 'GridSize.pdf"')
  gnuplot.ylabel('Time per Iteration [s]')
  gnuplot.plot('"results/runtimeOverSubdivisionFactor' + str(processes) + 'Processes' + str(gridSize) + 'GridSizeWithHeapCompression.txt" using 3:7 with linespoints ls 1 title "With Compression",' \
             + '"results/runtimeOverSubdivisionFactor' + str(processes) + 'Processes' + str(gridSize) + 'GridSizeWithoutHeapCompression.txt" using 3:7 with linespoints ls 2 title "Without Compression"')
         

def plot(processes, gridSize):
  import gnuplot_settings
  gnuplot = Gnuplot.Gnuplot(debug=1)
  gnuplot_settings.setLineStyles(gnuplot)
  
  gnuplot('set format y "%.3te%+03T"')
  gnuplot.title(str(processes) + ' Processes, Grid Size ' + str(gridSize))
  gnuplot.xlabel('Subdivision Factor')
  
  plotTimePerIteration(gnuplot, processes, gridSize)

if __name__ == '__main__':
  import argparse
  parser = argparse.ArgumentParser(description="Script for Gnuplotting Runtime over SubdivisionFactor")
  parser.add_argument('-p', '--processes', dest='processes', type=int, help='Number of Processes')
  parser.add_argument('-g', '--grid_size', dest='gridSize', type=int, help='Gridsize per Dimension')
  arguments = parser.parse_args()
  
  if(arguments.processes == None or arguments.gridSize == None):
    parser.print_help()
    exit()

  plot(arguments.processes, arguments.gridSize)
  
