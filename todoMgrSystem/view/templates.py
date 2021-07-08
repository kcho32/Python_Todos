from entity.models import Display,Todo
from controller import views
from exception.exception import NoneTypeError


def main_menu():
    main_display = Display().main()
    return main_display


def main_choice():
    main_choice = Display().main_choice()
    return main_choice


def input_display():
    id = str(input("ID: "))
    title = str(input("Title: "))
    content = str(input("Content: "))
    date = str(input("Date(mmdd): "))
    done = str(input("Done(Y/N): "))

    return Todo(id, title, content, date, done)


def add_schedule(schedule):
    views.add(schedule)
    return


def message_display(message):
    print(message)
    return


def mod_display():
    Display().id_display("수정")
    mod_id = Display().id_select()
    title = str(input("Title: "))
    content = str(input("Content: "))
    date = str(input("Date(MM/DD): "))
    done = str(input("Done(Y/N): "))
    return Todo(mod_id, title, content, date, done)


def del_display():
    Display().id_display("삭제")
    del_id = Display().id_select()
    return del_id


def find_display():
    Display().id_display("검색")
    find_id = Display().id_select()
    return find_id


def info_display(found):
    print("====== 상세 정보입니다 ======")
    print(found.todo_show())


def display_all(s_list):
    print("======저장 된 모든 정보입니다.======")
    if s_list == None:
        raise NoneTypeError()
    else:
        for schedule in s_list:
            print(schedule.todo_show())