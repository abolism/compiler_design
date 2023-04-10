from typing import Tuple
from dfa import StateType, TokenType
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
        file = open(input_file, "r")
        self.buffer = file.read()
        self.index = 0
        self.line = 1
        self.symbol_table = ["break", "else", "if", "int", "repeat", "return", "until", "void"]
        file.close()

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

    def get_next_token(self) -> Tuple[str, str]:
        if self.index >= len(self.buffer):
            raise Exception("no more input")
        current_state = self.dfa.get_start_state()
        # print(current_state)
        word = ""
        before_line = self.line
        # not_accepted_states = [StateTypes.SIMPLE, StateTypes.START]
        not_accepted = [StateType.SIMPLE, StateType.START]
        # while self.index < len(self.buffer) and current_state in not_accepted:
        while self.index < len(self.buffer) and current_state.is_accepted():
            alphabet = self.buffer[self.index]
            if alphabet == '\n':
                self.line += 1
            self.index += 1
            word = word + alphabet
            current_state = self.dfa.next_char(current_state, alphabet)
            # hold = None
            # if alphabet in current_state.transitions.keys():
            #     hold = current_state.transitions[alphabet]
            # if current_state.part_type == TokenTypes.COMMENT:
            #     hold = current_state.transitions['a']
            # else:
            #     hold = self.trash
            # current_state = hold
            # print(f'[{word}] -> {current_state}')

        type, token, deleted_character, error_message = current_state.move_forward(word)
        if type == "ID" and not token in self.symbol_table:
            self.symbol_table.append(token)
        if deleted_character:
            self.index -= 1
            if deleted_character == '\n':
                self.line -= 1
        return before_line, type, token, str(error_message)

    def get_symbol_table(self):
        return self.symbol_table

    def get_current_line(self):
        return self.current_line

    def get_current_char(self):
        return self.current_char

    def get_input_file(self):
        return self.input_file

    def get_dfa(self):
        return self.dfa

    # def change(self):
    #     print("this is the change")