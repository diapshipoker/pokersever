#!/usr/bin/python
# -*- coding: utf8 -*-
import time

class account:

    def __init__(self,db):

        self._db = db
        self.uid = 0
        self.chipsnum = 0
        self.price = 0
        self.ctype = 0
        self.des = ''
        self.ctime = 0

    def get_table(self,uid):
        mod = uid % 10
        def case1():
            return self._db.account
        def case2():
            return self._db.account1
        def case3():
            return self._db.account2
        def case4():
            return self._db.account3
        def case5():
            return self._db.account4
        def case6():
            return self._db.account5
        def case7():
            return self._db.account6
        def case8():
            return self._db.account7
        def case9():
            return self._db.account8
        def case10():
            return self._db.account9
        return {0:case1,1:case2,2:case3,3:case4,4:case5,5:case6,6:case7,7:case8,8:case9,9:case10}[mod]()

    def get_account_by_uid(self,uid,start,limit):

        try:
            table = self.get_table(uid)
            return table.find({'uid':uid}).limit(limit).skip(start)
        except IOError as e:
            print e
        else:
            return None

    def get_account_by_uid_ctype(self,uid,ctype,start,limit):

        try:
            table = self.get_table(uid)
            return table.find({'uid':uid,'ctype':ctype}).limit(limit).skip(start)
        except IOError as e:
            print e
        else:
            return None

    def save(self):

        try:
            table = self.get_table(self.uid)
            return table.save({'uid':self.uid,'chipsnum':self.chipsnum,'price':self.price,'ctype':self.ctype,'des':self.des,'ctime':time.time()})
        except IOError as e:
            print e
        else:
            return 0
