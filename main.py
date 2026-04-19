from pyamaze import maze,agent,COLOR
from collections import deque

def BFS(m,start=None):
    if start is None:
        start=(m.rows,m.cols)
    frontier= deque()
    frontier.append(start)
    bfsPath = {}
    explored=[start]
    bSearch=[]

    while len(frontier)>0:
        currCell=frontier.pop()
        if currCell==(1,1):
            break
        for d in "ESNW":
            if m.maze_map[currCell][d]==True:
                if d=="E":
                    childCell=(currCell[0],currCell[1]+1)
                elif d=="W":
                    childCell=(currCell[0],currCell[1]-1)
                elif d=="N":
                    childCell=(currCell[0]-1,currCell[1])
                elif d=="S":
                    childCell=(currCell[0]+1,currCell[1])
                if childCell in explored:
                    continue
                frontier.append(childCell)
                explored.append(childCell)
                bfsPath[childCell]=currCell
    fwdPath={}
    cell=(1,1)
    while cell!=start:
        fwdPath[bfsPath[cell]]=cell
        cell=bfsPath[cell]
    return fwdPath

if __name__=="__main__":
    # m=maze(5,5)                
    # m.CreateMaze(loadMaze="bfs.csv")
    # bSearch,bfsPath,fwdPath=BFS(m)
    # a=agent(m,footprints=True,color=COLOR.green,shape="square")
    # b=agent(m,footprints=True,color=COLOR.yellow,shape="square",filled=False)
    # c=agent(m,1,1,footprints=True,color=COLOR.cyan,shape="square",filled=True,goal=(m.rows))
    # m.tracePath({a:bSearch},delay=500)
    # m.tracePath({c:bfsPath})
    # m.tracePath({a:fwdPath})

    # a=agent(m,footprints=True)
    # m.tracePath({a:path})

    # m.run()

    m=maze(5, 4) 
    # m.CreateMaze(5,4,loopPercent=100) 
    m.CreateMaze(loopPercent=10,theme='light') 
    fwdPath=BFS(m) 
    a=agent(m,footprints=True,color=COLOR.yellow,shape='square',filled=True) 
    b=agent(m,footprints=True,color=COLOR.red,shape='square',filled=False) 
    # c=agent(m,5,4,footprints=True,color=COLOR.cyan,shape='square',filled=True,goal=(m.rows,m.cols)) 
    c=agent(m,1,1,footprints=True,color=COLOR.cyan,shape='square',filled=True,goal=(m.rows,m.cols)) 
    # m.tracePath({a:bSearch},delay=100) 
    # m.tracePath({c:bfsPath},delay=100) 
    m.tracePath({b:fwdPath},delay=100)

    m.run()