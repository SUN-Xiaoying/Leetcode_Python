def main():
    # while True:
    #     try:
    #         str = input()
    #         flag = 0
    #         for i in range(len(str)):
    #             if str[i]=='(': flag+=1
    #             elif str[i]==')': flag-=1
    #             else: break

    #             if flag<0:
    #                 break

    #         if flag==0: print("YES")
    #         else: print("NO")
    #     except:
    #         break
    while True:
        try:
            str=input()
            l = len(str)
            if l <2: 
                print(0)
                break
            res=0
            dp = [ 0 for i in range(l)]
            # 以当前字符结尾的匹配字符串的最大长度
            for i in range(1,l):
                if str[i] == ")":
                    pre = i-dp[i-1]-1
                    if(pre>=0 and str[pre]=="("):
                        dp[i]=dp[i-1] + 2
                        if pre>0:
                            dp[i]+=dp[pre-1]
                    res=max(res, dp[i])
            print(res)
        except:
            break
main()