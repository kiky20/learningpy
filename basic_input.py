name = input("what is your name? :")
(age) = input("How old are you? :")
stat = input("are you a patient (Y/n):")
print("Name :", name)
print("Age :", str(age))
if stat.upper() == "Y":
    print("Is a patient")
else:
    print("not a patient")
