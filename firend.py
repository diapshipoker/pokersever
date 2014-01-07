#!/usr/bin/python
# -*- coding: utf8 -*-

class firend:

    def __init__(self,db):
    
        self._db = db
        self._id = ''
        self.friendid = 0
        self.uid = 0

    def get_table(self,uid):
        mod = uid % 10
        def case1():
            return self._db.firend
        def case2():
            return self._db.firend1
        def case3():
            return self._db.firend2
        def case4():
            return self._db.firend3
        def case5():
            return self._db.firend4
        def case6():
            return self._db.firend5
        def case7():
            return self._db.firend6
        def case8():
            return self._db.firend7
        def case9():
            return self._db.firend8
        def case10():
            return self._db.firend9
        return {0:case1,1:case2,2:case3,3:case4,4:case5,5:case6,6:case7,7:case8,8:case9,9:case10}[mod]()

    def get_firend_by_uid(self,uid,start,limit):

        try:
            table = self.get_table(uid)
            return table.find({'uid':uid}).limit(limit).skip(start)
        except IOError as e:
            print e
        else:
            return None

    def save(self):

        try:
            table = self.get_table(self.uid)
            return table.save({'friendid':self.friendid,'uid':self.uid})
        except IOError as e:
            print e
        else:
            return 0

    def remove(self,uid,friend):

        try:
           table = self.get_table(uid)
           return table.remove({'friendid':friendid,'uid':uid})
        except IOError as e: 
            print e
        else:
            return 0
