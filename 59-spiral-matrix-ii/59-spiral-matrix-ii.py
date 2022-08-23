class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        ans = [[0 for i in range(n)] for j in range(n)]
        DIR = [(0,1), (1,0), (0,-1), (-1,0)]
        visited = set()
        i, j, d = 0, 0, 0
        inbound = lambda row, col: 0 <= row < n and 0 <= col < n
        val = 1
        while len(visited) < n * n:
            if (i,j) not in visited:
                ans[i][j] = val
                val += 1
            visited.add((i,j))

            if inbound(i + DIR[d][0],j + DIR[d][1]) and (i + DIR[d][0],j + DIR[d][1]) not in visited:
                i += DIR[d][0]
                j += DIR[d][1]
            
            else:
                if d < len(DIR) - 1:
                    d += 1
                    i += DIR[d][0]
                    j += DIR[d][1]
                else:
                    d = 0
                    i += DIR[d][0]
                    j += DIR[d][1]
        
        return ans