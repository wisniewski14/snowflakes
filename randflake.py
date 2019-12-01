import turtle  
import random
import math
snow = turtle.Turtle() 
snow.speed(0)
armlen=random.randint(180,220)
armwid=10
nbranch=random.randint(6,16)
awid=((armlen)/float(nbranch+1))
ls=[]
for i in range(nbranch):
  t=random.randint(0,50)
  if i<nbranch/2.0:
    t=t*((i)/float(nbranch))
  else:
    t=t*((nbranch-i)/float(nbranch))
  ls.append(int(awid)+t)
def rot(ang,x,y):
  newx=y*math.sin(ang)+x*math.cos(ang)
  newy=y*math.cos(ang)-x*math.sin(ang)
  return (newx,newy)
def halfarm(side,ang):
  snow.up()
  snow.setpos(rot(ang,0*side, armlen+(awid/2.0)/2.0))
  snow.down()
  snow.setpos(rot(ang,(awid/2.0)*side, armlen))
  snow.setpos(rot(ang,(awid/2.0)*side, 0))
  for i in range(nbranch):
    alen=ls[i]
    snow.up()
    snow.setpos(rot(ang,0*side, (i+0.5)*awid))
    snow.down()
    snow.setpos(rot(ang,alen*math.sqrt(3)*side, alen+(i+0.5)*awid))
    snow.setpos(rot(ang,alen*math.sqrt(3)*side, awid/2.0+alen+(i+0.5)*awid))
    snow.setpos(rot(ang,(alen-awid/4.0)*math.sqrt(3)*side, awid*(3.0/4.0)+alen+(i+0.5)*awid))
    snow.setpos(rot(ang,0*side, awid+(i+0.5)*awid))
turtle.tracer(0, 0)
for i in range(6):
  halfarm(1,i*math.pi/3.0)
  halfarm(-1,i*math.pi/3.0)
turtle.update()
turtle.done()
