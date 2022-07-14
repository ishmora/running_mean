'''
This program reads stdin from a file containing a list of numbers
For each item in the list, the program calculates and prints out the estimate of
the running mean, running standard deviation, and running median
Test out github a bit...
'''

import numpy as np
import pandas as pd
import math
import fileinput
from decimal import Decimal

def running_mean(x, N):
   cumsum = np.cumsum(np.insert(x, 0, 0)) 
   return (cumsum[N:] - cumsum[:-N]) / N

def median(data):
    data.sort()
    mid = len(data) // 2
    return (data[mid] + data[~mid]) / 2

# the list
samples = []
# num items in list
numS    = 0
# decimal precision
dec     = 0


print("****************************")
# get stdin from file
# filename is passed as commandline arg
for i in fileinput.input():
   try:
      i = float(i)
      samples.append(i)
      # get num items in list
      numS = len(samples)
   except:
      # ignore malformed input
      continue

   # check for decimal number
   if int(i) == float(i):
      dec = 0
   else:
      dec = 3

   # does number have a decimal part?
   if math.modf(float(i))[0] > 0:
      print("Running mean: ", '%.3f' % running_mean(samples, numS))
      print("Running stddev: ", '%.3f' % np.std(samples))
      print("Running median: ", np.median(samples))
   else:
      # is running mean an int?
      if (running_mean(samples,numS)[0].is_integer()):
         print("Running mean: ", int(running_mean(samples, numS)))
      else:
         # num has decimal part, use precision of 1
         print("Running mean: ", '%.1f' % running_mean(samples, numS))

      # numpy standard deviation, biased estimator         
      print("Running stddev: " '{0:.3f}'.format(np.std(samples)).rstrip('0').rstrip('.'))

      # same int/float check for median
      if (np.median(samples).is_integer()):
         print("Running median: {0:.{1}f}".format(np.median(samples),dec))
      else:
         print("Running median: {0:.{1}f}".format(np.median(samples),dec+1))

   print("****************************")

   



