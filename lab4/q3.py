# File: q3.py
# Author: Yuhao Ye
# Date: 06/28/2020
# Section: 529006730
# E-mail: yeyuhao1234@tamu.edu
# Description:
# TAsk for the number of rows, and the number of columns of matrix A on one line.
#  Ask for the number of rows, and the number of columns of matrix B on one line.
#  Ask for the numbers in each matrix.
# Then execute Matrix multiplication


matrix_A = input("Enter matrix A rows and columns: ").split()
matrix_B = input("Enter matrix B rows and columns: ").split()
A = input("Enter matrix A: ").split()
B = input("Enter matrx B: ").split()

print()
matrixA_rows = int(matrix_A[0])
matrixA_colums = int(matrix_A[1])
matrixB_rows = int(matrix_B[0])
matrixB_colums = int(matrix_B[1])
# the information of matrix C
matrixC_rows = matrixA_rows
matrixC_colums = matrixB_colums

# The information of matrix T
matrixT_rows = matrixC_colums
matrixT_colums =  matrixC_rows

if matrixA_rows <= 10 and matrixA_colums <= 10 and matrixB_colums <=10 and matrixB_rows <= 10:
    Matrix_A = list()
    Matrix_B = list()
    Matrix_C = list()
    Matrix_T = list()
    ## convert 1d list to multi- dimension list
    for rows in range(0,matrixA_rows):
        rows_list = list()
        for cols in range(0,matrixA_colums):
             rows_list.append(A[rows * matrixA_colums + cols])
        Matrix_A.append(rows_list)

    for rows in range(0,matrixB_rows):
        rows_list = list()
        for cols in range(0,matrixB_colums):
             rows_list.append(B[rows * matrixB_colums + cols])
        Matrix_B.append(rows_list)
    # print matrix
    print("Matrix A: ")
    for rows in range(0,matrixA_rows):
        for cols in range(0,matrixA_colums):
            print(Matrix_A[rows][cols],end=" ")
        print()

    print()
    print("Matrix B:")
    for rows in range(0, matrixB_rows):
        for cols in range(0, matrixB_colums):
            print(Matrix_B[rows][cols], end=" ")
        print()

    print()

    ## set all elemnt in Matrix C to zero
    if matrixA_colums != matrixB_rows:
        print("A and B cannot be multiplied due to size mismatch!")
    else:
        for rows in range(0, matrixC_rows):
            rows_list = list()
            for cols in range(0, matrixC_colums):
                rows_list.append(0)
            Matrix_C.append(rows_list)


        for rows in range(0,matrixA_rows):
            for cols in range(0,matrixB_colums):
              result = 0
              for rows_B in range(0,matrixB_rows):
                result += int(Matrix_A[rows][rows_B]) * int(Matrix_B[rows_B][cols])
              Matrix_C[rows][cols] = result

        print("Matrix C: ")
        for rows in range(matrixC_rows):
            for cols in range(matrixC_colums):
                print(Matrix_C[rows][cols],end = " ")
            print()
        print()

        print("Transpose matrix T: ")

        for rows in range(matrixT_rows):
            rows_list  =  list()
            for cols in range(matrixT_colums):
                rows_list.append(0)
            Matrix_T.append(rows_list)

        for rows in range(matrixC_rows):
            for cols in range(matrixC_colums):
                Matrix_T[cols][rows] = Matrix_C[rows][cols]

        for rows in range(matrixT_rows):
            for cols in range(matrixT_colums):
                print(Matrix_T[rows][cols],end =" ")
            print()

else:
    print("A and B cannot be multipiled due to the number of rows or columns exceed 10 ")



