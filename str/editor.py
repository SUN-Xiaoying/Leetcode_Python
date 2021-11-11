# 10/31 heelllo woow
# 63ms
while True:
    try:
        n=int(input())
        while n>0:
            s=input()
            if len(s)<3: 
                print(s)
                n-=1
                continue
            res=""
            for e in s:
                if len(res) <2:
                    res+=e
                    continue
                if len(res)>=2:
                    if e==res[-1] and e==res[-2]:
                        continue
                if len(res)>=3:
                    if e==res[-1] and res[-2]==res[-3]:
                        continue
                res+=e
            print(res)
            n-=1
    except:
        break