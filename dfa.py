'''

'''


class States:
    def __init__(self, state_type, state_name):
        self.state_type = state_type
        self.state_name = state_name

    def __str__(self):
        return f"{self.state_name}"

    def __repr__(self):
        return f"{self.state_name}"

    def __eq__(self, other):
        return self.state_name == other.state_name

    def __hash__(self):
        return hash(self.state_name)


class DFA:
    def __init__(self, start_state, final_states, accepting_states, transitions):
        self.start_state = start_state
        self.final_states = final_states
        self.accepting_states = accepting_states
        self.transitions = transitions

    def get_next_state(self, current_state, current_char):
        if current_state in self.transitions:
            if current_char in self.transitions[current_state]:
                return self.transitions[current_state][current_char]
        return None

    def get_next_token(self, current_state, current_char):
        if current_state in self.transitions:
            if current_char in self.transitions[current_state]:
                return self.transitions[current_state][current_char]
        return None

    def __str__(self):
        return f"start state: {self.start_state}\nfinal states: {self.final_states}\naccepting states: {self.accepting_states}\ntransitions: {self.transitions}"

    def __repr__(self):
        return f"start state: {self.start_state}\nfinal states: {self.final_states}\naccepting states: {self.accepting_states}\ntransitions: {self.transitions}"

    def __eq__(self, other):
        return self.start_state == other.start_state and self.final_states == other.final_states and self.accepting_states == other.accepting_states and self.transitions == other.transitions

    def __hash__(self):
        return hash((self.start_state, self.final_states, self.accepting_states, self.transitions))


class Transition:
    def __init__(self, state, char, next_state):
        self.state = state
        self.char = char
        self.next_state = next_state

    def __str__(self):
        return f"state: {self.state}, char: {self.char}, next_state: {self.next_state}"

    def __repr__(self):
        return f"state: {self.state}, char: {self.char}, next_state: {self.next_state}"

    def __eq__(self, other):
        return self.state == other.state and self.char == other.char and self.next_state == other.next_state

    def __hash__(self):
        return hash((self.state, self.char, self.next_state))


class StateType(Enum):
    START = 0
    FINAL = 1
    ACCEPTING = 2
    NORMAL = 3


class ErrorType(Enum):
    INVALID_TOKEN = 0
    INVALID_CHAR = 1
    INVALID_INPUT = 2


class CharType(Enum):
    WHITESPACE = 0
    LETTER = 1
    DIGIT = 2
    SYMBOL = 3
    ALL = 4


class TokenType(Enum):
    KEYWORD = 0
    IDENTIFIER = 1
    SYMBOL = 2
    NUMBER = 3
    STRING = 4
    COMMENT = 5
    WHITESPACE = 6
    INVALID = 7


def get_dfa():
    # get the dfa for the different types of tokens
    keyword_dfa = get_keyword_dfa()
    identifier_dfa = get_identifier_dfa()
    symbol_dfa = get_symbol_dfa()
    number_dfa = get_number_dfa()
    string_dfa = get_string_dfa()
    comment_dfa = get_comment_dfa()
    whitespace_dfa = get_whitespace_dfa()
    invalid_dfa = get_invalid_dfa()

    # merge the different types of tokens into one dfa
    dfa = merge_dfa(keyword_dfa, identifier_dfa)
    dfa = merge_dfa(dfa, symbol_dfa)
    dfa = merge_dfa(dfa, number_dfa)
    dfa = merge_dfa(dfa, string_dfa)
    dfa = merge_dfa(dfa, comment_dfa)
    dfa = merge_dfa(dfa, whitespace_dfa)
    dfa = merge_dfa(dfa, invalid_dfa)

    return dfa


# now we define get_keyword_dfa, get_identifier_dfa, get_symbol_dfa, get_number_dfa, get_string_dfa, get_comment_dfa, get_whitespace_dfa, get_invalid_dfa, merge_dfa

def get_keyword_dfa():
    # define the states
    start_state = States(StateType.START, "start")
    final_state = States(StateType.FINAL, "final")
    accepting_states = [final_state]
    states = [start_state, final_state]

    # define the transitions
    transitions = {}
    transitions[start_state] = {}
    transitions[start_state]["if"] = final_state
    transitions[start_state]["then"] = final_state
    transitions[start_state]["else"] = final_state
    transitions[start_state]["end"] = final_state
    transitions[start_state]["repeat"] = final_state
    transitions[start_state]["until"] = final_state
    transitions[start_state]["read"] = final_state
    transitions[start_state]["write"] = final_state

    # define the dfa
    dfa = DFA(start_state, final_state, accepting_states, transitions)

    return dfa


def get_identifier_dfa():
    # define the states
    start_state = States(StateType.START, "start")
    final_state = States(StateType.FINAL, "final")
    accepting_states = [final_state]
    states = [start_state, final_state]

    # define the transitions
    transitions = {}
    transitions[start_state] = {}
    transitions[start_state][CharType.LETTER] = final_state
    transitions[final_state] = {}
    transitions[final_state][CharType.LETTER] = final_state
    transitions[final_state][CharType.DIGIT] = final_state

    # define the dfa
    dfa = DFA(start_state, final_state, accepting_states, transitions)

    return dfa


def get_symbol_dfa():
    # define the states
    start_state = States(StateType.START, "start")
    final_state = States(StateType.FINAL, "final")
    accepting_states = [final_state]
    states = [start_state, final_state]

    # define the transitions
    transitions = {}
    transitions[start_state] = {}
    transitions[start_state][";"] = final_state
    transitions[start_state][":="] = final_state
    transitions[start_state]["+"] = final_state
    transitions[start_state]["-"] = final_state
    transitions[start_state]["*"] = final_state
    transitions[start_state]["("] = final_state
    transitions[start_state][")"] = final_state
    transitions[start_state]["<"] = final_state

    # define the dfa
    dfa = DFA(start_state, final_state, accepting_states, transitions)

    return dfa


def get_number_dfa():
    # define the states
    start_state = States(StateType.START, "start")
    final_state = States(StateType.FINAL, "final")
    accepting_states = [final_state]
    states = [start_state, final_state]

    # define the transitions
    transitions = {}
    transitions[start_state] = {}
    transitions[start_state][CharType.DIGIT] = final_state
    transitions[final_state] = {}
    transitions[final_state][CharType.DIGIT] = final_state

    # define the dfa
    dfa = DFA(start_state, final_state, accepting_states, transitions)

    return dfa


def get_string_dfa():
    # define the states
    start_state = States(StateType.START, "start")
    final_state = States(StateType.FINAL, "final")
    accepting_states = [final_state]
    states = [start_state, final_state]

    # define the transitions
    transitions = {}
    transitions[start_state] = {}
    transitions[start_state]["\""] = final_state
    transitions[final_state] = {}
    transitions[final_state][CharType.ALL] = final_state
    transitions[final_state]["\""] = final_state

    # define the dfa
    dfa = DFA(start_state, final_state, accepting_states, transitions)

    return dfa


def get_comment_dfa():
    # define the states
    start_state = States(StateType.START, "start")
    final_state = States(StateType.FINAL, "final")
    accepting_states = [final_state]
    states = [start_state, final_state]

    # define the transitions
    transitions = {}
    transitions[start_state] = {}
    transitions[start_state]["{"] = final_state
    transitions[final_state] = {}
    transitions[final_state][CharType.ALL] = final_state
    transitions[final_state]["}"] = final_state

    # define the dfa
    dfa = DFA(start_state, final_state, accepting_states, transitions)

    return dfa


def get_whitespace_dfa():
    # define the states
    start_state = States(StateType.START, "start")
    final_state = States(StateType.FINAL, "final")
    accepting_states = [final_state]
    states = [start_state, final_state]

    # define the transitions
    transitions = {}
    transitions[start_state] = {}
    transitions[start_state][" "] = final_state
    transitions[start_state]["\t"] = final_state
    transitions[start_state]["\n"] = final_state

    # define the dfa
    dfa = DFA(start_state, final_state, accepting_states, transitions)

    return dfa


def get_invalid_dfa():
    # define the states
    start_state = States(StateType.START, "start")
    final_state = States(StateType.FINAL, "final")
    accepting_states = [final_state]
    states = [start_state, final_state]

    # define the transitions
    transitions = {}
    transitions[start_state] = {}
    transitions[start_state][CharType.ALL] = final_state

    # define the dfa
    dfa = DFA(start_state, final_state, accepting_states, transitions)

    return dfa


def get_dfa_list():
    dfa_list = []
    dfa_list.append(get_keyword_dfa())
    dfa_list.append(get_identifier_dfa())
    dfa_list.append(get_symbol_dfa())
    dfa_list.append(get_number_dfa())
    dfa_list.append(get_string_dfa())
    dfa_list.append(get_comment_dfa())
    dfa_list.append(get_whitespace_dfa())
    dfa_list.append(get_invalid_dfa())

    return dfa_list


def get_token_list(dfa_list, input_string):
    token_list = []
    current_state = dfa_list[0].start_state
    current_token = ""
    current_token_type = ""
    current_token_line = 1
    current_token_column = 1
    current_token_start = 1
    current_token_end = 1
    current_token_start_column = 1
    current_token_end_column = 1
    current_token_start_line = 1
    current_token_end_line = 1
    current_char = ""
    current_char_type = ""
    current_char_line = 1
    current_char_column = 1
    current_char_index = 0
    current_dfa = dfa_list[0]
    current_dfa_index = 0
    current_dfa_list = dfa_list
    current_dfa_list_index = 0
    current_dfa_list_length = len(dfa_list)
    current_dfa_list_length_minus_one = current_dfa_list_length - 1
    current_dfa_list_length_minus_two = current_dfa_list_length - 2
    current_dfa_list_length_minus_three = current_dfa_list_length - 3
    current_dfa_list_length_minus_four = current_dfa_list_length - 4
    current_dfa_list_length_minus_five = current_dfa_list_length - 5
    current_dfa_list_length_minus_six = current_dfa_list_length - 6
    current_dfa_list_length_minus_seven = current_dfa_list_length - 7
    current_dfa_list_length_minus_eight = current_dfa_list_length - 8
    current_dfa_list_length_minus_nine = current_dfa_list_length - 9
    current_dfa_list_length_minus_ten = current_dfa_list_length - 10
    current_dfa_list_length_minus_eleven = current_dfa_list_length - 11
    current_dfa_list_length_minus_twelve = current_dfa_list_length - 12
    current_dfa_list_length_minus_thirteen = current_dfa_list_length - 13
    current_dfa_list_length_minus_fourteen = current_dfa_list_length - 14
    current_dfa_list_length_minus_fifteen = current_dfa_list_length - 15
    current_dfa_list_length_minus_sixteen = current_dfa_list_length - 16
    current_dfa_list_length_minus_seventeen = current_dfa_list