import datetime


class Module:
    def __init__(self, module_id: object, module_name: object, module_code: object) -> object:
        self.module_id = module_id
        self.module_name = module_name
        self.module_code = module_code

# The __str__ method in Python represents the class objects as a string  and it will print all attributes when u print the object (call)
    def __str__(self):
        return "Module Attributes :: " + self.module_id + ", " + self.module_name + ", " +self.module_code

# my_module_1 = Module("123","Maths","MATH-2022")
# my_module_2 = Module("222", "Science", "Sci 234")
# print(my_module_1)
# print(my_module_2)


class Coursework:
    due_date_obj = datetime.datetime.now()

    def __init__(self, coursework_id, coursework_name, module_id, due_date, requirements):
        self.coursework_id = coursework_id
        self.coursework_name = coursework_name
        self.module_id = module_id
        self.due_date = due_date
        self.requirements = requirements


    def __str__(self):
        return "Courseworks :: "  + self.coursework_id + ", " + self.coursework_name + ", " +self.module_id + ", " + self.due_date + ", " + self.requirements

# my_coursework = Coursework("1", "Network Commands ", "123")
# print(my_coursework)


class User:
    def __init__(self, user_id, first_name, last_name):
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return "User details :: "+ self.user_id + ", " + self.first_name + " " +self.last_name


