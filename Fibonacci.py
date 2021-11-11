
def matMul(a,b):
    res=[[0,0],[0,0]]
    res[0][0] = a[0][0]*b[0][0] + a[0][1]*b[1][0]
    res[0][1] = a[0][0]*b[0][1] + a[0][1]*b[1][1]
    res[1][0] = a[1][0]*b[0][0] + a[1][1]*b[1][0]
    res[1][1] = a[1][0]*b[0][1] + a[1][1]*b[1][1]
    return res

def matPow(a,n):
    res=[[1,0], [0,1]]
    while n:
        # bitwise 'and'
        if n&1 :
            res=matMul(res, a)
        a=matMul(a,a)
        n>>=1
    return res

def main():
    while True:
        try:
            n=int(input())
            MOD = 10**9+7
            mat= [[1,1], [1,0]]
            res= matPow(mat, n)
            print(res[0][0])

        except:
            break

main()

# if __name__ == '__main__':
#     def matMul(a, b):
#         res = [[0, 0], [0, 0]]
#         res[0][0] = (a[0][0] * b[0][0] % MOD + a[0][1] * b[1][0] % MOD) % MOD
#         res[0][1] = (a[0][0] * b[0][1] % MOD + a[0][1] * b[1][1] % MOD) % MOD
#         res[1][0] = (a[1][0] * b[0][0] % MOD + a[1][1] * b[1][0] % MOD) % MOD
#         res[1][1] = (a[1][0] * b[0][1] % MOD + a[1][1] * b[1][1] % MOD) % MOD
#         return res
#     def matPow(a, n):
#         res = [[1, 0], [0, 1]]
#         while n:
#             if n & 1:
#                 res = matMul(res, a)
#             a = matMul(a, a)
#             n >>= 1
#         return res
     
#     n = int(input())
#     MOD = 10 ** 9 + 7
#     mat = [[1, 1], [1, 0]]
#     res = matPow(mat, n - 1)
#     print(res[0][0])
