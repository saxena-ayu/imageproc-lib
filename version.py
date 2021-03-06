#!/usr/bin/env python

"""
Write version and date information to a .c file, so compiles can be updated

authors: ronf, fgb, apullin
"""

import sys, os, time

# Check and parse arguments
if len(sys.argv) < 2:
    print("Not enough arguments given. Need version string within single quotes.")
    sys.exit()

filename   = 'version.c'
fileheader = 'version.h'
version    = sys.argv[1] # version string within single quotes
date       = time.strftime("%a %b %d %H:%M:%S %Y")

# Write version and date information
fileout = open(filename,'w')
fileout.write(
'/* automatically generated by version.py - do not edit! */\n\n' + \
'#include "' + fileheader + '"\n\n'                              + \
'static char version[] = "' + version + ': ' + date + '";\n\n'   + \
'char* versionGetString(void) { return version; }')
fileout.close()

print('updated ' + os.getcwd() + os.sep + filename)
