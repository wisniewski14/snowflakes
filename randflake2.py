import turtle  
import random
import math
import time
import numpy as np


# vector substration
def vecsub(a, b):
    return [a[0] - b[0], a[1] - b[1], a[2] - b[2]]

# vector crossproduct
def veccross(x, y):
    v = [0, 0, 0]
    v[0] = x[1]*y[2] - x[2]*y[1]
    v[1] = x[2]*y[0] - x[0]*y[2]
    v[2] = x[0]*y[1] - x[1]*y[0]
    return v
gcount=0
# calculate normal from 3 verts
def Normal(v0, v1, v2):
    return veccross(vecsub(v0, v1),vecsub(v0, v2))

def line3d(line):
  global size
  wid=8.0
  x1=line[0][0]
  y1=line[0][1]
  x2=line[1][0]
  y2=line[1][1]
  scale=0.3
  scale=0.225
  wid=wid*scale
  x1=x1*scale
  x2=x2*scale
  y1=y1*scale
  y2=y2*scale
  z=(wid/2.0)*math.sqrt(3.0)
  if x1==x2:
    m=100000000000000000000000
  else:
    m=(y2-y1)/(x2-x1)
  if m==0:
    m2=100000000000000000000000
  else:
    m2=-1.0/m
  ang=math.atan(m)
  angper=math.atan(m2)
  xoper=1.0

  if y2<y1:
      xoper=-1
  
  cs6=math.cos(angper)*wid*math.cos(math.pi/6.0)*xoper
  si6=math.sin(angper)*wid*math.cos(math.pi/6.0)*xoper
  cs3=math.cos(angper)*wid*math.cos(math.pi/2.2)*xoper
  si3=math.sin(angper)*wid*math.cos(math.pi/2.2)*xoper

  x1a=x1+cs6
  x2a=x2+cs6
  y1a=y1+si6
  y2a=y2+si6
  x3a=x1-cs6
  x4a=x2-cs6
  y3a=y1-si6
  y4a=y2-si6

  x5a=x1+cs3
  x6a=x2+cs3
  y5a=y1+si3
  y6a=y2+si3
  x7a=x1-cs3
  x8a=x2-cs3
  y7a=y1-si3
  y8a=y2-si3

  oper=1.0
  if x2<x1:
      oper=-1

  cs6b=math.cos(ang)*wid*math.cos(math.pi/6.0)*oper
  si6b=math.sin(ang)*wid*math.cos(math.pi/6.0)*oper

  x9a=x1-cs6b
  x10a=x2+cs6b
  y9a=y1-si6b
  y10a=y2+si6b


  
  faces=[ \
          #### 4 sides
          #[[x1a,y1a,0],[x2a,y2a,0],[x2,y2,z]], \
          #[[x1a,y1a,0],[x2,y2,z],[x1,y1,z]], \
          #\
          #[[x1,y1,z],[x2,y2,z],[x4a,y4a,0]], \
          #[[x1,y1,z],[x4a,y4a,0],[x3a,y3a,0]], \
          #\
          #[[x3a,y3a,0],[x4a,y4a,0],[x2,y2,-z]], \
          #[[x3a,y3a,0],[x2,y2,-z],[x1,y1,-z]], \
          #\
          #[[x1,y1,-z],[x2,y2,-z],[x2a,y2a,0]], \
          #[[x1,y1,-z],[x2a,y2a,0],[x1a,y1a,0]], \
          #\
          #[[x1a,y1a,0],[x1,y1,z],[x9a,y9a,0]], \
          #[[x1,y1,z],[x3a,y3a,0],[x9a,y9a,0]], \
          #[[x3a,y3a,0],[x1,y1,-z],[x9a,y9a,0]], \
          #[[x1,y1,-z],[x1a,y1a,0],[x9a,y9a,0]], \
          #\
          #[[x2a,y2a,0],[x2,y2,-z],[x10a,y10a,0]], \
          #[[x2,y2,-z],[x4a,y4a,0],[x10a,y10a,0]], \
          #[[x4a,y4a,0],[x2,y2,z],[x10a,y10a,0]], \
          #[[x2,y2,z],[x2a,y2a,0],[x10a,y10a,0]] \
          ### 6 sides
          [[x1a,y1a,0],[x2a,y2a,0],[x6a,y6a,z]], \
          [[x1a,y1a,0],[x6a,y6a,z],[x5a,y5a,z]], \
          \
          [[x5a,y5a,z],[x6a,y6a,z],[x8a,y8a,z]], \
          [[x5a,y5a,z],[x8a,y8a,z],[x7a,y7a,z]], \
          \
          [[x7a,y7a,z],[x8a,y8a,z],[x4a,y4a,0]], \
          [[x7a,y7a,z],[x4a,y4a,0],[x3a,y3a,0]], \
          \
          [[x3a,y3a,0],[x4a,y4a,0],[x8a,y8a,-z]], \
          [[x3a,y3a,0],[x8a,y8a,-z],[x7a,y7a,-z]], \
          \
          [[x7a,y7a,-z],[x8a,y8a,-z],[x6a,y6a,-z]], \
          [[x7a,y7a,-z],[x6a,y6a,-z],[x5a,y5a,-z]], \
          \
          [[x5a,y5a,-z],[x6a,y6a,-z],[x2a,y2a,0]], \
          [[x5a,y5a,-z],[x2a,y2a,0],[x1a,y1a,0]], \
          \
          [[x1a,y1a,0],[x5a,y5a,z],[x9a,y9a,0]], \
          [[x5a,y5a,z],[x7a,y7a,z],[x9a,y9a,0]], \
          [[x7a,y7a,z],[x3a,y3a,0],[x9a,y9a,0]], \
          [[x3a,y3a,0],[x7a,y7a,-z],[x9a,y9a,0]], \
          [[x7a,y7a,-z],[x5a,y5a,-z],[x9a,y9a,0]], \
          [[x5a,y5a,-z],[x1a,y1a,0],[x9a,y9a,0]], \
          \
          [[x2a,y2a,0],[x6a,y6a,-z],[x10a,y10a,0]], \
          [[x6a,y6a,-z],[x8a,y8a,-z],[x10a,y10a,0]], \
          [[x8a,y8a,-z],[x4a,y4a,0],[x10a,y10a,0]], \
          [[x4a,y4a,0],[x8a,y8a,z],[x10a,y10a,0]], \
          [[x8a,y8a,z],[x6a,y6a,z],[x10a,y10a,0]], \
          [[x6a,y6a,z],[x2a,y2a,0],[x10a,y10a,0]] \
          ]
  write3d(faces)          
def circle3d():
  global size
  wid=8.0
  #scale=0.3
  scale=0.225
  ss=size*scale
  wid=wid*scale
  z=(wid/2.0)*math.sqrt(3.0)
  zd=z/5.0
  midrad=5.0*3.0
  midrad=midrad*scale
  rads=[[[midrad-z,midrad-zd],[midrad-zd,midrad+zd],[midrad+zd,midrad+z]],\
          [[midrad-zd,midrad-z],[midrad+zd,midrad-zd],[midrad+z,midrad+zd]]]
  zs=[[[0,z],[z,z],[z,0]],[[-z,0],[-z,-z],[0,-z]]]
  faces=[]
  for k in range(24):
    for i in range(2):
        for j in range(3):
          rad=rads[i][j]
          zz=zs[i][j]
          x1=math.cos(((2*math.pi)/24.0)*float(k))*rad[0]
          y1=ss+midrad+math.sin(((2*math.pi)/24.0)*float(k))*rad[0]
          x2=math.cos(((2*math.pi)/24.0)*float(k+1.0))*rad[0]
          y2=ss+midrad+math.sin(((2*math.pi)/24.0)*float(k+1.0))*rad[0]

          x3=math.cos(((2*math.pi)/24.0)*float(k))*rad[1]
          y3=ss+midrad+math.sin(((2*math.pi)/24.0)*float(k))*rad[1]
          x4=math.cos(((2*math.pi)/24.0)*float(k+1.0))*rad[1]
          y4=ss+midrad+math.sin(((2*math.pi)/24.0)*float(k+1.0))*rad[1]

          faces.append([[x1,y1,zz[0]],[x3,y3,zz[1]],[x2,y2,zz[0]]])
          faces.append([[x3,y3,zz[1]],[x4,y4,zz[1]],[x2,y2,zz[0]]])
  write3d(faces)

def write3d(faces):
  global gcount
  gcount+=1
  f.write("solid thing"+str(gcount)+"\n")
  for tri in faces:
    f.write("  facet normal")
    nor=Normal(tri[0],tri[1],tri[2])
    for i in nor:
      f.write(" "+str(i+size))
      #f.write(" "+str(np.float32(i)))
    f.write("\n    outer loop")
    for i in tri:
      f.write("\n      vertex")
      for j in i:
        f.write(" "+str(j+size))
        #f.write(" "+str(np.float32(j)))
    f.write("\n    endloop")
    f.write("\n  endfacet\n")
  f.write("endsolid thing"+str(gcount)+"\n")


def rot(ang,x,y):
  newx=y*math.sin(ang)+x*math.cos(ang)
  newy=y*math.cos(ang)-x*math.sin(ang)
  return (newx,newy)
def rotlist(ang,x,y):
  newx=y*math.sin(ang)+x*math.cos(ang)
  newy=y*math.cos(ang)-x*math.sin(ang)
  return [newx,newy]
def halfarm(side,ang,mud):
  snow.up()
  snow.setpos(rot(ang,0.0,size))
  snow.down()
  snow.setpos(0,0)
  line=[[0,0]]
  line.append(list(rot(ang,0,size)))
  line3d(line)
  for p in draw:
    line=[]
    for c in range(len(p)):
      if type(p[c]) is int:
        x1=pts[p[c]][0]+mud[p[c]][0]
        y1=pts[p[c]][1]+mud[p[c]][1]
      else:
        x1=p[c][0]
        y1=p[c][1]
      line.append(list(rot(ang,x1*side,y1)))
    #print(line)
    
    line3d(line)
    snow.up()
    snow.setpos(rot(ang,line[0][0]*side, line[0][1]))
    snow.down()
    snow.setpos(rot(ang,line[1][0]*side, line[1][1]))

    #snow.setpos(rot(ang,p[1][0]*side, p[1][1]))
#param=[[12,"Light Gray"],[1,"black"]]
param=[[12,"Light Gray"]]
#skew=0
npts=16
npts=10
snow = turtle.Turtle()
snow.speed(0)
snow.hideturtle()
turtle.tracer(0, 0)
sides=[1,-1]


#while(True):
skew=random.randint(0,0)
#print(skew)
size=200.0+float(random.randint(1,16))*2.0
pts=[]
draw=[]
fname="b"
for i in range(npts):
  #print(i)
  ra=random.randint(0,npts-1)
  rr=random.randint(0,npts-1)
  ry=random.randint(0,npts-1)
  #rr2=random.randint(0,npts-1)
  fname=fname+str(ra)+str(rr)+str(ry)
  ang1=((1.0/float(npts))*float(ra))*math.pi/6.0+math.pi/3.0
  rad1=((1.0/float(npts))*float(rr))*size
  p1=math.cos(ang1)*rad1
  p2=math.sin(ang1)*rad1
  pts.append([p1,p2])
  #draw.append([[0.0,((1.0/float(npts))*float(ry))*(rad1*0.5)+rad1*0.5],[p1,p2]])
  draw.append([[0.0,((1.0/float(npts))*float(ry))*(rad1*0.5)+rad1*0.5],i])
#print(pts)
rcon=random.randint(0,3)
for i in range(rcon):
  r1=random.randint(0,npts-1)
  r2=random.randint(0,npts-1)
  if r1!=r2:
    draw.append([r1,r2])
snow.clear()
print("New STL file: "+fname+".stl")
f=open(fname+'.stl','w')
#f.write("solid thing\n")
for i in range(6):
  mrs=[]
  for side in range(2):
    mr=[]
    for j in range(npts):
      m1=float(random.randint(-skew,skew))
      m2=float(random.randint(-skew,skew))
      mr.append([m1,m2])
    mrs.append(list(mr))
  for par in param:
    snow.pensize(par[0])
    snow.pencolor(par[1])
    snow.up()
    snow.setpos(0,size)
    snow.down()
    snow.circle(12)
    circle3d()
#    crad=16.0
#    for k in range(16):
#        line3d([\
#                [math.cos(((2*math.pi)/16.0)*float(k))*crad,\
#                size+crad+math.sin(((2*math.pi)/16.0)*float(k))*crad],\
#                [math.cos(((2*math.pi)/16.0)*float(k+1))*crad,\
#                size+crad+math.sin(((2*math.pi)/16.0)*float(k+1))*crad]\
#                ])
    for side in range(2):
      halfarm(sides[side],float(i)*math.pi/3.0,mrs[side])
turtle.update()
#time.sleep(2)


#f.write("endsolid thing\n")
f.close()
