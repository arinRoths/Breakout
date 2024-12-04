def intersect(x1, y1, x2, y2, x3, y3, x4, y4):
    try:
        ua = ((x4-x3)*(y1-y3)-(y4-y3)*(x1-x3))/((y4-y3)*(x2-x1)-(x4-x3)*(y2-y1))
        x = x1 + ua*(x2-x1)
        y = y1 + ua*(y2-y1)
        if(between(x,x1,x2) and between(x, x3, x4) and between(y, y1, y2) and between(y, y3,y4)):
            return(x,y)
    except:
        return None

def between( n, first, second):
    if(first<=n<=second):
        return True
    elif(second<=n<=first):
        return True
    return False

def edges(sx, sy, ex, ey):
    return( (sx,sy,ex,sy), (ex,sy,ex,ey), (ex,ey,sx,ey),(sx,ey,sx,sy))

def intersectAny( oneline, listoflines):
    #print (oneline)
    for x in listoflines:
        i= x + oneline
        if intersect(*i)!= None :
            return True
    return False
    
def hits(sx1,sy1,ex1,ey1,sx2,sy2,ex2,ey2):
    sideshit= []
    box1=edges(sx1,sy1,ex1,ey1)
    box2 = edges(sx2, sy2, ex2, ey2)
    if intersectAny(box1[0], box2) == True :
        sideshit.append('N')
    if intersectAny(box1[1], box2) == True :
        sideshit.append('E')
    if intersectAny(box1[2], box2) == True :
        sideshit.append('S')
    if intersectAny(box1[3], box2) == True :
        sideshit.append('W')
    return sideshit


if __name__ == '__main__':
    print( intersect( -1, 2, 1, -1, 1, 1, -2, -1 ) )
    print( intersect( -1, 2, 1, -1, 1, 1,  3,  4 ) )
    print( intersect(  1, 1, 2,  2, 1, 1,  2,  2 ) )
    print( intersect(  1, 1, 2,  2, 2, 1,  3,  2 ) )
    print( between( 1, 0, 2 ) )
    print( between( 1, 2, 0 ) )
    print( between( 1, 3, 4 ) )
    print( between( 1, 1, 2 ) )
    print( between( 1, 2, 1 ) )
    box1 = ( 1.5, 1, 9, 10 )
    print( edges( *box1 ) )
    box2 = ( 0, 0, .5, .5 )
    box3 = ( 0, 0,  5,  5 )
    box4 = ( 0, 0, 11,  2 )
    box5 = ( 0, 0, 11, 11 )
    box6 = ( 3, 3,  4,  4 )
    box7 = ( 4, 0,  5,  5 )
    print( intersectAny( box1, (box2,box3) ) )
    print( intersectAny( box1, (box2,    ) ) )
    print( intersectAny( box1, (box4,box5) ) )
    print( intersectAny( box1, (box4,    ) ) )
    print( intersectAny( box1, (box6,box7) ) )
    print( intersectAny( box1, (box6,    ) ) )
    print( hits( *(box1+box2) ) )
    print( hits( *(box1+box3) ) )
    print( hits( *(box1+box4) ) )
    print( hits( *(box1+box5) ) )
    print( hits( *(box1+box6) ) )
    print( hits( *(box1+box7) ) )
