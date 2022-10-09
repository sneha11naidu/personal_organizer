import DB_layer

#
db = DB_layer.get_db()
# list_collection_names is a key word to find collections in pymongo
print(db.list_collection_names())

all_modules = DB_layer.get_all_modules()
# will print only object
# print(">>>" + str(all_modules))
# will print str format bec we have overwritten in DomainClasses
for module in all_modules:
    print(module)
# dict_1 = all_modules[0]
# print(dict_1["module_id"])
# print(all_modules[0].get("module_id"))


all_coursework = DB_layer.get_courseworks_in_module("1234")
# will print only object
print(">>>" + str(all_coursework))
# will print str format bec we have overwritten in DomainClasses
for coursework in all_coursework:
    print(coursework)


DB_layer.delete_module("1234")


list_due_date = DB_layer.get_due_dates()
print(">>>>>>>>>>>" + str(list_due_date))

DB_layer.get_courseworks_in_module()