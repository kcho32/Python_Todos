from dao import file_registry
from exception.exception import DuplicatedError, NotFoundError
from entity import models
from view import templates

schedule = []

def is_in_schedule(id):
    #스케쥴 중복인지 확인하고
    #인덱스 돌려주기
    #없으면 -1
    global schedule
    for index, element in enumerate(schedule):
        if element.id == id:
            return index
    return -1
   
    

def add(added_schedule):
    index = is_in_schedule(added_schedule.id)
    global schedule
    
    if index == -1:
        schedule.append(added_schedule)
    else:
        raise DuplicatedError(added_schedule.id)
    
    
    

def dele(id):
    global schedule
    index = is_in_schedule(id)

    if index > -1:
        schedule.pop(index)
    else:
        raise NotFoundError(id)
    

def mod(mod_schedule):
    global schedule
    index = is_in_schedule(mod_schedule.id)

    if index > -1:
        schedule[index] = mod_schedule
    else:
        raise NotFoundError(mod_schedule.id)


def get_schedule(id):
    global schedule
    
    index = is_in_schedule(id)
    if index > -1:
        return schedule[index]    
    else:    
        raise NotFoundError(id)


def get_all():
    global schedule

    return schedule
    

def load_data():
    global schedule
    schedule = file_registry.SaveLoad().load()

def save_data():
    global schedule
    file_registry.SaveLoad().save(schedule)