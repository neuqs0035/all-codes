import pyinputplus as pyin

print("-----------------------------")
print("|      Matrix Addition      |")
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

def add_matrix(matrix1,matrix2):

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