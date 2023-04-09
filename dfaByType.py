from ENUMS import StateTypes, TokenTypes
from dfa import State, DFA
from enum import Enum, auto
from dfa import getDfa

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
    # ALL = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789=;:,[](){}+-*</\n\r\t\v\f "


# types of errors to be handled according to doc
class ErrorType(Enum):
    SIMPLE = 1
    INVALID_INPUT = 'Invalid input'
    UNCLOSED_COMMENT = 'Unclosed comment'
    UNMATCHED_COMMENT = 'Unmatched comment'
    INVALID_NUMBER = 'Invalid number'


# types of states in DFA
class State_Type(Enum):
    SIMPLE = 1
    START = 2
    ACCEPT = 3
    ACCEPT_WITH_RETURN = 4
    ACCEPT_ID_KEYWORD = 5
    ERROR = 6
    ERROR_WITH_RETURN = 7

# returns transitions for a given token type
def transition_function(token_type: str):
    transitions = []
    if token_type == "COMMENT":
        toState0 = {'/': 1}
        toState1 = {'*': 2}
        toState2 = {'*': 3}
        toState3 = {'*': 3, '/': 4}
        for character in CharacterType.WHITESPACE.value + CharacterType.SYMBOLS.value + CharacterType.ALPHABETS.value + CharacterType.DIGITS.value:
            # if character not in "/*":
            if character != '*':
                toState1[character] = 5
                toState2[character] = 2
            if character not in "/*":
                toState3[character] = 2

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

        transitions.append(toState0)
        transitions.append(toState1)
        transitions.append(toState2)
        transitions.append(toState3)
        transitions.append({})

    elif token_type == "ID_KEYWORD":
        toState0 = {}
        toState1 = {}

        for character in CharacterType.WHITESPACE.value + CharacterType.SYMBOLS.value + CharacterType.ALPHABETS.value + CharacterType.DIGITS.value:
            if character in CharacterType.ALPHABETS.value:
                toState0[character] = 1
            if character in CharacterType.DIGITS.value + CharacterType.ALPHABETS.value:
                toState1[character] = 1
            if character in CharacterType.WHITESPACE.value + CharacterType.SYMBOLS.value:
                toState1[character] = 2

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

        transitions.append(toState0)
        transitions.append(toState1)
        transitions.append({})


    elif token_type == "NUM":
        toState0 = {}
        toState1 = {}

        for character in CharacterType.WHITESPACE.value + CharacterType.SYMBOLS.value + CharacterType.ALPHABETS.value + CharacterType.DIGITS.value:
            if character in CharacterType.DIGITS.value:
                toState0[character] = 1
                toState1[character] = 1
            if character in CharacterType.WHITESPACE.value + CharacterType.SYMBOLS.value:
                toState1[character] = 2
            if character in CharacterType.ALPHABETS.value:
                toState1[character] = 3

        # for character in CharType.digits.value:
        #     state0[character] = 1
        # for character in CharType.digits.value:
        #     state1[character] = 1
        # for character in CharType.whitespaces.value + CharType.symbols.value:
        #     state1[character] = 2
        # for character in CharType.alphabets.value:
        #     state1[character] = 3

        transitions.append(toState0)
        transitions.append(toState1)
        transitions.append({})
        transitions.append({})

    elif token_type == "WHITESPACE":
        toState0 = {}
        for character in CharacterType.WHITESPACE.value:
            toState0[character] = 1
        transitions.append(toState0)
        transitions.append({})

    elif token_type == "SYMBOL":
        transitions = [{} for _ in range(19)]
        for id, character in enumerate(CharacterType.SYMBOLS.value):
            if character != '/':
                transitions[0][character] = id + 1
        transitions[1]['='] = 15
        transitions[2]['/'] = 18
        for character in CharacterType.WHITESPACE.value + CharacterType.SYMBOLS.value + CharacterType.ALPHABETS.value + CharacterType.DIGITS.value:
            if character != '=':
                transitions[1][character] = 16
            if character != '/':
                transitions[2][character] = 17

    else:
        raise Exception("Invalid type")

    return transitions

# get DFA for comment
transitions = transition_function("COMMENT")
# states = [[] for i in range(6)]
# states[0] = State(0, transitions[0], StateTypes.START, None)
# states[1] = State(1, transitions[1], StateTypes.SIMPLE, None)
# states[2] = State(2, transitions[2], StateTypes.SIMPLE, TokenTypes.comment)
# states[3] = State(3, transitions[3], StateTypes.SIMPLE, TokenTypes.comment)
# states[4] = State(4, transitions[4], StateTypes.ACCEPT, TokenTypes.comment)
# states[5] = State(5, {}, StateTypes.ERROR_WITH_EXTRA_CHAR, TokenTypes.comment, ErrorType.INVALID_INPUT.value)

# states = [state0, state1, state2, state3, state4, state5]
states = []
states.append(State(0, transitions[0], StateTypes.START, None))
states.append(State(1, transitions[1], StateTypes.SIMPLE, None))
states.append(State(2, transitions[2], StateTypes.SIMPLE, TokenTypes.comment))
states.append(State(3, transitions[3], StateTypes.SIMPLE, TokenTypes.comment))
states.append(State(4, transitions[4], StateTypes.ACCEPT, TokenTypes.comment))
states.append(State(5, {}, StateTypes.ERROR_WITH_EXTRA_CHAR, TokenTypes.comment, ErrorType.INVALID_INPUT.value))
commentDfa = DFA(states)

# get DFA for id_keyword
transitions = transition_function("ID_KEYWORD")
# state0 = State(0, transitions[0], StateTypes.START, TokenTypes.idKeyword)
# state1 = State(1, transitions[1], StateTypes.SIMPLE, TokenTypes.idKeyword)
# state2 = State(2, transitions[2], StateTypes.ACCEPT_WITH_EXTRA_CHAR, TokenTypes.idKeyword)
# states = [state0, state1, state2]
states = []
states.append(State(0, transitions[0], StateTypes.START, TokenTypes.idKeyword))
states.append(State(1, transitions[1], StateTypes.SIMPLE, TokenTypes.idKeyword))
states.append(State(2, transitions[2], StateTypes.ACCEPT_WITH_EXTRA_CHAR, TokenTypes.idKeyword))
id_KeywordDfa = DFA(states)

# get DFA for num
transitions = transition_function("NUM")
# state0 = State(0, transitions[0], StateTypes.START, TokenTypes.num)
# state1 = State(1, transitions[1], StateTypes.SIMPLE, TokenTypes.num)
# state2 = State(2, transitions[2], StateTypes.ACCEPT_WITH_EXTRA_CHAR, TokenTypes.num)
# state3 = State(3, transitions[3], StateTypes.ERROR, TokenTypes.num, ErrorType.INVALID_NUMBER.value)
# states = [state0, state1, state2, state3]
states = []
states.append(State(0, transitions[0], StateTypes.START, TokenTypes.num))
states.append(State(1, transitions[1], StateTypes.SIMPLE, TokenTypes.num))
states.append(State(2, transitions[2], StateTypes.ACCEPT_WITH_EXTRA_CHAR, TokenTypes.num))
states.append(State(3, transitions[3], StateTypes.ERROR, TokenTypes.num, ErrorType.INVALID_NUMBER.value))
numDfa = DFA(states)

# get DFA for symbol
transitions = transition_function("SYMBOL")
states = []
states.append(State(0, transitions[0], StateTypes.START, TokenTypes.symbol))
states.append(State(1, transitions[1], StateTypes.SIMPLE, TokenTypes.symbol))
states.append(State(2, transitions[2], StateTypes.SIMPLE, TokenTypes.symbol))
for i in range(12):
    states.append(State(i + 3, transitions[i + 3], StateTypes.ACCEPT, TokenTypes.symbol))
# for i in range(3, 15):
#     states.append(State(i, transitions[i], StateTypes.ACCEPT, DfaPartTypes.symbol))
states.append(State(15, transitions[15], StateTypes.ACCEPT, TokenTypes.symbol))
states.append(State(16, transitions[16], StateTypes.ACCEPT_WITH_EXTRA_CHAR, TokenTypes.symbol))
states.append(State(17, transitions[17], StateTypes.ACCEPT_WITH_EXTRA_CHAR, TokenTypes.symbol))
states.append(State(18, transitions[18], StateTypes.ERROR, TokenTypes.symbol, ErrorType.UNMATCHED_COMMENT.value))
symbolDfa = DFA(states)

#get DFA for whitespace
transitions = transition_function("WHITESPACE")
# state0 = State(0, transitions[0], StateTypes.START, TokenTypes.whitespace)
# state1 = State(1, transitions[1], StateTypes.ACCEPT, TokenTypes.whitespace)
# # states.append(state0)
# # states.append(state1)
# states = [state0, state1]
states = []
states.append(State(0, transitions[0], StateTypes.START, TokenTypes.whitespace))
states.append(State(1, transitions[1], StateTypes.ACCEPT, TokenTypes.whitespace))
whitespaceDfa = DFA(states)

# # get DFA for error
# state0 = State(0, {}, StateTypes.ERROR, None, ErrorType.INVALID_INPUT.value)
# states = [state0]
# errorDfa = DFA(states)

# # get DFA for end
# state0 = State(0, {}, StateTypes.END, None)
# states = [state0]
# endDfa = DFA(states)

# DFA for all types merged
merged_dfa = getDfa([commentDfa, id_KeywordDfa, numDfa, symbolDfa, whitespaceDfa])


