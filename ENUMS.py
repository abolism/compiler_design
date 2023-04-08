from enum import Enum, auto

class StateTypes(Enum):
    SIMPLE = 1
    START = 2
    ACCEPT = 3
    ACCEPT_WITH_EXTRA_CHAR = 4
    ACCEPT_ID_OR_KEYWORD = 5
    ERROR = 6
    ERROR_WITH_EXTRA_CHAR = 7

class ErrorTypes(Enum):
    SIMPLE = 1
    INVALID_NUMBER = 'Invalid number'
    UNMATCHED_COMMENT = 'Unmatched comment'
    INVALID_INPUT = 'Invalid input'
    UNCLOSED_COMMENT = 'Unclosed comment'

class CharTypes(Enum):
    alphabets = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    digits = "0123456789"
    symbols = "=*;:,[](){}+-</"
    whitespaces = "\n\r\t\v\f "
    all = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789=;:,[](){}+-*</\n\r\t\v\f "

class DfaPartTypes(Enum):
    num = 1
    idKeyword = 2
    whitespace = 3
    symbol = 4
    comment = 5