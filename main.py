from config import DB_URI, TMDB_KEY
from tmdb import TMDB
from pymongo import MongoClient
# DB_URI should be a url to mongodb with ?retryWrites=false
client = MongoClient(DB_URI)


class DataBase:
    def __init__(self, client, db_name):
        self.db = client[db_name]
        print("Initialized database.")

    def add_list(self, list):
        print("Adding a list to database:", list)
        self.db.lists.insert_one(list)


tmdb = TMDB(TMDB_KEY)
tmdb.search_tv('Lucifer')

# TODO:
# When TheMovieDB adds tv-show lists
# Search TV Show -> Get lists -> add tv shows which are in the same list
# That way select the recommended tv show