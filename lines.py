while True:
    try:
        user_input=int(input("Enter the lines (Enter 0 to exit) "))
        if(user_input==0):
            break
        else:
            for i in range(0,user_input):
                for j in range(0,i):                    
                    print(" ",end=" ")
                print(i+1)
    except:
        print("Enter the integer")