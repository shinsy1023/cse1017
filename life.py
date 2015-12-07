# Game of Life
# rules
# (한산사) 생존 이웃이 둘 미만인 생존세포
# (생존) 생존 이웃이 둘 또는 셋인 생존세포
# (복잡사) 생존 이웃이 넷 이상인 생존세포
# (환생) 생존 이웃이 셋인 사망세포 

from tkinter import *

class Life(object):
    def __init__(self, pat, rows, cols):
        self.rows = rows
        self.cols = cols
        self.matrix = self.__create_empty_matrix()
        self.__create_init_matrix(pat)

    def __create_empty_matrix(self):
        # 원소가 모두 0인 self.cols x self.rows 중첩리스트를 만들어 내줌 
        return [[False for _ in range(self.cols)] 
                for _ in range(self.rows)]        

    def __create_init_matrix(self, pat):
        # 시작 페턴 pat을 받아 self.matrix의 중앙에 위치시킴
        pat_rows = len(pat)
        pat_cols = len(pat[0])
        flat_pat = sum(pat,[])
        center_x = (self.cols - pat_cols) // 2
        center_y = (self.rows - pat_rows) // 2
        for i in range(center_x, center_x + pat_rows):
            for j in range(center_y, center_y + pat_cols):
                self.matrix[i][j] = flat_pat.pop(0)
        
    def __neighbors(self, x, y):
        count = 0
        if x==0 or y==0 or x==self.cols-1 or y==self.rows-1:
            if x==0 and y==0:
                if self.matrix[0][1]==1:
                    count+=1
                if self.matrix[1][0]==1:
                    count+=1
                if self.matrix[1][1]==1:
                    count+=1
            elif x==0:
                if self.matrix[y-1][x]==1:
                    count+=1
                if self.matrix[y+1][x]==1:
                    count+=1
                if self.matrix[y-1][x+1]==1:
                    count+=1
                if self.matrix[y][x+1]==1:
                    count+=1
                if self.matrix[y+1][x+1]==1:
                    count+=1
            elif y==0:
                if self.matrix[y][x-1]==1:
                    count+=1
                if self.matrix[y+1][x-1]==1:
                    conut+=1
                if self.matrix[y+1][x]==1:
                    count+=1
                if self.matrix[y+1][x+1]==1:
                    count+=1
            elif x==self.cols-1:
                if self.matrix[y-1][x-1]==1:
                    count+=1
                if self.matrix[y][x-1]==1:
                        count+=1
                if self.matrix[y+1][x-1]==1:
                    conut+=1
                if self.matrix[y-1][x]==1:
                    count+=1
                if self.matrix[y+1][x]==1:
                    count+=1
            elif y==self.rows-1:
                if self.matrix[y-1][x-1]==1:
                    count+=1
                if self.matrix[y][x-1]==1:
                    count+=1
                if self.matrix[y-1][x]==1:
                    count+=1
                if self.matrix[y-1][x+1]==1:
                    count+=1
                if self.matrix[y][x+1]==1:
                    count+=1
        else:
            if self.matrix[y-1][x-1]==1:
                count+=1
            if self.matrix[y][x-1]==1:
                    count+=1
            if self.matrix[y+1][x-1]==1:
                conut+=1
            if self.matrix[y-1][x]==1:
                count+=1
            if self.matrix[y+1][x]==1:
                count+=1
            if self.matrix[y-1][x+1]==1:
                count+=1
            if self.matrix[y][x+1]==1:
                count+=1
            if self.matrix[y+1][x+1]==1:
                count+=1# 좌표 (x,y) 주위의 8개 셀에서 살아있는 셀의 개수를 세어서 count에 기억함
        return count
        
    def lifecycle(self):
        future = self.__create_empty_matrix() # 새로운 matrix 생성
        for row in range(self.rows):
            for col in range(self.cols):
                if self.matrix[row][col]==1:
                    if self.__neighbors(col, row)==2 or self.__neighbors(col, row)==3:
                        future[row][col]=1
                    else:
                        future[row][col]=0
                else:
                    if self.__neighbors(col, row)==2:
                        future[row][col]=1
                    else:
                        future[row][col]=0# 생존에 따라 각 셀의 다음 세대 생사여부를 판단하여 future에 기록한다.
        self.matrix = future # 세대 교체

class Pattern(object):
    # Still Lifes
    BLOCK = [[1,1],[1,1]]
    BEEHIVE = [[0,1,1,0],[1,0,0,1],[0,1,1,0]]
    LOAF = [[0,1,1,0],[1,0,0,1],[0,1,0,1],[0,0,1,0]]
    BOAT = [[1,1,0],[1,0,1],[0,1,0]]
    
    # Oscillators
    BLINKER = [[1,1,1]]
    TOAD = [[0,1,1,1],[1,1,1,0]]
    BEACON = [[1,1,0,0],[1,0,0,0],[0,0,0,1],[0,0,1,1]]
    PULSAR = [[0,0,1,1,1,0,0,0,1,1,1,0,0],
              [0,0,0,0,0,0,0,0,0,0,0,0,0],
              [1,0,0,0,0,1,0,1,0,0,0,0,1],
              [1,0,0,0,0,1,0,1,0,0,0,0,1],
              [1,0,0,0,0,1,0,1,0,0,0,0,1],
              [0,0,1,1,1,0,0,0,1,1,1,0,0],
              [0,0,0,0,0,0,0,0,0,0,0,0,0],
              [0,0,1,1,1,0,0,0,1,1,1,0,0],
              [1,0,0,0,0,1,0,1,0,0,0,0,1],
              [1,0,0,0,0,1,0,1,0,0,0,0,1],
              [1,0,0,0,0,1,0,1,0,0,0,0,1],
              [0,0,0,0,0,0,0,0,0,0,0,0,0],
              [0,0,1,1,1,0,0,0,1,1,1,0,0]]
    PENTADECATHLON = [[1,1,1],
                      [1,0,1],
                      [1,1,1],
                      [1,1,1],
                      [1,1,1],
                      [1,1,1],
                      [1,0,1],
                      [1,1,1]]
    
    # Spaceships
    GLIDER = [[1,1,1],[1,0,0],[0,1,0]]
    LIGHTWEIGHT_SPACESHIP = [[0,1,0,0,1],
                             [1,0,0,0,0],
                             [1,0,0,0,1],
                             [1,1,1,1,0]]
    
    # Methuselahs
    R_PENTOMINO = [[0,1,1],[1,1,0],[0,1,0]]
    DIEHARD = [[0,0,0,0,0,0,1,0],
               [1,1,0,0,0,0,0,0],
               [0,1,0,0,0,1,1,1]]
    ACORN = [[0,1,0,0,0,0,0],
             [0,0,0,1,0,0,0],
             [1,1,0,0,1,1,1]]
    
    # Indefinitely Growing
    INFINITY1 = [[0,0,0,0,0,0,1,0],
                 [0,0,0,0,1,0,1,1],
                 [0,0,0,0,1,0,1,0],
                 [0,0,0,0,1,0,0,0],
                 [0,0,1,0,0,0,0,0],
                 [1,0,1,0,0,0,0,0]]
    INFINITY2 = [[1,1,1,0,1],
                 [1,0,0,0,0],
                 [0,0,0,1,1],
                 [0,1,1,0,1],
                 [1,0,1,0,1]]
    INFINITY3 = [[1,1,1,1,1,1,1,1,0,1,1,1,1,1,0,0,0,1,1,1,0,0,0,0,0,0,1,1,1,1,1,1,1,0,1,1,1,1,1]]
    GOSPER_GLIDER_GUN =  [
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,1,0],
[0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,1,0],
[0,1,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0],
[0,1,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,1,1,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,1,0,0,1,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]] # (to be filled)
    
class LifeWriter(object):
    def __init__(self, life, width, height, unit):
        self.__life = life
        self.__unit = unit
        root = Tk()
        root.title("Game of Life")
        root.geometry(str(width+5)+"x"+str(height+5))
        self.__canvas = Canvas(root, width=width, height=height)
        self.__canvas.grid()
        self.__draw_matrix()
        self.animate()
        root.mainloop()

    def animate(self):
        self.__canvas.delete(ALL)
        self.__life.lifecycle()
        self.__draw_matrix# Canvas 전체를 지우고 세대교체를 한다음 __draw_matrix()를 호출하여 새로 그린다.  
        self.__canvas.after(500, self.animate)

    def __draw_matrix(self):
        for row in range(self.__life.rows):
            for col in range(self.__life.rows):
                if self.__life.matrix[col][row]==1:

                else:
                    
# self.__life.matrix의 원소를 하나씩 검사하여 1에 해당하는 셀을 빨간색 정사각형으로 칠한다.
    
class LifeController(object):
    def __init__(self, pattern, width, height, unit):
        life = Life(pattern, width//unit, height//unit)
        LifeWriter(life, width, height, unit).animate()

# main
width = 640
height = 480
unit = 10 # set it to 4 for INFINITY3
LifeController(Pattern.PENTADECATHLON, width, height, unit)

