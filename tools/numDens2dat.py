#!/usr/bin/env python

# Script: numDens2dat.py
# Author: Mario Orsi (m.orsi at qmul.ac.uk, www.orsi.sems.qmul.ac.uk)
# Purpose: This script processes a file containing a number density
#          distribution generated by 'fix ave/spatial'
# Syntax: numDens2dat.py inputFile
# Example: numDens2dat.py numDensChol.zProfile > ndpChol.dat
# Notes:  - inputFile = LAMMPS output file generated by fix ave/spatial

import sys,os,string

if len(sys.argv) != 2:
  print "Syntax: numDens2dat.py inputFile"
  sys.exit()

inFileName = sys.argv[1]
inFile = open(inFileName, "r")
lines = inFile.readlines()
inFile.close()

angstrom3_to_nm3 = 0.001 # 1 A^3 = 0.001 nm^3

# calculate and electron density:
for line in lines:
    if line[0] != '#': # ignore comments
        words = string.split(line)
        if len(words) == 4:
            coord = float(words[1])
            numDensity = float(words[3])
            print coord, numDensity/angstrom3_to_nm3 # [A, nm^(-3)]
