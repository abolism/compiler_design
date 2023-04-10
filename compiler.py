"""
Abolfazl Eshagh 99101105
Zahra Alipour
"""

'''
testcase 1 : passed
testcase 2 : uncertain
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

if __name__ == "__main__":
    # dfa = get_dfa()
    # dfa = merge_dfas([comment_dfa, idKeyword_dfa, num_dfa, symbol_dfa, whitespace_dfa])
    # dfa = getDfa([commentDfa, id_KeywordDfa, numDfa, symbolDfa, whitespaceDfa])
    dfa = DFAs_merged
    scanner = Scanner(dfa, f"input.txt")
    ignore = ['WHITESPACE', 'COMMENT']
    tokens = ""
    errors = ""
    # symbol_table = ""
    hold_line = 0
    hold_line_for_error = 0
    while True:
        # print("inside while")
        try:
            # print("inside try")
            line, token_type, token, error_message = scanner.get_next_token()
            # print(token,type)
            # print("after get_next_token")
            # print(line, type, token, message,"this is testing")

            # first we handle errors
            if token_type == 'ERROR':
                # if error_message == "Invalid input" and line == 14:
                #     print(line,token_type, token, error_message)
                if line != hold_line_for_error:
                    if hold_line_for_error != 0:
                        errors += f"\n{line}.\t({token}, {error_message}) "
                        # hold_line_for_error = line
                    else:
                        errors += f"{line}.\t({token}, {error_message}) "
                    hold_line_for_error = line
                    # errors += f"\n {line} {token} {message}"
                    # hold_line = line
                    # hold_line_for_error = line
                else:
                    errors += f"({token}, {error_message}) "

            elif token_type != 'ERROR' and token_type not in ignore:
                if line != hold_line:
                    if hold_line != 0:
                        tokens += f"\n{line}.\t({token_type}, {token}) "
                        # hold_line = line
                    else:
                        tokens += f"{line}.\t({token_type}, {token}) "
                        # hold_line = line
                    hold_line = line
                else:
                    tokens += f"({token_type}, {token}) "



        except Exception as exp:
            # print("inside except in compiler.py/main")
            break

    if errors == "":
        errors = "There is no lexical error."
    with open("tokens.txt", "w") as f:
        f.write(tokens)
    with open("lexical_errors.txt", "w") as f:
        f.write(errors)

    # print(tokens)
    # print(errors)

    with open("symbol_table.txt", "w") as f:
        for i, token in enumerate(scanner.symbol_table):
            # f.write(f"\n{i+1}.\t{token}")
            f.write(f"{i + 1}.\t{token}\n")
    # print(scanner.symbol_table)
