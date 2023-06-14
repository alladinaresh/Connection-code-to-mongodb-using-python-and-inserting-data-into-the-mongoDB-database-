from pymongo import MongoClient
from faker import Faker
import time
#Importing Faker for creating fake data
faker = Faker()
connection_string = "mongodb://localhost:27017"

#Making connection between mongodb with python
def create_connection_and_return_client(connection_string):
    try:
        client = MongoClient(connection_string)
        print("Connecting Successfully...")
        return client
    except Exception as Err:
        return Err
client = create_connection_and_return_client(connection_string)

#Creating a database
def creating_database(client):
    try:
        database = client["apple_database"]
        print("Database created Successfully....")
        return database
    except Exception as Err:
        return Err
database = creating_database(client)

#Creating a collection in a database
def creating_collection(database):
    try:
        collection = database.create_collection("workers_details")
        print("Collection created successfully......")
        return collection
    except Exception as Err:
        return Err
collection = creating_collection(database)

#Inserting data(documents) into the collection
def inserting_data_in_database():
# Generate and insert the data
    try:
        for i in range(1, 100002):
            name = faker.name()
            first_name = faker.first_name()
            last_name = faker.last_name()
            address = faker.address()
            email = faker.email()
            phone_number = faker.phone_number()
            sentence = faker.sentence()

            data = {
                'name': name,
                'first_name': first_name,
                'last_name': last_name,
                'address': address,
                'email': email,
                'phone_number': phone_number,
                'sentence': sentence,
            }
            collection.insert_one(data)
            if i % 10000 == 0:
                print(f"Inserted {i} records.")
    except Exception as Err:
        print(f"Error is {Err}")
inserting_data_in_database()

#Creating indexing to a texted field and searching some data
def creating_indexing_and_searching_data(collection):
    try:
        collection.create_index([("sentence","text")])
        print("Indexing Created Successfully")
        value = collection.find({"$text":{"$search":"\"doctor political\"","$caseSensitive":True}})
        for i in value:
            print(i)
    except Exception as Err:
        print(Err)
creating_indexing_and_searching_data(collection)

#compound indexing(Before)
def data_search():
    try:
        value = collection.find({"name":{'$eq':'Christoper'}})
        for i in value:
            print(i)
    except Exception as Err:
        print(Err)
start_time = time.time()
data_search()
overall_time = time.time() - start_time
print(f' Before Indexing Execution Time is: {overall_time} seconds')

# After
def creating_text_index(collection):
    try:
        collection.create_index({"name":1,"email":1})
        print("Index Created Successfully")
    except Exception as Err:
        print(Err)
creating_collection(collection)
def data_search_after_indexing():
    try:
        value = collection.find({"name":{'$eq':'Christoper'}})
        for i in value:
            print(i)
    except Exception as Err:
        print(Err)
start_time = time.time()
data_search_after_indexing()
overall_time = time.time() - start_time
print(f' After Indexing Execution Time is: {overall_time} seconds')
client.close()
