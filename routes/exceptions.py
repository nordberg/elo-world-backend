class HTTPException(Exception):
    def __init__(self, message):
        super().__init__(message)


class BadRequest(HTTPException):
    def __init__(self, message):
        super().__init__(message)
        self.message = message
        self.http_code = 400


class NotFound(HTTPException):
    def __init__(self, message):
        super().__init__(message)
        self.message = message
        self.http_code = 404
