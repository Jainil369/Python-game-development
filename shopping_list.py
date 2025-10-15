print("Welcome to the online shopping centre")
print("please select your choices and input them")

menu = {"jacket":50,"trousers":20,"hoodie":27,"cap":12,"shoes":70}
bill = {}

for key,value in menu.items():
    print(key,value)

count = 0    

while True:
    item = input("please choose what you want to buy")    
    if item == "end":
        break
    quantity = int(input("how many of them do you want to buy"))    
    bill[item] = quantity

for key,value in bill.items():
    print(key,menu[key],value,menu[key] * value)
    count =  count + menu[key] * value

print("The final price is" + str(count))    


    