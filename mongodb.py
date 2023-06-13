from pymongo import MongoClient

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
def inserting_data_into_collection(my_coll):
    try:
        my_coll.insert_many([
            {
            "name":"Jeevr",
            "age":21,
            "gender":"Male",
            "class":"B-tech",
            "department":"Mech",
            "hobbies":["reading books","playing shuttle"]
        },
           {                 
            "name":"Venukumar",
            "age":25,
            "gender":"Male",
            "class":"B-tech",
            "department":"ECE",
            "hobbies":["reading books","playing shuttle"]
            
        },
           {"name":"Suneeth mohan",
            "age":19,
            "gender":"Female",
            "class":"B-tech",
            "department":"CSE",
            "hobbies":["reading books","playing shuttle"]
            
        }
           ,{
            "name":"Karthik3",
            "age":25,
            "gender":"Male",
            "class":"B-tech",
            "department":"CSE",
            "hobbies":["reading books","playing shuttle"]
            
        }])
        print("Query Executed Successfully")
    except Exception as Err:
        print(Err)
inserting_data_into_collection(collection)

def get_student_details(collection):
    try:
        student_details = collection.find()
        print("Data extracted Successfully")
        return student_details
    except Exception as Err:
        print(Err)
student_details = get_student_details(collection)

def get_details_according_to_values(key,value):
    try:
        student_dt = collection.find({key:value})
        print("Get the Details Successfully......")
        return student_dt
    except Exception as Err:
        print(Err)   
result = get_details_according_to_values("age",23)
print(type(result))
for student in result:
    print(student)

#getting_the_value_one
value = collection.find_one("age")
#COUNTING CONCEPTS
#q1:get the no of persons in a collection
try:
    
    count_of_documents = collection.count_documents({})
    print(f'No of documents is {count_of_documents}')
except Exception as Err:
    print(Err)
#q1:get the no of persons in a collection whose age age == some value
def get_the_count_whose_age_22(key,value):
    try:
        count =  collection.count_documents({key:value})
        print("Query_executed Successfully")
        return count
    except Exception as Err:
        return Err 
result = get_the_count_whose_age_22("age",22)
print(f'count is {result}')









