# 你需要输入一个n，一个数k，然后输入一个长度为n个大小的数组arr，然后你需要在arr上找满足>=K的最左位置，并且输出这个位置，如果不存在这个位置就输出-1。
# 输入描述:
# 第一行输入一个n，k
# 第二行输入长度为n个大小的数组arr

while True:
    try:
        n,k=map(int, input().split())
        arr=list(map(int, input().split()))
        arr.sort()
    
        left, right=0,n-1
        minIndex=n-1
        while left<=right:
            index=(right+left)//2
            if arr[index] >= k:
                left, right=left, index-1
                minIndex=min(minIndex, index)
            else:
                left, right=index+1, right
        
        if arr[minIndex]>=k: 
            print(minIndex)
        else: print(-1)  
        
    except:
        break