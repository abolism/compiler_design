from enum import Enum, auto
from typing import List, Dict, Tuple
class StateType(Enum):
    SIMPLE = 1
    START = 2
    ACCEPT = 3
    ACCEPT_WITH_RETURN = 4
    ACCEPT_ID_KEYWORD = 5
    ERROR = 6
    ERROR_WITH_RETURN = 7

class TokenType(Enum):
    NUM = 1
    ID_KEYWORD = 2
    WHITESPACE = 3
    SYMBOL = 4
    COMMENT = 5

KEYWORDS = ["if", "else", "void", "int", "repeat", "break", "until", "return"]

# types of valid characters according to doc
class CharacterType(Enum):
    ALPHABETS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    DIGITS = "0123456789"
    SYMBOLS = "=*;:,[](){}+-</"
    WHITESPACE = "\n\r\t\v\f "
    ALL = ALPHABETS + DIGITS + SYMBOLS + WHITESPACE
    # ALL = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789=;:,[](){}+-*</\n\r\t\v\f "


# types of errors to be handled according to doc
class ErrorType(Enum):
    SIMPLE = 1
    INVALID_INPUT = 'Invalid input'
    UNCLOSED_COMMENT = 'Unclosed comment'
    UNMATCHED_COMMENT = 'Unmatched comment'
    INVALID_NUMBER = 'Invalid number'


# types of states in DFA


# class StateType:
#     def __init__(self, state_type: StateTypes, part_type=None, error_message_type=None):
#         self.type = state_type
#         if error_message_type:
#             self.error_message = error_message_type.value()
#         self.part_type = part_type


class State:
    def __init__(self, id: int, transitions: Dict[str, int], type: StateType, part: TokenType = None,
                 error: ErrorType = None):
        self.id = id
        self.transitions = transitions
        self.state_type = type
        self.part_type = part
        self.error = error

    def __str__(self):
        return f'{self.id} - {self.state_type} - {self.part_type}'

    def get_token(self, word: str) -> Tuple[str, str, str, str]:
        if self.state_type == StateType.ACCEPT or self.state_type == StateType.ACCEPT_WITH_RETURN or self.state_type == StateType.SIMPLE:
            extra_char = ''
            if self.state_type == StateType.ACCEPT_WITH_RETURN:
                extra_char = word[-1]
                word = word[:-1]
            if self.part_type == TokenType.NUM:
                return "NUM", word, extra_char, None
            elif self.part_type == TokenType.ID_KEYWORD:
                if word in KEYWORDS:
                    return "KEYWORD", word, extra_char, None
                else:
                    return "ID", word, extra_char, None
            elif self.part_type == TokenType.WHITESPACE:
                return "WHITESPACE", word, extra_char, None
            elif self.part_type == TokenType.SYMBOL:
                return "SYMBOL", word, extra_char, None
            else:
                if self.state_type != StateType.SIMPLE:
                    return "COMMENT", word, extra_char, None
                else:
                    if len(word) > 7:
                        word = word[0:7] + '...'
                    return "ERROR", word, '', ErrorType.UNCLOSED_COMMENT.value
        elif self.state_type == StateType.ERROR or self.state_type == StateType.ERROR_WITH_RETURN:
            extra_char = ''
            if self.state_type == StateType.ERROR_WITH_RETURN:
                extra_char = word[-1]
                word = word[:-1]
            return "ERROR", word, extra_char, self.error

    def is_accept(self) -> bool:
        if self.state_type != StateType.SIMPLE and self.state_type != StateType.START:
            return True
        return False

""" now we want to implement class State like below:
1. Creates a State class that has the following attributes:
    a. id - the state number
    b. transitions - a dictionary that maps a character to a state
    c. state_type - an enum that indicates the type of state
    d. part_type - an enum that indicates the type of token that the state can accept
    e. error - an enum that indicates the type of error that the state can accept
2. The class has the following methods:
    a. __init__ - the constructor
    b. __str__ - a string representation of the state
    c. get_token - a function that returns the token type, the token, and the extra character
    d. is_accept - a function that checks if the state is an accept state """







class DFA:
    def __init__(self, states: List[State], should_update: bool = True):
        self.states = states
        for state in states:
            if state.state_type == StateType.START:
                self.start_state = state
        if should_update:
            self.update_transactions()
        else:
            self.trash = State(-1, {}, StateType.ERROR, None, ErrorType.INVALID_INPUT.value)

    def update_transactions(self):
        for state in self.states:
            for alph in state.transitions.keys():
                next_state_id = state.transitions[alph]
                state.transitions[alph] = list(filter(lambda x: x.id == next_state_id, self.states))[0]

    def get_next(self, state: State, alphabet: str) -> State:
        if alphabet in state.transitions.keys():
            return state.transitions[alphabet]
        if state.part_type == TokenType.COMMENT:
            return state.transitions['a']
        return self.trash

    def get_start_node(self) -> State:
        return self.start_state


def get_dfa(dfas: List[DFA]) -> DFA:
    start_state = State(0, {}, StateType.START)
    states = [start_state]
    cnt = 1
    for dfa in dfas:
        for state in dfa.states:
            state.id += cnt
            if state.state_type == StateType.START:
                state.state_type = StateType.SIMPLE
                for key, value in state.transitions.items():
                    if key in start_state.transitions.keys():
                        raise NotImplementedError
                    start_state.transitions[key] = value
        states = states + dfa.states
        cnt += len(dfa.states)
    return DFA(states, False)