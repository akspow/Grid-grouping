grid=[[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],

[1, 1 ,1, 1, 0, 0, 0, 0, 0, 0],

[1 ,1, 1, 0, 0, 0, 0, 1, 1, 1],

[1, 1, 0, 0, 1, 0, 0, 1, 1 ,1],

[1, 0, 1, 0, 0, 1, 1, 0, 0, 0],

[0, 0, 0, 0, 0, 0, 0, 0 ,0, 0],

[0, 0 ,0, 0, 0 ,0 ,0 ,0, 0, 0],

[1 ,1 ,1, 1 ,1, 1 ,1 ,1 ,1, 1],

[0 ,0, 0, 0, 0, 0, 0, 0, 0, 0],

[1 ,1, 1, 1, 1, 1, 1, 1, 1 ,1]]

def colcount(rowindex,colindex):
        cx=colindex
        c=0
        for i in range(0,10):
            try:
                if grid[rowindex][cx+1]==1:
                    grid[rowindex][cx+1]=0
                    c+=1
                    cx+=1
                elif grid[rowindex][cx+1]==0:
                    break
            except IndexError:
                 continue
        for i in range(0,10):
            try:
                if grid[rowindex][colindex-1]==1 and colindex-1>=0:
                    grid[rowindex][colindex-1]=0
                    c+1
                    colindex-=1
                elif grid[rowindex][colindex-1]==0:
                    break
            except IndexError:
                continue
        return c
def rowcount(rowindex,colindex):
        rx=rowindex
        c=0
        for i in range(0,10):
            try:
                if grid[rx+1][colindex]==1:
                    grid[rx+1][colindex]=0
                    c+=colcount(rx+1,colindex)
                    c+=1
                    rx+=1
                elif grid[rx+1][colindex]==0:
                    break
            except IndexError:
                continue
        for i in range(0,10):
            try:
                if grid[rowindex-1][colindex]==1 and rowindex-1>=0:
                    grid[rowindex-1][colindex]=0
                    c+=colcount(rowindex-1,colindex)
                    c+=1
                    rowindex-=1
                elif grid[rowindex-1][colindex]==0:
                    break
            except IndexError:
                continue
        return c
grid2=[]
for row in range(0,10):
    for col in range(0,10):
        if grid[row][col]==1:
            count=1
            count+=colcount(row,col)+rowcount(row,col)
            grid2.append(count)
print(grid2)
