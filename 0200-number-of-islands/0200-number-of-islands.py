class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        q=collections.deque()
        islands=0
        visited=set()
        def bfs(r,c):
            directions=[[0,1],[0,-1],[1,0],[-1,0]]
            
            visited.add((r,c))
            q.append((r,c))

            while q:
                row,col=q.popleft()
                for dr,dc in directions:
                    nr=row+dr
                    nc=col+dc
                    if nr in range(rows) and nc in range(cols) and grid[nr][nc]=="1" and (nr,nc) not in visited:
                        visited.add((nr,nc))
                        q.append((nr,nc))


        for r in range(rows):
                for c in range(cols):
                    if grid[r][c]=="1" and (r,c) not in visited:
                        bfs(r,c)
                        islands=islands+1

        return islands
