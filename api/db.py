import os
from dotenv import load_dotenv
import pymongo

load_dotenv()

#%%
DATABASE_PORT = os.environ.get('DATABASE_PORT') or 27017
client = pymongo.MongoClient("localhost", int(DATABASE_PORT))

#%%
db = client.myDatabase
