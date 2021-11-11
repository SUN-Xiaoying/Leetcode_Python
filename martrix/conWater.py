N = int(input())
nums = list(map(int, input().split()))
 
res = 0
maxH = max(nums)
idx = nums.index(maxH)
leftH,rightH = 0, 0
for i in range(idx):
    if nums[i] < leftH:
        res += (leftH - nums[i])
    else:
        leftH = nums[i]
for i in range(N-1, idx, -1):
    if nums[i] < rightH:
        res += (rightH - nums[i])
    else:
        rightH = nums[i]
print(res)

# while True:
#     try:
#         n= int(input())
#         if n<3: 
#             print(0)
#             break
#         N=input().split()
#         arr=[]
#         for i in range(0,n):
#             arr[i]=int(N[i])
#         total=0
#         l, r=1, len(arr)-2
#         l_max,r_max=arr[0], arr[-1]
#         while l<r:
#             if arr[l]<=arr[r]:
#                 if l_max < arr[l]:
#                     l_max = arr[l]
#                 else:
#                     total+=l_max-arr[l]
#                 l+=1      
#             else:
#                 if r_max < arr[r]:
#                     r_max = arr[r]
#                 else:
#                     total+=r_max-arr[r]
#                 r-=1
#         print(total)

#     except:
#         break