from pymongo import MongoClient
import certifi

conn_str = "mongodb+srv://WeichunHung:weichun4473@cluster0.b8fsi.mongodb.net/test"
client = MongoClient(conn_str, tlsCAFile=certifi.where())
mydb = client['test']
my_collection = mydb['Ettoday_SportNews']

try:

    news_list =[]
    my_collection.insert_many(news_list)
    for x in my_collection.find():
        print(x)



except Exception as e:
    print(e)