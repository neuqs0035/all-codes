import pyinputplus as pyin

print("-----------------------------")
print("|    Matrix Substraction    |")
print("-----------------------------")

def input_matrix(row,col):

	matrix = []
	rows = []

	print("")

	for i in range(0,row):
		for j in range(0,col):

			rows.append(pyin.inputInt(prompt=f"Enter Element For Position m[{i}][{j}] : "))
			
		matrix.append(rows)
		rows = []

	return matrix

def substract_matrix(matrix1,matrix2):

	output_matrix = []
	rows = []

	for row in range(len(matrix1)):

		for col in range(len(matrix1[0])):

			element = matrix1[row][col] + matrix2[row][col]
			rows.append(element)

		output_matrix.append(rows)
		rows = []

	return output_matrix

def display_matrix(matrix):

	for row in range(len(matrix)):

		for col in range(len(matrix[0])):

			print(f"|   {matrix[row][col]}",end="   ")

		print("|")

	print(f"\nOrder = {len(matrix)} x {len(matrix[0])}\n")
	

print("\nFor Matrix 1 :-")
m1_row_count = pyin.inputInt(prompt="\nEnter No Of Rows : ",greaterThan=0)
m1_col_count = pyin.inputInt(prompt="\nEnter No Of Columns : ",greaterThan=0)

print("\nFor Matrix 2 :-")
m2_row_count = pyin.inputInt(prompt="\nEnter No Of Rows : ",greaterThan=0)
m2_col_count = pyin.inputInt(prompt="\nEnter No Of Columns : ",greaterThan=0)

if (m1_col_count+m1_row_count) != (m2_col_count+m2_row_count):
	print("\nBoth Matrix's Orders Are Not Same , Substraction Is Not Possible")
	
else:
	
	print("\nFor Matrix 1 :-")
	matrix1 = input_matrix(m1_row_count,m1_col_count)
	print("\nFor Matrix 2 :-")
	matrix2 = input_matrix(m1_row_count,m1_col_count)

	output_matrix = substract_matrix(matrix1,matrix2)
	print("\nOutput Matrix\n")
	display_matrix(output_matrix)