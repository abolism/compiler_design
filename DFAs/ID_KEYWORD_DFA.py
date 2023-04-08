from ENUMS import CharTypes, StateTypes, ErrorTypes, DfaPartTypes
from dfa import State, StateType, DFA


def make_transitions():
    transitions0 = {}
    for ch in CharTypes.alphabets.value:
        transitions0[ch] = 1

    transitions1 = {}
    for ch in CharTypes.digits.value + CharTypes.alphabets.value:
        transitions1[ch] = 1
    for ch in CharTypes.whitespaces.value + CharTypes.symbols.value:
        transitions1[ch] = 2

    return [transitions0, transitions1, {}]

transitions = make_transitions()
state0 = State(0, transitions[0], StateTypes.START, DfaPartTypes.idKeyword)
state1 = State(1, transitions[1], StateTypes.SIMPLE, DfaPartTypes.idKeyword)
state2 = State(2, transitions[2], StateTypes.ACCEPT_WITH_EXTRA_CHAR, DfaPartTypes.idKeyword)
states = [state0, state1, state2]
idKeyword_dfa = DFA(states)