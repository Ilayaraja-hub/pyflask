#from flask import Flask
from flask_pymongo import pymongo
from bson.objectid import ObjectId
import app
#from app import app


def connection():

    CONNECTION_STRING = "mongodb+srv://ibharathidasan:sRrL4Erwc8ypEK1q@contract-prediction.bagbs.mongodb.net/?retryWrites=true&w=majority"

    client = pymongo.MongoClient(CONNECTION_STRING)
    db = client.get_database('pymongo')
    collection_table = db["collection"]
    return collection_table


def list_all():
    files_obj = connection().find()
    files = [i for i in files_obj]
    return files
    print(files)


def find_one(id):
    return(connection().find_one(ObjectId(id)))


def insert_one(query):
    return connection().insert_one(query)
    print("Inserted in DB successfully")


def update_one(id, query):
    connection().update_one({'_id': ObjectId(id)}, query)
    print("updated in DB successfully")


def delete_all():
    x = connection().delete_many({})
    print(x.deleted_count, " documents deleted.")

# delete_all()
# print("111111111111111")
# id_=insert_one({"name":"test","queue":"Scan","status":"On Queue","doc_type":"Lease Agreement"}).inserted_id
# print("222222222222222")
# print(id_)
# update_one('62f0e856fd942baebe1f383a',{"$set": {'queue':'Validation2','status':'Ready'}})
# print("updated_test")
