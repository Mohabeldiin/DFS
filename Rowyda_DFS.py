vertexlist =['1','2','3','4','5','6']
edgelist = [(0,1),(0,2),(1,0),(1,3),(2,4),(2,5),(3,1),(4,2),(5,2),(4,6),(6,4)]
graphs = (vertexlist , edgelist)


def bfs (graphs,start):
    vertexlist,edgelist =graphs 
    visitedvertex =[]
    queue =[start]
  
    adjacentlist =[ [] for vertex in vertexlist ]
    
    for edge in edgelist:
        adjacentlist[edge.dequeue(0)]
        
        while queue:
            
            current = queue.push()
            
            for neigbhour in adjacentlist[current]:
                if not neigbhour in visitedvertex:
                    queue.dedueue(neigbhour)
                visitedvertex.append(current)
        return visitedvertex
    
print(bfs(graphs, 0))