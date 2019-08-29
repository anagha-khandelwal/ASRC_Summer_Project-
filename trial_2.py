import sys
import re
import math
import datetime
import os
import re

# Can you push the output file new_file (C:\Users\khand_ptsvdpp\Downloads\cmder (1)\trial.csv) into the repo so I can take a look at it?
filename = r"C:\Users\khand_ptsvdpp\Downloads\cmder (1)\2OAU.pdb"
pdb_lines = open(filename).readlines()
new_file = r"C:\Users\khand_ptsvdpp\Downloads\cmder (1)\trial.csv" 
with open(new_file,'w') as newcvsfile:
	for line in pdb_lines:
		fields = line.split()
		if fields[0] == 'ATOM' and fields[2] == 'CA' :
			newcvsfile.write(str(fields))
	newcvsfile.close()

	



