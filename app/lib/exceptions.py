# Standard Library Imports
# None

# 3rd-Party Imports
# None

# App-Local Imports
# None

class ApiException(Exception):
    def __init__(self, message, exit_code):
        self.message = message
        self.exit_code = exit_code


class ConfigException(ApiException):
    pass


class DocumentDoesNotExistException(Exception):
    pass
