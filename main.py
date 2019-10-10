#!/usr/bin/python
f = open('file.txt', 'r')
ar = f.readlines()
f.close()


def lines(x1,y1,x2,y2,X1,Y1,X2,Y2,name):
	A1 = y1 - y2
	B1 = x2 - x1
	C1 = x1*y2 - x2*y1
	A2 = Y1 - Y2
	B2 = X2 - X1
	C2 = X1*Y2 - X2*Y1
	if B1*A2 - B2*A1 and A1:
  	  yy = (C2*A1 - C1*A2) / (B1*A2 - B2*A1)
  	  xx = (-C1 - B1*yy) / A1
 	  point(xx, yy, name)
	elif B1*A2 - B2*A1 and A2:
  	  yy = (C2*A1 - C1*A2) / (B1*A2 - B2*A1)
  	  xx = (-C2 - B2*yy) / A2
 	  point(xx, yy, name)
	else:
 	   print("lines",name, "||.")


def point(xx, yy, name):
    if min(x1, x2) <= xx <= max(x1, x2):
        print("lines",name, "intersections, resoults ({0:f}, {1:f}).".
              format(xx, yy))
    else:
        print('lines',name,'not intersection ')
 
 
for line in range (len(ar)):
 print(ar[line])
 s = ar[line]
 name = s[:4]
 x1 = int(s[-9:-8])
 y1 = int(s[-8:-7])
 x2 = int(s[-7:-6])
 y2 = int(s[-6:-5])
 X1 = int(s[-5:-4])
 Y1 = int(s[-4:-3])
 X2 = int(s[-3:-2])
 Y2 = int(s[-2:-1])
 lines(x1,y1,x2,y2,X1,Y1,X2,Y2,name)

