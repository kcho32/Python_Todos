from entity import models
from controller import views
import os.path


class SaveLoad():
    def __init__(self):
        pass

    def save(self, save_list):
        save_file = open("../todoMgrSystem/data.dat", "w")
        for index, schedule in enumerate(save_list):
            print()
            save_file.write("{0},{1},{2},{3},{4}\n".format(save_list[index].id,save_list[index].title,save_list[index].content,save_list[index].date,save_list[index].done))
        save_file.close()
        
    def load(self):
        fileExist = os.path.isfile("../todoMgrSystem/data.dat")
        schedule = []
        if fileExist:
            load_file = open("../todoMgrSystem/data.dat", "r")
            while True:
                data = load_file.readline().strip("\n")
                if not data:
                    break
                data_list = data.split(",")
                loaded_schedule = models.Todo(data_list[0],data_list[1],data_list[2],data_list[3],data_list[4])
                schedule.append(loaded_schedule)
                

            load_file.close()
        return schedule
