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
				for lines2 in pdb_lines:
					fields2 = line.split()
					print("this is field",fields[5], fields[6], fields[7])
					print("this is field2", fields2[5],fields2[6], fields2[7]) 
			
	newcvsfile.close()

	



