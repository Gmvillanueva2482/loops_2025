#Loops video  https://www.youtube.com/watch?v=KWgYha0clzw&t=1s&pp=ygUOYnJvIGNvZGUgbG9vcHM%3D
#While loops  

# for loops= execute a block of code a fixed number of times

for x in range(1,11):
    print(x)
print ("HAPPY NEW YEAR!")


for x in reversed(range(1,11,2)):
    print(x)
print ("HAPPY NEW YEAR!")

Credit_card= "1234-5678-9012-3456"

for x in Credit_card:
    print()

for x in range (1,21):
    if x == 13:
        continue
    else:
        print(x)
        
for x in range (1,21):
    if x == 13:
        break
    else:
        print(x)