n=int(input())
m=int(input())
fs=[]
for i in range(n):
    row = list(map(int, input().split()))
    fs.append(row)

count=0
for row in fs:
    for i in row:
        if i<0:
            count+=1
   
print(count)
