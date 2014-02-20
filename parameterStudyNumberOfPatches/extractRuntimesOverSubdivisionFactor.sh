#!/bin/bash

./extractAndParseRuntimes.sh "11Processes486*WithHeapCompression" | sort -n -k 3 > results/runtimeOverSubdivisionFactor11Processes486GridSizeWithHeapCompression.txt
./extractAndParseRuntimes.sh "11Processes1458*WithHeapCompression" | sort -n -k 3 > results/runtimeOverSubdivisionFactor11Processes1458GridSizeWithHeapCompression.txt
./extractAndParseRuntimes.sh "11Processes4374*WithHeapCompression" | sort -n -k 3 > results/runtimeOverSubdivisionFactor11Processes4374GridSizeWithHeapCompression.txt
./extractAndParseRuntimes.sh "11Processes13122*WithHeapCompression" | sort -n -k 3 > results/runtimeOverSubdivisionFactor11Processes13122GridSizeWithHeapCompression.txt
./extractAndParseRuntimes.sh "92Processes486*WithHeapCompression" | sort -n -k 3 > results/runtimeOverSubdivisionFactor92Processes486GridSizeWithHeapCompression.txt
./extractAndParseRuntimes.sh "92Processes1458*WithHeapCompression" | sort -n -k 3 > results/runtimeOverSubdivisionFactor92Processes1458GridSizeWithHeapCompression.txt
./extractAndParseRuntimes.sh "92Processes4374*WithHeapCompression" | sort -n -k 3 > results/runtimeOverSubdivisionFactor92Processes4374GridSizeWithHeapCompression.txt
./extractAndParseRuntimes.sh "92Processes13122*WithHeapCompression" | sort -n -k 3 > results/runtimeOverSubdivisionFactor92Processes13122GridSizeWithHeapCompression.txt

./extractAndParseRuntimes.sh "11Processes486*WithoutHeapCompression" | sort -n -k 3 > results/runtimeOverSubdivisionFactor11Processes486GridSizeWithoutHeapCompression.txt
./extractAndParseRuntimes.sh "11Processes1458*WithoutHeapCompression" | sort -n -k 3 > results/runtimeOverSubdivisionFactor11Processes1458GridSizeWithoutHeapCompression.txt
./extractAndParseRuntimes.sh "11Processes4374*WithoutHeapCompression" | sort -n -k 3 > results/runtimeOverSubdivisionFactor11Processes4374GridSizeWithoutHeapCompression.txt
./extractAndParseRuntimes.sh "11Processes13122*WithoutHeapCompression" | sort -n -k 3 > results/runtimeOverSubdivisionFactor11Processes13122GridSizeWithoutHeapCompression.txt
./extractAndParseRuntimes.sh "92Processes486*WithoutHeapCompression" | sort -n -k 3 > results/runtimeOverSubdivisionFactor92Processes486GridSizeWithoutHeapCompression.txt
./extractAndParseRuntimes.sh "92Processes1458*WithoutHeapCompression" | sort -n -k 3 > results/runtimeOverSubdivisionFactor92Processes1458GridSizeWithoutHeapCompression.txt
./extractAndParseRuntimes.sh "92Processes4374*WithoutHeapCompression" | sort -n -k 3 > results/runtimeOverSubdivisionFactor92Processes4374GridSizeWithoutHeapCompression.txt
./extractAndParseRuntimes.sh "92Processes13122*WithoutHeapCompression" | sort -n -k 3 > results/runtimeOverSubdivisionFactor92Processes13122GridSizeWithoutHeapCompression.txt
