#!/bin/bash

./extractAndParseRuntimes.sh "11Processes*6SubdivisionFactor*WithHeapCompression"  | sort -n -k 2 > results/runtimeOverGridSize11Processes6SubdivisionFactorWithHeapCompression.txt
./extractAndParseRuntimes.sh "11Processes*18SubdivisionFactor*WithHeapCompression" | sort -n -k 2 > results/runtimeOverGridSize11Processes18SubdivisionFactorWithHeapCompression.txt
./extractAndParseRuntimes.sh "11Processes*54SubdivisionFactor*WithHeapCompression" | sort -n -k 2 > results/runtimeOverGridSize11Processes54SubdivisionFactorWithHeapCompression.txt
./extractAndParseRuntimes.sh "92Processes*6SubdivisionFactor*WithHeapCompression"  | sort -n -k 2 > results/runtimeOverGridSize92Processes6SubdivisionFactorWithHeapCompression.txt
./extractAndParseRuntimes.sh "92Processes*18SubdivisionFactor*WithHeapCompression" | sort -n -k 2 > results/runtimeOverGridSize92Processes18SubdivisionFactorWithHeapCompression.txt
./extractAndParseRuntimes.sh "92Processes*54SubdivisionFactor*WithHeapCompression" | sort -n -k 2 > results/runtimeOverGridSize92Processes54SubdivisionFactorWithHeapCompression.txt

./extractAndParseRuntimes.sh "11Processes*6SubdivisionFactor*WithoutHeapCompression"  | sort -n -k 2 > results/runtimeOverGridSize11Processes6SubdivisionFactorWithoutHeapCompression.txt
./extractAndParseRuntimes.sh "11Processes*18SubdivisionFactor*WithoutHeapCompression" | sort -n -k 2 > results/runtimeOverGridSize11Processes18SubdivisionFactorWithoutHeapCompression.txt
./extractAndParseRuntimes.sh "11Processes*54SubdivisionFactor*WithoutHeapCompression" | sort -n -k 2 > results/runtimeOverGridSize11Processes54SubdivisionFactorWithoutHeapCompression.txt
./extractAndParseRuntimes.sh "92Processes*6SubdivisionFactor*WithoutHeapCompression"  | sort -n -k 2 > results/runtimeOverGridSize92Processes6SubdivisionFactorWithoutHeapCompression.txt
./extractAndParseRuntimes.sh "92Processes*18SubdivisionFactor*WithoutHeapCompression" | sort -n -k 2 > results/runtimeOverGridSize92Processes18SubdivisionFactorWithoutHeapCompression.txt
./extractAndParseRuntimes.sh "92Processes*54SubdivisionFactor*WithoutHeapCompression" | sort -n -k 2 > results/runtimeOverGridSize92Processes54SubdivisionFactorWithoutHeapCompression.txt

