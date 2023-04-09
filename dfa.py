from enum import Enum, auto
from typing import List, Dict, Tuple

# keywords as given by the doc
KEYWORDS = ["if", "else", "void", "int", "repeat", "break", "until", "return"]


# types of states in DFA
class StateType(Enum):
    SIMPLE = 1
    START = 2
    ACCEPT = 3
    ACCEPT_WITH_RETURN = 4
    ACCEPT_ID_KEYWORD = 5
    ERROR = 6
    ERROR_WITH_RETURN = 7


# types of tokens in C_Minus according to doc
class TokenType(Enum):
    NUM = 1
    ID_KEYWORD = 2
    WHITESPACE = 3
    SYMBOL = 4
    COMMENT = 5


# types of valid characters according to doc
class CharacterType(Enum):
    ALPHABETS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    DIGITS = "0123456789"
    SYMBOLS = "=*;:,[](){}+-</"
    WHITESPACE = "\n\r\t\v\f "
    ALL = ALPHABETS + DIGITS + SYMBOLS + WHITESPACE


# types of errors to be handled according to doc
class ErrorType(Enum):
    SIMPLE = 1
    INVALID_INPUT = 'Invalid input'
    UNCLOSED_COMMENT = 'Unclosed comment'
    UNMATCHED_COMMENT = 'Unmatched comment'
    INVALID_NUMBER = 'Invalid number'


class State:
    def __init__(self, id: int, transitions: Dict[str, int], state_type: StateType, part_type: TokenType = None,
                 error_message: ErrorType = None):
        self.id = id
        self.transitions = transitions
        self.state_type = state_type
        self.part_type = part_type
        self.error_message = error_message

    def __str__(self):
        return f'{self.id} - {self.state_type} - {self.part_type}'

    # gets lexeme returns (type, lexeme, character to be returned(if there is any), error message(if needed))
    def move_pointer(self, lexeme: str):
        accepting_states = [StateType.ACCEPT, StateType.ACCEPT_WITH_RETURN, StateType.SIMPLE]
        error_states = [StateType.ERROR, StateType.ERROR_WITH_RETURN]
        char_to_return = ""
        # first we check if an error has occured:
        if self.state_type in error_states:
            if self.state_type == StateType.ERROR_WITH_RETURN:
                char_to_return = lexeme[-1]
                # remove the additional character from the lexeme
                lexeme = lexeme.rstrip(char_to_return)
            return "ERROR", lexeme, char_to_return, self.error_message

        elif self.state_type in accepting_states:
            if self.state_type == StateType.ACCEPT_WITH_RETURN:
                char_to_return = lexeme[-1]
                lexeme = lexeme.rstrip(char_to_return)
            if self.part_type == TokenType.ID_KEYWORD:
                if lexeme not in KEYWORDS:
                    return "ID", lexeme, char_to_return, None
                else:
                    return "KEYWORD", lexeme, char_to_return, None
            elif self.part_type == TokenType.NUM:
                return "NUM", lexeme, char_to_return, None

            elif self.part_type == TokenType.SYMBOL:
                return "SYMBOL", lexeme, char_to_return, None

            elif self.part_type == TokenType.WHITESPACE:
                return "WHITESPACE", lexeme, char_to_return, None

            else:
                if self.state_type != StateType.SIMPLE:
                    return "COMMENT", lexeme, char_to_return, None
                else:
                    if len(lexeme) > 7:
                        lexeme = lexeme[:7] + '...'
                    return "ERROR", lexeme, '', ErrorType.UNCLOSED_COMMENT.value

class DFA:
    def __init__(self, states: List[State], update: bool = True):
        self.states = states
        # set start state in DFA
        for state in states:
            if state.state_type == StateType.START:
                self.start_state = state
        if update:
            '''usage removed'''
            for state in self.states:
                for char in state.transitions.keys():
                    next_state_id = state.transitions[char]
                    next_state = [s for s in self.states if s.id == next_state_id][0]
                    state.transitions[char] = next_state
        else:
            self.ignore = State(-1, {}, StateType.ERROR, None, ErrorType.INVALID_INPUT.value)

    '''usage removed'''
    # def get_next(self, state: State, alphabet: str):
    #     if alphabet in state.transitions.keys():
    #         return state.transitions[alphabet]
    #     if state.part_type == TokenType.COMMENT:
    #         return state.transitions['a']
    #     return self.ignore

    '''usage removed'''
    # def get_start_node(self):
    #     return self.start_state


def get_dfa(type_specific_DFAs: List[DFA]):
    start_state = State(0, {}, StateType.START)
    dfa_states = [start_state]
    counter = 0
    for dfa in type_specific_DFAs:
        for dfa_state in dfa.states:
            dfa_state.id += counter + 1
            if dfa_state.state_type == StateType.START:
                dfa_state.state_type = StateType.SIMPLE
                for key, value in dfa_state.transitions.items():
                    if key in start_state.transitions.keys():
                        raise NotImplementedError
                    start_state.transitions[key] = value
        counter += len(dfa.states)
        dfa_states = dfa_states + dfa.states
    return DFA(dfa_states, False)


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
