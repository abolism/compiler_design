class Scanner:
    def __init__(self, dfa, input_file):
        self.dfa = dfa
        self.input_file = input_file
        self.file = open(input_file, "r")
        self.symbol_table = []
        self.current_char = self.file.read(1)
        self.current_index = 0
        self.current_line = 1
        # self.file.close()

    def get_next_token(self):
        if self.current_char == '':
            self.file.close()
            raise Exception("End of file reached!")

        state = self.dfa.start_state
        token = ""
        while True:
            state = self.dfa.get_next_state(state, self.current_char)
            if state is None:
                break
            token = token + self.current_char
            self.current_char = self.file.read(1)
            if self.current_char == '\n':
                self.current_line = self.current_line + 1

        if state in self.dfa.final_states:
            if state in self.dfa.accepting_states:
                if state == 'ID_KEYWORD':
                    if token in self.dfa.keywords:
                        return self.current_line, 'KEYWORD', token, None
                    else:
                        if token not in self.symbol_table:
                            self.symbol_table.append(token)
                        return self.current_line, 'ID', token, None
                elif state == 'NUM':
                    return self.current_line, 'NUM', token, None
                elif state == 'SYMBOL':
                    return self.current_line, 'SYMBOL', token, None
                elif state == 'COMMENT':
                    return self.current_line, 'COMMENT', token, None
            else:
                return self.current_line, 'WHITESPACE', token, None
        else:
            return self.current_line, 'ERROR', token, 'Invalid token!'

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

    def change(self):
        print("this is the change")