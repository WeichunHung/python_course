from pymongo import MongoClient
import certifi

conn_str = "mongodb+srv://WeichunHung:weichun4473@cluster0.b8fsi.mongodb.net/test"

client = MongoClient(conn_str, tlsCAFile=certifi.where())
mydb = client['test']
my_collection = mydb['User']

try:
    # topic_list = [{'name': 'Tom', 'age': 26},{'name': 'Wei', 'age': 27},{'name': 'Henry', 'age': 18}]
    # my_collection.insert_many(topic_list)  #Create

    # for x in my_collection.find(): #Read
    #     print(x)
    # myquery = {'$or':[{'name': 'Tom'},{'name': 'Wei'},{'name': 'Henry'}]}
    # newvalues = {'$set': {'age': '27'}}
    # my_collection.update_many(myquery, newvalues)  #Update
    # my_collection.delete_many({}) #Delete
    my_collection.delete_one({'name':'Henry', 'age': 18}) #Delete
    for x in my_collection.find():
        print(x)


except Exception as e:
    print(e)