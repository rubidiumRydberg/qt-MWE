#! /bin/bash

#This very small shell script
#will convert the PYQT UI file 
#into a python class. Requires
#pyuic5 to be available in the path
#This is usually automatic upon
#installation of PYQT5

pyuic5 GUI.ui -o GUI.py