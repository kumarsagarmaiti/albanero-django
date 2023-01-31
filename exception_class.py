class EmptyFieldException(Exception):
    def __init__(self, field):
        self.field = field

    def __str__(self):
        return self.field
