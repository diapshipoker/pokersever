#!/usr/bin/python
# -*- coding: utf8 -*-
import ctypes

class pokerlib:
    def __init__(self):
        self.so = ctypes.CDLL("./libpoker.so")
        self.deck = (ctypes.c_int*52)(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)
        self.so.init_main(ctypes.pointer(self.deck))

    def shuffle_deck(self,d):
        self.so.shuffle_deck(ctypes.pointer(d))

    def eval_5hand_fast(self,h):
        return self.so.eval_5hand_fast(ctypes.pointer(h))

    def eval_6hand_fast(self,h):
        return self.so.eval_6hand_fast(ctypes.pointer(h))

    def eval_7hand_fast(self,h):
        return self.so.eval_7hand_fast(ctypes.pointer(h))

    def hand_rank(self,v):
        return self.so.hand_rank(ctypes.c_short(v))

    def eval_brandname(self,h):
        n=(ctypes.c_int*2)(0,0)
        self.so.hand_brandname(ctypes.c_int(h),ctypes.pointer(n))
        return (n[1],n[0])

    def find_card_value(self,r,s):
        i=self.so.find_card(ctypes.c_int(r),ctypes.c_int(s),self.deck)
        return self.deck[i]
             
    def cmp_hand_size(self,vlist):
        iterlen = len(vlist)
        smalllest = vlist[0]
        a = []
        n = 0
        for i in range(1,iterlen):
            if vlist[i][0] < smallest[0]:
                smallest = vlist[i]
        for j in range(0,iterlen):
            if vlist[j][0] == smallest[0]:
                a[n]=vlist[j][0]
                n = n + 1
        if len(a) > 1:
            a=self.cmp_hand_valsize(a)
    
        return a

    def cmp_hand_valsize(self,a):
        iterlen = len(a)
        smallest = a[0]
        b = []
        n = 0
        for i in range(1,iterlen):
            if a[i][1] < smallest[1]:
                smallest = a[i]
        for j in range(0,iterlen):
            if a[j][1] == smallest[1]:
                b[n]=a[j][1]
                n = n + 1

        return b
