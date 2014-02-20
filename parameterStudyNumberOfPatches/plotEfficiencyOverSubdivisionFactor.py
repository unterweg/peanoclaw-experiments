from numpy import *
import Gnuplot, Gnuplot.funcutils

def plotTimePerIteration(gnuplot, gridSize):
  gnuplot('set terminal pdf dashed enhanced font "arial, 14" size 14cm,10cm')
  gnuplot('set output "figures/efficiencyOverSubdivisionFactor' + str(gridSize) + 'GridSize.pdf"')
  gnuplot.ylabel('Parallel Efficiency')
  gnuplot.plot('"< paste results/runtimeOverSubdivisionFactor11Processes' + str(gridSize) + 'GridSizeWithHeapCompression.txt results/runtimeOverSubdivisionFactor92Processes' + str(gridSize) + 'GridSizeWithHeapCompression.txt" using 3:($7/$14/9.1) with linespoints ls 1 title "With Compression",' \
             + '"< paste results/runtimeOverSubdivisionFactor11Processes' + str(gridSize) + 'GridSizeWithoutHeapCompression.txt results/runtimeOverSubdivisionFactor92Processes' + str(gridSize) + 'GridSizeWithoutHeapCompression.txt" using 3:($7/$14/9.1) with linespoints ls 2 title "Without Compression"')

def plot(gridSize):
  import gnuplot_settings
  gnuplot = Gnuplot.Gnuplot(debug=1)
  gnuplot_settings.setLineStyles(gnuplot)
  
  gnuplot('set format y "%.3te%+03T"')
  gnuplot.title('Parallel Efficiency 10 to 92 workers, Grid Size ' + str(gridSize))
  gnuplot.xlabel('Subdivision Factor')
  
  plotTimePerIteration(gnuplot, gridSize)

if __name__ == '__main__':
  import argparse
  parser = argparse.ArgumentParser(description="Script for Gnuplotting Runtime over SubdivisionFactor")
  parser.add_argument('-g', '--grid_size', dest='gridSize', type=int, help='Gridsize per Dimension')
  arguments = parser.parse_args()
  
  if(arguments.gridSize == None):
    parser.print_help()
    exit()

  plot(arguments.gridSize)
