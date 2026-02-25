import math

class Student():
    def __init__(self,name,rollno,maths,physics,chemistry,biology):
        self.name = name
        self.rollno = rollno
        self.maths = maths
        self.physics = physics
        self.chemistry = chemistry
        self.biology = biology
    def display(self):
        print("In maths ", self.name ,"  got:",self.maths)
        print("In physics" ,self.name ," got:", self.physics)
        print("In chemistry",self.name," got:",self.chemistry)
        print("In biology:",self.name," got",self.biology)
    def total(self):
        total = self.maths + self.physics + self.chemistry + self.biology
        print("Total marks of",self.name,"is:",total)        
    def percentage(self):
        total = self.maths + self.physics + self.chemistry + self.biology
        percentage = (total/400)*100
        print("Percentage of",self.name,"is:",percentage)
        
Bob = Student("Bob",5,85,90,80,95)
Mark = Student("Mark",11,68,78,88,92)  

print("What would you like to see?")
print("1. See your marks")
print("2. Total marks")
print("3. Percentage")

while True:
    choice = int(input("Enter your choice:"))
    if choice == 1 :
        Bob.display()
        Mark.display() 
    elif choice == 3:
        Bob.percentage()
        Mark.percentage()
    elif choice == 2:
        Bob.total()
        Mark.total()    
    else:
        print("Invalid choice, please try again.")    
