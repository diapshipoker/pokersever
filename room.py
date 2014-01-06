#!/usr/bin/python
# -*- coding: utf8 -*-

class room:

    def __init__(self,db):

        self._db = db
        self._id = ''
        self.id = 0
        self.smallblind = 0
        self.bigblind = 0
        self.buysmallchips = 0
        self.buybigchips = 0
        self.nownumber = 0
        self.maxnumber = 0
        self.start = 0
    
    def get_room_limit(self,start,limit):

        try:
            return self._db.room.find().limit(limit).skip(start)
        except IOError as e:
            print e
        else:
            return None
    
    def get_room_one_by_id(self,id):
        
        try:
            return self._db.room.find_one({'id':id})
        except IOError as e:
            print e
        else:
            return None

    def get_room__by_limit_order(self,limit,order):
        
        try:
            return self._db.room.find().sort('id',order).limit(limit);
        except IOError as e:
            print e
        else:
            return None

    def save(self):
    
        try:
           return self._db.room.save({'id':self.id,'smallblind':self.smallblind,
                                      'bigblind':self.bigblind,'buysmallchips':self.buysmallchips,
                                      'buybigchips':self.buybigchips,'maxnumber':self.maxnumber,
                                      'nownumber':self.nownumber,'start':self.start})
        except IOError as e:
           print e
        else:
           return 0

    def update(self):
    
        try:
           return self._db.room.update({'id':self.id},{'$set':{'nownumber':self.nownumber,'start':self.start}})
        except IOError as e:
           print e
        else:
           return 0
