from pymongo import MongoClient
import certifi

conn_str = "mongodb+srv://WeichunHung:weichun4473@cluster0.b8fsi.mongodb.net/test"

client = MongoClient(conn_str, tlsCAFile=certifi.where())
mydb = client['test']
my_collection = mydb['Ettoday_SportNews']

try:
    news_list = [{'Title': '陳俊秀林泓育快醒了\u3000曾總：不會輕易調動棒次', 'Date': '\r\n                        2022年04月26日 18:38                    ', 'Link': 'https://sports.ettoday.net/news/2238375'},
{'Title': '蔣智賢、岳少華下二軍引熱議\u3000丘總解釋原因', 'Date': '\r\n                        2022年04月26日 16:02                    ', 'Link': 'https://sports.ettoday.net/news/2238169'},
{'Title': '美國網球女將退役後轉當成人影音網紅\u3000超辣身材引網友暴動', 'Date': '\r\n                        2022年04月26日 07:46                    ', 'Link': 'https://sports.ettoday.net/news/2237741'},
{'Title': '富邦大規模異動\u3000蔣智賢、陽耀勳、王勝偉等5人下二軍', 'Date': '\r\n                        2022年04月25日 17:48                    ', 'Link': 'https://sports.ettoday.net/news/2237585'},
{'Title': '鵜鶘逼平太陽！威廉森賽前輕鬆扣籃\u3000美媒：如果他回歸', 'Date': '\r\n                        2022年04月26日 00:25                    ', 'Link': 'https://sports.ettoday.net/news/2237693'},
{'Title': '悍將終於拉新人！王苡丞、董子恩、莊韋恩上一軍立刻先發', 'Date': '\r\n                        2022年04月26日 15:52                    ', 'Link': 'https://sports.ettoday.net/news/2238071'},
{'Title': '味全龍挑戰4連勝交手統一獅\u3000郭郁政強碰胡智為', 'Date': '\r\n                        2022年04月26日 00:32                    ', 'Link': 'https://sports.ettoday.net/news/2237697'},
{'Title': '攻城獅「復古之夜」\u3000M＆N球衣高國豪實著演繹', 'Date': '\r\n                        2022年04月26日 00:35                    ', 'Link': 'https://sports.ettoday.net/news/2237654'},
{'Title': 'T1職籃「消失的兩分」爭議\u3000聯盟承認疏失將懲處', 'Date': '\r\n                        2022年04月25日 16:59                    ', 'Link': 'https://sports.ettoday.net/news/2237545'},
{'Title': '主控悍將陳堅恩驚傳退役\u3000攻城獅29日辦引退儀式', 'Date': '\r\n                        2022年04月25日 16:39                    ', 'Link': 'https://sports.ettoday.net/news/2237501'}]

    my_collection.insert_many(news_list)
    for x in my_collection.find():
        print(x)



except Exception as e:
    print(e)