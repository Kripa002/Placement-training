n = input()
count = 0

for i in n:
    if i == '{':
        count += 1
    elif i == '}':
        if count == 0:
            print("Not Matching")
            break
        count -= 1
else:
    if count == 0:
        print("Matching")
    else:
        print("Not Matching")

   
