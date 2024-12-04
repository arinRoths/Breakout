#!/usr/bin/python
from intersect import *
from tkinter import *

root = Tk()
class MyCanvas(Canvas):
  def __init__( this, *args, **kwargs ):
    Canvas.__init__( this, *args, **kwargs )
    this.ball = this.makeBall( 300 ,  300 )
    this.rectangle = this.makeRectangle(225,475)
    this.ball_velocity_x = 5/3
    this.ball_velocity_y = 9/3
    this.fall_velocity_y = 0
    this.fall2_velocity_y = 0
    this.fall3_velocity_y = 0
    this.fall4_velocity_y = 0
    this.fall5_velocity_y = 0
    this.fall6_velocity_y = 0
    this.fall7_velocity_y = 0
    this.fall8_velocity_y = 0
    this.fall9_velocity_y = 0
    this.fall10_velocity_y = 0
    this.fall_velocity_x = 0
    for x in range (0, 500, 50):
       for y in range(50, 150, 10):
        if y==50:
          this.makeStrong(x,y)
        elif y == 70:
          this.makeStrong(x,y)
        elif y == 90:
          this.makeStrong(x,y)
        elif y == 110:
          this.makeStrong(x,y)
        elif y==130:
          this.makeStrong(x,y)
        else:
          this.makeBlock(x,y)

    this.fall=this.makefall(0,150)
    this.fall2 = this.makefall(50,150)
    this.fall3 = this.makefall(100,150)
    this.fall4 = this.makefall(150,150)
    this.fall5 = this.makefall(200,150)
    this.fall6 = this.makefall(250,150)
    this.fall7 = this.makefall(300, 150)
    this.fall8 = this.makefall(350, 150)
    this.fall9 = this.makefall(400, 150)
    this.fall10 = this.makefall(450,150)
    this.fall1=this.makefall(0,130)
    this.fall12 = this.makefall(50,130)
    this.fall13 = this.makefall(100,130)
    this.fall14 = this.makefall(150,130)
    this.fall15 = this.makefall(200,130)
    this.fall16 = this.makefall(250,130)
    this.fall17 = this.makefall(300, 130)
    this.fall18 = this.makefall(350, 130)
    this.fall19 = this.makefall(400, 130)
    this.fall110 = this.makefall(450,130)
        


    this.bind("<KeyPress>", this.keyWasPressed)
    this.bind( "<Motion>", this.mouseHasMoved )
    this.focus_set();
  
  def makeBall( this, x, y, color="blue"):  
    return this.create_oval( x, y, x+5, y+5, fill=color )

  def makeRectangle(this, x, y, color="red"):
    return this.create_rectangle(x, y, x+50, y+10, fill=color)

  def makeBlock(this, x, y, color="red"):
    return this.create_rectangle(x, y, x+50, y+10, fill=color, tags="block")

  def makeStrong(this, x, y, color= "purple"):
    return this.create_rectangle(x,y, x+50, y+10, fill=color, tags="Sblock")

  def makefall(this, x, y, color = "orange"):
    return this.create_rectangle(x,y, x+50, y+10, fill=color, tags="Fblock")
  
  def makeRectangleO(this, x, y, color="orange"):
    return this.create_rectangle(x, y, x+50, y+10, fill=color)



  def eachFrame(this):
    sx, sy, ex, ey = this.coords(this.ball)
    ix, iy, jx, jy = this.coords(this.rectangle)
    #print(sx, sy, ex, ey)
    allblocks = this.find_withtag( "block" )
    strongBlocks = this.find_withtag("Sblock")
    fallblock = this.find_withtag("Fblock")

    if (len(allblocks) ==0 and  len(strongBlocks)==0 and len(fallblock)==0):
        raise(Exception("You win! Go you!"))
    list1 = []
    list2 =[]
    list3 = []
    list4 = []
    #xCoord = 0
    for block in allblocks:
        ax,ay,bx,by = this.coords(block)
        if hits(ax,ay,bx,by,sx,sy,ex,ey):
            #print( hits(ax,ay,bx,by,sx,sy,ex,ey))
            #raise(Exception("hit a block"))
            list1 = list1 + hits(ax,ay,bx,by,sx,sy,ex,ey)
            this.delete(block)
    for Sblock in strongBlocks:
        ax,ay,bx,by = this.coords(Sblock)
        if hits(ax,ay,bx,by,sx,sy,ex,ey):
            #print( hits(ax,ay,bx,by,sx,sy,ex,ey))
            #raise(Exception("hit a block"))
            list2 = list2 + hits(ax,ay,bx,by,sx,sy,ex,ey)
            this.delete(Sblock)
            this.makeBlock(ax,ay)
    for Fblock in fallblock:
        ax,ay,bx,by = this.coords(Fblock)
        if hits(ax,ay,bx,by,sx,sy,ex,ey):
            list4.append(ax)
            this.delete(Fblock)
            #this.makeRectangleO(ax,ay)

            #print( hits(ax,ay,bx,by,sx,sy,ex,ey))
            #raise(Exception("hit a block"))
            list3  = list3 + hits(ax,ay,bx,by,sx,sy,ex,ey)
            #this.fall_velocity_y= 1
    #if 'N' in list2 or list3 or list1:
    #        this.ball_velocity_y = -1*this.ball_velocity_y
    #elif 'E' in list2 or list3 or list1:
    #        this.ball_velocity_x = -1*this.ball_velocity_x
    #elif 'S' in list2 or list3 or list1:
    #        this.ball_velocity_y = -1*this.ball_velocity_y
    #elif 'W' in list2 or list3 or list1:
    #        this.ball_velocity_x = -1*this.ball_velocity_x
    if 'N' in list2:
            this.ball_velocity_y = -1*this.ball_velocity_y
    elif 'E' in list2:
            this.ball_velocity_x = -1*this.ball_velocity_x
    elif 'S' in list2:
            this.ball_velocity_y = -1*this.ball_velocity_y
    elif 'W' in list2:
            this.ball_velocity_x = -1*this.ball_velocity_x
    if 'N' in list3:
            this.ball_velocity_y = -1*this.ball_velocity_y
    elif 'E' in list3:
            this.ball_velocity_x = -1*this.ball_velocity_x
    elif 'S' in list3:
            this.ball_velocity_y = -1*this.ball_velocity_y
    elif 'W' in list3:
            this.ball_velocity_x = -1*this.ball_velocity_x
    if 'N' in list1:
            this.ball_velocity_y = -1*this.ball_velocity_y
    elif 'E' in list1:
            this.ball_velocity_x = -1*this.ball_velocity_x
    elif 'S' in list1:
            this.ball_velocity_y = -1*this.ball_velocity_y
    elif 'W' in list1:
            this.ball_velocity_x = -1*this.ball_velocity_x
  
    if(sx<=0 or ex>=500):
        this.ball_velocity_x = -1*this.ball_velocity_x
    if(sy<=0):
        this.ball_velocity_y = -1*this.ball_velocity_y
    if(ey>=500):

        this.ball_velocity_y = -1*this.ball_velocity_y
        raise(Exception("You lost! Ya dork!"))
    if(ex>ix and sx<jx and ey>iy):
        this.ball_velocity_y = -1*this.ball_velocity_y
    this.move(this.ball, this.ball_velocity_x, this.ball_velocity_y)
    if 0 in list4:
        this.fall = this.makeRectangleO(0,150)
        this.fall_velocity_y= 1
        #this.move(this.fall, this.fall_velocity_x, this.fall_velocity_y)
    if 50 in list4:
        this.fall2 = this.makeRectangleO(50,150)
        this.fall2_velocity_y= 1
        
    if 100 in list4:
        this.fall3 = this.makeRectangleO(100,150)
        this.fall3_velocity_y= 1
        #this.move(this.fall3, this.fall_velocity_x, this.fall_velocity_y)
    if 150 in list4:
        this.fall4 = this.makeRectangleO(150,150)
        this.fall4_velocity_y= 1
        #this.move(this.fall4, this.fall_velocity_x, this.fall_velocity_y)
    if 200 in list4:
        this.fall5 = this.makeRectangleO(200,150)
        this.fall5_velocity_y= 1
        #this.move(this.fall5, this.fall_velocity_x, this.fall_velocity_y)
    if 250 in list4:
        this.fall6 = this.makeRectangleO(250,150)
        this.fall6_velocity_y= 1
        #this.move(this.fall6, this.fall_velocity_x, this.fall_velocity_y)
    if 300 in list4:
        this.fall7 = this.makeRectangleO(300,150)
        this.fall7_velocity_y= 1
        #this.move(this.fall7, this.fall_velocity_x, this.fall_velocity_y)
    if 350 in list4:
        this.fall8 = this.makeRectangleO(350,150)
        this.fall8_velocity_y= 1
        #this.move(this.fall8, this.fall_velocity_x, this.fall_velocity_y)
    if 400 in list4:
        this.fall9 = this.makeRectangleO(400,150)
        this.fall9_velocity_y= 1
        #this.move(this.fall9, this.fall_velocity_x, this.fall_velocity_y)
    if 450 in list4:
        this.fall10 = this.makeRectangleO(450,150)
        this.fall10_velocity_y= 1
        #this.move(this.fall10, this.fall_velocity_x, this.fall_velocity_y)

    this.move(this.fall, this.fall_velocity_x, this.fall_velocity_y)
    this.move(this.fall2, this.fall_velocity_x, this.fall2_velocity_y)
    this.move(this.fall3, this.fall_velocity_x, this.fall3_velocity_y)
    this.move(this.fall4, this.fall_velocity_x, this.fall4_velocity_y)
    this.move(this.fall5, this.fall_velocity_x, this.fall5_velocity_y)
    this.move(this.fall6, this.fall_velocity_x, this.fall6_velocity_y)
    this.move(this.fall7, this.fall_velocity_x, this.fall7_velocity_y)
    this.move(this.fall8, this.fall_velocity_x, this.fall8_velocity_y)
    this.move(this.fall9, this.fall_velocity_x, this.fall9_velocity_y)
    this.move(this.fall10, this.fall_velocity_x, this.fall10_velocity_y)



    



    
  def keyWasPressed(this, event=None):
    key = event.keysym
    sx, sy, ex, ey = this.coords(this.rectangle)
    if(key== 'Left' and (ex-25>=0 and sx-25 >=0) ):
     this.move(this.rectangle,-25, 0)
    if(key=='Right' and (ex+25<=500 and sx+25<=500)):
     this.move(this.rectangle, 25, 0)
    print("just pressed:", key)
    
  def mouseHasMoved( this, event ):
      #print( event.x, event.y )
      ix, iy, jx, jy = this.coords(this.rectangle)
      current = (jx+ix)/2
      this.move(this.rectangle, (event.x -current), 0)

  def circleMove(this):
    for x in range (0, 100, 20):
      for y in range(0, 75, 15):
        this.move(this.rectangle, x,y)
      

canvas = MyCanvas(root, width=500, height=500)
canvas.pack()

while(True):
  canvas.eachFrame()
  root.update()
#!/usr/bin/python