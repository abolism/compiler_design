# compiler phase two?

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def parse(self):
        return self.parse_program()

    def parse_program(self):
        return ('program', self.parse_declaration_list())

    def parse_declaration_list(self):
        declarations = []
        while self.peek_type() in ['int', 'void']:
            declarations.append(self.parse_declaration())
        return ('declaration_list', declarations)

    def parse_declaration(self):
        decl_initial = self.parse_declaration_initial()
        decl_prime = self.parse_declaration_prime()
        return ('declaration', decl_initial, decl_prime)

    def parse_declaration_initial(self):
        type_specifier = self.consume()
        id = self.consume()
        return ('declaration_initial', type_specifier, id)

    def parse_declaration_prime(self):
        if self.peek() == '(':
            return ('fun_declaration_prime', self.parse_fun_declaration_prime())
        else:
            return ('var_declaration_prime', self.parse_var_declaration_prime())

    def parse_var_declaration_prime(self):
        if self.peek() == ';':
            self.consume(';')
            return ('var_declaration_end',)
        elif self.peek() == '[':
            self.consume('[')
            num = int(self.consume())
            self.consume(']')
            self.consume(';')
            return ('var_declaration_array', num)

    def parse_fun_declaration_prime(self):
        self.consume('(')
        params = self.parse_params()
        self.consume(')')
        compound_stmt = self.parse_compound_stmt()
        return ('fun_declaration', params, compound_stmt)

    def parse_params(self):
        if self.peek() == 'int':
            type_specifier = self.consume()
            id = self.consume()
            param_prime = self.parse_param_prime()
            param_list = self.parse_param_list()
            return ('params_int', type_specifier, id, param_prime, param_list)
        elif self.peek() == 'void':
            type_specifier = self.consume()
            return ('params_void', type_specifier)

    def parse_param_list(self):
        params = []
        while self.peek() == ',':
            self.consume(',')
            params.append(self.parse_param())
        return ('param_list', params)

    def parse_param(self):
        decl_initial = self.parse_declaration_initial()
        param_prime = self.parse_param_prime()
        return ('param', decl_initial, param_prime)

    def parse_param_prime(self):
        if self.peek() == '[':
            self.consume('[')
            self.consume(']')
            return ('param_array',)
        else:
            return ('param_end',)

    # def parse_compound_stmt(self):
    #
    # # ...
    #
    # # ...

    def peek(self):
        if self.pos < len(self.tokens):
            return self.tokens[self.pos][1]
        else:
            return None

    def peek_type(self):
        if self.pos < len(self.tokens):
            return self.tokens[self.pos][0]
        else:
            return None

    def consume(self, expected=None):
        token = self.peek()
        if expected and token != expected:
            raise Exception(f"Expected {expected}, got {token}")
        self.pos += 1
        return token

    def print_parse_tree(self):
        print(self.parse())
        # print(self.ast)

    def get_parse_tree(self):
        return self.parse()


# Load the tokenized input from the file
with open('tokens.txt', 'r') as f:
    tokens = [tuple(line.strip().split()) for line in f]

# Create a new parser object
parser = Parser(tokens)

# Parse the tokenized input
ast = parser.parse()

# Print the AST
print(ast)