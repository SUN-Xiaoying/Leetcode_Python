# Time: O(N^2)
# Space: O(1)

while True:
    try:
        n=int(input())
        a=list(map(int, input().split()))
        if n<2: print(*a)
        n=len(a)
        for i in range(n):
            minIndex=i
            for j in range(i,n):
                if a[j]<a[minIndex]: minIndex=j
            a[i],a[minIndex]=a[minIndex],a[i]
        print(*a)
    except:
        break