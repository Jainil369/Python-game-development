capitals = {"india":"new dehli","netherlands":"amsterdam"}
print(capitals["india"])
capitals["england"] = "london"
print(capitals)
capitals["england"] = "London"
print(capitals)
del capitals["netherlands"]
print(capitals)
for i in capitals:
    print(i,capitals[i])
for key,value in capitals.items():
    print(key,value)    