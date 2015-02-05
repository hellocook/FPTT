class Solution:
    # @param triangle, a list of lists of integers
    # @return an integer
    def minimumTotal(self, triangle):
             result = [[0 for col in range(4)] for row in range(4)]
             result[0][0] = triangle[0][0]
             for i in range(len(triangle)-1):
                 for j in range(len(triangle[i+1])):
                     if j - 1 >= 0:
                         if result[i+1][j-1] == 0:
                             result[i+1][j-1] = triangle[i+1][j-1] + result[i][j]
                         else:
                             if result[i+1][j-1] > triangle[i+1][j-1] + result[i][j]:
                                 result[i+1][j-1] = triangle[i+1][j-1] + result[i][j
                                                                                   if result[i+1][j] == 0:
                         result[i+1][j] = triangle[i+1][j] + result[i][j]
                              else:
                        if result[i+1][j] >  triangle[i+1][j] + result[i][j]:
                            result[i+1][j] =  triangle[i+1][j] +
                            result[i][j]
                     if j + 1 <= len(triangle[i+1]):
                         if result[i+1][j+1] == 0:
                             result[i+1][j+1] = triangle[i+1][j+1] + result[i][j]
                         else:
                             if result[i+1][j+1] > triangle[i+1][j+1] + result[i][j]:
                                 result[i+1][j+1] = 	triangle[i+1][j+1] + result[i][j]
             Max = 10000
              for i in triangle[3]:
                if i < Max:
                                Max = i
               return Maxa




s = Solution()
A = [[2],[3,4],[6,5,7],[4,1,8,3]]
print (s.minimumTotal(A))


