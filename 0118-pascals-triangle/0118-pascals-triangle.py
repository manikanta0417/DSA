class Solution(object):
    def generate(self, numRows):
        res=[]
        for i in range(0,numRows):
            lst=[]
            for j in range(0,i+1):
                if j==0 or i==j:
                    lst.append(1)
                else:
                    r=res[i-1][j-1]+res[i-1][j]
                    lst.append(r)
            res.append(lst)
        return res