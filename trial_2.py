import sys
import re
import math
import datetime
import os
import re

filename = r"C:\Users\khand_ptsvdpp\Downloads\cmder (1)\2OAU.pdb"
pdb_lines = open(filename).readlines()
new_file = r"C:\Users\khand_ptsvdpp\Downloads\cmder (1)\trial.csv" 
with open(new_file,'w') as newcvsfile:
	for line in pdb_lines:
		fields = line.split()
		if fields[0] == 'ATOM' and fields[2] == 'CA' :
			newcvsfile.write(str(fields))
	newcvsfile.close()

	



