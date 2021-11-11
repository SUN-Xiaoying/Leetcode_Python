# O(N)
# def main():
#     while True:
#         try:
#             n,k=map(int, input().split())
#             arr=list(map(int, input().split()))
#             left=0
#             m=0
#             for i in range(n):
#                 while arr[i]-arr[left]>=k:
#                     left+=1
#                 m=max(m,i-left+1)
#             print(m)
#         except:
#             break
# main()

from math import comb
while True:
    try:
        ppl=3
        n,d=map(int,input().split())
        arr=list(map(int,input().split()))

        left, right, total=0,2,0
        while left<n-2:
            while right<n and arr[right]-arr[left]<=d:
                right+=1
            if right-left>=ppl:
                total+=comb(right-left-1,ppl-1)
            left+=1

        print(total%99997867)
    except:
        break