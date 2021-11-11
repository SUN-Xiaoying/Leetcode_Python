# Time: O(N^2)
# Space: O(1)

while True:
    try:
        n=int(input())
        arr=list(map(int, input().split()))  
        for i in range(n-1):
            for j in range(n-i):
                if arr[j]>arr[j+1]:
                    arr[j],arr[j+1] = arr[j+1],arr[j]
        print(*arr)
    except:
        break