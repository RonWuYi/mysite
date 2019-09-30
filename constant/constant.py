import os
import datetime
import string
# from datetime import datetime
from pathlib import Path
# print(datetime.now())
# print('{0:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now()))

time_string = '{0:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now())

temp = []


for i in range(len(time_string)-1):
    if time_string[i] not in string.digits:
        temp.append('_')
    else:
        temp.append(time_string[i])
        # temp[i] = time_string[i]

# for i in time_string:
#     if i != string.digits:
#         temp[time_string.index] = '_'
#     else:
#         temp[i] =

# print(temp)
# print(('').join(temp))


# temp = time_string.replace('-', '_')
# time_string.replace(' ', '_')
# time_string.replace(':', '_')

# print(temp)
# for i in datetime.now():
#     print(i)
# print(type(datetime.now()))
def time_string():
    time_string = '{0:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now())

    temp = []
    for i in range(len(time_string)-1):
        if time_string[i] not in string.digits:
            temp.append('_')
        else:
            temp.append(time_string[i])
    return ('').join(temp)


def cur_folder() :
    return os.getcwd()

def cur_path():
    return str(Path.cwd())
