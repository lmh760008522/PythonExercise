import pymongo

#创建数据库（使用MongoClient 对象，并且指定连接的 URL 地址和要创建的数据库名）
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["runoobdb"]

#创建集合
mycol = mydb["sites"]

#插入文档
mydict = { "name": "RUNOOB", "alexa": "10000", "url": "https://www.runoob.com" }
x = mycol.insert_one(mydict)

#判断数据库是否存在
dblist = myclient.list_database_names()
if "runoobdb" in dblist:
	print("ok")
else:
	print("not ok")

#插入多个文档
mylist = [
  { "name": "Taobao", "alexa": "100", "url": "https://www.taobao.com" },
  { "name": "QQ", "alexa": "101", "url": "https://www.qq.com" },
  { "name": "Facebook", "alexa": "10", "url": "https://www.facebook.com" },
  { "name": "知乎", "alexa": "103", "url": "https://www.zhihu.com" },
  { "name": "Github", "alexa": "109", "url": "https://www.github.com" }
]
x = mycol.insert_many(mylist)

#查询di一条数据
x = mycol.find_one()

#数据排序
mydoc = mycol.find().sort("alexa",-1)

#查询所有数据
for x in mycol.find():
	print(x)
#查询指定字段
myquery = {"name":"QQ"}
for x in mycol.find(myquery):
	print(x)

#删除文档
mycol.delete_one(myquery)

#删除所有文档
x = mycol.delete_many({})
#print(x.delete_count(),"个文档已删除")
#删除集合
mycol.drop()