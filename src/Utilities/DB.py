from pymongo import MongoClient


def my_collection(Pass):

    User = 'DisJoin'
 

    URL = 'mongodb+srv://'+User +':'+  Pass + '@cluster0.eowpu.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'
          #'mongodb+srv://<username>:<password>@cluster0.eowpu.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'
    try:
        conn = MongoClient(URL)
    except:
        return -1

    mydb = conn['DisJoin_data']
    mycol = mydb["Current_data"]

    mycol.delete_many({})

    return mycol
