players = {}
print("welcome to the football players game")
print("If you want to add or change a player please enter add ")
print("if you want to view a player pleasea enter view ")
print("if you want to delete a player please enter delete ")
print("if you want to end the game please enter end")

while True:
    ans = input("enter your choice")
    if ans == "add":
        print("Please enter the first name of the football player")
        answer1 = input()
        print("Please enter the last name of the football player")
        answer2 = input()
        players[answer1] = answer2
    elif ans == "delete" :
        print("Please enter the first name of the football player")
        ans1 = input()
        del players[ans1]    
    elif ans == "view":
        for key,value in players.items():
            print(key,value)
    elif ans == "end":
        print("I hope you enjoyed the game. Please see your existing players below")
        for key,value in players.items():
            print(key,value)
        break 

