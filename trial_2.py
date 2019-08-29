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
			# now since we know the code is running fine, we can add more things to it
			# 1. delete the line below
			# 2. remember our job is to creat a cvs file that has the heading of (look at the excel sheet we made together). So the first 
			#thing we need to make sure is the distance between residues 
			# 2.1 calculate the distance between all the CA atoms between all residues, so go and add another for loop underneath line 12 
			#(name is line2) this will make sure that the code goes though all redidues 
			# 2.2 underneath line 13, splite the new line to fields (name them fields2)
			# 2.3 underneath line 14, display the x,y,z coordinates of both fields.  code below
			#print("this is field ",field[5],field[6],field[7])
			#print("this is field2 ",field[5],field[6],field[7])
			newcvsfile.write(str(fields))
	newcvsfile.close()

	



