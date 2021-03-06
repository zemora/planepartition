from piscript.PiModule import *
from math import *

init(500, 200)
center()
scale(100)

setlinewidth(2.5)

L = 0.6
ca = cos(pi/6)
sa = sin(pi/6)


gsave()
translate(-1.5, -0.2)
newpath()
moveto(0, 0)
lineto(0, 1)
stroke(1, 0, 0)

newpath()
moveto(0, 0)
lineto(-ca, -sa)
stroke(1, 0, 0)

newpath()
moveto(0, 0)
lineto(ca, -sa)
stroke(1, 0, 0)

newpath()
circle(0, 0, 0.05)
fill(1)
setlinewidth(1)
stroke(0, 0, 1)
grestore()


setarrowdims(0.04, 0.2)
newpath()
arrow((-0.5, 0), (0.5, 0))
stroke()

gsave()
translate(1.5, -0.2)

newpath()
moveto(0, 1)
lineto(0, 1-L)
stroke(1, 0, 0)

newpath()
moveto((1-L)*ca, -(1-L)*sa)
lineto(ca, -sa)
stroke(1, 0, 0)

newpath()
moveto(-(1-L)*ca, -(1-L)*sa)
lineto(-ca, -sa)
stroke(1, 0, 0)

gsave()
newpath()
moveto(0, 1-L)
lineto(-(1-L)*ca, -(1-L)*sa)
lineto((1-L)*ca, -(1-L)*sa)
closepath()
setlinewidth(1)
setdash([4, 4], 0)
stroke(0.5)
grestore()

setlinewidth(1)
newpath()
circle(0, 1-L, 0.03)
fill(1)
stroke(0, 0, 1)
newpath()
circle(-(1-L)*ca, -(1-L)*sa, 0.03)
fill(1)
stroke(0, 0, 1)
newpath()
circle((1-L)*ca, -(1-L)*sa, 0.03)
fill(1)
stroke(0, 0, 1)
grestore()
finish()
