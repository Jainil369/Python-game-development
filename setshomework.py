maths = {"John","Mary","Sarah","Adam"}
science = {"Adam","Jessica","Mary","David"}

print("Students that are in both classes are" , maths.intersection(science))
print("Students that are in Maths but not in science are" , maths.difference(science))
print(maths)
print(science)
print("The students that are taking either of the two subjects are" , maths.union(science))