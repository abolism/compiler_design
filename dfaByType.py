from ENUMS import StateTypes, TokenTypes
from dfa import State, StateType, DFA
from enum import Enum, auto

class CharType(Enum):
    alphabets = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    digits = "0123456789"
    symbols = "=*;:,[](){}+-</"
    whitespaces = "\n\r\t\v\f "
    all = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789=;:,[](){}+-*</\n\r\t\v\f "

class StateType(Enum):
    SIMPLE = 1
    START = 2
    ACCEPT = 3
    ACCEPT_WITH_EXTRA_CHAR = 4
    ACCEPT_ID_OR_KEYWORD = 5
    ERROR = 6
    ERROR_WITH_EXTRA_CHAR = 7

class ErrorType(Enum):
    SIMPLE = 1
    INVALID_NUMBER = 'Invalid number'
    UNMATCHED_COMMENT = 'Unmatched comment'
    INVALID_INPUT = 'Invalid input'
    UNCLOSED_COMMENT = 'Unclosed comment'

class TokenType(Enum):
    num = 1
    idKeyword = 2
    whitespace = 3
    symbol = 4
    comment = 5

def transition_function(type : str):
    transitions = []
    if type == "COMMENT":
        state0 = {'/' : 1}
        state1 = {'*' : 2}
        state2 = {'*' : 3}
        state3 = {'/': 4, '*': 3}
        for character in CharType.whitespaces.value + CharType.symbols.value + CharType.alphabets.value + CharType.digits.value:
            # if character not in "/*":
            if character != '*':
                state1[character] = 5
                state2[character] = 2
            if character not in "/*":
                state3[character] = 2

        # for ch in CharType.alphabets.value + CharType.digits.value + CharType.symbols.value + CharType.whitespaces.value:
        #     if ch not in '*':
        #         state1[ch] = 5
        #
        # state2 = {'*': 3}
        # for ch in CharType.all.value:
        #     if ch not in '*':
        #         state2[ch] = 2
        #
        # state3 = {'/': 4, '*': 3}
        # for ch in CharType.all.value:
        #     if ch not in '*/':
        #         state3[ch] = 2

        transitions.append(state0)
        transitions.append(state1)
        transitions.append(state2)
        transitions.append(state3)
        transitions.append({})

    elif type == "ID_KEYWORD":
        state0 = {}
        state1 = {}

        for character in CharType.whitespaces.value + CharType.symbols.value + CharType.alphabets.value + CharType.digits.value:
            if character in CharType.alphabets.value:
                state0[character] = 1
            if character in CharType.digits.value + CharType.alphabets.value:
                state1[character] = 1
            if character in CharType.whitespaces.value + CharType.symbols.value:
                state1[character] = 2

        # for character in CharType.alphabets.value:
        #     state0[character] = 1
        # for character in CharType.digits.value + CharType.alphabets.value:
        #     state1[character] = 1
        # for character in CharType.whitespaces.value + CharType.symbols.value:
        #     state1[character] = 2

        # state0 = {}
        # for ch in CharType.alphabets.value:
        #     state0[ch] = 1
        #
        # state1 = {}
        # for ch in CharType.digits.value + CharType.alphabets.value:
        #     state1[ch] = 1
        # for ch in CharType.whitespaces.value + CharType.symbols.value:
        #     state1[ch] = 2

        transitions.append(state0)
        transitions.append(state1)
        transitions.append({})


    elif type == "NUM":
        state0 = {}
        state1 = {}

        for character in CharType.whitespaces.value + CharType.symbols.value + CharType.alphabets.value + CharType.digits.value:
            if character in CharType.digits.value:
                state0[character] = 1
                state1[character] = 1
            if character in CharType.whitespaces.value + CharType.symbols.value:
                state1[character] = 2
            if character in CharType.alphabets.value:
                state1[character] = 3

        # for character in CharType.digits.value:
        #     state0[character] = 1
        # for character in CharType.digits.value:
        #     state1[character] = 1
        # for character in CharType.whitespaces.value + CharType.symbols.value:
        #     state1[character] = 2
        # for character in CharType.alphabets.value:
        #     state1[character] = 3

        transitions.append(state0)
        transitions.append(state1)
        transitions.append({})
        transitions.append({})

    elif type == "WHITESPACE":
        state0 = {}
        for character in CharType.whitespaces.value:
            state0[character] = 1
        transitions.append(state0)
        transitions.append({})

    elif type == "SYMBOL":
        transitions = [{} for _ in range(19)]
        for id, character in enumerate(CharType.symbols.value):
            if character != '/':
                transitions[0][character] = id + 1
        transitions[1]['='] = 15
        transitions[2]['/'] = 18
        for character in CharType.whitespaces.value + CharType.symbols.value + CharType.alphabets.value + CharType.digits.value:
            if character != '=':
                transitions[1][character] = 16
            if character != '/':
                transitions[2][character] = 17

    else:
        raise Exception("Invalid type")

    return transitions


transitions = transition_function("COMMENT")
state0 = State(0, transitions[0], StateTypes.START, None)
state1 = State(1, transitions[1], StateTypes.SIMPLE, None)
state2 = State(2, transitions[2], StateTypes.SIMPLE, TokenTypes.comment)
state3 = State(3, transitions[3], StateTypes.SIMPLE, TokenTypes.comment)
state4 = State(4, transitions[4], StateTypes.ACCEPT, TokenTypes.comment)
state5 = State(5, {}, StateTypes.ERROR_WITH_EXTRA_CHAR, TokenTypes.comment, ErrorType.INVALID_INPUT.value)
states = [state0, state1, state2, state3, state4, state5]
commentDfa = DFA(states)

transitions = transition_function("ID_KEYWORD")
state0 = State(0, transitions[0], StateTypes.START, TokenTypes.idKeyword)
state1 = State(1, transitions[1], StateTypes.SIMPLE, TokenTypes.idKeyword)
state2 = State(2, transitions[2], StateTypes.ACCEPT_WITH_EXTRA_CHAR, TokenTypes.idKeyword)
states = [state0, state1, state2]
id_KeywordDfa = DFA(states)

transitions = transition_function("NUM")
state0 = State(0, transitions[0], StateTypes.START, TokenTypes.num)
state1 = State(1, transitions[1], StateTypes.SIMPLE, TokenTypes.num)
state2 = State(2, transitions[2], StateTypes.ACCEPT_WITH_EXTRA_CHAR, TokenTypes.num)
state3 = State(3, transitions[3], StateTypes.ERROR, TokenTypes.num, ErrorType.INVALID_NUMBER.value)
states = [state0, state1, state2, state3]
numDfa = DFA(states)

transitions = transition_function("SYMBOL")
states = []
states.append(State(0, transitions[0], StateTypes.START, TokenTypes.symbol))
states.append(State(1, transitions[1], StateTypes.SIMPLE, TokenTypes.symbol))
states.append(State(2, transitions[2], StateTypes.SIMPLE, TokenTypes.symbol))
for i in range(12):
    states.append(State(i + 3, transitions[i+3], StateTypes.ACCEPT, TokenTypes.symbol))
# for i in range(3, 15):
#     states.append(State(i, transitions[i], StateTypes.ACCEPT, DfaPartTypes.symbol))
states.append(State(15, transitions[15], StateTypes.ACCEPT, TokenTypes.symbol))
states.append(State(16, transitions[16], StateTypes.ACCEPT_WITH_EXTRA_CHAR, TokenTypes.symbol))
states.append(State(17, transitions[17], StateTypes.ACCEPT_WITH_EXTRA_CHAR, TokenTypes.symbol))
states.append(State(18, transitions[18], StateTypes.ERROR, TokenTypes.symbol, ErrorType.UNMATCHED_COMMENT.value))
symbolDfa = DFA(states)

transitions = transition_function("WHITESPACE")
state0 = State(0, transitions[0], StateTypes.START, TokenTypes.whitespace)
state1 = State(1, transitions[1], StateTypes.ACCEPT, TokenTypes.whitespace)
# states.append(state0)
# states.append(state1)
states = [state0, state1]
whitespaceDfa = DFA(states)