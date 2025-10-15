import random

one = [["_","_","_","_","_" ],["_","_","_","_","_" ],["_","_","_","_","_" ],["_","_","_","_","_" ],["_","_","_","_","_" ]]

for i in range(len(one)):
    for j in range(len(one[i])):
        print(one[i][j],end = " ")
    print()    

x,y = (random.randint(1,5),random.randint(1,5))  
print(x,y)

while True:
    v = input("Enter where you think the treasure is").split()
    a,b = tuple(v)
    if int(a) > x:
        print("go up")
    elif int(a) < x:
        print("Go down") 
    elif int(b) > y:
        print("go left")
    elif int(b) < y:
        print("go right")           
    elif (int(a),int(b)) == (x,y):
        print("you have found the treasure")    
        break    