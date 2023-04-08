from enum import Enum, auto

class StateTypes(Enum):
    SIMPLE = 1
    START = 2
    ACCEPT = 3
    ACCEPT_WITH_EXTRA_CHAR = 4
    ACCEPT_ID_OR_KEYWORD = 5
    ERROR = 6
    ERROR_WITH_EXTRA_CHAR = 7

class TokenTypes(Enum):
    num = 1
    idKeyword = 2
    whitespace = 3
    symbol = 4
    comment = 5