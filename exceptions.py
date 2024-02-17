class RuleValidationException(Exception):
    def __init__(self, message):
        super().__init__(message)


class RuleInvalidArgumentException(Exception):
    def __init__(self, message):
        super().__init__(message)
