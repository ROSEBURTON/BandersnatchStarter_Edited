from dotenv import load_dotenv  # To load stored monsters in MongoDB
from MonsterLab import Monster  # has dictionary of monsters and their qualities
from pandas import DataFrame  # we transform monsters to a dataframe and from that convert to table
from pymongo import MongoClient  # we pass in argument os.getenv here to start connecting to Mongo
import os  # using operating system for access to database using getenv


#  code reformatting with
class Database:  # in main.py we say from app.data import Database names case-sensitive
    def __init__(self):
        load_dotenv()
        client = MongoClient(os.getenv("DB_URL"))
        db = client["Central_Database"]
        self.collection = db["This_Space_Collective"]  # collection name comes from MongoDB

    def seed(self, amount=1000):  # populate a min of 1,000 monsters
        for _ in range(amount):  # for each in range of (cyan number)
            monster = Monster().to_dict()
            self.collection.insert_one(monster)

    def reset(self, amount=1000):
        for _ in range(amount):
            #  deletes all documents from the collection
            self.collection.delete_many({})  # .collection.delete_many({}) term for Mongo

    def count(self) -> int:
        return self.collection.count_documents({})  # collection.count_documents({} term for Mongo

    def dataframe(self) -> DataFrame:
        cursor = self.collection.find({}, {"_id": 0})  # .collection.find({} term for Mongo
        df = DataFrame(cursor)
        return df

    def html_table(self) -> str:  # html needed because of Flask application online
        df = self.dataframe()
        table = df.to_html(index=True)  # converts pandas dataframe for website
        return table


if __name__ == '__main__':
    db = Database()
    # db.reset()  # resets seeded number
    db.seed(1000)
    print(db.count())
    print(list(db.collection.find({}, {"_id": 0})))
    # print(list(db.collection.find({"Type": "Dragon"}, {"_id": 0, "Sanity": 45.22})))
