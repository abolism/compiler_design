from ENUMS import CharTypes, StateTypes, ErrorTypes, DfaPartTypes
from dfa import State, StateType, DFA


def make_transitions():
    transitions0 = {}
    for ch in CharTypes.whitespaces.value:
        transitions0[ch] = 1
    return [transitions0, {}]

transitions = make_transitions()
state0 = State(0, transitions[0], StateTypes.START, DfaPartTypes.whitespace)
state1 = State(1, transitions[1], StateTypes.ACCEPT, DfaPartTypes.whitespace)
states = [state0, state1]
whitespace_dfa = DFA(states)
