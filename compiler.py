"""
Abolfazl Eshagh 99101105
"""

'''
phase 1, Scanner
testcase 1 : passed
testcase 2 : passed
testcase 3 : passed
testcase 4 : passed
testcase 5 : passed
testcase 6 : passed
testcase 7 : passed
testcase 8 : passed
testcase 9 : passed
testcase 10 : passed
'''

from dfa import get_dfa
from dfaByType import commentDfa, id_KeywordDfa, numDfa, symbolDfa, whitespaceDfa, DFAs_merged
from scanner import Scanner
from parser1 import Parser
'''
but by running the line above we get an error saying : ImportError: cannot import name 'Parser' from 'parser' (unknown location)
so I changed the name of parser1.py to parser1.py and then I could import it
'''

if __name__ == "__main__":
    dfa = DFAs_merged
    scanner = Scanner(dfa, f"input.txt")
    ignore = ['WHITESPACE', 'COMMENT']
    tokens = ""
    errors = ""
    hold_line = 0
    hold_line_for_error = 0
    while True:
        try:
            line, token_type, token, error_message = scanner.get_next_token()

            # first we handle errors
            if token_type == 'ERROR':
                if line != hold_line_for_error:
                    if hold_line_for_error != 0:
                        errors += f"\n{line}.\t({token}, {error_message}) "
                    else:
                        errors += f"{line}.\t({token}, {error_message}) "
                    hold_line_for_error = line
                else:
                    errors += f"({token}, {error_message}) "

            elif token_type != 'ERROR' and token_type not in ignore:
                if line != hold_line:
                    if hold_line != 0:
                        tokens += f"\n{line}.\t({token_type}, {token}) "
                    else:
                        tokens += f"{line}.\t({token_type}, {token}) "
                    hold_line = line
                else:
                    tokens += f"({token_type}, {token}) "



        except Exception as exp:
            break

    if errors == "":
        errors = "There is no lexical error."
    with open("tokens.txt", "w") as f:
        f.write(tokens)
    with open("lexical_errors.txt", "w") as f:
        f.write(errors)

    with open("symbol_table.txt", "w") as f:
        for i, token in enumerate(scanner.symbol_table):
            f.write(f"{i + 1}.\t{token}\n")

    parser = Parser("tokens.txt")
    parser.parse()
    parser.print_parse_tree()
    parse_tree = parser.get_parse_tree()

    '''
    now we want to print the parse tree in a file
    '''
    with open("parse_tree.txt", "w") as f:
        f.write(str(parse_tree))


