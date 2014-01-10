#!/usr/bin/python
# -*- coding: utf8 -*-

class board:

    def __init__(self,roomid,ctime):
        self.no = 1
        self.roomid = roomid
        self.state = 0
        self.ctime = ctime

    def newboardno(self,ctime):
        self.no += 1
        self.state = 0
        self.ctime = ctime




