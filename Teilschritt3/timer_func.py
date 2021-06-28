from database import EPSDatabase
import time
def timer(func):
    def time_dec(*args):
        before = time.time()
        func(*args)
        print(f"Function took {round(time.time() - before, 3)} seconds")

    return time_dec
@timer
def create_number():
        number = EPSDatabase.Select_latest().fetchall()
        if number != None:
            if len(number) != 0:
                number = int(number[0][0])
                counter = number
                print(counter)
                return counter
@timer
def create():
    
    counter = 0
    for value in EPSDatabase.print_table().fetchall():
        if int(value[0]) > counter:
            counter = int(value[0])
    
    print(counter)
    return counter
@timer
def cast():
    counter = EPSDatabase.hightest().fetchall()
    print(counter)
def double():
    fetch = EPSDatabase.print_table().fetchall()
    double_counter = 0
    for value in fetch:
        

create_number()
create()
cast()