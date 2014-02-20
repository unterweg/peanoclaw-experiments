from numpy import *
import Gnuplot, Gnuplot.funcutils

def plotTimePerIteration(gnuplot, processes, subdivisionFactor):
  gnuplot('set terminal pdf dashed enhanced font "arial, 14" size 14cm,10cm')
  gnuplot('set output "figures/runtimePerIterationOverGridSize' + str(processes) + 'Processes' + str(subdivisionFactor) + 'SubdivisionFactor.pdf"')
  gnuplot.ylabel('Time per Iteration [s]')
  gnuplot.plot('"results/runtimeOverGridSize' + str(processes) + 'Processes' + str(subdivisionFactor) + 'SubdivisionFactorWithHeapCompression.txt" using 2:7 with linespoints ls 1 title "With Compression",' \
             + '"results/runtimeOverGridSize' + str(processes) + 'Processes' + str(subdivisionFactor) + 'SubdivisionFactorWithoutHeapCompression.txt" using 2:7 with linespoints ls 2 title "Without Compression"')
             
def plotTimePerCell(gnuplot, processes, subdivisionFactor):
  gnuplot('set terminal pdf dashed enhanced font "arial, 14" size 14cm,10cm')
  gnuplot('set output "figures/runtimePerCellOverGridSize' + str(processes) + 'Processes' + str(subdivisionFactor) + 'SubdivisionFactor.pdf"')
  gnuplot.ylabel('Time per Cell [s]')
  gnuplot.plot('"results/runtimeOverGridSize' + str(processes) + 'Processes' + str(subdivisionFactor) + 'SubdivisionFactorWithHeapCompression.txt" using 2:($7/$2/$2) with linespoints ls 1 title "With Compression",' \
             + '"results/runtimeOverGridSize' + str(processes) + 'Processes' + str(subdivisionFactor) + 'SubdivisionFactorWithoutHeapCompression.txt" using 2:($7/$2/$2) with linespoints ls 2 title "Without Compression"')

def plot(processes, subdivisionFactor):
  import gnuplot_settings
  gnuplot = Gnuplot.Gnuplot(debug=1)
  gnuplot_settings.setLineStyles(gnuplot)
  
  gnuplot('set format y "%.3te%+03T"')
  gnuplot.title(str(processes) + ' Processes, Subdivision Factor ' + str(subdivisionFactor))
  gnuplot.xlabel('Grid Size per Dimension')
  
  plotTimePerIteration(gnuplot, processes, subdivisionFactor)
  plotTimePerCell(gnuplot, processes, subdivisionFactor)
  
if __name__ == '__main__':
  import argparse
  parser = argparse.ArgumentParser(description="Script for Gnuplotting Runtime over GridSize")
  parser.add_argument('-p', '--processes', dest='processes', type=int, help='Number of Processes')
  parser.add_argument('-s', '--subdivision_factor', dest='subdivisionFactor', type=int, help='Subdivision Factor for Patches')
  arguments = parser.parse_args()
  
  if(arguments.processes == None or arguments.subdivisionFactor == None):
    parser.print_help()
    exit()

  print "processes=", arguments.processes, "subdivfac=", arguments.subdivisionFactor
  plot(arguments.processes, arguments.subdivisionFactor)
  
