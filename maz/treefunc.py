
from config import *

def treefunc(mazelist, width, height):
    
    arrayrows = width-1
    arraycolumns = height-1
    width  -= 1
    height -= 1

    mazetree = {}
    
    i = 0
    while i <= height:
        j = 0
        while j <= width:
            tempnode = []
            if int(mazelist[(width+1)*i+j]) == 0:
                if i > 0:
                    if int(mazelist[(width+1)*(i-1)+j]) == 0:
                        tempnode.append((width+1)*(i-1)+j)
                if i < height:
                    if int(mazelist[(width+1)*(i+1)+j]) == 0:
                        tempnode.append((width+1)*(i+1)+j)
                if j > 0:
                    if int(mazelist[(width+1)*i+(j-1)]) == 0:
                        tempnode.append((width+1)*i+(j-1))
                if j < width:
                    if int(mazelist[(width+1)*i+(j+1)]) == 0:
                        tempnode.append((width+1)*i+(j+1))
            mazetree[(width+1)*i+j]=tempnode
            j = j+1
        i = i+1
    return mazetree


#EXAMPLE#

#01000#
#00010#
#10111#
#00000#

def bfs(graph,root,search):
      visited = []
      queue   = [root]
      while True:
           node=queue.pop(0)
           if node not in visited:
                visited.append(node)
                queue.extend(graph[node])
           if node==search:
                break
      return visited


def dfs(graph,root,search):
  visited =[]
  stack   =[root]
  while True:
      if DEBUGMODE: print(visited, stack)
      node=stack.pop()
      if node not in visited:
          visited.append(node)
      if node==search:
          break
      nextnodes = [x for x in graph[node] if x not in visited]
      stack.extend(nextnodes)
  return visited
