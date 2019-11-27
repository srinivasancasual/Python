def checkPlaindrome(word):
    j=len(word)-1
    for i in range(0,j):
        if not word[i]==word[j]:
            return False
        j=j-1
    else:
        return True
while True:
    user_input=input("Enter the word (Enter exit to exit application) ")
    if(user_input=="exit"):
        print("Exiting","bye")
        break
    if checkPlaindrome(user_input):
        print("Given String is palindrome")
    else:
        print("Given String is not a palindrome")
