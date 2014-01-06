#!/usr/bin/python
# -*- coding: utf8 -*-

class roommember:

    def __init__(self,db):

        self._db = db
        self.roomid = 0
        self.uid = 0
        self.joinchips = 0
        self.totalchips = 0
        self.boardnum = 0
        self.wins = 0
        self.maxhand = ''
        self.behavior = ''
 
    def get_table(self,roomid):
        mod = roomid % 10
        def case1():
            return self._db.roommember
        def case2():
            return self._db.roommember1
        def case3():
            return self._db.roommember2
        def case4():
            return self._db.roommember3
        def case5():
            return self._db.roommember4
        def case6():
            return self._db.roommember5
        def case7():
            return self._db.roommember6
        def case8():
            return self._db.roommember7
        def case9():
            return self._db.roommember8
        def case10():
            return self._db.roommember9
        return {0:case1,1:case2,2:case3,3:case4,4:case5,5:case6,6:case7,7:case8,8:case9,9:case10}[mod]()

    def get_roommember_by_roomid_uid(self,roomid,uid):

        try:
            table = self.get_table(roomid)
            return table.find_one({'roomid':roomid,'uid':uid})
        except IOError as e:
            print e
        else:
            return None

    def get_roommember_by_roomid(self,roomid):
        
        try:
            table = self.get_table(roomid)
            return table.find({'roomid':roomid})
        except IOError as e:
            print e
        else:
            return None

    def get_roommember_by_roomid_behavior(self,roomid,behavior):

        try:
            table = self.get_table(roomid)
            return table.find({'roomid':roomid,'behavior':behavior})
        except IOError as e:
            print e
        else:
            return None

    def save(self):

        try:
           table = self.get_table(self.roomid)
           return table.save({'roomid':self.roomid,'uid':self.uid,
                                      'joinchips':self.joinchips,'totalchips':self.totalchips,
                                      'boardnum':self.boardnum,'wins':self.wins,
                                      'maxhand':self.maxhand,'behavior':self.behavior})
        except IOError as e:
           print e
        else:
           return 0

    def update(self):

        try:
           table = self.get_table(self.roomid)
           return table.update({'roomid':self.roomid,'uid':self.uid},
                                             {'$set':{'totalchips':self.totalchips,
                                              'boardnum':self.boardnum,'wins':self.wins,
                                              'maxhand':self.maxhand,'behavior':self.behavior}})
        except IOError as e:
           print e
        else:
           return 0
