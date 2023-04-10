from enum import Enum, auto
from typing import List, Dict, Tuple

KEYWORDS = ["if", "else", "void", "int", "repeat", "break", "until", "return"]


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


# types of errors to be handled according to doc
class ErrorType(Enum):
    SIMPLE = 1
    INVALID_INPUT = 'Invalid input'
    UNCLOSED_COMMENT = 'Unclosed comment'
    UNMATCHED_COMMENT = 'Unmatched comment'
    INVALID_NUMBER = 'Invalid number'


# types of valid characters according to doc
class CharacterType(Enum):
    SYMBOLS = "=*;:,[](){}+-</"
    ALPHABETS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    DIGITS = "0123456789"
    WHITESPACE = "\n\r\t\v\f "
    ALL = ALPHABETS + DIGITS + SYMBOLS + WHITESPACE


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

    # gets lexeme and returns the (type, lexeme, character to retrieve(if there is any), error_message(if needed))
    def move_forward(self, lexeme: str):
        accept_states = [StateType.ACCEPT, StateType.ACCEPT_WITH_RETURN, StateType.SIMPLE]
        error_states = [StateType.ERROR, StateType.ERROR_WITH_RETURN]
        character_to_return = ""
        # first we check if we got an error
        if self.state_type in error_states:
            if self.state_type == StateType.ERROR_WITH_RETURN:
                character_to_return = lexeme[-1]
                lexeme = lexeme.rstrip(character_to_return)
            return "ERROR", lexeme, character_to_return, self.error_message

        elif self.state_type in accept_states:
            if self.state_type == StateType.ACCEPT_WITH_RETURN:
                character_to_return = lexeme[-1]
                lexeme = lexeme.rstrip(character_to_return)
            if self.part_type == TokenType.ID_KEYWORD:
                if lexeme not in KEYWORDS:
                    return "ID", lexeme, character_to_return, None
                else:
                    return "KEYWORD", lexeme, character_to_return, None

            elif self.part_type == TokenType.WHITESPACE:
                return "WHITESPACE", lexeme, character_to_return, None

            elif self.part_type == TokenType.SYMBOL:
                return "SYMBOL", lexeme, character_to_return, None

            elif self.part_type == TokenType.NUM:
                return "NUM", lexeme, character_to_return, None

            else:
                if self.state_type == StateType.SIMPLE:
                    if len(lexeme) > 7:
                        lexeme = lexeme[:7] + '...'
                    return "ERROR", lexeme, character_to_return, ErrorType.UNCLOSED_COMMENT.value
                else:
                    return "COMMENT", lexeme, character_to_return, None

    def is_accepted(self):
        not_accepted = [StateType.SIMPLE, StateType.START]
        if self.state_type not in not_accepted:
            return False
        return True


class DFA:
    def __init__(self, states: List[State], update: bool = True):
        self.states = states
        for state in states:
            if state.state_type == StateType.START:
                self.start_state = state
        if update:
            for state in self.states:
                for char in state.transitions.keys():
                    hold_next_state_id = state.transitions[char]
                    # state.transitions[char] = list(filter(lambda x: x.id == hold_next_state_id, self.states))[0]
                    next_state = [s for s in self.states if s.id == hold_next_state_id][0]
                    state.transitions[char] = next_state

            # self.update_transactions()
        else:
            self.ignore = State(-1, {}, StateType.ERROR, None, ErrorType.INVALID_INPUT.value)

    '''usage removed'''
    # def update_transactions(self):
    #     for state in self.states:
    #         for alph in state.transitions.keys():
    #             next_state_id = state.transitions[alph]
    #             state.transitions[alph] = list(filter(lambda x: x.id == next_state_id, self.states))[0]
    '''was unable to remove usage'''

    def get_start_state(self) -> State:
        return self.start_state

    '''was unable to remove usage'''

    def next_char(self, state: State, alphabet: str) -> State:
        if alphabet in state.transitions.keys():
            return state.transitions[alphabet]
        if state.part_type == TokenType.COMMENT:
            return state.transitions['a']
        return self.ignore


def get_dfa(type_specific_dfas: List[DFA]) -> DFA:
    start_state = State(0, {}, StateType.START)
    merged_states = [start_state]
    counter = 0
    for dfa in type_specific_dfas:
        for dfa_state in dfa.states:
            dfa_state.id += counter + 1
            if dfa_state.state_type == StateType.START:
                dfa_state.state_type = StateType.SIMPLE
                for key, value in dfa_state.transitions.items():
                    if key in start_state.transitions.keys():
                        raise NotImplementedError
                    start_state.transitions[key] = value
        merged_states = merged_states + dfa.states
        counter += len(dfa.states)
    return DFA(merged_states, False)
