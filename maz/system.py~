
from config import *
from gui.canvasex import *
from maz.treefunc import *
from math import *

class Maze():
     def __init__(self, width, height):
          self.width   = width
          self.height  = height
          self.map     = [1]*width*height

class Arrow():
     def __init__(self, vertices, item):
          self.vertices = vertices
          self.item = item


class System():
     def __init__(self, canvasex):
          self.canvasex = canvasex
          self.canvas   = canvasex.canvas
          
          ## Maze Data 와 그에 대응하는 Graphic Object
          self.origin   = Origin(0.0, 0.0, 0.0, 1.0, 1.0)
          self.maze     = Maze(50, 50)
          self.colormap = ColorMap(['white','gray15'],0,1)
          self.bitmap   = \
               canvasex.createBitmap(
                    self.maze.map, 1, 1, 50, 50,
                    self.origin,
                    self.colormap, None)

          ## Cursur 정보
          self.cursurx      = 0
          self.cursury      = 0
          self.color_cursur = 'white'
          rect = self.bitmap.polys[0:8]
          self.cursur_item = \
               self.canvasex.createLineLoop(rect, 0, 4,
               self.origin, self.color_cursur)

          ## Tree : TreeArrows 는 화살표의 pos[]를
          ## 모두 가지고 있는데 이래야 origin, viewport
          ## 변화에 빨리 대응 가능하다.
          self.tree              = None
          self.treefunc          = treefunc
          self.tree_arrows       = []
          ## BFS, DFS Solution
          self.bfs_solution      = None
          self.bfs_solution_path = None
          self.bfs_step          = 0
          self.bfs_count         = 0
          self.dfs_solution      = None
          self.dfs_solution_path = None
          self.dfs_step          = 0
          self.dfs_count         = 0
          ## BFS, DFS Show
          self.bfs_show = False
          self.bfs_path_show = False
          self.dfs_show = False
          self.dfs_path_show = False

          ## 데코레이션 정보 (커서색만 유일하게 Cursur 쪽에)
          self.color_outline      = 'black'
          self.color_backgournd   = 'steel blue'
          ## 테코 (트리,페치)
          self.color_tree         = 'forest green'
          self.color_bfs_path     = 'red'
          self.color_bfs_solution = 'orange'
          self.color_dfs_path     = 'red'
          self.color_dfs_solution = 'orange'

     ### 커서관련
     def redrawCursur(self):
          index = self.cursury * self.maze.width + self.cursurx
          rect  = self.bitmap.polys[index*8:index*8+8]
          self.canvasex.coordsLineLoop(self.cursur_item,
               rect, 0, 4, self.origin)
          self.canvas.tag_raise(self.cursur_item)
          

     def moveCursur(self, x, y):
          self.cursurx += x
          self.cursury += y
          self.cursurx = max(0,min(self.cursurx,self.maze.width-1))
          self.cursury = max(0,min(self.cursury,self.maze.height-1))
          self.redrawCursur()
          

     def empty(self):
          index = self.cursury * self.maze.width + self.cursurx
          self.maze.map[index]=0
          self.canvas.itemconfig(
               self.bitmap.items[index], fill=self.colormap.list[0])

     def block(self):
          index = self.cursury * self.maze.width + self.cursurx
          self.maze.map[index]=1
          self.canvas.itemconfig(
               self.bitmap.items[index], fill=self.colormap.list[1])

     ### 비트맵을 새로 생성하거나 이동
     def newBitmap(self, mmap, width, height):
          self.delTree()
          self.canvasex.deleteBitmap(self.bitmap)
          
          self.maze = Maze(width, height)
          self.maze.map = mmap

          wsize = 0
          hsize = 0
          if width < height:
               hsize = 1
               wsize = width/height
          else:
               hsize = height/width
               wsize = 1
          self.canvasex.deleteBitmap(self.bitmap)
          self.bitmap = self.canvasex.createBitmap(
               self.maze.map, wsize, hsize,
               width, height, self.origin, self.colormap, None)
          self.cursurx = 0
          self.cursury = 0
          self.redrawCursur()
          

     def newEmptyBitmap(self, width, height):
          self.delTree()
          self.maze = Maze(width, height)
          self.canvasex.deleteBitmap(self.bitmap)
          wsize = 0
          hsize = 0
          if width < height:
               hsize = 1
               wsize = width/height
          else:
               hsize = height/width
               wsize = 1
          bitmap = self.canvasex.createBitmap(
                    self.maze.map,
                    wsize, hsize,
                    width, height,
                    self.origin,
                    self.colormap, None)
          self.bitmap = bitmap
          self.cursurx = 0
          self.cursury = 0
          self.redrawCursur()
     
     
     def moveBitmap(self, x, y):
          self.origin.move(x, y)
          self.canvasex.coordsBitmap(self.bitmap, self.origin)
          self.redrawCursur()
          self.redrawTree()
          
     def rotateBitmap(self, deg):
          self.origin.rotate(deg)
          self.canvasex.coordsBitmap(self.bitmap, self.origin)
          self.redrawCursur()
          self.redrawTree()

     def scaleBitmap(self, x, y, limit):
          self.origin.scale(x, y)
          if self.origin.sx < limit : self.origin.sx = limit
          if self.origin.sy < limit : self.origin.sy = limit
          self.canvasex.coordsBitmap(self.bitmap, self.origin)
          self.redrawCursur()
          self.redrawTree()

     def updateOrigin(self):
          self.canvasex.coordsBitmap(self.bitmap, self.origin)
          self.redrawCursur()
          self.redrawTree()


     ### 트리 얻기
     def __createArrow__(self, si, ei):
          arrow_vertices = [0.1,0.05,  0.1,-0.05,  0.7,-0.1,  0.7,-0.25,
                1.0,0.0,  0.7,0.25,  0.7,0.1]
          polys = self.bitmap.polys
          sx = (polys[si*8]   + polys[si*8+4])/2
          sy = (polys[si*8+1] + polys[si*8+5])/2
          ex = (polys[ei*8]   + polys[ei*8+4])/2
          ey = (polys[ei*8+1] + polys[ei*8+5])/2
          dx = ex-sx
          dy = ey-sy
          dsize = sqrt(dx**2 + dy**2)
          a = dx/dsize
          b = dy/dsize
          vertices = [0]*14
          for i in range(7):
               px = arrow_vertices[i*2]  *dsize
               py = arrow_vertices[i*2+1]*dsize
               vertices[i*2]   = a*px - b*py + sx
               vertices[i*2+1] = b*px + a*py + sy
          item = self.canvasex.createPolygon(vertices,
               0, 7, self.origin, self.color_tree)
          return Arrow(vertices, item)


     def getTree(self):
          for arrow in self.tree_arrows:
               self.canvasex.deleteItem(arrow.item)
                    
          maze = self.maze
          self.tree = self.treefunc(maze.map, maze.width, maze.height)
          #self.filter_one_direct(self.tree)
          for si in range(maze.width*maze.height):
               for ei in self.tree[si]:
                    item = self.__createArrow__(si, ei)
                    self.tree_arrows.append(item)

          
     def delTree(self):
          self.tree = None
          for arrow in self.tree_arrows:
               self.canvasex.deleteItem(arrow.item)

     def redrawTree(self):
          for arrow in self.tree_arrows:
               self.canvasex.coordsPolygon(arrow.item,
                    arrow.vertices, 0, 7, self.origin)

     ### BFS
     def getBFSSolution(self):
          if self.tree is not None:
               global DEBUGMODE
               from_ = 0
               to    = self.maze.width*self.maze.height - 1
               self.bfs_solution = bfs(self.tree, from_, to)
               if DEBUGMODE: print("bfs_solution : "+str(self.bfs_solution))
               s = self.bfs_solution
               self.bfs_count = len(s)
               self.bfs_step  = 0
               self.bfs_solution_path = [s[-1]];  c = s[-1]
               if DEBUGMODE: print('find path : ',end='')
               if DEBUGMODE: print(c, end='>')
               for i in range(len(s)-2, -1, -1):
                    if s[i] in self.tree[c]:
                         c = s[i];  self.bfs_solution_path.append(c)
                         if DEBUGMODE: print(c, end='>')
               if DEBUGMODE: print('end')
               print('넓이우선탐색 : ' + str(self.bfs_solution_path))
               self.bfs_gen = True
               self.bfs_show = True
               self.bfs_path_show = True
               

     def getDFSSolution(self):
          if self.tree is not None:
               global DEBUGMODE
               from_ = 0
               to     = self.maze.width*self.maze.height -1
               self.dfs_solution = dfs(self.tree, from_, to)
               s = self.dfs_solution
               self.dfs_count = len(s)
               self.dfs_step  = 0
               if DEBUGMODE: print("dfs_solution : "+str(s))
               if DEBUGMODE: print("find path : ")
               path = [0]
               for i in range(1,len(s)):
                    if DEBUGMODE: print(path)
                    nextnodes = self.tree[s[i]]
                    c = path.pop()
                    while c not in nextnodes: c = path.pop()
                    path += [c, s[i]]
               self.dfs_solution_path = path
               print('깊이우선탐색 : ' + str(self.dfs_solution_path))
               self.dfs_gen = True
               self.dfs_show = True
               self.dfs_path_show = True


     def showBFSSolutionAll(self):
          for i in range(0, self.bfs_count):
               item_index = self.bfs_solution[i]
               self.canvas.itemconfig(self.bitmap.items[item_index], fill=self.color_bfs_solution)
          self.bfs_show = True
     def showDFSSolutionAll(self):
          for i in range(0, self.dfs_count):
               item_index = self.dfs_solution[i]
               self.canvas.itemconfig(self.bitmap.items[item_index], fill=self.color_dfs_solution)
          self.dfs_show = True
     def showBFSSolutionPath(self):
          for index in self.bfs_solution_path:
               self.canvas.itemconfig(self.bitmap.items[index], fill=self.color_bfs_path)
          self.bfs_path_show =True
     def showDFSSolutionPath(self):
          for index in self.dfs_solution_path:
               self.canvas.itemconfig(self.bitmap.items[index], fill=self.color_dfs_path)
          self.dfs_path_show = True
     def showBFSSolution(self):
          for i in range(0, self.bfs_step):
               item_index = self.bfs_solution[i]
               self.canvas.itemconfig(self.bitmap.items[item_index], fill=self.color_bfs_solution)
          self.bfs_show = True
     def showDFSSolution(self):
          for i in range(0, self.dfs_step):
               item_index = self.dfs_solution[i]
               self.canvas.itemconfig(self.bitmap.items[item_index], fill=self.color_bfs_solution)
          self.dfs_show = True
     def hideBFSSolution(self):
          print('hide bfs solution')
          if self.bfs_solution is None : return
          for index in self.bfs_solution:
               self.canvas.itemconfig(self.bitmap.items[index], fill=self.colormap.list[0])
          self.bfs_show = False
     def hideDFSSolution(self):
          if self.dfs_solution is None : return
          print('hide dfs solution')
          for index in self.dfs_solution:
               self.canvas.itemconfig(self.bitmap.items[index], fill=self.colormap.list[0])
          self.dfs_show = False
     def hideBFSSolutionPath(self):
          if self.bfs_solution_path is None : return
          print('hide bfs path solution')
          for index in self.bfs_solution_path:
               self.canvas.itemconfig(self.bitmap.items[index], fill=self.colormap.list[0])
          self.bfs_path_show = False
     def hideDFSSolutionPath(self):
          if self.dfs_solution_path is None : return
          print('hide dfs path solution')
          for index in self.dfs_solution_path:
               self.canvas.itemconfig(self.bitmap.items[index], fill=self.colormap.list[0])
          self.dfs_path_show = False
     def showNextBFSSolution(self):
          if not(self.bfs_show) or self.bfs_step >= self.bfs_count : return False
          index = self.bfs_solution[self.bfs_step]
          self.canvas.itemconfig(self.bitmap.items[index], fill=self.color_bfs_solution)
          self.bfs_step += 1
          return True
     def showPrevBFSSolution(self):
          if not(self.bfs_show) or self.bfs_step <= 0 : return False
          self.bfs_step -= 1
          index = self.bfs_solution[self.bfs_step]
          self.canvas.itemconfig(self.bitmap.items[index], fill=self.colormap.list[0])
          return True
     def showNextDFSSolution(self):
          if not(self.dfs_show) or self.dfs_step >= self.dfs_count : return False
          index = self.dfs_solution[self.dfs_step]
          self.canvas.itemconfig(self.bitmap.items[index], fill=self.color_dfs_solution)
          self.dfs_step += 1
          return True
     def showPrevDFSSolution(self):
          if not(self.dfs_show) or self.dfs_step <= 0 : return False
          self.dfs_step -= 1
          index = self.dfs_solution[self.dfs_step]
          self.canvas.itemconfig(self.bitmap.items[index], fill=self.colormap.list[0])
          return True
     def delDFSSolution(self):
          if self.dfs_gen:
               self.hideDFSSolution()
               self.dfs_gen = False
     def delBFSSolution(self):
          if self.bfs_gen:
               self.hideBFSSolution()
               self.dfs_gen = False
     def delSolution(self):
          self.hideDFSSolution()
          self.hideBFSSolution()
     def clearSolution(self):
          if self.dfs_solution is not None:
               print('hide dfs solution')
               for index in self.dfs_solution:
                    self.canvas.itemconfig(self.bitmap.items[index], fill=self.colormap.list[0])
          if self.bfs_solution is not None:
               print('hide bfs solution')
               for index in self.bfs_solution:
                    self.canvas.itemconfig(self.bitmap.items[index], fill=self.colormap.list[0])
          self.dfs_step = 0
          self.bfs_step = 0


     ### 저장, 불러오기
     def save(self, path):
          return

     def open(self, path, max_width, max_height):
          return
     
     def save(self, path):
          maze = self.maze
          string = ""
          string += (str(maze.width) + "x" + str(maze.height) + "\n")
          i = 0
          for row in range(maze.height):
               for cul in range(maze.width):
                    if maze.map[i] != 0: string += str(1)
                    else: string += str(0)
                    i += 1
               string += "\n" 
          file = open(path,"w")
          file.write(string)
          file.close()

     def open(self, path, max_width, max_height):
          
          file = open(path,"r")
          try:
               lines    = file.read().split("\n")
               line     = lines.pop(0)
               metas    = line.split("x")
               width   = int(metas[0])
               height  = int(metas[1])
               widht   = max(2, min(width, max_width))
               height  = max(2, min(height, max_height))
               mbitmap  = [0]*width*height
               j=0
               k=0
               for k in range(height):
                    line = lines[k]
                    for i in range(width):
                         if int(line[i]) != 0: mbitmap[j] = 1
                         else: mbitmap[j] = 0
                         j+=1
                    k+=1
               self.newBitmap(mbitmap,width,height)

          except Exception as e:
               print("reading error")
               print(e)

          finally:
               file.close()
               


