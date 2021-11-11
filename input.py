def main():
    arr=[-1,0,0,1,2,-2]
    target=0
    # arr=[2,2,2,2]
    # target=8
    l=len(arr)
    if l < 4: print([])
    res=[]

    def initPointer(n):
        pointers[0]+=n
        pointers[1]=pointers[0]+1
        pointers[2]=pointers[1]+1
        pointers[3]=pointers[2]+1

    pointers=[0,1,2,3]

    def movePointer(i):
        while pointers[i]<l-(4-i-1):
            tmp=arr[pointers[0]]+arr[pointers[1]]+arr[pointers[2]]+arr[pointers[3]]
            if tmp==target:
                res.append([arr[pointers[0]],arr[pointers[1]],arr[pointers[2]],arr[pointers[3]]])
            pointers[i]+=1

    while pointers[0]<l-3:
        
        movePointer(3)
        pointers[2]+=1
        pointers[3]=-1

        movePointer(2)

        pointers[1]+=1
        pointers[2]=-2
        movePointer(1)

        initPointer(pointers[0]+1)
    print(res)

main()

# sort()
# 