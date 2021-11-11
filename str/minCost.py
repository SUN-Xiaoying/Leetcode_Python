# from collections import Counter

import string


def main():
    while True:
        try:
            s1=input()
            s2=input()  
            ic,dc,rc=input().split()
            ic=int(ic)
            dc=int(dc)
            rc=int(rc)
            if not s1: 
                print("NOT S1: ",int(ic*len(s2)))
                break
            if not s2: 
                print("NOT S2: ", int(dc*len(s1)))
                break
            if len(s1) >= len(s2):
                longs = s1
                shorts = s2
            else:
                longs = s2
                shorts = s1
                tmp = ic
                ic = dc
                dc= tmp
            dp=[0 for x in range(len(shorts)+1)]
            for i in range(1, len(shorts)+1):
                dp[i] = i*ic 
            print(dp)
            for i in range(1, len(longs)+1):
                pre=dp[0]
                dp[0]=dc*i
                for j in range(1,len(shorts)+1):
                    tmp = dp[j]
                    if(longs[i-1]==shorts[j-1]):
                        dp[j]=pre
                    else:
                        dp[j]=pre+rc
                    dp[j]=min(dp[j],dp[j-1]+ic)
                    dp[j]=min(dp[j],tmp+dc)
                    pre=tmp
                    print(dp)
            print(dp[-1])

        except:
            break
main()