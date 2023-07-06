from tkinter import *
from tkinter import ttk
from tkinter.ttk import Style

import DB_layer
from functools import partial
import DomainClasses as domain

global delete_btn
global module_id


def show_due_date_event_handler():
    clear_main_page()

    ttk.Label(frame, text="~~ Due Dates of Coursework ~~").grid(column=2, row=1)

    # all_due_dates_list = DB_layer.








def edit_coursework_event_handler(coursework_id, coursework_name, due_date, requirements):
    print(str(coursework_id) + "::" + str(coursework_name) + "::" + str(due_date) + "::" + str(requirements))
    # construct a module object and pass it to the DB_Layer to add to MongoDB
    # module_id is available at global level
    coursework_temp = domain.Coursework(str(coursework_id),
                                        str(coursework_name),
                                        str(module_id),
                                        str(due_date),
                                        str(requirements))
    DB_layer.edit_coursework(coursework_temp)
    # Go back to the all modules page
    all_coursework_event_handler(module_id)


def show_edit_coursework_event_handler(coursework_id, coursework_name, due_date, requirements):
    clear_main_page()

    ttk.Label(frame, text="~~ Edit Coursework ~~").grid(column=2, row=1)

    ttk.Label(frame, text="COURSEWORK ID:").grid(column=0, row=2)
    coursework_id_entry = ttk.Entry(frame)
    coursework_id_entry.insert(0, coursework_id)
    coursework_id_entry.grid(column=2, row=2)

    ttk.Label(frame, text="COURSEWORK NAME:").grid(column=0, row=3)
    coursework_name_entry = ttk.Entry(frame)
    coursework_name_entry.insert(0, coursework_name)
    coursework_name_entry.grid(column=2, row=3)

    ttk.Label(frame, text="DUE DATE:").grid(column=0, row=4)
    due_date_entry = ttk.Entry(frame)
    due_date_entry.insert(0, due_date)
    due_date_entry.grid(column=2, row=4)

    ttk.Label(frame, text="REQUIREMENTS:").grid(column=0, row=5)
    requirements_entry = ttk.Entry(frame)
    requirements_entry.insert(0, requirements)
    requirements_entry.grid(column=2, row=5)

    button = ttk.Button(frame, text="Save Coursework",
                        command=lambda: edit_coursework_event_handler(coursework_id_entry.get(),
                                                                     coursework_name_entry.get(),
                                                                     due_date_entry.get(),
                                                                     requirements_entry.get()))
    button.grid(column=2, row=7)


def edit_module_event_handler(module_id, module_name, module_code):
    print(str(module_id) + "::" + str(module_name) + "::" + str(module_code))
    # construct a module object and pass it to the DB_Layer to add to MongoDB
    module_temp = domain.Module(str(module_id), str(module_name), str(module_code))
    DB_layer.edit_module(module_temp)
    # Go back to the all modules page
    all_modules_event_handler()


def show_edit_module_event_handler(module_id, module_name, module_code):
    clear_main_page()

    ttk.Label(frame, text="~~ Edit a Module ~~").grid(column=2, row=1)

    ttk.Label(frame, text="MODULE ID:").grid(column=0, row=2)
    module_id_entry = ttk.Entry(frame)
    module_id_entry.insert(0, module_id)
    module_id_entry.grid(column=2, row=2)

    ttk.Label(frame, text="MODULE NAME:").grid(column=0, row=3)
    module_name_entry = ttk.Entry(frame)
    module_name_entry.insert(0,module_name)
    module_name_entry.grid(column=2, row=3)

    ttk.Label(frame, text="MODULE CODE:").grid(column=0, row=4)
    module_code_entry = ttk.Entry(frame)
    module_code_entry.insert(0, module_code)
    module_code_entry.grid(column=2, row=4)

    ttk.Button(frame, text="Save Module",
               command=lambda: edit_module_event_handler
               (module_id_entry.get(),
                module_name_entry.get(),
                module_code_entry.get())).grid(column=2, row=5)


def delete_coursework_event_handler(coursework_id):
    print()
    # call DBLayer to delete the coursework
    DB_layer.delete_coursework(coursework_id)
    all_coursework_event_handler(module_id)


def delete_module_event_handler(module_id):
    print()
    # call DBLayer to delete the module
    DB_layer.delete_module(module_id)
    all_modules_event_handler()


def add_coursework_event_handler(coursework_id, coursework_name, due_date, requirements):
    print(str(coursework_id) + "::" + str(coursework_name) + "::" + str(due_date)
          + str(requirements) + "::" + str(module_id))
    # construct a coursework object and pass it to the DB_Layer to add to MongoDB
    coursework_temp = domain.Coursework(
        str(coursework_id), str(coursework_name), str(module_id), str(due_date), str(requirements))
    DB_layer.add_coursework(coursework_temp)
    all_coursework_event_handler(module_id)


def show_add_coursework_event_handler():
    clear_main_page()

    ttk.Label(frame, text="~~ Add a new Coursework ~~").grid(column=2, row=1)

    ttk.Label(frame, text="COURSEWORK ID:").grid(column=0, row=2)
    coursework_id_entry = ttk.Entry(frame)
    coursework_id_entry.grid(column=2, row=2)

    ttk.Label(frame, text="COURSEWORK NAME:").grid(column=0, row=3)
    coursework_name_entry = ttk.Entry(frame)
    coursework_name_entry.grid(column=2, row=3)

    ttk.Label(frame, text="DUE DATE:").grid(column=0, row=4)
    due_date_entry = ttk.Entry(frame)
    due_date_entry.grid(column=2, row=4)

    ttk.Label(frame, text="REQUIREMENTS:").grid(column=0, row=5)
    requirements_entry = ttk.Entry(frame)
    requirements_entry.grid(column=2, row=5)

    button = ttk.Button(frame, text="Add New Coursework",
               command=lambda:add_coursework_event_handler(coursework_id_entry.get(),
                                                            coursework_name_entry.get(),
                                                            due_date_entry.get(),
                                                            requirements_entry.get()))
    button.grid(column=2, row=7)


def all_coursework_event_handler(module_id_param):

    # make the module_id variable global so that it can be used in the coursework methods.
    global module_id

    module_id = module_id_param

    clear_main_page()

    ttk.Button(frame, text="HOME", command=all_modules_event_handler).grid(column=70, row=1)

    ttk.Label(frame, text="**Courseworks**").grid(column=0, row=2)
    ttk.Label(frame, text="**Due-date**").grid(column=20, row=2)
    ttk.Label(frame, text="**Requirements**").grid(column=40, row=2)


    all_coursework_list = DB_layer.get_courseworks_in_module(module_id)
    counter1 = 5
    for coursework in all_coursework_list:
        counter1 = counter1+1
        ttk.Label(frame, text=coursework.coursework_name).grid(column=0, row=counter1)
        ttk.Label(frame, text=coursework.due_date).grid(column=20, row=counter1)
        ttk.Label(frame, text=coursework.requirements).grid(column=40, row=counter1)

        ttk.Button(frame, text="edit", command=partial(show_edit_coursework_event_handler,
                                                       coursework.coursework_id,
                                                       coursework.coursework_name,
                                                       coursework.due_date,
                                                       coursework.requirements)).grid(column=60, row=counter1)
        ttk.Button(frame, text="delete", command=partial(delete_coursework_event_handler,
                                                         coursework.coursework_id))\
            .grid(column=70, row=counter1)


    ttk.Button(frame, text="Add New Coursework", command=show_add_coursework_event_handler)\
        .grid(column=40, row=1)


def add_module_event_handler(module_id, module_name, module_code):
    print(str(module_id) + "::" + str(module_name) + "::" + str(module_code))
    # construct a module object and pass it to the DB_Layer to add to MongoDB
    module_temp = domain.Module(str(module_id), str(module_name), str(module_code))
    DB_layer.add_module(module_temp)
    all_modules_event_handler()


def show_add_module_event_handler():
    clear_main_page()

    ttk.Label(frame, text="~~ Add a new Module ~~").grid(column=2, row=1)

    ttk.Label(frame, text="MODULE ID:").grid(column=0, row=2)
    module_id_entry = ttk.Entry(frame)
    module_id_entry.grid(column=2, row=2)

    ttk.Label(frame, text="MODULE NAME:").grid(column=0, row=3)
    module_name_entry = ttk.Entry(frame)
    module_name_entry.grid(column=2, row=3)

    ttk.Label(frame, text="MODULE CODE:").grid(column=0, row=4)
    module_code_entry = ttk.Entry(frame)
    module_code_entry.grid(column=2, row=4)

    ttk.Button(frame, text="Add New Module",
               command= lambda: add_module_event_handler
               (module_id_entry.get(), module_name_entry.get(), module_code_entry.get())).grid(column=2, row=5)


def popupmsg(msg):
    popup = Tk()
    popup.wm_title("message box")
    label = ttk.Label(popup, text=msg)
    label.pack(side="top", fill="x", pady=10)
    B1 = ttk.Button(popup, text="Okay", command = popup.destroy)
    B1.pack()
    popup.mainloop()


# event handler for Modules button
def all_modules_event_handler():
    clear_main_page()
    ttk.Label(frame, text="List of Modules").grid(column=0, row=2)
    # add a button to "insert new modules"
    ttk.Button(frame, text="Add New Module",
               command=show_add_module_event_handler).grid(column=3, row=3)
    ttk.Button(frame, text="Due date of Courseworks",
               command=show_due_date_event_handler).grid(column=6, row=4)

    try:
        all_modules_list = DB_layer.get_all_modules()
        counter = 4
        for module in all_modules_list:
            counter = counter+1
            ttk.Button(frame, text=module.module_name,
                       command=partial(all_coursework_event_handler, module.module_id)).grid(column=0, row=counter,
                                                                                             sticky=W)
            ttk.Button(frame, text="edit", command=partial(show_edit_module_event_handler,
                                                           module.module_id,
                                                           module.module_name,
                                                           module.module_code)).grid(column=2, row=counter)
            ttk.Button(frame, text="delete", command=partial(delete_module_event_handler,
                                                             module.module_id)).grid(column=3, row=counter)

    except Exception as e:
        print("Could not connect to DataBase" + str(e))
        popupmsg("Could not connect to DB" + str(e))


    # finally:


# partial(save_selected_option, ans_option_1_tuple

# clears all widgets in the root page


def clear_main_page():
    for widgets in root.winfo_children():
        widgets.destroy()
    # A rectangular frame in Tk lets you organize and group widgets
    global frame
    frame = ttk.Frame(root, padding=10)
    # # The grid() geometry manager organises widgets in a table-like structure in the parent widget.
    frame.grid()


def start_gui():
    global root, frame


    # starts the GUI
    # It also creates a toplevel window, known as the root window, which serves as the main window of the application.
    root = Tk()
    # set the title
    root.title('personal Student Organizer')
    # A rectangular frame in Tk lets you organize and group widgets
    frame = ttk.Frame(root, padding=10)
    # # The grid() geometry manager organises widgets in a table-like structure in the parent widget.
    frame.grid()

    # configure button style...this may work on windows, but not on mac.
    button_style = Style()
    button_style.configure('W.TButton', background='blue', foreground='black', font=('Arial', 14))

    ttk.Label(frame, text="Personal Organiser!").grid(column=0, row=0)
    ttk.Label(frame, text="Student!").grid(column=6, row=5)
    ttk.Label(frame, text="Teacher").grid(column=10, row=9)
    ttk.Button(frame, text="Modules", style='W.TButton', command=all_modules_event_handler).grid(column=1, row=0)

    # connect to mongodb and get the database cursor
    DB_layer.get_db()
    root.mainloop()



    # bhajipala
    # panipuri



# for merging



start_gui()
