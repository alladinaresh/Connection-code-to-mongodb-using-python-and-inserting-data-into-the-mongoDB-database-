
from pymongo import MongoClient
import pymongo

def create_database_connection(connection_string):
    try:
        client = MongoClient(connection_string)
        print("Connecting successfully")
        return client
    except Exception as err:
        return err
connection_str = "mongodb://localhost:27017/"
client = create_database_connection(connection_str)

def create_database(client):
    try:
        database = client.get_database("tutorial")
        print("Database Created Successfully")
        return database
    except Exception as Err:
        return Err
    
database = create_database(client)
def inserting_the_collection(db):
    try:
        collection = db["student_details"]
        print("Collection Created Successfully")
        return collection
    except Exception as Err:
        return Err
collection = inserting_the_collection(database)
try:
    # creating an single key
    collection.create_index("name")
    print("Query Executed Successfully")
except Exception as Err:
    print(Err)

# getting index

# creating Multiple indexes
index_field = [("name",1),("age",-1),("gender",1)]
collection.create_index(index_field)
indexes = collection.index_information()
print(indexes)
print(type(indexes))
for index_name,index_details in indexes.items():
    print(f'Index Name: {index_name}')
    print(f"Index details:{index_details}\n")
    
# Multikey Indexing
collection.create_index("hobbies")
indexes = collection.index_information()
print(indexes)
print(type(indexes))
for index_name,index_details in indexes.items():
    print(f'Index Name: {index_name}')
    print(f"Index details:{index_details}\n")


