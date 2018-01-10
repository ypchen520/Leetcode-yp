"""
if using 
[ str = str + pivot ]
instead of 
[ list.append(pivot) ] 
the runtime will fall significantly:
5x ms --> 8x ms
"""
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        dictSay = {}
        dictSay[1] = [1]
        for i in range(2,n+1):
            dictSay[i] = []
            numCount = 0
            pivot = dictSay[i-1][0]
            for j in range(0, len(dictSay[i-1])):
                if(dictSay[i-1][j] == pivot):
                    numCount = numCount + 1
                    if(j == len(dictSay[i-1])-1):
                        dictSay[i].append(numCount)
                        dictSay[i].append(pivot)
                else:
                    dictSay[i].append(numCount)
                    dictSay[i].append(pivot)
                    pivot = dictSay[i-1][j]
                    numCount = 1
                    if(j == len(dictSay[i-1])-1):
                        dictSay[i].append(numCount)
                        dictSay[i].append(pivot)
                    
        ans = "".join(str(a) for a in dictSay[n])
        return ans
                
                
                
            
            
