
from math import *

class Origin():
     def __init__(self, x, y, deg, sx, sy):
          self.x = x
          self.y = y
          rad = radians(deg)
          self.a = cos(rad)
          self.b = sin(rad)
          self.sx = sx
          self.sy = sy

     def move(self, x, y):
          self.x += x
          self.y += y
          
     def rotate(self, deg):
          rad = radians(deg);
          a = cos(rad); b = sin(rad)
          self_a = self.a
          self.a = self_a*a - self.b*b
          self.b = self.b*a + self_a*b

     def scale(self, sx, sy):
          if sx is not 0 : self.sx *= sx
          if sy is not 0 : self.sy *= sy
          

     def transform(self, x, y, deg):
          self.x += x
          self.y += y
          rad = radians(deg);
          a = cos(rad); b = sin(rad)
          self_a = self.a
          self.a = self_a*a - self.b*b
          self.b = self.b*a + self_a*b


class Vertices():
     def __init__(self, vertices):
          self.count = len(vertices)//2
          self.pos   = vertices
          self.tan   = [0.0]*self.count*2
          self.siz   = [0.0]*self.count*2
          v=self.pos; t=self.tan; s=self.siz;
          print(vertices)
          for i in range(self.count):
               tx       = v[i*2]   - v[i*2-2]
               ty       = v[i*2+1] - v[i*2-1]
               size     = sqrt(tx**2 + ty**2)
               s[i*2]   = size
               t[i*2]   = tx/size 
               t[i*2+1] = ty/size

class Bitmap():
     def __init__(self, width, height):
          self.width  = width
          self.height = height
          self.polys  = None
          self.items  = None


class ColorMap():
     def __init__(self, mlist, mmin, mmax):
          self.list = mlist
          self.min  = mmin
          self.max  = mmax


class CanvasEx():
     def __init__(self, canvas):
          print(canvas)
          hwidth  = int(canvas["width"])//2
          hheight = int(canvas["height"])//2
          self.canvas = canvas
          self.ox = hwidth
          self.oy = hheight
          self.sx = hheight
          self.sy = hheight
          self.bgr = 0x22
          self.bgg = 0x33
          self.bgb = 0x55
          color = self.bgr * 0x010000 +\
                  self.bgg * 0x000100 +\
                  self.bgb * 0x000001
          self.canvas["bg"]= "#%06X"%(color)

     def updatebg(self):
          color = r * 0x010000 +\
                  g * 0x000100 +\
                  b * 0x000001
          self.canvas["bg"]= "#%06X"%(color)

     def setbg(self, r,g,b):
          if r < 0 : r = 0;
          if 0xff < r : r = 0xff
          if g < 0 : g = 0;
          if 0xff < g : g = 0xff
          if b < 0 : b = 0;
          if 0xff < b : b = 0xff
          self.bgr = r
          self.bgg = g
          self.bgb = b
          color = r * 0x010000 +\
                  g * 0x000100 +\
                  b * 0x000001
          self.canvas["bg"]= "#%06X"%(color)


     def viewport(self, ox, oy, sx, sy):
          self.ox = ox
          self.oy = oy
          self.sx = sx
          self.sy = sy


     def coordinate(self, vertices, offset, count, origin):
          count = len(vertices)//2
          x = origin.x
          y = origin.y
          a = origin.a
          b = origin.b
          coords = [0]*2*count
          for i in range(count):
               Px  = vertices[i*2 + offset]*origin.sx
               Py  = vertices[i*2 + offset +1]*origin.sy
               Pgx = a*Px - b*Py + x
               Pgy = b*Px + a*Py + y
               coords[i*2]   = self.ox + Pgx* self.sx
               coords[i*2+1] = self.oy - Pgy* self.sy
          return coords


     def deleteItem(self, item):
          self.canvas.delete(item)

     def createPolygon(self, vertices, offset, count, origin, color):
          coords = self.coordinate(vertices, offset, count, origin)
          return self.canvas.create_polygon(coords, fill=color)

     def coordsPolygon(self, item, vertices, offset, count, origin):
          coords = self.coordinate(vertices, offset, count, origin)
          self.canvas.coords(item, coords)

     def createLineLoop(self, vertices, offset, count, origin, color):
          coords = self.coordinate(vertices, offset, count, origin)
          coords += [coords[0], coords[1]]
          return self.canvas.create_line(coords, fill=color)

     def coordsLineLoop(self, item, vertices, offset, count, origin):
          coords = self.coordinate(vertices, offset, count, origin)
          coords += [coords[0], coords[1]]
          self.canvas.coords(item, coords)


     def createBitmap(self, bitmap, wsize, hsize,
                      width, height, origin, colormap, outline):

          mbitmap = Bitmap(width, height)
          if colormap is None:
               colormap = ColorMap(['white','red'], 0, 1)
          if outline is None:
               outline = 'black'

          index = 0
          block_width  = 2*wsize/width
          block_height = 2*hsize/height
          mbitmap.polys = []
          for row in range(height):
               for cul in range(width):
                    left      = -wsize + block_width  * (cul)
                    right     = -wsize + block_width  * (cul+1)
                    top       =  hsize - block_height * (row)
                    bottom    =  hsize - block_height * (row+1)
                    mbitmap.polys += \
                         [left, top, left, bottom, right, bottom, right, top]
                    index += 1

          coords = self.coordinate(mbitmap.polys,0,index,origin)
          
          mbitmap.items = [0]*width*height
          index = 0
          for row in range(height):
               for cul in range(width):
                    colorid = max(colormap.min, min(bitmap[index], colormap.max))
                    color = colormap.list[colorid]
                    item = self.canvas.create_polygon(coords[index*8:index*8+8],
                         fill=color, outline=outline)
                    mbitmap.items[index] = item
                    index += 1
                    
          return mbitmap
                    

     def coordsBitmap(self, bitmap, origin):
          count  = bitmap.width*bitmap.height
          coords = self.coordinate(bitmap.polys, 0, count*4, origin)
          for index in range(count):
               self.canvas.coords(bitmap.items[index],
                    coords[index*8:index*8+8])
               

     def colorBitmap(self, bitmap, colormap):
          count  = bitmap.width*bitmap.height
          if colormap is None:
               colormap = Colormap(['white','black'], 0, 1)
          for index in range(count):
               colorid = max(colormap.min,min(bitmap[index], colormap.max))
               color = colormap[colorid]
               self.canvas.itemconfig(bitmap.items[index], fill=color)
               

     def deleteBitmap(self, bitmap):
          for item in bitmap.items:
               self.canvas.delete(item)
          
