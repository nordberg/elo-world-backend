class NotFound(Exception):
    def __init__(self, message):
        super(NotFound, self).__init__(message)
        self.message = message
