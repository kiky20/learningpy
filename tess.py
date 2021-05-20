#This is a simple example using if else statement

#first you need to declare a variabble with input(), and change the data type into int()
sat = int(input("Masukan nilai dari 1- 100 : "))
sat <= 100
#stating condition with if first: and else: last. if it is more than two condition use elif: between them
if sat >= 90:
    print("Nilai A")
elif sat >= 80:
    print("Nilai B ")
elif sat >= 75:
    print("Nilai C ")
elif sat >= 70:
    print("Nilai D ")
elif sat >= 60:
    print("Nilai E ")
else:
    print("FAILURE!!")
