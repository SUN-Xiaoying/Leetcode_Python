while True:
    try:
        n=int(input())
        arr1=list(map(int, input().split()))
        m=int(input())
        arr2=list(map(int, input().split()))
        p1, p2=0,0

        result=[]
        while p1<n and p2<m:
            if (arr1[p1]==arr2[p2]):
                result.append(arr1[p1])
                p1+=1
                p2+=1
            elif arr1[p1] < arr2[p2]:
                p1+=1
            else: p2+=1
        print(*result)
    except:
        break