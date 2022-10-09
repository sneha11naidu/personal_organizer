import datetime


def get_date_obj_old(date_str:str) -> datetime:
    # date_str = "17-05-2022"
    y = date_str.split("-")
    print(y)
    x = datetime.datetime(int(y[2]), int(y[1]), int(y[0]))
    # print(x)
    # return x

def get_date_obj(date_str:str, date_format:str) -> datetime:
    date_time_obj = datetime.datetime.strptime(date_str, date_format)
    print(date_time_obj)
    return date_time_obj

# takes a list of  string datetimes nd converts into list of datetime objects
def get_datetime_obj_list(list_datetime:list, date_format:str) -> list:
    list_of_datetime_obj = []
    for x in list_datetime:
        datetime_obj = get_date_obj(str(x), date_format)
        list_of_datetime_obj.append(datetime_obj)
    print(list_of_datetime_obj)
    return list_of_datetime_obj


def sort_datetime_list(datetime_list: list) -> list:
    sorted_list = sorted(datetime_list)
    return sorted_list


# get_date_obj("17-05-2022")
#
# get_date_obj_new("17-05-2022", '%d-%m-%Y')
# datatime_obj = get_date_obj_new("15-May-2022", '%d-%B-%Y')
# datatime_obj = get_date_obj_new("17May22", '%d%B%y')
