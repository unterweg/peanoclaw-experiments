from numpy import *
import Gnuplot, Gnuplot.funcutils

def plotTimePerIteration(gnuplot, subdivisionFactor):
  gnuplot('set terminal pdf dashed enhanced font "arial, 14" size 14cm,10cm')
  gnuplot('set output "figures/efficiencyOverGridSize' + str(subdivisionFactor) + 'SubdivisionFactor.pdf"')
  gnuplot.ylabel('Parallel Efficiency')
  gnuplot.plot('"< paste results/runtimeOverGridSize11Processes' + str(subdivisionFactor) + 'SubdivisionFactorWithHeapCompression.txt results/runtimeOverGridSize92Processes' + str(subdivisionFactor) + 'SubdivisionFactorWithHeapCompression.txt" using 2:($7/$14/9.1) with linespoints ls 1 title "With Compression",' \
             + '"< paste results/runtimeOverGridSize11Processes' + str(subdivisionFactor) + 'SubdivisionFactorWithoutHeapCompression.txt results/runtimeOverGridSize92Processes' + str(subdivisionFactor) + 'SubdivisionFactorWithoutHeapCompression.txt" using 2:($7/$14/9.1) with linespoints ls 2 title "Without Compression"')

def plot(subdivisionFactor):
  import gnuplot_settings
  gnuplot = Gnuplot.Gnuplot(debug=1)
  gnuplot_settings.setLineStyles(gnuplot)
  
  gnuplot('set format y "%.3te%+03T"')
  gnuplot.title('Parallel Efficiency 10 to 92 workers, Subdivision Factor ' + str(subdivisionFactor))
  gnuplot.xlabel('Grid Size per Dimension')
  
  plotTimePerIteration(gnuplot, subdivisionFactor)

if __name__ == '__main__':
  import argparse
  parser = argparse.ArgumentParser(description="Script for Gnuplotting Runtime over GridSize")
  parser.add_argument('-s', '--subdivision_factor', dest='subdivisionFactor', type=int, help='Subdivision Factor for Patches')
  arguments = parser.parse_args()
  
  if(arguments.subdivisionFactor == None):
    parser.print_help()
    exit()

  plot(arguments.subdivisionFactor)
