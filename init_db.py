from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient('localhost', 27017)
db = client.dbsparta

db.screw.drop()
doc = {
        'content': "Study Python",
        'start': "06/03/2021",
        'finish': '06/06/2021',
        'comment': 'Quick!',
        'url': '',
        'remind': 'X',
        'done': False,
        'group': 1,
        'tododone': ""
    }

db.screw.insert_one(doc)

doc = {
        'content': "Study JS",
        'start': "06/10/2021",
        'finish': '06/20/2021',
        'comment': 'JSSSSSS!',
        'url': '',
        'remind': 'X',
        'done': False,
        'group': 1,
        'tododone': ""
    }

db.screw.insert_one(doc)

doc = {
        'content': "Study Java",
        'start': "06/30/2021",
        'finish': '07/10/2021',
        'comment': 'JAVAAAA!',
        'url': '',
        'remind': 'X',
        'done': True,
        'group': 1,
        'tododone': ""

    }

db.screw.insert_one(doc)

doc = {
        'content': "Make Project",
        'start': "06/02/2021",
        'finish': '06/05/2021',
        'comment': 'PROJECT!!!!!',
        'url': '',
        'remind': 'X',
        'done': False,
        'group': 2,
        'tododone': ""
    }

db.screw.insert_one(doc)

doc = {
        'content': "Make Project",
        'start': "06/10/2021",
        'finish': '06/20/2021',
        'comment': 'PROJECT!!!!!',
        'url': '',
        'remind': 'X',
        'done': False,
        'group': 2,
        'tododone': ""
    }

db.screw.insert_one(doc)

doc = {
        'content': "Make Project",
        'start': "06/10/2021",
        'finish': '06/20/2021',
        'comment': '3 PROJECT!!!!!',
        'url': '',
        'remind': 'X',
        'done': False,
        'group': 3,
        'tododone': ""
    }

db.screw.insert_one(doc)

doc = {
        'content': "Make Project",
        'start': "06/10/2021",
        'finish': '06/20/2021',
        'comment': '4 PROJECT!!!!!',
        'url': '',
        'remind': 'X',
        'done': False,
        'group': 4,
        'tododone': ""
    }

db.screw.insert_one(doc)
