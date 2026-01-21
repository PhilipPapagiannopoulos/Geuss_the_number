import random
y = 5000
count=0
win = 0
lives=10

x = random.randint(1,1000)

while y != x and lives > 0:
    y = int(input("Guess a number between 1 and 1000:"))
    count += 1
    if x > y :
      print("go up")
      lives -= 1
    elif x < y:
      print("go down")
      lives -= 1
    elif x == y:
      win = 1
    print("you have ", lives, "lives left")

if win == 1:
    print ("You won with"  ,count, ("tries"))
    print("The number was", x)
else:
    print("The number was", x)