one = [[1,2,3],[4,5,6],[7,8,9]]
two = [[1,2,3],[4,5,6],[7,8,9]]

three = [[0,0,0],[0,0,0],[0,0,0]]

count = 0

"""for i in range(len(one)):
    for j in range(len(two)):
         ans = (one[i][i] + two[j][j])
         print(ans)         
         
for i in range(len(one)):
    for j in range(len(one[i])):
        three[i][j] = one[i][j] + two[i][j]
    print()  

for i in range(len(one)):
    for j in range(len(one[i])-1,-1,-1):
        print(one[i][j],end = " ")      
    print()

print(three)"""

for i in range(len(one)):
    for j in range(len(one[i])):
        count = count + one[i][j]

print(count)       