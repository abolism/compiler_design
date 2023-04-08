from ENUMS import CharTypes, StateTypes, ErrorTypes, DfaPartTypes
from dfa import State, StateType, DFA


def make_transitions():
    transitions = [{} for _ in range(19)]
    for id, ch in enumerate(CharTypes.symbols.value):
        if ch != '/':
            transitions[0][ch] = id+1
    transitions[1]['='] = 15
    transitions[2]['/'] = 18
    for ch in CharTypes.all.value:
        if ch != '=':
            transitions[1][ch] = 16
        if ch != '/':
            transitions[2][ch] = 17
    return transitions

transitions = make_transitions()
states = []
states.append(State(0, transitions[0], StateTypes.START, DfaPartTypes.symbol))
states.append(State(1, transitions[1], StateTypes.SIMPLE, DfaPartTypes.symbol))
states.append(State(2, transitions[2], StateTypes.SIMPLE, DfaPartTypes.symbol))
for i in range(3, 15):
    states.append(State(i, transitions[i], StateTypes.ACCEPT, DfaPartTypes.symbol))

states.append(State(15, transitions[15], StateTypes.ACCEPT, DfaPartTypes.symbol))
states.append(State(16, transitions[16], StateTypes.ACCEPT_WITH_EXTRA_CHAR, DfaPartTypes.symbol))

states.append(State(17, transitions[17], StateTypes.ACCEPT_WITH_EXTRA_CHAR, DfaPartTypes.symbol))
states.append(State(18, transitions[18], StateTypes.ERROR, DfaPartTypes.symbol, ErrorTypes.UNMATCHED_COMMENT.value))
symbol_dfa = DFA(states)

