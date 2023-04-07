"Abolfazl Eshagh 99101105"
"Zahra Alipour"



from scanner import Scanner
from dfa import getDfa
if __name__ == "__main__":
    dfa = getDfa()
    scanner = Scanner(dfa, f"input.txt")
    ignore = ['WHITESPACE', 'COMMENT']
    tokens = ""
    errors = ""
    hold_line = 0
    while True:
        try:
            line, type, token, message = scanner.get_next_token()
            # print(line, type, token, message)
            if type not in ignore and type != 'ERROR':
                if line != hold_line:
                    tokens += f"\n {line} {type} {token}"
                    hold_line = line
                else:
                    tokens += f"{type} {token}"

            elif type == 'ERROR':
                if line != hold_line:
                    errors += f"\n {line} {token} {message}"
                    hold_line = line
                else:
                    errors += f"{token} {message}"

        except Exception as exp:
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
            f.write(f"{i} {token}")

    print(scanner.symbol_table)