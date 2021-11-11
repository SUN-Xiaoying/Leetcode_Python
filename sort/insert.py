# Time: O(N^2) - O(N), Related to data status
# Space: O(N)

while True:
    try:
        n=int(input())
        a=list(map(int, input().split()))
        if n<2: print(*a)
        n=len(a)
        for i in range(1,n):
            j=i-1
            while j>=0 and a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
                j-=1
        print(*a)
    except:
        break