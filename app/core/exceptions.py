class BaseCustomException(Exception):
    def __init__(self, msg: str = ""):
        self.msg = msg

    def __str__(self):
        return self.msg


class UnexpectedApiResponseException(BaseCustomException):
    pass


class UnexpectedDataException(BaseCustomException):
    pass


class RepoException(BaseCustomException):
    pass


class InvalidStatusException(BaseCustomException):
    pass
