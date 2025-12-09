# notes on while loops
# While loop = execute some code While some condition remains true
#name = input("Enter your name:")

#if name == "":
    #print("You did not enter your name")
#else:
    #print(f"Hello {name}")

#while name == "":
    #print("You did not enter your name")
   # name = input("Enter your name:")
#print(f"Hello {name}")

#age = int(input("Enter your age:"))

#while age < 0 :
    #print (" Age can't be negative")
    #age= int(input("Enter your age:"))

#print(f"You are (age) years old")

#food =  input("Enter a food you like (q to quit):")
#food_list = []
#while not food == "q":
    #print(f"you like {food}")
   # food = ("Enter a food you like (q to quit):")

#print("bye")

#num = int(input(" Enter a # between 1 - 10:"))

#while num < 1 or num > 10:
  #print (f:{num} is not valid")
  #num = int(input(" Enter a # between 1 - 10:"))

#print ( f" Your number is {num}")
# Given:g
colors = ["red", "blue", "green", "yellow", "purple"]

# Challenge:
# Use a while loop to print each color UNTIL you find "yellow".
# Do NOT print "yellow" — stop before it.

for color in colors:
    if color == "yellow":
        break
    else:
        print(color)

for color in colors:
    if color == "yellow":
        continue
    else:
        print(color)



index = 0
while index < len(colors):
    if colors[index] == "yellow":
        break
    print(colors[index])
    index += 1 # increment the index to avoid infinite loop