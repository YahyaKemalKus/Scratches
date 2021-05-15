from .models import LOG
from datetime import datetime
from os.path import isfile


def log_to_txt(filename:str, mode = 'a',**kwargs): #can combine with log_to_json for less coding and process.
    if not isfile(filename):                       #more explicit now but more processing
        f = open(filename, mode='w')
        f.close()

    for key,value in kwargs.items():
        if not isinstance(value,str):
            kwargs[key] = str(value)

    with open(filename, mode=mode) as f:
        f.write(str(kwargs).replace(",", "\n") + '\n\n')


def log_to_json(filename:str,mode = 'r+',**kwargs):
    if not isfile(filename):
        f = open(filename, mode='w')
        f.write("[]")
        f.close()

    for key,value in kwargs.items():
        if not isinstance(value, str):
            kwargs[key] = str(value)

    with open(filename, mode = mode) as f: #this way I don't need to turn the json data into python object
        f.seek(0, 2)                       #and keep them in memory
        curr_pos = f.tell()
        f.seek(curr_pos - 1)
        comma = ",\n\n"
        if curr_pos == 2:
            comma = "" #for first dictionary

        kwargs = comma + str(kwargs).replace("'","\"")
        kwargs = kwargs.replace(",",",\n")+"]"
        f.write(kwargs)


def MiddlewareLogger(func):
    def wrapper(*args, **kwargs):
        request = args[1]
        username = request.user.username
        ip_addr = request.META.get('REMOTE_ADDR')
        func_name = args[2].__name__
        date = datetime.now()
        url = request.path
        log_dict = {'USERNAME' : username,
                    'IP_ADDR'  : ip_addr,
                    'FUNC_NAME': func_name,
                    'DATE'     : date,
                    'URL'      : url,
                    }

        LOG.logmanager.create(**log_dict) #log to database
        log_to_txt(filename= 'log.txt',**log_dict)#log to txt
        log_to_json('log.json',**log_dict) #log to json

        result = func(*args, **kwargs)
        return result

    return wrapper