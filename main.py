import ctypes
import os
import time
from pokerlib import *
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
print "=================%d\n" % a0[0]
#boardname=(ctypes.c_char*2)('0','0');
boardname=(ctypes.c_int*2)(0,0)
so.hand_brandname(a0[0],ctypes.pointer(boardname))
print  "%d==%d\n" % (boardname[0],boardname[1])
hh=[0,0]
hh[0]=boardname[0]
hh[1]=boardname[1]
print  "%d==%d\n" % (hh[0],hh[1])
qq=so.find_card(ctypes.c_int(boardname[1]),ctypes.c_int(boardname[0]),c)
if a0[0] == c[qq]:
  print "true"
else:
  print "false"
  time.sleep(10)








poker = pokerlib()
phand1 = (ctypes.c_int*7)(0,0,0,0,0,0,0)
phand2 = (ctypes.c_int*7)(0,0,0,0,0,0,0)
rhand1=[]
rhand2=[]
phand1[0] = poker.deck[0]
phand1[1] = poker.deck[1]
phand1[2] = poker.deck[2]
phand1[3] = poker.deck[3]
phand1[4] = poker.deck[4]
phand2[0] = poker.deck[5]
phand2[1] = poker.deck[6]
phand2[2] = poker.deck[7]
phand2[3] = poker.deck[8]
phand2[4] = poker.deck[9]
val = poker.eval_5hand_fast(phand1)
cardn = poker.hand_rank(val)
rhand1.append(cardn)
rhand1.append(val)
rhand1.append(1)
val = poker.eval_5hand_fast(phand2)
cardn = poker.hand_rank(val)
rhand2.append(cardn)
rhand2.append(val)
rhand2.append(2)
arank =[]
arank.append(rhand1)
arank.append(rhand2)
print arank
print "=======%d----%d---%d\n" % (poker.deck[0],val,cardn)
mrank=poker.cmp_hand_size(arank)
print mrank
