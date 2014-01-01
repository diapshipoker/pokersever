import ctypes
import os
import time
so = ctypes.CDLL("./libpoker.so")
values_rank=['','Straight Flush','Four of a Kind','Full House','Flush','Straight','Three of a Kind','Two Pair','One Pair','High Card']
c=(ctypes.c_int*52)(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)
#b=so.entest(ctypes.pointer(c));
so.init_main(ctypes.pointer(c))
print c[0]
so.shuffle_deck(ctypes.pointer(c))
print len(c)
a0=(ctypes.c_int*5)(0,0,0,0,0)
a1=(ctypes.c_int*2)(0,0)
a2=(ctypes.c_int*2)(0,0)
a3=(ctypes.c_int*2)(0,0)
a4=(ctypes.c_int*2)(0,0)
a5=(ctypes.c_int*2)(0,0)
n=0
k=0
def handa(m):
  def case1():
    return a0
  def case2():
    return a1
  def case3():
    return a2
  def case4():
    return a3
  def case5():
    return a4
  def case6():
    return a5
  return {0:case1,1:case2,2:case3,3:case4,4:case5,5:case6}[m]()

for i in range(12):
  if i % 2 == 0:
    handa(k)[n] = c[i]
    n = n+1
  else:
    handa(k)[n] = c[i]
    n = 0
    k = k+1
a0[2]=c[12]
a0[3]=c[13]
a0[4]=c[14]

h = so.eval_5hand(ctypes.pointer(a0))
v = so.hand_rank(h)
print values_rank[v]
