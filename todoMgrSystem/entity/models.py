class Todo():
    def __init__(self, id, title, content, date, done):
        #id, title, content, date, done
        self.id = str(id)
        self.title = str(title)
        self.content = str(content)
        self.date = str(date)
        self.done = done
        
    def todo_show(self):
        phrase = "ID:\t\t{0}\nTitle:\t\t{1}\nContent:\t{2}\nDate:\t\t{3}\nDone:\t\t{4}\n".format(self.id, self.title, self.content, self.date, self.done)
        return phrase



class Display():
    def __init__(self):
        pass
     
    def main(self):
        print("원하시는 기능을 선택하세요.")
        print("1. 일정 추가")
        print("2. 일정 수정")
        print("3. 일정 삭제")
        print("4. 일정 검색")
        print("5. 모든 일정 확인")
        print("6. 종료")

    def main_choice(self):
        choice = str(input("선택: "))
        return choice


    def id_display(self, act):
        print("{0}할 ID를 입력하세요.".format(act))

    def id_select(self):
        id = str(input("ID: "))
        return id

    def mod_sub(self):
        print("수정하고 싶은 데이터를 선택하세요")
        print("1. title")
        print("2. content")
        print("3. date")
        print("4. done")
        print("5. all")
        print("6. 취소")

    def mod_sub_select(self):
        choice = str(input("선택: "))
        return choice





    


    





if __name__ == "__main__":
    main = Display()
    a = Display().main_choice()
    print(a)