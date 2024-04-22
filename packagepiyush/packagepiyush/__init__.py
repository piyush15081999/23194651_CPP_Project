import datetime
import random

def uniquekey(a,b):
    now = datetime.datetime.now()
    date_string = now.strftime("%Y%m%d%H%M%S")
    date_int = int(date_string)
    rand=random.randint(a,b)
    return int(str(date_int)+str(rand))