
def bfs(graph,root,search):
  visited=[]
  que=[root]
  while que:
    node=que.pop(0)
    if node not in visited:
      visited.extend(node)
    que.extend(graph[node])
    if node==search:
      break
  return visited
