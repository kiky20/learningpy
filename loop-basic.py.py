#this is a for loop statement
for v in range(6):
  print(v)
#the v is just a random variable,it will print the int()

#in below is a "while loops" example
#start by declaring a variabel(or you can use exsited variabel)
x = 1
#stating the condition first
while x <= 5:
    print(x)
    #dont forget the order too like this one. or it will looping endlessly
    x += 1
#and this one is nested loop
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)

#this is another loop example
for x in range(5):
  for y in range(2):
    print(f"{x},{y}")
