class DuplicatedError(Exception):
    def __init__(self, message):
        super().__init__(message+ " 중복된 ID입니다")

    def __str__(self):
        return super().__str__()


class NotFoundError(Exception):
    def __init__(self, message):
        super().__init__(message+ " 존재하지 않는 ID입니다.")

    def __str__(self):
        return super().__str__()


class NoneTypeError(Exception):
    def __init__(self):
        super().__init__("아무 데이터도 존재하지 않습니다.")

    def __str__(self):
        return super().__str__()