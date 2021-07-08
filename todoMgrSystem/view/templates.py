from controller import views
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
    data = views.get_schedule(mod_id)
    print(data.todo_show())
    Display().mod_sub()
    choice = Display().mod_sub_select()
    

    if choice == "1":
        title = str(input("Title: "))
        content = data.content
        date = data.date
        done = data.done
        return Todo(mod_id, title, content, date, done)
    elif choice == "2":
        content = str(input("Content: "))
        title = data.title
        date = data.date
        done = data.done
        return Todo(mod_id, title, content, date, done)
    elif choice == "3":
        date = str(input("Date(MMDD): "))
        content = data.content
        title = data.title
        done = data.done
        return Todo(mod_id, title, content, date, done)
    elif choice == "4":
        done = str(input("Done(Y/N): "))
        content = data.content
        date = data.date
        title = data.title
        return Todo(mod_id, title, content, date, done)
    elif choice == "5":
        title = str(input("Title: "))
        content = str(input("Content: "))
        date = str(input("Date(MMDD): "))
        done = str(input("Done(Y/N): "))
        return Todo(mod_id, title, content, date, done)
    elif choice == "6":
        print("돌아갑니다.")
        return data
    else:
        print("잘못 입력하셨습니다")
        return data


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