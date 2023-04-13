import pymongo
import certifi
con_str = "mongodb+srv://fsdi:test1234@cluster0.qge8afq.mongodb.net/?retryWrites=true&w=majority"

client = pymongo.MongoClient(con_str, tlsCAFile=certifi.where())
db = client.get_database("onlinestore_ch35")
