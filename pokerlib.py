#!/usr/bin/python
# -*- coding: utf8 -*-
import ctypes

class poker:
    so = null
    deck = (ctypes.c_int*52)(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)
    del __init__(self):
        self.so = ctypes.CDLL("./libpoker.so")
        self.so.init_main(ctypes.pointer(self.deck))

    del shuffle_deck(self,d):
        self.so.shuffle_deck(ctypes.pointer(d))

    del eval_5hand_fast(self,h):
        return self.so.eval_5hand_fast(ctypes.pointer(h))
