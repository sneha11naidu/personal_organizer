# importing pymongo library
import datetime

import pymongo
# for security
import certifi
# as domain = u can access by writing domain instead of DomainClasses
import DomainClasses as domain
# pretty print - prints data in a pretty manner
import pprint
# data in mongodb is stored in json documents
import json
import BR_utils

# method to access the Mongodb layer
global module_collection
global coursework_collection
global db
global CONNECTION_STRING
CONNECTION_STRING = "mongodb+srv://snehanaidu:mongodb1234@cluster0.qa2k5fz.mongodb.net/?retryWrites=true&w=majority"
def get_db():
  '''Connecting to the Mongodb(database) using the pymongo library and Mongo Client.
   Testing if the connection was successful
   Accessing a specific Database
   And listing down all the connections in the Database'''
  global db
  # putting the connecting url in a variable
  global CONNECTION_STRING
  # connecting to mongodb
  client = pymongo.MongoClient(CONNECTION_STRING, tlsCAFile=certifi.where())
  # testing the connection
  db = client.test
  # accessing the "PersonalOrganiser" database
  db = client["PersonalOrganiser"]
  # list_collection_names is a key word to find collections in pymongo
  # print(db.list_collection_names())
  return db


# listing all documents from Modules collection
def get_all_modules():
    '''Accessing the module collection from inside the database
    It returns a list of dictionaries
    we convert it to list of objects (obj from Domain classes layer)
    so that we can call it from GUI
    This is object oriented programming '''
    global module_collection
    module_collection = db["Modules"]

# It returns a list of dictionaries
    all_modules = list(module_collection.find({}))
    # print("All modules: " + str(all_modules))
    list_all_modules_objects = []
# module_dict is x here nd as it is modules in dict format we named it
    for module_dict in all_modules:
        # assigning variables nd value to module_dict
        module_id = module_dict["module_id"]    # module_id from classes
        module_name = module_dict["module_name"]
        module_code = module_dict["module_code"]
        module_object = domain.Module(module_id, module_name, module_code)
        list_all_modules_objects.append(module_object)

    print(list_all_modules_objects)
# return causes the function to stop executing and hand a value back to whatever called it.
    return list_all_modules_objects


  # counting number of documents
  # count = module_collection.count_documents({})
  # # finding a specific document
  # pprint.pprint(module_collection.find_one())
  # pprint.pprint(module_collection.find_one({"module_id": "32"}))
  # for loop to print all documents in a particular collection
  # for module in module_collection.find():
  #   pprint.pprint(module)
  #   print("first field:" + str(module["module_id"]))


def get_courseworks_in_module(module_id:str) -> list:
    """Gets and returns the courseworks in a module

        Parameters
        ----------
        module_id : str
            The unique id identifying the module

        Returns
        -------
        list
            list of objects of class Coursework
        """
    global coursework_collection
    coursework_collection = db["Coursework"]
# It returns a list of dictionaries
    myquery = {"module_id": module_id}
    coursework = list(coursework_collection.find(myquery))
    print("All coursework: " + str(coursework))
    list_coursework_objects = []
# coursework_dict is x here nd as it is coursework in dict format we named it
    for coursework_dict in coursework:
        # assigning variables nd value to coursework_dict
        coursework_id = coursework_dict.get("coursework_id")  # coursework_id from classes
        coursework_name = coursework_dict.get("coursework_name")
        module_id = coursework_dict.get("module_id")
        due_date = coursework_dict.get("due_date")
        requirements = coursework_dict.get("requirements")
        coursework_object = domain.Coursework(coursework_id, coursework_name, module_id, due_date, requirements)
        # creating a datetime object from due_date string
        coursework_object.due_date_obj = BR_utils.get_date_obj(str(coursework_object.due_date), '%d/%m/%Y')
        #
        list_coursework_objects.append(coursework_object)

    list_coursework_objects.sort(key=lambda cw: cw.due_date_obj)
    # for coursework in list_coursework_objects:
    #     due_date = coursework.due_date
    #     due_date_datetime_obj = BR_utils.get_date_obj(due_date, '%d/%m/%Y')
    #     print("***************" + str(due_date_datetime_obj))
    #     list_coursework_objects.sort(key=lambda x: x.due_date_obj)

    print(list_coursework_objects)
    return list_coursework_objects


def add_module(module: domain.Module):
    print("Method to add a module:: " + str(module))
    module_collection.insert_one({"module_id": module.module_id,
                                  "module_name": module.module_name, "module_code": module.module_code})
    print("Module inserted into DB successfully")


def add_coursework(coursework: domain.Coursework):
    print("Method to add a coursework:: " + str(coursework))
    coursework_collection.insert_one({"coursework_id": coursework.coursework_id,
                                      "coursework_name": coursework.coursework_name,
                                      "module_id": coursework.module_id,
                                      "due_date": coursework.due_date,
                                      "requirements": coursework.requirements})
    print("Coursework inserted into DB successfully")


def delete_module(module_id:str):
    myquery = {"module_id": module_id}
    module_collection.delete_one(myquery)
    print("Module deleted successfully::" + str(module_id))


def delete_coursework(coursework_id:str):
    myquery = {"coursework_id": coursework_id}
    coursework_collection.delete_one(myquery)
    print("Coursework deleted successfully::" + str(coursework_id))


def edit_module(module: domain.Module):
    print("Method to Edit a module:: " + str(module))
    myquery = {"module_id": module.module_id}

    new_values = { "$set": {"module_id": module.module_id,
               "module_name": module.module_name,
               "module_code": module.module_code}
                }
    module_collection.update_one(myquery, new_values)
    print("Module saved successfully")


def edit_coursework(coursework: domain.Coursework):
    print("Method to Edit a coursework:: " + str(coursework))
    myquery = {"coursework_id": coursework.coursework_id}

    new_values = {"$set": {"coursework_id": coursework.coursework_id,
                           "coursework_name": coursework.coursework_name,
                           "module_id": coursework.module_id,
                           "due_date": coursework.due_date,
                           "requirements": coursework.requirements}
                  }
    coursework_collection.update_one(myquery, new_values)
    print("Coursework saved successfully")


def get_due_dates():
    due_date_collection = db["Coursework"]

    for due_date in due_date_collection.find({"due_date":0}):
        print(due_date)







