#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param mat int整型二维数组 
# @param n int整型 
# @return int整型二维数组
#
from typing import List

class Solution:

    def rotateEdge(self, mat, a:int, b:int, c:int, d:int):
        tmp=0
        for i in range(d-b):
            tmp = mat[a][b+i]
            mat[a][b+i] = mat[c-i][b]
            mat[c-i][b] = mat[c][d-i]
            mat[c][d-i] = mat[a+i][d]
            mat[a+i][d] = tmp
        return mat
    
    def rotateMatrix(self , mat: List[List[int]], n: int) -> List[List[int]]:
        # write code here
        a=0
        b=0
        c=len(mat)-1
        d=len(mat[0])-1
        while a<c:
            mat = self.rotateEdge(mat, a, b, c, d)
            a+=1
            b+=1
            c-=1
            d-=1
        return mat
        