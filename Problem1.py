# Fernando Valadez-Nunez
# 03/05/2020

# The program will take two inputs from a user and check whether they are equal
# or not

if __name__=="__main__" :

    string1 = input("Enter the first variable: ")
    print(string1, end ="\n")

    string2 = input("Enter the second variable: ")
    print(string2, end ="\n")

    print("Are both variables the same: ", end = " ")

    if (string1 == string2) :
        print("Yes")

    else :
        print("No")
