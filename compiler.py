"Abolfazl Eshagh 99101105"
"Zahra Alipour"


from dfaByType import commentDfa, id_KeywordDfa, numDfa, symbolDfa, whitespaceDfa

from dfa import DFA, merge_dfas
from DFAs.COMMENT_DFA import comment_dfa
from DFAs.ID_KEYWORD_DFA import idKeyword_dfa
from DFAs.NUM_DFA import num_dfa
from DFAs.SYMBOL_DFA import symbol_dfa
from DFAs.WHITESPACE_DFA import whitespace_dfa


from scanner import Scanner
# from dfa import DFA,get_dfa
if __name__ == "__main__":
    # dfa = get_dfa()
    # dfa = merge_dfas([comment_dfa, idKeyword_dfa, num_dfa, symbol_dfa, whitespace_dfa])
    dfa = merge_dfas([commentDfa, idKeyword_dfa, numDfa, symbolDfa, whitespaceDfa])
    scanner = Scanner(dfa, f"input.txt")
    ignore = ['WHITESPACE', 'COMMENT']
    tokens = ""
    errors = ""
    hold_line = 0
    hold_line_for_error = 0
    while True:
        # print("inside while")
        try:
            # print("inside try")
            line, type, token, message = scanner.get_next_token()
            # print(token,type)
            # print("after get_next_token")
            # print(line, type, token, message,"this is testing")
            if type not in ignore and type != 'ERROR':
                if line != hold_line :
                    if hold_line != 0:
                        tokens += f"\n{line}.\t({type}, {token}) "
                        hold_line = line
                    else:
                        tokens += f"{line}.\t({type}, {token}) "
                        hold_line = line
                else:
                    tokens += f"({type}, {token}) "

            elif type == 'ERROR':
                if line != hold_line_for_error:
                    if hold_line_for_error != 0:
                        errors += f"\n{line}.\t({token}, {message}) "
                        # hold_line_for_error = line
                    else:
                        errors += f"{line}.\t({token}, {message}) "
                    hold_line_for_error = line
                    # errors += f"\n {line} {token} {message}"
                    # hold_line = line
                    # hold_line_for_error = line
                else:
                    errors += f"({token}, {message}) "

        except Exception as exp:
            # print("inside except")
            break

    if errors == "":
        errors = "There is no lexical error."
    with open("tokens.txt", "w") as f:
        f.write(tokens)
    with open("lexical_errors.txt", "w") as f:
        f.write(errors)

    print(tokens)
    print(errors)

    with open("symbol_table.txt", "w") as f:
        for i, token in enumerate(scanner.symbol_table):
            # f.write(f"\n{i+1}.\t{token}")
            f.write(f"{i + 1}.\t{token}\n")
    print(scanner.symbol_table)