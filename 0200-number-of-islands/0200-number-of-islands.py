class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        visited=set()
        q=collections.deque()
        rows=len(grid)
        cols=len(grid[0])
        island=0

        def bfs(r,c):
            directions=[[0,1],[0,-1],[1,0],[-1,0]]
            
            visited.add((r,c))
            q.append((r,c))
            while q:
                row,col=q.popleft()
                for dr, dc in directions:
                    r=row+dr
                    c=col+dc
                    if r in range(rows) and c in range(cols) and (r,c) not in visited and grid[r][c]=="1":
                        visited.add((r,c))
                        q.append((r,c))

       

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] =="1" and (r,c) not in visited:
                    bfs(r,c)
                    island=island+1
        return island

        
                
