from dfa import State, DFA, StateType, TokenType, get_dfa, CharacterType, ErrorType


# returns transitions for a given token type
def transition_function(token_type: str):
    transitions = []
    if token_type == "COMMENT":
        toState = []
        toState.append({'/': 1})
        toState.append({'*': 2})
        toState.append({'*': 3})
        toState.append({'*': 3, '/': 4})
        for character in CharacterType.WHITESPACE.value + CharacterType.SYMBOLS.value + CharacterType.ALPHABETS.value + CharacterType.DIGITS.value:
            # if character not in "/*":
            if character != '*':
                toState[1][character] = 5
                toState[2][character] = 2
            if character not in "/*":
                toState[3][character] = 2

        transitions.append(toState[0])
        transitions.append(toState[1])
        transitions.append(toState[2])
        transitions.append(toState[3])
        transitions.append({})

    elif token_type == "ID_KEYWORD":
        toState = []
        toState.append({})
        toState.append({})

        for character in CharacterType.WHITESPACE.value + CharacterType.SYMBOLS.value + CharacterType.ALPHABETS.value + CharacterType.DIGITS.value:
            if character in CharacterType.ALPHABETS.value:
                toState[0][character] = 1
            if character in CharacterType.DIGITS.value + CharacterType.ALPHABETS.value:
                toState[1][character] = 1
            if character in CharacterType.WHITESPACE.value + CharacterType.SYMBOLS.value:
                toState[1][character] = 2

        transitions.append(toState[0])
        transitions.append(toState[1])
        transitions.append({})


    elif token_type == "NUM":
        toState = []
        toState.append({})
        toState.append({})

        for character in CharacterType.WHITESPACE.value + CharacterType.SYMBOLS.value + CharacterType.ALPHABETS.value + CharacterType.DIGITS.value:
            if character in CharacterType.DIGITS.value:
                toState[0][character] = 1
                toState[1][character] = 1
            if character in CharacterType.WHITESPACE.value + CharacterType.SYMBOLS.value:
                toState[1][character] = 2
            if character in CharacterType.ALPHABETS.value:
                toState[1][character] = 3

        transitions.append(toState[0])
        transitions.append(toState[1])
        transitions.append({})
        transitions.append({})

    elif token_type == "WHITESPACE":
        toState = []
        toState.append({})
        for character in CharacterType.WHITESPACE.value:
            toState[0][character] = 1
        transitions.append(toState[0])
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
states = []
states.append(State(0, transitions[0], StateType.START, None))
states.append(State(1, transitions[1], StateType.SIMPLE, None))
states.append(State(2, transitions[2], StateType.SIMPLE, TokenType.COMMENT))
states.append(State(3, transitions[3], StateType.SIMPLE, TokenType.COMMENT))
states.append(State(4, transitions[4], StateType.ACCEPT, TokenType.COMMENT))
states.append(State(5, {}, StateType.ERROR_WITH_RETURN, TokenType.COMMENT, ErrorType.INVALID_INPUT.value))
commentDfa = DFA(states)

# get DFA for id_keyword
transitions = transition_function("ID_KEYWORD")
states = []
states.append(State(0, transitions[0], StateType.START, TokenType.ID_KEYWORD))
states.append(State(1, transitions[1], StateType.SIMPLE, TokenType.ID_KEYWORD))
states.append(State(2, transitions[2], StateType.ACCEPT_WITH_RETURN, TokenType.ID_KEYWORD))
id_KeywordDfa = DFA(states)

# get DFA for num
transitions = transition_function("NUM")
states = []
states.append(State(0, transitions[0], StateType.START, TokenType.NUM))
states.append(State(1, transitions[1], StateType.SIMPLE, TokenType.NUM))
states.append(State(2, transitions[2], StateType.ACCEPT_WITH_RETURN, TokenType.NUM))
states.append(State(3, transitions[3], StateType.ERROR, TokenType.NUM, ErrorType.INVALID_NUMBER.value))
numDfa = DFA(states)

# get DFA for symbol
transitions = transition_function("SYMBOL")
states = []
states.append(State(0, transitions[0], StateType.START, TokenType.SYMBOL))
states.append(State(1, transitions[1], StateType.SIMPLE, TokenType.SYMBOL))
states.append(State(2, transitions[2], StateType.SIMPLE, TokenType.SYMBOL))
for i in range(12):
    states.append(State(i + 3, transitions[i + 3], StateType.ACCEPT, TokenType.SYMBOL))
states.append(State(15, transitions[15], StateType.ACCEPT, TokenType.SYMBOL))
states.append(State(16, transitions[16], StateType.ACCEPT_WITH_RETURN, TokenType.SYMBOL))
states.append(State(17, transitions[17], StateType.ACCEPT_WITH_RETURN, TokenType.SYMBOL))
states.append(State(18, transitions[18], StateType.ERROR, TokenType.SYMBOL, ErrorType.UNMATCHED_COMMENT.value))
symbolDfa = DFA(states)

# get DFA for whitespace
transitions = transition_function("WHITESPACE")
states = []
states.append(State(0, transitions[0], StateType.START, TokenType.WHITESPACE))
states.append(State(1, transitions[1], StateType.ACCEPT, TokenType.WHITESPACE))
whitespaceDfa = DFA(states)

# # get DFA for error

# DFA for all types merged
DFAs_merged = get_dfa([commentDfa, id_KeywordDfa, numDfa, symbolDfa, whitespaceDfa])
