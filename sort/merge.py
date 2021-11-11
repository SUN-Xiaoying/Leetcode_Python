# Time: O(NlogN)
# Space: O(N)

def merge(a, l, m, r):
    i, p1, p2=0, l, m+1
    help=[0]*(r-l+1)
    while p1<=m and p2<=r:
        if a[p1] <= a[p2]:
            help[i] = a[p1]
            i+=1
            p1+=1
        else: 
            help[i] = a[p2]
            i+=1
            p2+=1
    while p1<=m:
        help[i] = a[p1]
        i+=1
        p1+=1

    while p2<=r:
        help[i] = a[p2]
        i+=1
        p2+=1
    # WHY a=help doesn't work?
    for i in range(len(help)):
        a[l+i]=help[i]

def process(a, l, r):
    if l==r: 
        return
    mid = l+((r-l)>>1)
    process(a,l,mid)
    process(a, mid+1, r)
    merge(a, l, mid, r)

def main():
    n=int(input())
    a=list(map(int,input().split()))
    l,r=0,len(a)-1
    process(a,l,r)
    print(*a)

main()
