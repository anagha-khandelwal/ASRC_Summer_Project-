import sys
import re
import math
import datetime
import os
import re

create trial.csv file 
filename = "\Users\khand_ptsvdpp\Downloads\cmder\2OAU.pdb"

pdb_lines = open(filename).readlines()
new_file = "trial.csv"

for line in pdb_lines:
    fields = line.split()
    if fields[0] == 'ATOM' and fields[2] == 'CA':
	xi = float(fields[6])
	yi = float(fields[7])
	zi = float(fields[8])
	dis = 