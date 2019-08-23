import sys
import re
import math
import datetime
import os
import re

create trial.csv file 
filename = "\Users\khand_ptsvdpp\Downloads\cmder\2OAU.pdb"

pdb_lines = open(filename).readlines()
new_file = "trial.csv"  # I would create the new files in the same directory as 2OAU.pdb, so write it as new_file = "\Users\khand_ptsvdpp\Downloads\cmder\trial.csv"

# Before going into the PDB file, I would create the new file, just uncomment the line below
#with open(new_file,'w') as newcvsfile:
	for line in pdb_lines: 
		fields = line.split()
		if fields[0] == 'ATOM' and fields[2] == 'CA':
		# Here I would first make sure that the code is running, so I would just append the lines that starts with ATOM and have CA is col 2, again uncomment the 2 lines below and run the code
		#newcvsfile.write(fields)
	#newcvsfile.close()

	# comment the 4 lines below, otherwise the code won't run
	xi = float(fields[6])
	yi = float(fields[7])
	zi = float(fields[8])
	dis = 
