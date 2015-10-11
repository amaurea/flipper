#use to import all Flipper routines with:
#from flipper import *


#Useful python builtins
import os,sys,time
import numpy

#Pylab
import pylab
pylab.load = numpy.loadtxt
#Other dependencies
import healpy

#flipper specific
import astLib
import astLib.astWCS, astLib.astCoords
from . import utils, flipperDict, fftTools, liteMap, prewhitener, flTrace, mtm

pylab.load  = numpy.loadtxt
