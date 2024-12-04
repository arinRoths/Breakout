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
    this.thing2_velocity_x = 5/3
    this.thing2_velocity_y = 9/3
    #this.thing = this.makeRectangle(30,20)
    this.thing2 = this.makeBlock(150, 150)
    #for x in range (0, 500, 50):
     #  for y in range(50, 200, 10):
      #     this .makeBlock(x,y)
    
    #this.block = this.makeBlock(30,20)
    #for x in range (0, 100, 20):
      #for y in range(0, 75, 15):
        #this.block = this.makeBlock(30,20)
        #this.move(this.block, x,y)
    #this.circleMove(block)
    #this.makeBlock(0, 100)
    #this.makeBlock(0, 110)
    #this.makeBlock(0, 120)
    #this.makeBlock(0,130)
    #this.makeBlock(0,250)
    this.bind("<KeyPress>", this.keyWasPressed)
    this.bind( "<Motion>", this.mouseHasMoved )
    this.focus_set();
  
  def makeBall( this, x, y, color="blue"):  
    return this.create_oval( x, y, x+5, y+5, fill=color )

  def makeRectangle(this, x, y, color="red"):
    return this.create_rectangle(x, y, x+50, y+10, fill=color)

  def makeBlock(this, x, y, color="red"):
    return this.create_rectangle(x, y, x+50, y+10, fill=color, tags="block")

  
  def eachFrame(this):
    sx, sy, ex, ey = this.coords(this.ball)
    ix, iy, jx, jy = this.coords(this.rectangle)
            
    #print(sx, sy, ex, ey)
    allblocks = this.find_withtag( "block" )
    if (len(allblocks) ==0):
        raise(Exception("You win! Go you!"))
    list1 = []
    for block in allblocks:
        ax,ay,bx,by = this.coords(block)
        if hits(ax,ay,bx,by,sx,sy,ex,ey):
            #print( hits(ax,ay,bx,by,sx,sy,ex,ey))
            #raise(Exception("hit a block"))
            list1 = list1 + hits(ax,ay,bx,by,sx,sy,ex,ey)
            this.delete(block)
    if 'N' in list1:
            this.ball_velocity_y = -1*this.ball_velocity_y
    if 'E' in list1:
            this.ball_velocity_x = -1*this.ball_velocity_x
    if 'S' in list1:
            this.ball_velocity_y = -1*this.ball_velocity_y
    if 'W' in list1:
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

    cx,cy,dx,dy = this.coords(this.thing2)
    if(cx<=100 or dx>=300):
        this.thing2_velocity_x = -1*this.thing2_velocity_x
    
    if(cy<=100 or dy>=300):
        this.thing2_velocity_y = -1*this.thing2_velocity_y
    
    this.move(this.thing2, this.thing2_velocity_x, this.thing2_velocity_y)
    #this.block = this.makeBlock(30,20)
    



    
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
        this.move(this.block, x,y)
      

canvas = MyCanvas(root, width=500, height=500)
canvas.pack()

while(True):
  canvas.eachFrame()
  root.update()
