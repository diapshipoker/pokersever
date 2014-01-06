import pymongo
from room import *
client = pymongo.MongoClient("192.168.1.236", 27017)
db = client.poker

objroom = room(db)
objroom.id = 2
objroom.smallblind = 2
objroom.bigblind = 4
objroom.buysmallchips = 20
objroom.buybigchips = 40
objroom.maxnumber = 10
objroom.start = 0

#n=objroom.save()
#print n

a=objroom.get_room__by_limit_order(1,pymongo.DESCENDING)
print a[1]
