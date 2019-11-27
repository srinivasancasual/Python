while True:
    try:
        r=int(input("Enter the Rows of matrix :(Enter 0 to exit) "))
        c=int(input("Enter the Columns of matrix :(Enter 0 to exit) "))
        if r==0 or c==0:
            break
        print("Enter Matrix 1")
        matrix1=[]
        for i in range(r):
            row=[]
            for j in range(c):
                user_input=int(input("Enter the value of {0} {1} ".format(i,j)))
                row.append(user_input)
            matrix1.append(row)
        matrix2=[]
        print("Enter Matrix 2")
        for i in range(r):
            row2=[]
            for j in range(c):
                user_input=int(input("Enter the value of {0} {1} ".format(i,j)))
                row2.append(user_input)
            matrix2.append(row2)
        #print("Matrix 1 - "+matrix1+"\nMatix2 -"+matrix2)
        condition=int(input("1.Addition\n2.Multiplication\n3.Transporse\nOther Input to exit"))
        if condition==1:
            if r==c:
                matrix3=[]
                for i in range(r):
                    row3=[]
                    for j in range(c):
                            row3.append(matrix1[i][j]+matrix2[i][j])
                    matrix3.append(row3)
                print(matrix3)
            else:
                print("Order matrix 1 must be equal to Order of matirx 2")
        elif condition==2:
            if r==c:
                matrix3=[]
                for i in range(r):
                    row3=[]
                    for j in range(c):
                        row3.append(matrix1[i][j]*matrix2[i][j])
                    matrix3.append(row3)
                print(matrix3)
            else:
                print("Order matrix 1 must be equal to Order of matirx 2")
        elif condition==3:
            matrix1t=[]
            matrix2t=[]
            for i in range(r):
                row1=[]
                row2=[]
                for j in range(c):
                    row1.append(matrix1[j][i])
                    row2.append(matrix2[j][i])
                matrix1t.append(row1)
                matrix2t.append(row2)
            print(matrix1t)
            print(matrix2t)
        else:
            break
    except:
        print("Enter Valid Integer")
               
