n = int(input())                    
nums = list(map(int, input().split())) 
b=set(nums)
if len(b)<len(nums):
    print("true")
else:
    print("false")
