#This is a simple example using if else statement

#first you need to declare a variabble with input(), and change the data type into int()
sat = int(input("what is your marks between 1- 100 : "))
sat <= 100
#stating condition with if first: and else: last. if it is more than two condition use elif: between them
if sat >= 90:
    print("Grade A")
elif sat >= 80:
    print("Grade B ")
elif sat >= 75:
    print("Grade C ")
elif sat >= 70:
    print("Grade D ")
elif sat >= 60:
    print("Grade E ")
else:
    print(" such a FAILURE!!")
