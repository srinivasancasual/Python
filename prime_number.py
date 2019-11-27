while True:
    try:
        user_input=int(input("Enter the number N - (Enter 0 to exit, N should be >=2)"))
        if user_input==0:
            print("Exiting")
            break
        else:
            for i in range(2,user_input+1):
                for j in range(2,i):
                    if i%j==0:
                        break
                else:
                    print(i,end=" ")
    except:
        print("Enter Integer")
def get_prime(user_input):
    primeList=[]
    if user_input==0:
        print("Exiting")
        return
    else:
        for i in range(2,user_input+1):
            for j in range(2,i):
                if i%j==0:
                    break
            else:
                primeList.append(i)
        return primeList
print(get_prime(100))
