from ENUMS import CharTypes, StateTypes, ErrorTypes, DfaPartTypes
from dfa import State, StateType, DFA


def make_transitions():
    transitions0 = {'/':1}        
    transitions1 = {'*':2}
    for ch in CharTypes.alphabets.value + CharTypes.digits.value + CharTypes.symbols.value + CharTypes.whitespaces.value:
        if ch not in '*':
            transitions1[ch] = 5
            
    transitions2 = {'*':3}
    for ch in CharTypes.all.value:
        if ch not in '*':
            transitions2[ch] = 2

    transitions3 = {'/':4, '*':3}
    for ch in CharTypes.all.value:
        if ch not in '*/':
            transitions3[ch] = 2

    return [transitions0, transitions1, transitions2, transitions3, {}]


transitions = make_transitions()
state0 = State(0, transitions[0], StateTypes.START, None)
state1 = State(1, transitions[1], StateTypes.SIMPLE, None)
state2 = State(2, transitions[2], StateTypes.SIMPLE, DfaPartTypes.comment)
state3 = State(3, transitions[3], StateTypes.SIMPLE, DfaPartTypes.comment)
state4 = State(4, transitions[4], StateTypes.ACCEPT, DfaPartTypes.comment)
state5 = State(5, {}, StateTypes.ERROR_WITH_EXTRA_CHAR, DfaPartTypes.comment, ErrorTypes.INVALID_INPUT.value)
states = [state0, state1, state2, state3, state4, state5]
comment_dfa = DFA(states)