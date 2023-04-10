from typing import Tuple
from dfa import StateType, TokenType
# this import is for the functions moved to this class from DFA and State classes to improve runtime speed:
from dfa import DFA, State


class Scanner:
    def __init__(self, dfa, input_file):
        # self.dfa = dfa
        # self.input_file = input_file
        # self.file = open(input_file, "r")
        # self.symbol_table = []
        # self.current_char = self.file.read(1)
        # self.current_index = 0
        # self.current_line = 1
        # # self.file.close()
        self.dfa = dfa
        self.file_address = input_file
        self.file = open(input_file, "r")
        # read file into a string (buffer)
        self.file_text = self.file.read()
        self.current_index = 0
        self.line = 1
        # self.keywords = ["break", "else", "if", "int", "repeat", "return", "until", "void"]
        # self.symbol_table = ["break", "else", "if", "int", "repeat", "return", "until", "void"]
        self.symbol_table = []
        self.symbol_table = self.add_keywords(self.symbol_table)
        self.file.close()

    def add_keywords(self, list):
        keywords = ["break", "else", "if", "int", "repeat", "return", "until", "void"]
        list = list + keywords
        return list

    # def get_next_token(self):
    #     if self.current_char == '':
    #         self.file.close()
    #         raise Exception("End of file reached!")
    #
    #     state = self.dfa.start_state
    #     token = ""
    #     while True:
    #         state = self.dfa.get_next_state(state, self.current_char)
    #         if state is None:
    #             break
    #         token = token + self.current_char
    #         self.current_char = self.file.read(1)
    #         if self.current_char == '\n':
    #             self.current_line = self.current_line + 1
    #
    #     if state in self.dfa.final_states:
    #         if state in self.dfa.accepting_states:
    #             if state == 'ID_KEYWORD':
    #                 if token in self.dfa.keywords:
    #                     return self.current_line, 'KEYWORD', token, None
    #                 else:
    #                     if token not in self.symbol_table:
    #                         self.symbol_table.append(token)
    #                     return self.current_line, 'ID', token, None
    #             elif state == 'NUM':
    #                 return self.current_line, 'NUM', token, None
    #             elif state == 'SYMBOL':
    #                 return self.current_line, 'SYMBOL', token, None
    #             elif state == 'COMMENT':
    #                 return self.current_line, 'COMMENT', token, None
    #         else:
    #             return self.current_line, 'WHITESPACE', token, None
    #     else:
    #         return self.current_line, 'ERROR', token, 'Invalid token!'

    def get_start_state(self, dfa: DFA):
        return dfa.start_state

    def next_char(self, dfa: DFA, state: State, alphabet: str):
        if alphabet in state.transitions.keys():
            return state.transitions[alphabet]
        if state.part_type == TokenType.COMMENT:
            return state.transitions['a']
        return dfa.ignore

    # this function was modified to do the exact opposite of what it did before (what it was supposed to do)
    def is_accepted(self, state: State):
        not_accepted = [StateType.SIMPLE, StateType.START]
        if state.state_type not in not_accepted:
            return False
        return True

    def get_next_token(self):
        if self.current_index >= len(self.file_text):
            raise Exception("There is no more input")
        # we can use the function defined in the DFA class but to improve the runtime speed we can use the function we defined in Scanner Class
        # current_state = self.dfa.get_start_state()
        current_state = self.get_start_state(self.dfa)
        # print(current_state)
        lexeme = ""
        current_line = self.line
        not_accepted = [StateType.SIMPLE, StateType.START]
        # while self.index < len(self.buffer) and current_state in not_accepted:
        # we can use the function defined in the DFA class but to improve the runtime speed we can use the function we defined in Scanner Class
        while self.current_index < len(self.file_text) and self.is_accepted(current_state):
        # while self.index < len(self.buffer) and current_state.is_accepted():
            # char = self.file_text[self.current_index]
            char = self.get_current_char()
            if char == '\n':
                self.line += 1
            self.current_index += 1
            lexeme = lexeme + char
            # we can use the function defined in the DFA class but to improve the runtime speed we can use the function we defined in Scanner Class
            current_state = self.next_char(self.dfa, current_state, char)
            # current_state = self.dfa.next_char(current_state, alphabet)

            # hold = None
            # if alphabet in current_state.transitions.keys():
            #     hold = current_state.transitions[alphabet]
            # if current_state.part_type == TokenTypes.COMMENT:
            #     hold = current_state.transitions['a']
            # else:
            #     hold = self.trash
            # current_state = hold

            # print(f'[{word}] -> {current_state}')

        token_type, token, char_to_return, error_message = current_state.move_forward(lexeme)

        if char_to_return != '':
            self.current_index -= 1
            if char_to_return == '\n':
                self.line -= 1
        if token_type == "ID" and token not in self.symbol_table:
            self.symbol_table.append(token)
        # we have already added the keywords to symbol table in constractor so no need to check for token_type == "KEYWORD"

        # if current_line == 14:
            # print(current_state, token_type, token, str(error_message),char_to_return)
        return current_line, token_type, token, str(error_message)

    def get_symbol_table(self):
        return self.symbol_table

    def get_current_line(self):
        return self.line

    def get_current_char(self):
        return self.file_text[self.current_index]

    def get_file_address(self):
        return self.file_address

    def get_dfa(self):
        return self.dfa

    def get_current_index(self):
        return self.current_index

    # def change(self):
    #     print("this is the change")
