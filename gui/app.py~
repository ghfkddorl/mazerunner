
import os
from tkinter import *
from gui.canvasex import *
from maz.system   import *

class Application(Tk):
     def __init__(self, main_dir):
          super().__init__()

          self.main_dir = main_dir
          self.main_save_dir = os.path.join(main_dir,'save')
          
          self.title("메이즈러너?")

          self.desc = \
               "화살표 : 커서이동\n"+\
               "e : 지우기, b : 채우기,\n" +\
               "마우스를 통한 화면이동\n" +\
               "줌기능 지원\n" +\
			   "왼쪽위가 출발\n 오른쪽아래 도작"

          ### 레이아웃
          self.sidebar = Frame(self, width=150,bg='#cccccc')
          self.sidebar.pack_propagate(0)
          self.sidebar.pack(side=LEFT, fill=Y, expand=False)
          self.actionbar = Frame(self, height=40)
          self.actionbar.pack_propagate(0)
          self.actionbar.pack(side=TOP, fill=X, expand=False)
          self.viewer = Frame(self, bg='#ffffff')
          self.viewer.pack(fill=BOTH, expand=True)

          ## 액션바::과정
          self.stepbar = Frame(self.actionbar)
          self.stepbar_btn_auto_prev = Button(self.stepbar,
               text='<<')
          self.stepbar_btn_prev = Button(self.stepbar,
               text='<')
          self.stepbar_btn_stop = Button(self.stepbar,
               text='ㅁ')
          self.stepbar_btn_next = Button(self.stepbar,
               text='>')
          self.stepbar_btn_auto_next = Button(self.stepbar,
               text='>>')
          self.stepbar_step = Label(self.stepbar,
               text='step=0')
          self.stepbar.pack(side=LEFT,fill=Y,padx=13,pady=6)
          self.stepbar_btn_auto_prev.pack(side=LEFT, fill=Y)
          self.stepbar_btn_prev.pack(side=LEFT, fill=Y)
          self.stepbar_btn_stop.pack(side=LEFT, fill=Y)
          self.stepbar_btn_next.pack(side=LEFT, fill=Y)
          self.stepbar_btn_auto_next.pack(side=LEFT, fill=Y)
          self.stepbar_step.pack(side=LEFT, fill=Y)
          
          ### 액션바::주소창(저장/불러오기)
          self.adressbar = Frame(self.actionbar)
          self.adressbar_sv = StringVar()
          self.adressbar_entry = Entry(self.adressbar,
               textvariable=self.adressbar_sv, width=80)
          recommands = os.listdir(self.main_save_dir)
          self.adressbar_list = OptionMenu(self.adressbar,
               self.adressbar_sv, *recommands)
          self.adressbar_btn_save = Button(self.adressbar,
               text='저장')
          self.adressbar_btn_load = Button(self.adressbar,
               text='불러오기')
          self.adressbar.pack(side=RIGHT, padx=13)
          self.adressbar_entry.pack(
               side=LEFT, fill=Y, expand=True)
          self.adressbar_list.config(width=1,
               fg='#eeeeee',bg='#eeeeee',
               activebackground='#eeeeee',
               activeforeground='#eeeeee')
          self.adressbar_list.pack(
               side=LEFT, fill=Y, expand=True)
          self.adressbar_btn_save.pack(
               side=LEFT, fill=Y, expand=True)
          self.adressbar_btn_load.pack(
               side=LEFT, fill=Y, expand=True)
          self.adressbar_sv.set(os.path.join(main_dir,"save","default.txt"))

          ### 사이드바::인포박스
          self.infobox = Frame(self.sidebar)
          self.infobox_lab  = Label(self.infobox,
               text="사용법", anchor=W, bg='gray')
          self.infobox_info = Label(self.infobox,
               text=self.desc)
          self.infobox.pack(fill=X,padx=5,pady=10)
          self.infobox_lab.pack(fill=X)
          self.infobox_info.pack(fill=X)


          ### 사이드바::새로만들기
          self.toolnew = Frame(self.sidebar)
          self.toolnew_lab = Label(self.toolnew,
               text="새로만들기(가로/세로)",
               anchor=W, bg='gray')
          self.toolnew_x = Scale(self.toolnew,
               orient=HORIZONTAL,
               from_=2, to=100, resolution=1)
          self.toolnew_y = Scale(self.toolnew,
               orient=HORIZONTAL,
               from_=2, to=100, resolution=1)
          self.toolnew_btn = Button(self.toolnew,
               text='만들기')
          self.toolnew.pack(fill=X,padx=5,pady=10)
          self.toolnew_lab.pack(fill=X)
          self.toolnew_x.pack(fill=X)
          self.toolnew_y.pack(fill=X)
          self.toolnew_btn.pack(side=RIGHT)

          ### 사이드바::풀이법
          self.solverbox = Frame(self.sidebar)
          self.solverbox_lab = Label(self.solverbox,
               text='풀이법', anchor=W, bg='gray')
          self.solverbox_btn_getGraph = Button(self.solverbox,
               text='그래프 얻기(갱신)')
          self.solverbox_btn_dfs = Button(self.solverbox,
               text='깊이 우선 탐색 얻기(갱신)')
          self.solverbox_btn_bfs = Button(self.solverbox,
               text='넓이 우선 탐색 얻기(갱신)')
          self.solverbox_btn_delGraph = Button(self.solverbox,
               text='그래프 지우기')
          self.solverbox.pack(fill=X,padx=5,pady=10)
          self.solverbox_lab.pack(fill=X)
          self.solverbox_btn_getGraph.pack(fill=X)
          self.solverbox_btn_dfs.pack(fill=X)
          self.solverbox_btn_bfs.pack(fill=X)
          self.solverbox_btn_delGraph.pack(fill=X)

          ## 깊이 넓이 우선 탐색
          self.solverbox_btn_dfs_path = Button(self.solverbox,
               text='깊이 우선 탐색(경로)')
          self.solverbox_btn_bfs_path = Button(self.solverbox,
               text='넓이 우선 탐색(경로)')
          self.solver_btn_clear = Button(self.solverbox,
               text='경로지우기')
          self.solverbox_btn_dfs_path.pack(fill=X)
          self.solverbox_btn_bfs_path.pack(fill=X)
          self.solver_btn_clear.pack(fill=X)

          self.solverbox_btn_bfs.config(state='disable')
          self.solverbox_btn_dfs.config(state='disable')
          self.solverbox_btn_bfs_path.config(state='disable')
          self.solverbox_btn_dfs_path.config(state='disable')

          self.info_solution_len = Label(self.solverbox, text='solution_len=')
          self.info_solution_len.pack()
          self.info_path_len = Label(self.solverbox, text='path_len=')
          self.info_path_len.pack()

          
          ### 뷰어 and 엔진
          self.canvas = Canvas(self.viewer, width=1000, height=700, bg='steel blue')
          self.canvas.focus_set()
          self.canvas.pack(fill=BOTH, expand=True)
          self.canvasex = CanvasEx(self.canvas)
          self.system   = System(self.canvasex)

          ################################################
          ################################################

          ### 마우스 동작 + focuse set
          self.moveing = False
          self.firstx  = 0
          self.firsty  = 0
          self.foriginx = 0
          self.foriginy = 0
          def startmove(event):
               self.canvas.focus_set()
               self.firstx = event.x
               self.firsty = event.y
               self.foriginx = self.system.origin.x
               self.foriginy = self.system.origin.y
               
          def move(event):
               origin = self.system.origin
               dx = event.x - self.firstx
               dy = event.y - self.firsty
               rate =  2/int(self.canvas['height'])
               origin.x = self.foriginx + dx*rate
               origin.y = self.foriginy - dy*rate
               self.system.updateOrigin()
        
          self.canvas.bind("<Button-1>", startmove)
          self.canvas.bind("<B1-Motion>", move)


          def zoom(event):
               if event.delta < 0:
                    self.system.scaleBitmap(0.8, 0.8, 0.01)
               else:
                    self.system.scaleBitmap(1.25, 1.25, 0.01)

          def linux_button5(event):
               self.system.scaleBitmap(0.8, 0.8, 0.01)

          def linux_button4(event):
               self.system.scaleBitmap(1.25, 1.25, 0.01)

          self.canvas.bind('<MouseWheel>', zoom)         # for windows, osx
          self.canvas.bind('<Button-4>', linux_button4)  # for linux
          self.canvas.bind('<Button-5>', linux_button5)  # for linux

          ### 기본 이동동작 및 작동
          self.blockmode = False
          self.emptymode = False
          def moveLeft(event):
               self.system.moveCursur(-1, 0)
               if self.blockmode : self.system.block()
               if self.emptymode : self.system.empty()
               
          def moveRight(event):
               self.system.moveCursur( 1, 0)
               if self.blockmode : self.system.block()
               if self.emptymode : self.system.empty()
               
          def moveTop(event):
               self.system.moveCursur( 0,-1)
               if self.blockmode : self.system.block()
               if self.emptymode : self.system.empty()
               
          def moveBottom(event):
               self.system.moveCursur( 0, 1)
               if self.blockmode : self.system.block()
               if self.emptymode : self.system.empty()

          def onEmptyMode(event):
               self.emptymode = True
               self.system.empty()
          def offEmptyMode(event):
               self.emptymode = False

          def onBlockMode(event):
               self.blockmode = True
               self.system.block()
          def offBlockMode(event):
               self.blockmode = False
               
          self.canvas.bind('<Left>',   moveLeft)
          self.canvas.bind('<Right>',  moveRight)
          self.canvas.bind('<Up>',     moveTop)
          self.canvas.bind('<Down>',   moveBottom)
          self.canvas.bind('<KeyPress-e>',   onEmptyMode)
          self.canvas.bind('<KeyRelease-e>', offEmptyMode)
          self.canvas.bind('<KeyPress-b>',   onBlockMode)
          self.canvas.bind('<KeyRelease-b>', offBlockMode)

          def newBitmap(event):
               self.solverbox_btn_bfs.config(state='disable')
               self.solverbox_btn_dfs.config(state='disable')
               self.solverbox_btn_bfs_path.config(state='disable')
               self.solverbox_btn_dfs_path.config(state='disable')
               self.system.newEmptyBitmap(
                    self.toolnew_x.get(),
                    self.toolnew_y.get())
          self.toolnew_btn.bind('<Button-1>', newBitmap)

          ## 그래프 표시
          def getGraph(event):
               self.system.getTree()
               self.solverbox_btn_bfs.config(state='normal')
               self.solverbox_btn_dfs.config(state='normal')
          def delGraph(event):
               self.system.delSolution()
               self.system.delTree()
               self.solverbox_btn_bfs.config(state='disable')
               self.solverbox_btn_dfs.config(state='disable')
               self.solverbox_btn_bfs_path.config(state='disable')
               self.solverbox_btn_dfs_path.config(state='disable')
          self.solverbox_btn_getGraph.bind('<Button-1>', getGraph)
          self.solverbox_btn_delGraph.bind('<Button-1>', delGraph)

          # 탐색
          self.mode = 0
          def getDFSSolution(event):
               self.system.getDFSSolution()
               self.solverbox_btn_dfs_path.config(state='normal')
               self.mode = 1
          def getBFSSolution(event):
               self.system.getBFSSolution()
               self.solverbox_btn_bfs_path.config(state='normal')
               self.mode = 2
          self.solverbox_btn_bfs.bind('<Button-1>', getBFSSolution)
          self.solverbox_btn_dfs.bind('<Button-1>', getDFSSolution)
          def showDFSSolutionPath(event):
               system = self.system
               if system.bfs_show: system.hideBFSSolution()
               if system.bfs_path_show: system.hideBFSSolutionPath()
               self.system.showDFSSolutionAll()
               self.system.showDFSSolutionPath()
               self.mode = 1
               self.info_solution_len.config(text="soltion_len=%d"%(len(system.dfs_solution)))
               self.info_path_len.config(text="path_len=%d"%(len(system.dfs_solution_path)))
          self.solverbox_btn_dfs_path.bind('<Button-1>', showDFSSolutionPath)
          def showBFSSolutionPath(event):
               system = self.system
               if system.dfs_show: system.hideDFSSolution()
               if system.dfs_path_show: system.hideDFSSolutionPath()
               self.system.showBFSSolutionAll()
               self.system.showBFSSolutionPath()
               self.mode = 2
               self.info_solution_len.config(text="soltion_len=%d"%(len(system.bfs_solution)))
               self.info_path_len.config(text="path_len=%d"%(len(system.bfs_solution_path)))
          self.solverbox_btn_bfs_path.bind('<Button-1>', showBFSSolutionPath)


          ### Auto Run
          self.stepbar_auto_prev_run = False
          self.stepbar_auto_next_run = False
          def onNext(event):
               if self.mode == 1: #DFS
                    self.system.showNextDFSSolution()
                    self.stepbar_step.config(text=\
                         "step=%d"%(self.system.dfs_step))
               if self.mode == 2:
                    self.system.showNextBFSSolution()
                    self.stepbar_step.config(text=\
                         "step=%d"%(self.system.bfs_step))
          def onPrev(event):
               if self.mode == 1: #DFS
                    self.system.showPrevDFSSolution()
                    self.stepbar_step.config(text=\
                         "step=%d"%(self.system.dfs_step))
               if self.mode == 2:
                    self.system.showPrevBFSSolution()
                    self.stepbar_step.config(text=\
                         "step=%d"%(self.system.bfs_step))
          def onAutoPrevFrame():
               onPrev(None)
               if (self.mode is not 0) and self.stepbar_auto_prev_run:
                    self.after(25, onAutoPrevFrame)
          def onAutoPrev(event):
               print("auto prev : on")
               if self.stepbar_auto_prev_run == False:
                    self.stepbar_auto_next_run = False
                    self.stepbar_auto_prev_run = True
                    self.after(25, onAutoPrevFrame)
          def onAutoNextFrame():
               onNext(None)
               if (self.mode is not 0) and self.stepbar_auto_next_run:
                    self.after(25, onAutoNextFrame)
          def onAutoNext(event):
               print("auto next : on")
               if self.stepbar_auto_next_run == False:
                    self.stepbar_auto_prev_run = False
                    self.stepbar_auto_next_run = True
                    self.after(25, onAutoNextFrame)
          def onAutoStop(event):
               self.stepbar_auto_next_run = False
               self.stepbar_auto_prev_run = False
          self.stepbar_btn_next.bind('<Button-1>', onNext)
          self.stepbar_btn_prev.bind('<Button-1>', onPrev)
          self.stepbar_btn_stop.bind('<Button-1>',onAutoStop)
          self.stepbar_btn_auto_prev.bind('<Button-1>', onAutoPrev)
          self.stepbar_btn_auto_next.bind('<Button-1>', onAutoNext)

          ### 저장, 불러오기
          def openf(event):
               path = self.adressbar_sv.get()
               if not (path.startswith(r'C:') or path.startswith(r'/')):
                    path = os.path.join(self.main_save_dir,path)
               print("open... : " + path)
               self.system.open(path, 100, 100)
               self.solverbox_btn_bfs.config(state='disable')
               self.solverbox_btn_dfs.config(state='disable')
               self.solverbox_btn_bfs_path.config(state='disable')
               self.solverbox_btn_dfs_path.config(state='disable')

          def savef(event):
               path = self.adressbar_sv.get()
               if not (path.startswith(r'C:') or path.startswith(r'/')):
                    path = os.path.join(self.main_save_dir,path)
               print("save... : " + path)
               self.system.save(path)

          def clear(event):
               self.system.clearSolution()
               
          self.adressbar_btn_load.bind('<Button-1>', openf)
          self.adressbar_btn_save.bind('<Button-1>', savef)
          self.bind('<Control-s>', openf)
          self.bind('<Control-o>', openf)
          self.solver_btn_clear.bind('<Button-1>', clear)
          

          
          
