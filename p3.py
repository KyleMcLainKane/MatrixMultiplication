#
# Program #3 (p3.py)
# Program designed to take in matrices from file and multiply them
# CS320-1
# 10-14-19
# Author: Kyle McLain Kane cssc0498
#

# Header comment section (typical assignment info)
import sys

# This function begins execution of program.
# Verify data input filename provided on command line: len(sys.argv)
# If error, output message for user: Usage: p3.py dataFileName'
# and quit, using sys.exit()
#
# Declare A, B, call read_matrices to initialize A, B, and store
# return value as C
#
# Print A and B contents
#
# Call mult_matrices
#
# Print result contents
#
def main():
	print("Program #3, cssc0498, Kyle McLain Kane")
	
	if len(sys.argv) != 2:
		print("Usage: p3.py dataFileName")
		sys.exit()
	
	#Initializing the matrices	
	A = []
	B = []	
	C = []
	
	C = read_matrices(A,B)
	
	#Printing the contents of A and B
	print("Matrix A contents:")
	print_matrix(A)
	print("Matrix B contents:")
	print_matrix(B)	
	
	mult_matrices(A,B,C)
	
	print("Matrix A * B is:")
	print_matrix(C)
	
	sys.exit()


# This function reads m, n, and p from the datafile.
# Then matrices A and B are filled from the datafile.
# Matrix C is then allocated size m x p.
# The values for m, n, and p are local values filled in by this function
# PARAMETERS in order are:
# list matrix A
# list matrix B
# RETURN matrix C
#
def read_matrices(A,B):
	m = 0;
	n = 0;
	p = 0;
	
	try:		
		with open(sys.argv[1], 'r') as f:	
			m = [int(x) for x in next(f).split()] # read line
			n = [int(x) for x in next(f).split()] # read line
			p = [int(x) for x in next(f).split()] # read line
		
			#Filling the matrices	
			for i in range(0,m[0]):
				A.append([int(x) for x in next(f).split()])
			for i in range(0,n[0]):	
				B.append([int(x) for x in next(f).split()])	
			
			#Giving C the correct size matrix for mult	
			C = [[0 for i in range(p[0])] for j in range(m[0])]
			return C
	except IOError:
		print ("File not found")	
		sys.exit()
										
	

		
# This function prints a matrix. Rows and columns should be preserved.
# PARAMETERS in order are:
# list The matrix to print
#
def print_matrix(matrix):
	for i in range(len(matrix)):
		for j in range(len(matrix[i])):
			print('\t', matrix[i][j], end = ' ')
		print()	
	print()	

	
# The two matrices A and B are multiplied, and matrix C contains the
# result.
# PARAMETERS in order are:
# list Matrix A
# list Matrix B
# list Matrix C (all zeros at this point)
#
def mult_matrices(A,B,C):
	for i in range(len(A)): 
    		for j in range(len(B[0])): 
        		for k in range(len(B)): 
           			 C[i][j] += A[i][k] * B[k][j] 

		
# Begin program
if __name__ == '__main__':
 main()
