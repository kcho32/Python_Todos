#from view.templates import main_choice, main_menu, input_display, add_schedule, message_display
from exception.exception import DuplicatedError, NotFoundError
from view import templates
from controller import views
from dao import file_registry

views.load_data()


while True:
    #메인메뉴 불러오기
    templates.main_menu()

    #메인메뉴에서 선택지를 choice에 저장 저장
    choice = templates.main_choice()
    
    if choice == "1":
        #스케쥴 추가하기
        schedule = templates.input_display()
        try:    
            views.add(schedule)
            templates.message_display(schedule.id + " 등록 성공")
        except DuplicatedError as error:
            templates.message_display(error)

    elif choice == "2":
        mod_schedule = templates.mod_display() #객체 받아옴
        try:
            views.mod(mod_schedule)
            templates.message_display(mod_schedule.id+" 수정 완료")
        except NotFoundError as error:
            templates.message_display(error)
    
    elif choice == "3":
        #스케쥴 삭제하기
        del_schedule = templates.del_display() #id 받아옴
        try:
            views.dele(del_schedule)
            templates.message_display(del_schedule+" 삭제 완료")
        except NotFoundError as error:
            templates.message_display(error)

    elif choice == "4":
        find_schedule = templates.find_display() #id 받아옴
        
        try:
            found = views.get_schedule(find_schedule)
            templates.info_display(found)
        except NotFoundError as error:
            templates.message_display(error)

    elif choice == "5":
        all_scheduloe = views.get_all() #list불러옴
        templates.display_all(all_scheduloe)

    elif choice == "6":
        views.save_data()
        print("종료합니다.")
        
        break
    else:
        print("잘못 선택하셨습니다. 1, 2, 3, 5 중 고르세요.\n")

    




