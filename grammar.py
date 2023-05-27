# grammar = {
#     "terminals": [
#         "$",
#         "(",
#         ")",
#         "*",
#         "+",
#         ",",
#         "-",
#         "/",
#         ":",
#         ";",
#         "<",
#         "=",
#         "[",
#         "]",
#         "{",
#         "}",
#         "NUM",
#         "ID",
#         "repeat",
#         "until",
#         "int",
#         "void",
#         "break",
#         "if",
#         "endif",
#         "else",
#         "while",
#         "return",
#         "switch",
#         "case",
#         "default",
#         "=="
#     ],
#     "non_terminals": [
#         "$accept",
#         "Program",
#         "Declaration-list",
#         "Declaration",
#         "Declaration-initial",
#         "Declaration-prime",
#         "Var-declaration-prime",
#         "Fun-declaration-prime",
#         "Type-specifier",
#         "Params",
#         "Param-list",
#         "Param",
#         "Param-prime",
#         "Compound-stmt",
#         "Statement-list",
#         "Statement",
#         "Expression-stmt",
#         "Selection_stmt",
#         "Iteration_stmt",
#         "Return_stmt",
#         "Return_stmt",
#         "Expression",
#         "B",
#         "H",
#         "Simple_expression_zegond",
#         "Simple_expression_prime",
#         "C",
#         "Relop",
#         "Additive_expression",
#         "Additive_expression_prime",
#         "Additive_expression_zegond",
#         "D",
#         "Addop",
#         "Term",
#         "Term_prime",
#         "Term_zegond",
#         "G",
#         "Factor",
#         "Var_call_prime",
#         "Var_prime",
#         "Factor_prime",
#         "Factor_zegond",
#         "Args",
#         "Arg_list",
#         "Arg_list_prime"
#         # "case_condition",
#         # "dummy_save",
#         # "jpf"
#     ],
#     "grammar": {
#         "0": [
#             "$accept",
#             "->",
#             "program",
#             "$"
#         ],
#         "1": [
#             "program",
#             "->",
#             "declaration_list"
#         ],
#         "2": [
#             "declaration_list",
#             "->",
#             "declaration",
#             "declaration_list"
#         ],
#         "3": [
#             "declaration_list",
#             "->",
#             "epsilon"
#         ],
#         "4": [
#             "declaration",
#             "->",
#             "declaration_initial",
#             "declaration_prime"
#         ],
#         "5": [
#             "declaration_initial",
#             "->",
#             "type_specifier",
#             "id"
#         ],
#         "6": [
#             "declaration_prime",
#             "->",
#             "fun_declaration_prime"
#         ],
#         "7": [
#             "declaration_prime",
#             "->",
#             "var_declaration_prime"
#         ],
#         "8": [
#             "var_declaration_prime",
#             "->",
#             ";"
#         ],
#         "9": [
#             "var_declaration_prime",
#             "->",
#             "[",
#             "NUM",
#             "]",
#             ";"
#         ],
#         "10": [
#             "fun_declaration_prime",
#             "->",
#             "(",
#             "params",
#             ")",
#             "compound_stmt"
#         ],
#         "11": [
#             "type_specifier",
#             "->",
#             "int"
#         ],
#         "12": [
#             "type_specifier",
#             "->",
#             "void"
#         ],
#         "13": [
#             "params",
#             "->",
#             "int",
#             "id",
#             "param_prime",
#             "param_list"
#         ],
#         "14": [
#             "params",
#             "->",
#             "void"
#         ],
#         "15": [
#             "param_list",
#             "->",
#             ",",
#             "param",
#             "param_list"
#         ],
#         "16": [
#             "param_list",
#             "->",
#             "epsilon"
#         ],
#         "17": [
#             "param",
#             "->",
#             "declaration_initial",
#             "param_prime"
#         ],
#         "18": [
#             "param_prime",
#             "->",
#             "[",
#             "]"
#         ],
#         "19": [
#             "param_prime",
#             "->",
#             "epsilon"
#         ],
#         "20": [
#             "compound_stmt",
#             "->",
#             "{",
#             "declaration_list",
#             "statement_list",
#             "}"
#         ],
#         "21": [
#             "statement_list",
#             "->",
#             "statement",
#             "statement_list"
#         ],
#         "22": [
#             "statement_list",
#             "->",
#             "epsilon"
#         ],
#         "23": [
#             "statement",
#             "->",
#             "expression_stmt"
#         ],
#         "24": [
#             "statement",
#             "->",
#             "compound_stmt"
#         ],
#         "25": [
#             "statement",
#             "->",
#             "selection_stmt"
#         ],
#         "26": [
#             "statement",
#             "->",
#             "iteration_stmt"
#         ],
#         "27": [
#             "statement",
#             "->",
#             "return_stmt"
#         ],
#         "28": [
#             "expression_stmt",
#             "->",
#             "expression",
#             ";"
#         ],
#         "29": [
#             "expression_stmt",
#             "->",
#             "break",
#             ";"
#         ],
#         "30": [
#             "expression_stmt",
#             "->",
#             ";"
#         ],
#         "31": [
#             "selection_stmt",
#             "->",
#             "if",
#             "(",
#             "expression",
#             ")",
#             "statement",
#             "else",
#             "statement"
#         ],
#         "32": [
#             "iteration_stmt",
#             "->",
#             "repeat",
#             "statement",
#             "until",
#             "(",
#             "expression",
#             ")"
#         ],
#         "33": [
#             "return_stmt",
#             "->",
#             "return",
#             "return_stmt_prime"
#         ],
#         "34": [
#             "return_stmt_prime",
#             "->",
#             ";"
#         ],
#         "35": [
#             "return_stmt_prime",
#             "->",
#             "expression",
#             ";"
#         ],
#         "36": [
#             "expression",
#             "->",
#             "simple_expression_zegond"
#         ],
#         "37": [
#             "expression",
#             "->",
#             "id",
#             "b"
#         ],
#         "38": [
#             "b",
#             "->",
#             "expression"
#         ],
#         "39": [
#             "b",
#             "->",
#             "[",
#             "expression",
#             "]",
#             "h"
#         ],
#         "40": [
#             "b",
#             "->",
#             "simple_expression_prime"
#         ],
#         "41": [
#             "h",
#             "->",
#             "=",
#             "expression"
#         ],
#         "42": [
#             "h",
#             "->",
#             "g",
#             "d",
#             "c"
#         ],
#         "43": [
#             "simple_expression_zegond",
#             "->",
#             "additive_expression_zegond",
#             "c"
#         ],
#         "44": [
#             "simple_expression_prime",
#             "->",
#             "additive_expression_prime",
#             "c"
#         ],
#         "45": [
#             "c",
#             "->",
#             "relop",
#             "additive_expression"
#         ],
#         "46": [
#             "c",
#             "->",
#             "epsilon"
#         ],
#         "47": [
#             "relop",
#             "->",
#             "<"
#         ],
#         "48": [
#             "relop",
#             "->",
#             "=="
#         ],
#         "49": [
#             "additive_expression",
#             "->",
#             "term",
#             "d"
#         ],
#         "50": [
#             "additive_expression_prime",
#             "->",
#             "term_prime",
#             "d"
#         ],
#         "51": [
#             "additive_expression_zegond",
#             "->",
#             "term_zegond",
#             "d"
#         ],
#         "52": [
#             "d",
#             "->",
#             "addop",
#             "term",
#             "d"
#         ],
#         "53": [
#             "d",
#             "->",
#             "epsilon"
#         ],
#         "54": [
#             "addop",
#             "->",
#             "+"
#         ],
#         "55": [
#             "addop",
#             "->",
#             "-"
#         ],
#         "56": [
#             "term",
#             "->",
#             "factor",
#             "g"
#         ],
#         "57": [
#             "term_prime",
#             "->",
#             "factor_prime",
#             "g"
#         ],
#         "58": [
#             "term_zegond",
#             "->",
#             "factor_zegond",
#             "g"
#         ],
#         "59": [
#             "g",
#             "->",
#             "*",
#             "factor",
#             "g"
#         ],
#         "60": [
#             "g",
#             "->",
#             "epsilon"
#         ],
#         "61": [
#             "factor",
#             "->",
#             "(",
#             "expression",
#             ")"
#         ],
#         "62": [
#             "factor",
#             "->",
#             "id",
#             "var_call_prime"
#         ],
#         "63": [
#             "factor",
#             "->",
#             "num"
#         ],
#         "64": [
#             "var_call_prime",
#             "->",
#             "args"
#         ],
#         "65": [
#             "var_call_prime",
#             "->",
#             "var_prime"
#         ],
#         "66": [
#             "var_prime",
#             "->",
#             "[",
#             "expression",
#             "]"
#         ],
#         "67": [
#             "var_prime",
#             "->",
#             "epsilon"
#         ],
#         "68": [
#             "factor_prime",
#             "->",
#             "(",
#             "args",
#             ")"
#         ],
#         "69": [
#             "factor_prime",
#             "->",
#             "epsilon"
#         ],
#         "70": [
#             "factor_zegond",
#             "->",
#             "(",
#             "expression",
#             ")"
#         ],
#         "71": [
#             "factor_zegond",
#             "->",
#             "num"
#         ],
#         "72": [
#             "args",
#             "->",
#             "arg_list"
#         ],
#         "73": [
#             "args",
#             "->",
#             "epsilon"
#         ],
#         "74": [
#             "arg_list",
#             "->",
#             "expression",
#             "arg_list_prime"
#         ],
#         "75": [
#             "arg_list_prime",
#             "->",
#             ",",
#             "expression",
#             "arg_list_prime"
#         ],
#         "76": [
#             "arg_list_prime",
#             "->",
#             "epsilon"
#         ]
#
#     },
#     "first": {
#         "$accept": [
#             "int",
#             "void"
#         ],
#         "program": [
#             "int",
#             "void",
#             "epsilon"
#         ],
#         "declaration_list": [
#             "int",
#             "void",
#             "epsilon"
#         ],
#         "declaration": [
#             "int",
#             "void"
#         ],
#         "declaration_initial": [
#             "int",
#             "void"
#         ],
#         "declaration_prime": [
#             ";",
#             "[",
#             "("
#         ],
#         "var_declaration_prime": [
#             ";",
#             "["
#         ],
#         "fun_declaration_prime": [
#             "("
#         ],
#         "type_specifier": [
#             "int",
#             "void"
#         ],
#         "params": [
#             "int",
#             "void"
#         ],
#         "param_list": [
#             ",",
#             "epsilon"
#         ],
#         "param": [
#             "int",
#             "void"
#         ],
#         "param_prime": [
#             "[",
#             "epsilon"
#         ],
#         "compound_stmt": [
#             "{"
#         ],
#         "statement_list": [
#             "{",
#             "return",
#             "if",
#             "(",
#             "{",
#             "break",
#             "repeat",
#             ";",
#             "ID",
#             "epsilon"
#         ],
#         "statement": [
#             "{",
#             "return",
#             "if",
#             "(",
#             "{",
#             "break",
#             "repeat",
#             ";",
#             "ID"
#         ],
#         "expression_stmt": [
#             "(",
#             "{",
#             "break",
#             ";",
#             "ID"
#         ],
#         "selection_stmt": [
#             "if"
#         ],
#         "iteration_stmt": [
#             "repeat"
#         ],
#         "return_stmt": [
#             "return"
#         ],
#         "return_stmt_prime": [
#             "(",
#             "{",
#             ";",
#             "ID"
#         ],
#         "expression": [
#             "(",
#             "{",
#             "ID"
#         ],
#         "b": [
#             "(",
#             "==",
#             "<",
#             "=",
#             "+",
#             "-",
#             "*",
#             "epsilon"
#         ],
#         "h": [
#             "==",
#             "<",
#             "=",
#             "+",
#             "-",
#             "*",
#             "epsilon"
#         ],
#         "simple_expression_zegond": [
#             "num",
#             "("
#         ],
#         "simple_expression_prime": [
#             "(",
#             "==",
#             "<",
#             "+",
#             "-",
#             "*",
#             "epsilon"
#
#         ],
#         "c": [
#             "==",
#             "<",
#             "epsilon"
#         ],
#         "relop": [
#             "==",
#             "<"
#         ],
#         "additive_expression": [
#             "(",
#             "NUM",
#             "ID"
#         ],
#         "additive_expression_prime": [
#             "epsilon",
#             "*",
#             "+",
#             "-",
#             "("
#         ],
#         "additive_expression_zegond": [
#             "(",
#             "num"
#         ],
#         "d": [
#             "+",
#             "-",
#             "epsilon"
#         ],
#         "addop": [
#             "+",
#             "-"
#         ],
#         "term": [
#             "(",
#             "NUM",
#             "ID"
#         ],
#         "term_prime": [
#             "(",
#             "*",
#             "epsilon"
#         ],
#         "term_zegond": [
#             "(",
#             "num"
#         ],
#         "g": [
#             "*",
#             "epsilon"
#         ],
#         "factor": [
#             "(",
#             "NUM",
#             "ID"
#         ],
#         "var_call_prime": [
#             "(",
#             "[",
#             "epsilon"
#         ],
#         "var_prime": [
#             "[",
#             "epsilon"
#         ],
#         "factor_prime": [
#             "(",
#             "epsilon"
#         ],
#         "factor_zegond": [
#             "(",
#             "num"
#         ],
#         "args": [
#             "(",
#             "NUM",
#             "ID",
#             "epsilon"
#         ],
#         "arg_list": [
#             "(",
#             "NUM",
#             "ID"
#         ],
#         "Arg_list_prime": [
#             ",",
#             "epsilon"
#         ]
#     },
#     # #now based on the grammar and first set we want to find the follow set
#     # "follow": {
#
#     "follow": {
#         "$accept": [],
#         "Program": [
#             "$"
#         ],
#         "Declaration_list": [
#             "id",
#             ";",
#             "num",
#             "(",
#             "{",
#             "}",
#             "break",
#             "if",
#             "return,"
#             "$"
#         ],
#         "Declaration": [
#             "id",
#             ";",
#             "num",
#             "(",
#             "{",
#             "}",
#             "break",
#             "if",
#             "return,"
#             "$",
#             "int",
#             "void"
#         ],
#         "Declaration_initial": [
#             ";",
#             "[",
#             "(",
#             ")",
#             ","
#         ],
#         "Declaration_prime": [
#             "id",
#             ";",
#             "num",
#             "(",
#             "{",
#             "}",
#             "break",
#             "if",
#             "return",
#             "int",
#             "void",
#             "repeat",
#             "$"
#         ],
#         "Var_declaration_prime": [
#             "id",
#             ";",
#             "num",
#             "(",
#             "int",
#             "void",
#             "{",
#             "}",
#             "break",
#             "if",
#             "return",
#             "repeat",
#             "$"
#         ],
#         "Fun_declaration_prime": [
#             "id",
#             ";",
#             "num",
#             "(",
#             "int",
#             "void",
#             "{",
#             "}",
#             "break",
#             "if",
#             "return",
#             "repeat",
#             "$"
#         ],
#         "Type_specifier": [
#             "id"
#         ],
#         "Params": [
#             ")"
#         ],
#         "Param_list": [
#             ")"
#         ],
#         "Param": [
#             ",",
#             "("
#         ],
#         "Param_prime": [
#             ",",
#             "("
#         ],
#         "Compound_stmt": [
#             "id",
#             ";",
#             "num",
#             "(",
#             "int",
#             "void",
#             "{",
#             "}",
#             "break",
#             "if",
#             "return",
#             "repeat",
#             "$",
#             "else",
#             "until"
#         ],
#         "Statement_list": [
#             "}"
#         ],
#         "Statement": [
#             "id",
#             ";",
#             "num",
#             "(",
#             "{",
#             "}",
#             "break",
#             "if",
#             "return,"
#             "else",
#             "until"
#         ],
#         "Expression_stmt": [
#             "id",
#             ";",
#             "num",
#             "(",
#             "{",
#             "}",
#             "break",
#             "if",
#             "return,"
#             "else",
#             "until"
#         ],
#         "Selection_stmt": [
#             "id",
#             ";",
#             "num",
#             "(",
#             "{",
#             "}",
#             "break",
#             "if",
#             "return,"
#             "else",
#             "until"
#         ],
#         "Iteration_stmt": [
#             "id",
#             ";",
#             "num",
#             "(",
#             "{",
#             "}",
#             "break",
#             "if",
#             "return,"
#             "else",
#             "until"
#         ],
#         "Return_stmt": [
#             "id",
#             ";",
#             "num",
#             "(",
#             "{",
#             "}",
#             "break",
#             "if",
#             "return,"
#             "else",
#             "until"
#         ],
#         "Return_stmt_prime": [
#             "id",
#             ";",
#             "num",
#             "(",
#             "{",
#             "}",
#             "break",
#             "if",
#             "return,"
#             "else",
#             "until"
#         ],
#         "Expression": [
#             ";",
#             ")",
#             "]",
#             ","
#         ],
#         "b": [
#             ";",
#             ")",
#             "]",
#             ","
#         ],
#         "h": [
#             ";",
#             ")",
#             "]",
#             ","
#         ],
#         "simple_expression_zegond": [
#             ";",
#             ")",
#             "]",
#             ","
#         ],
#         "Simple_expression_prime": [
#             ";",
#             ")",
#             "]",
#             ","
#         ],
#         "c": [
#             ";",
#             ")",
#             "]",
#             ","
#         ],
#         "Relop": [
#             "(",
#             "NUM",
#             "ID"
#         ],
#         "Var": [
#             ";",
#             ")"
#         ],
#         "Additive_expression": [
#             ";",
#             ")",
#             "]",
#             ","
#         ],
#         "Additive_expression_prime": [
#             ";",
#             ")",
#             "]",
#             ",",
#             "<",
#             "=="
#         ],
#         # "Simple_expression": [
#         #     ";",
#         #     ")"
#         # ],
#
#
#         "Additive_expression_zegond": [
#             ";",
#             ")",
#             "]",
#             ",",
#             "<",
#             "=="
#         ],
#         "D": [
#             ";",
#             ")",
#             "]",
#             ",",
#             "<",
#             "=="
#         ],
#         "Addop": [
#             "(",
#             "NUM",
#             "ID"
#         ],
#         "Term": [
#             ";",
#             ")",
#             "]",
#             ",",
#             "<",
#             "==",
#             "+",
#             "-"
#         ],
#         "Term_prime": [
#             ";",
#             ")",
#             "]",
#             ",",
#             "<",
#             "==",
#             "+",
#             "-"
#         ],
#         "Term_zegond": [
#             ";",
#             ")",
#             "]",
#             ",",
#             "<",
#             "==",
#             "+",
#             "-"
#         ],
#         "G": [
#             ";",
#             ")",
#             "]",
#             ",",
#             "<",
#             "==",
#             "+",
#             "-"
#         ],
#         "Factor": [
#             ";",
#             ")",
#             "]",
#             ",",
#             "<",
#             "==",
#             "+",
#             "-",
#             "*"
#         ],
#         "Var_call_prime": [
#             ";",
#             ")",
#             "]",
#             ",",
#             "<",
#             "==",
#             "+",
#             "-",
#             "*"
#         ],
#         "Var_prime": [
#             ";",
#             ")",
#             "]",
#             ",",
#             "<",
#             "==",
#             "+",
#             "-",
#             "*"
#         ],
#         "Factor_prime": [
#             ";",
#             ")",
#             "]",
#             ",",
#             "<",
#             "==",
#             "+",
#             "-",
#             "*"
#         ],
#         "Factor_zegond": [
#             ";",
#             ")",
#             "]",
#             ",",
#             "<",
#             "==",
#             "+",
#             "-",
#             "*"
#         ],
#         "Args": [
#             ")"
#         ],
#         "Arg_list": [
#             ")"
#         ],
#         "Arg_list_prime": [
#             ")"
#         ]
#     },
#     #now using first sets, follow sets, and the grammar rules above, we want to implement parse table
#     #parse table is a 2D array, each row is a non-terminal, and each column is a terminal
#     "parse_table": {
#         "Program": {
#             "id": ["Declaration_list"],
#             "int": ["Declaration_list"],
#             "void": ["Declaration_list"],
#             "$": ["Declaration_list"]
#         },
#         "Declaration_list": {
#             "id": ["Declaration", "Declaration_list_prime"],
#             "int": ["Declaration", "Declaration_list_prime"],
#             "void": ["Declaration", "Declaration_list_prime"],
#             "$": ["Declaration", "Declaration_list_prime"]
#         },
#         "Declaration_list_prime": {
#             "id": ["Declaration", "Declaration_list_prime"],
#             "int": ["Declaration", "Declaration_list_prime"],
#             "void": ["Declaration", "Declaration_list_prime"],
#             "$": []
#         },
#         "Declaration": {
#             "id": ["Type_specifier", "id", "Declaration_prime"],
#             "int": ["Type_specifier", "id", "Declaration_prime"],
#             "void": ["Type_specifier", "id", "Declaration_prime"]
#         },
#         "Declaration_prime": {
#             "(": ["Fun_declaration"],
#             "[": ["Var_declaration"]
#         },
#         "Var_declaration": {
#             "[": ["[", "num", "]", ";"]
#         },
#         "Type_specifier": {
#             "id": ["id"],
#             "int": ["int"],
#             "void": ["void"]
#         },
#         "Fun_declaration": {
#             "(": ["(", "Params", "Compound_stmt"]
#         },
#         "Params": {
#             "int": ["int", "id", "Param_list"],
#             "void": ["void", "Params_prime"]
#         },
#         "Param_list": {
#             "int": ["Param", "Param_prime"],
#             "void": ["Param", "Param_prime"]
#         },
#         "Param": {
#             "int": ["int", "id"],
#             "void": ["void", "id"]
#         },
#         "Param_prime": {
#             ",": [",", "Param", "Param_prime"],
#             ")": []
#         },
#         "Compound_stmt": {
#             "{": ["{", "Local_declarations", "Statement_list", "}"]
#         },
#         "Statement_list": {
#             "}": []
#         },
#         "Statement": {
#             "id": ["Expression_stmt"],
#             ";": ["Expression_stmt"],
#             "num": ["Expression_stmt"],
#             "(": ["Expression_stmt"],
#             "{": ["Expression_stmt"],
#             "if": ["Selection_stmt"],
#             "while": ["Iteration_stmt"],
#             "return": ["Return_stmt"]
#         },
#         "Expression_stmt": {
#             "id": ["Expression", ";"],
#             ";": [";"],
#             "num": ["Expression", ";"],
#             "(": ["Expression", ";"],
#             "{": ["Expression", ";"]
#         },
#         "Selection_stmt": {
#             "if": ["if", "(", "Expression", ")", "Statement", "Selection_stmt_prime"]
#         },
#         "Selection_stmt_prime": {
#             "else": ["else", "Statement"],
#             ";": [";"]
#         },
#         "Iteration_stmt": {
#             "while": ["while", "(", "Expression", ")", "Statement"]
#         },
#         "Return_stmt": {
#             "return": ["return", "Return_stmt_prime"]
#         },
#         "Return_stmt_prime": {
#             ";": [";"],
#             "id": ["Expression", ";"],
#             "num": ["Expression", ";"],
#             "(": ["Expression", ";"],
#             "{": ["Expression", ";"]
#         },
#         "Expression": {
#             "id": ["Var", "=", "Expression_zegond"],
#             "num": ["Simple_expression"],
#             "(": ["Simple_expression"],
#             ";": ["Simple_expression"],
#             ")": ["Simple_expression"],
#             "]": ["Simple_expression"],
#             ",": ["Simple_expression"],
#             "<": ["Simple_expression"],
#             "==": ["Simple_expression"]
#         },
#         "Expression_zegond": {
#             ";": ["Simple_expression"],
#             ")": ["Simple_expression"],
#             "]": ["Simple_expression"],
#             ",": ["Simple_expression"],
#             "<": ["Simple_expression"],
#             "==": ["Simple_expression"],
#             "id": ["Simple_expression"],
#             "num": ["Simple_expression"],
#             "(": ["Simple_expression"]
#         },
#         "Var": {
#             "id": ["id", "Var_prime"]
#         },
#         "Var_prime": {
#             "[": ["[", "Expression", "]"],
#             "=": [],
#             ";": [],
#             ")": [],
#             "]": [],
#             ",": [],
#             "<": [],
#             "==": []
#         },
#         "Simple_expression": {
#             ";": ["Additive_expression"],
#             ")": ["Additive_expression"],
#             "]": ["Additive_expression"],
#             ",": ["Additive_expression"],
#             "<": ["Additive_expression"],
#             "==": ["Additive_expression"],
#             "id": ["Additive_expression", "Simple_expression_prime"],
#             "num": ["Additive_expression", "Simple_expression_prime"],
#             "(": ["Additive_expression", "Simple_expression_prime"]
#         },
#         "Simple_expression_prime": {
#             ";": [],
#             ")": [],
#             "]": [],
#             ",": [],
#             "<": [],
#             "==": [],
#             "id": ["Relop", "Additive_expression"],
#             "num": ["Relop", "Additive_expression"],
#             "(": ["Relop", "Additive_expression"]
#         },
#         "Relop": {
#             "<": ["<"],
#             "==": ["=="]
#         },
#         "Additive_expression": {
#             "id": ["Term", "Additive_expression_prime"],
#             "num": ["Term", "Additive_expression_prime"],
#             "(": ["Term", "Additive_expression_prime"]
#         },
#         "Additive_expression_prime": {
#             ";": [],
#             ")": [],
#             "]": [],
#             ",": [],
#             "<": [],
#             "==": [],
#             "id": [],
#             "num": [],
#             "(": [],
#             "+": ["Addop", "Term", "Additive_expression_prime"],
#             "-": ["Addop", "Term", "Additive_expression_prime"]
#         },
#         "Addop": {
#             "+": ["+"],
#             "-": ["-"]
#         },
#         "Term": {
#             "id": ["Factor", "Term_prime"],
#             "num": ["Factor", "Term_prime"],
#             "(": ["Factor", "Term_prime"]
#         },
#         "Term_prime": {
#             ";": [],
#             ")": [],
#             "]": [],
#             ",": [],
#             "<": [],
#             "==": [],
#             "id": [],
#             "num": [],
#             "(": [],
#             "+": [],
#             "-": [],
#             "*": ["Mulop", "Factor", "Term_prime"],
#             "/": ["Mulop", "Factor", "Term_prime"]
#         },
#         "Mulop": {
#             "*": ["*"],
#             "/": ["/"]
#         },
#         "Factor": {
#             "id": ["id", "Factor_prime"],
#             "num": ["num"],
#             "(": ["(", "Expression", ")"]
#         },
#         "Factor_prime": {
#             "[": ["[", "Expression", "]"],
#             ";": [],
#             ")": [],
#             "]": [],
#             ",": [],
#             "<": [],
#             "==": [],
#             "id": [],
#             "num": [],
#             "(": [],
#             "*": [],
#             "/": [],
#             "+": [],
#             "-": [],
#             "=": []
#         },
#         "Call": {
#             "id": ["id", "(", "Args", ")"]
#         },
#         "Args": {
#             "id": ["Arg_list"],
#             "num": ["Arg_list"],
#             "(": ["Arg_list"],
#             ")": [],
#             ")": ["Arg_list"]
#         },
#         "Arg_list": {
#             "id": ["Expression", "Arg_list_prime"],
#             "num": ["Expression", "Arg_list_prime"],
#             "(": ["Expression", "Arg_list_prime"]
#         },
#         "Arg_list_prime": {
#             ")": [],
#             ")": [],
#             ",": ["Expression", "Arg_list_prime"]
#         }
#     }
# }
import nt

grammar = {
    'start_symbol': 'Program',
    'non_terminals': [
        "$accept",
        "Program",
        "Declaration_list",
        "Declaration",
        "Declaration_initial",
        "Declaration-prime",
        "Var-declaration-prime",
        "Fun-declaration-prime",
        "Type-specifier",
        "Params",
        "Param-list",
        "Param",
        "Param-prime",
        "Compound-stmt",
        "Statement-list",
        "Statement",
        "Expression-stmt",
        "Selection-stmt",
        "Else-stmt",
        "Iteration-stmt",
        "Return-stmt",
        "Return-stmt-prime",
        "Expression",
        "B",
        "H",
        "simple_expression-zegond",
        "Simple-expression-prime",
        "C",
        "Relop",
        "Additive-expression",
        "Additive-expression-prime",
        "Additive-expression-zegond",
        "D",
        "Addop",
        "Term",
        "Term-prime",
        "Term-zegond",
        "G",
        "Factor",
        "Var-call-prime",
        "Var-prime",
        "Factor-prime",
        "Factor-zegond",
        "Args",
        "Arg-list",
        "Arg-list-prime"
        # "case_condition",
        # "dummy_save",
        # "jpf"
    ],
    'terminals': [
        "id",
        ";",
        "num",
        "[",
        "]",
        "(",
        ")",
        "int",
        "void",
        ",",
        "{",
        "}",
        "break",
        "if",
        "else",
        "repeat",
        "until",
        "return",
        "=",
        "<",
        "==",
        "+",
        "-",
        "*",
        "epsilon"
    ],
    'productions': {
        # 'E': [['T', 'E_']],
        # 'E_': [['+', 'T', 'E_'], []],
        # 'T': [['int', 'T_']],
        # 'T_': [['*', 'int', 'T_'], []]

        # "0": [
        #     "$accept",
        #     "->",
        #     "program",
        #     "$"
        # ],
        # "1": [
        #     "program",
        #     "->",
        #     "declaration_list"
        # ],
        # "2": [
        #     "declaration_list",
        #     "->",
        #     "declaration",
        #     "declaration_list"
        # ],
        # "3": [
        #     "declaration_list",
        #     "->",
        #     "epsilon"
        # ],
        # "4": [
        #     "declaration",
        #     "->",
        #     "declaration_initial",
        #     "declaration_prime"
        # ],
        # "5": [
        #     "declaration_initial",
        #     "->",
        #     "type_specifier",
        #     "id"
        # ],
        # "6": [
        #     "declaration_prime",
        #     "->",
        #     "fun_declaration_prime"
        # ],
        # "7": [
        #     "declaration_prime",
        #     "->",
        #     "var_declaration_prime"
        # ],
        # "8": [
        #     "var_declaration_prime",
        #     "->",
        #     ";"
        # ],
        # "9": [
        #     "var_declaration_prime",
        #     "->",
        #     "[",
        #     "NUM",
        #     "]",
        #     ";"
        # ],
        # "10": [
        #     "fun_declaration_prime",
        #     "->",
        #     "(",
        #     "params",
        #     ")",
        #     "compound_stmt"
        # ],
        # "11": [
        #     "type_specifier",
        #     "->",
        #     "int"
        # ],
        # "12": [
        #     "type_specifier",
        #     "->",
        #     "void"
        # ],
        # "13": [
        #     "params",
        #     "->",
        #     "int",
        #     "id",
        #     "param_prime",
        #     "param_list"
        # ],
        # "14": [
        #     "params",
        #     "->",
        #     "void"
        # ],
        # "15": [
        #     "param_list",
        #     "->",
        #     ",",
        #     "param",
        #     "param_list"
        # ],
        # "16": [
        #     "param_list",
        #     "->",
        #     "epsilon"
        # ],
        # "17": [
        #     "param",
        #     "->",
        #     "declaration_initial",
        #     "param_prime"
        # ],
        # "18": [
        #     "param_prime",
        #     "->",
        #     "[",
        #     "]"
        # ],
        # "19": [
        #     "param_prime",
        #     "->",
        #     "epsilon"
        # ],
        # "20": [
        #     "compound_stmt",
        #     "->",
        #     "{",
        #     "declaration_list",
        #     "statement_list",
        #     "}"
        # ],
        # "21": [
        #     "statement_list",
        #     "->",
        #     "statement",
        #     "statement_list"
        # ],
        # "22": [
        #     "statement_list",
        #     "->",
        #     "epsilon"
        # ],
        # "23": [
        #     "statement",
        #     "->",
        #     "expression_stmt"
        # ],
        # "24": [
        #     "statement",
        #     "->",
        #     "compound_stmt"
        # ],
        # "25": [
        #     "statement",
        #     "->",
        #     "selection_stmt"
        # ],
        # "26": [
        #     "statement",
        #     "->",
        #     "iteration_stmt"
        # ],
        # "27": [
        #     "statement",
        #     "->",
        #     "return_stmt"
        # ],
        # "28": [
        #     "expression_stmt",
        #     "->",
        #     "expression",
        #     ";"
        # ],
        # "29": [
        #     "expression_stmt",
        #     "->",
        #     "break",
        #     ";"
        # ],
        # "30": [
        #     "expression_stmt",
        #     "->",
        #     ";"
        # ],
        # "31": [
        #     "selection_stmt",
        #     "->",
        #     "if",
        #     "(",
        #     "expression",
        #     ")",
        #     "statement",
        #     "else",
        #     "statement"
        # ],
        # "32": [
        #     "iteration_stmt",
        #     "->",
        #     "repeat",
        #     "statement",
        #     "until",
        #     "(",
        #     "expression",
        #     ")"
        # ],
        # "33": [
        #     "return_stmt",
        #     "->",
        #     "return",
        #     "return_stmt_prime"
        # ],
        # "34": [
        #     "return_stmt_prime",
        #     "->",
        #     ";"
        # ],
        # "35": [
        #     "return_stmt_prime",
        #     "->",
        #     "expression",
        #     ";"
        # ],
        # "36": [
        #     "expression",
        #     "->",
        #     "simple_expression_zegond"
        # ],
        # "37": [
        #     "expression",
        #     "->",
        #     "id",
        #     "b"
        # ],
        # "38": [
        #     "b",
        #     "->",
        #     "expression"
        # ],
        # "39": [
        #     "b",
        #     "->",
        #     "[",
        #     "expression",
        #     "]",
        #     "h"
        # ],
        # "40": [
        #     "b",
        #     "->",
        #     "simple_expression_prime"
        # ],
        # "41": [
        #     "h",
        #     "->",
        #     "=",
        #     "expression"
        # ],
        # "42": [
        #     "h",
        #     "->",
        #     "g",
        #     "d",
        #     "c"
        # ],
        # "43": [
        #     "simple_expression_zegond",
        #     "->",
        #     "additive_expression_zegond",
        #     "c"
        # ],
        # "44": [
        #     "simple_expression_prime",
        #     "->",
        #     "additive_expression_prime",
        #     "c"
        # ],
        # "45": [
        #     "c",
        #     "->",
        #     "relop",
        #     "additive_expression"
        # ],
        # "46": [
        #     "c",
        #     "->",
        #     "epsilon"
        # ],
        # "47": [
        #     "relop",
        #     "->",
        #     "<"
        # ],
        # "48": [
        #     "relop",
        #     "->",
        #     "=="
        # ],
        # "49": [
        #     "additive_expression",
        #     "->",
        #     "term",
        #     "d"
        # ],
        # "50": [
        #     "additive_expression_prime",
        #     "->",
        #     "term_prime",
        #     "d"
        # ],
        # "51": [
        #     "additive_expression_zegond",
        #     "->",
        #     "term_zegond",
        #     "d"
        # ],
        # "52": [
        #     "d",
        #     "->",
        #     "addop",
        #     "term",
        #     "d"
        # ],
        # "53": [
        #     "d",
        #     "->",
        #     "epsilon"
        # ],
        # "54": [
        #     "addop",
        #     "->",
        #     "+"
        # ],
        # "55": [
        #     "addop",
        #     "->",
        #     "-"
        # ],
        # "56": [
        #     "term",
        #     "->",
        #     "factor",
        #     "g"
        # ],
        # "57": [
        #     "term_prime",
        #     "->",
        #     "factor_prime",
        #     "g"
        # ],
        # "58": [
        #     "term_zegond",
        #     "->",
        #     "factor_zegond",
        #     "g"
        # ],
        # "59": [
        #     "g",
        #     "->",
        #     "*",
        #     "factor",
        #     "g"
        # ],
        # "60": [
        #     "g",
        #     "->",
        #     "epsilon"
        # ],
        # "61": [
        #     "factor",
        #     "->",
        #     "(",
        #     "expression",
        #     ")"
        # ],
        # "62": [
        #     "factor",
        #     "->",
        #     "id",
        #     "var_call_prime"
        # ],
        # "63": [
        #     "factor",
        #     "->",
        #     "num"
        # ],
        # "64": [
        #     "var_call_prime",
        #     "->",
        #     "args"
        # ],
        # "65": [
        #     "var_call_prime",
        #     "->",
        #     "var_prime"
        # ],
        # "66": [
        #     "var_prime",
        #     "->",
        #     "[",
        #     "expression",
        #     "]"
        # ],
        # "67": [
        #     "var_prime",
        #     "->",
        #     "epsilon"
        # ],
        # "68": [
        #     "factor_prime",
        #     "->",
        #     "(",
        #     "args",
        #     ")"
        # ],
        # "69": [
        #     "factor_prime",
        #     "->",
        #     "epsilon"
        # ],
        # "70": [
        #     "factor_zegond",
        #     "->",
        #     "(",
        #     "expression",
        #     ")"
        # ],
        # "71": [
        #     "factor_zegond",
        #     "->",
        #     "num"
        # ],
        # "72": [
        #     "args",
        #     "->",
        #     "arg_list"
        # ],
        # "73": [
        #     "args",
        #     "->",
        #     "epsilon"
        # ],
        # "74": [
        #     "arg_list",
        #     "->",
        #     "expression",
        #     "arg_list_prime"
        # ],
        # "75": [
        #     "arg_list_prime",
        #     "->",
        #     ",",
        #     "expression",
        #     "arg_list_prime"
        # ],
        # "76": [
        #     "arg_list_prime",
        #     "->",
        #     "epsilon"
        # ]
        "$accept": [["program", "$"]],
        "program": [["declaration_list"]],
        "declaration_list": [["declaration", "declaration_list"], ["epsilon"]],
        "declaration": [["declaration_initial", "declaration_prime"]],
        "declaration_initial": [["type_specifier", "id"]],
        "declaration_prime": [["var_declaration_prime"], ["fun_declaration_prime"]],
        "var_declaration_prime": [["var_prime", ";"], [";"]],
        "fun_declaration_prime": [["(", "params", ")", "compound_stmt"]],
        "type_specifier": [["int"], ["void"]],
        "params": [["int", "id", "param_prime", "param_list,"], ["void"]],
        "param_list": [["param", "param_list"], ["epsilon"]],
        "param": [["declaration_initial", "param_prime"]],
        "param_prime": [["[", "]"], ["epsilon"]],
        # "param_zegond": [["id", "param_zegond_prime"]],
        # "param_zegond_prime": [["var_prime"], ["epsilon"]],
        "compound_stmt": [["{", "declaration_list", "statement_list", "}"]],
        "statement_list": [["statement", "statement_list"], ["epsilon"]],
        # "statement_list": [["statement", "statement_list"], ["epsilon"]],
        "statement": [["expression_stmt"], ["compound_stmt"], ["selection_stmt"], ["iteration_stmt"], ["return_stmt"]],
        "expression_stmt": [["expression", ";"], [";"], ["break", ";"]],
        "selection_stmt": [["if", "(", "expression", ")", "statement", "else", "statement"]],
        # "selection_stmt_prime": [["else", "statement"], ["epsilon"]],
        "iteration_stmt": [["repeat", "statement", "until", "(", "expression", ")"]],
        "return_stmt": [["return", "return_stmt_prime"]],
        "return_stmt_prime": [["expression", ";"], [";"]],
        "expression": [["simple_expression_zegond"], ["id", "b"]],
        "b": [["expression"], ["[", "]", "expression", "h"], ["simple_expression_prime"]],
        "h": [["expression"], ["g", "d", "c"]],
        "simple_expression_zegond": [["Additive_expression_zegond", "c"]],
        "Simple_expression_prime": [["Additive_expression_prime", "C"]],
        "C": [["Relop", "Additive-expression"], ["EPSILON"]],
        "Relop": [["<"], ["=="]],

        # "var": [["id", "var_prime"]],
        # "simple_expression": [["additive_expression", "simple_expression_zegond"]],
        # "simple_expression_zegond": [["relop", "additive_expression"], ["epsilon"]],
        "additive_expression": [["term", "d"]],
        "additive_expression_prime": [["term_prime", "d"]],
        "additive_expression_zegond": [["term_zegond", "d"]],
        "d": [["Addop", "Term", "D"], ["EPSILON"]],
        "addop": [["+"], ["-"]],
        "term": [["factor", "g"]],
        "term_prime": [["factor_prime", "g"]],
        "term_zegond": [["Factor_zegond", "G"]],
        "g": [["*", "factor", "g"], ["epsilon"]],
        "factor": [["(", "expression", ")"], ["id", "var_call_prime"], ["num"]],
        "var_call_prime": [["(", "args", ")"], ["var_prime"]],
        "args": [["arg_list"], ["epsilon"]],
        "var_prime": [["[", "Expression", "]"], ["EPSILON"]],
        "factor_prime": [["(", "args", ")"], ["epsilon"]],
        "factor_zegond": [["(", "expression", ")"], ["num"]],
        "args": [["arg_list"], ["epsilon"]],
        "arg_list": [["expression", "arg_list_prime"]],
        "arg_list_prime": [[",", "expression", "arg_list_prime"], ["epsilon"]]
        # },

    },
    "first_sets": {

        "$accept": {
            "int",
            "void"
        },
        "program": {
            "int",
            "void",
            "epsilon"
        },
        "declaration_list": {
            "int",
            "void",
            "epsilon"
        },
        "declaration": {
            "int",
            "void"
        },
        "declaration_initial": {
            "int",
            "void"
        },
        "declaration_prime": {
            ";",
            "[",
            "("
        },
        "var_declaration_prime": {
            ";",
            "["
        },
        "fun_declaration_prime": {
            "("
        },
        "type_specifier": {
            "int",
            "void"
        },
        "params": {
            "int",
            "void"
        },
        "param_list": {
            ",",
            "epsilon"
        },
        "param": {
            "int",
            "void"
        },
        "param_prime": {
            "[",
            "epsilon"
        },
        "compound_stmt": {
            "{"
        },
        "statement_list": {
            "{",
            "return",
            "if",
            "(",
            "{",
            "break",
            "repeat",
            ";",
            "ID",
            "epsilon"
        },
        "statement": {
            "{",
            "return",
            "if",
            "(",
            "{",
            "break",
            "repeat",
            ";",
            "ID"
        },
        "expression_stmt": {
            "(",
            "{",
            "break",
            ";",
            "ID"
        },
        "selection_stmt": {
            "if"
        },
        "iteration_stmt": {
            "repeat"
        },
        "return_stmt": {
            "return"
        },
        "return_stmt_prime": {
            "(",
            "{",
            ";",
            "ID"
        },
        "expression": {
            "(",
            "{",
            "ID"
        },
        "b": {
            "(",
            "==",
            "<",
            "=",
            "+",
            "-",
            "*",
            "epsilon"
        },
        "h": {
            "==",
            "<",
            "=",
            "+",
            "-",
            "*",
            "epsilon"
        },
        "simple_expression-zegond": {
            "num",
            "("
        },
        "simple_expression_prime": {
            "(",
            "==",
            "<",
            "+",
            "-",
            "*",
            "epsilon"

        },
        "c": {
            "==",
            "<",
            "epsilon"
        },
        "relop": {
            "==",
            "<"
        },
        "additive_expression": {
            "(",
            "NUM",
            "ID"
        },
        "additive_expression_prime": {
            "epsilon",
            "*",
            "+",
            "-",
            "("
        },
        "additive_expression_zegond": {
            "(",
            "num"
        },
        "d": {
            "+",
            "-",
            "epsilon"
        },
        "addop": {
            "+",
            "-"
        },
        "term": {
            "(",
            "NUM",
            "ID"
        },
        "term_prime": {
            "(",
            "*",
            "epsilon"
        },
        "term_zegond": {
            "(",
            "num"
        },
        "g": {
            "*",
            "epsilon"
        },
        "factor": {
            "(",
            "NUM",
            "ID"
        },
        "var_call_prime": {
            "(",
            "[",
            "epsilon"
        },
        "var_prime": {
            "[",
            "epsilon"
        },
        "factor_prime": {
            "(",
            "epsilon"
        },
        "factor_zegond": {
            "(",
            "num"
        },
        "args": {
            "(",
            "NUM",
            "ID",
            "epsilon"
        },
        "arg_list": {
            "(",
            "NUM",
            "ID"
        },
        "Arg_list_prime": {
            ",",
            "epsilon"
        }
    },
    'follow_sets': {
        "$accept": [],
        "Program": [
            "$"
        ],
        "Declaration_list": [
            "id",
            ";",
            "num",
            "(",
            "{",
            "}",
            "break",
            "if",
            "return,"
            "$"
        ],
        "Declaration": [
            "id",
            ";",
            "num",
            "(",
            "{",
            "}",
            "break",
            "if",
            "return,"
            "$",
            "int",
            "void"
        ],
        "Declaration_initial": [
            ";",
            "[",
            "(",
            ")",
            ","
        ],
        "Declaration_prime": [
            "id",
            ";",
            "num",
            "(",
            "{",
            "}",
            "break",
            "if",
            "return",
            "int",
            "void",
            "repeat",
            "$"
        ],
        "Var_declaration_prime": [
            "id",
            ";",
            "num",
            "(",
            "int",
            "void",
            "{",
            "}",
            "break",
            "if",
            "return",
            "repeat",
            "$"
        ],
        "Fun_declaration_prime": [
            "id",
            ";",
            "num",
            "(",
            "int",
            "void",
            "{",
            "}",
            "break",
            "if",
            "return",
            "repeat",
            "$"
        ],
        "Type_specifier": [
            "id"
        ],
        "Params": [
            ")"
        ],
        "Param_list": [
            ")"
        ],
        "Param": [
            ",",
            "("
        ],
        "Param_prime": [
            ",",
            "("
        ],
        "Compound_stmt": [
            "id",
            ";",
            "num",
            "(",
            "int",
            "void",
            "{",
            "}",
            "break",
            "if",
            "return",
            "repeat",
            "$",
            "else",
            "until"
        ],
        "Statement_list": [
            "}"
        ],
        "Statement": [
            "id",
            ";",
            "num",
            "(",
            "{",
            "}",
            "break",
            "if",
            "return,"
            "else",
            "until"
        ],
        "Expression_stmt": [
            "id",
            ";",
            "num",
            "(",
            "{",
            "}",
            "break",
            "if",
            "return,"
            "else",
            "until"
        ],
        "Selection_stmt": [
            "id",
            ";",
            "num",
            "(",
            "{",
            "}",
            "break",
            "if",
            "return,"
            "else",
            "until"
        ],
        "Iteration_stmt": [
            "id",
            ";",
            "num",
            "(",
            "{",
            "}",
            "break",
            "if",
            "return,"
            "else",
            "until"
        ],
        "Return_stmt": [
            "id",
            ";",
            "num",
            "(",
            "{",
            "}",
            "break",
            "if",
            "return,"
            "else",
            "until"
        ],
        "Return_stmt_prime": [
            "id",
            ";",
            "num",
            "(",
            "{",
            "}",
            "break",
            "if",
            "return,"
            "else",
            "until"
        ],
        "Expression": [
            ";",
            ")",
            "]",
            ","
        ],
        "b": [
            ";",
            ")",
            "]",
            ","
        ],
        "h": [
            ";",
            ")",
            "]",
            ","
        ],
        "simple_expression_zegond": [
            ";",
            ")",
            "]",
            ","
        ],
        "Simple_expression_prime": [
            ";",
            ")",
            "]",
            ","
        ],
        "c": [
            ";",
            ")",
            "]",
            ","
        ],
        "Relop": [
            "(",
            "NUM",
            "ID"
        ],
        "Var": [
            ";",
            ")"
        ],
        "Additive_expression": [
            ";",
            ")",
            "]",
            ","
        ],
        "Additive_expression_prime": [
            ";",
            ")",
            "]",
            ",",
            "<",
            "=="
        ],
        # "Simple_expression": [
        #     ";",
        #     ")"
        # ],

        "Additive_expression_zegond": [
            ";",
            ")",
            "]",
            ",",
            "<",
            "=="
        ],
        "D": [
            ";",
            ")",
            "]",
            ",",
            "<",
            "=="
        ],
        "Addop": [
            "(",
            "NUM",
            "ID"
        ],
        "Term": [
            ";",
            ")",
            "]",
            ",",
            "<",
            "==",
            "+",
            "-"
        ],
        "Term_prime": [
            ";",
            ")",
            "]",
            ",",
            "<",
            "==",
            "+",
            "-"
        ],
        "Term_zegond": [
            ";",
            ")",
            "]",
            ",",
            "<",
            "==",
            "+",
            "-"
        ],
        "G": [
            ";",
            ")",
            "]",
            ",",
            "<",
            "==",
            "+",
            "-"
        ],
        "Factor": [
            ";",
            ")",
            "]",
            ",",
            "<",
            "==",
            "+",
            "-",
            "*"
        ],
        "Var_call_prime": [
            ";",
            ")",
            "]",
            ",",
            "<",
            "==",
            "+",
            "-",
            "*"
        ],
        "Var_prime": [
            ";",
            ")",
            "]",
            ",",
            "<",
            "==",
            "+",
            "-",
            "*"
        ],
        "Factor_prime": [
            ";",
            ")",
            "]",
            ",",
            "<",
            "==",
            "+",
            "-",
            "*"
        ],
        "Factor_zegond": [
            ";",
            ")",
            "]",
            ",",
            "<",
            "==",
            "+",
            "-",
            "*"
        ],
        "Args": [
            ")"
        ],
        "Arg_list": [
            ")"
        ],
        "Arg_list_prime": [
            ")"
        ]
    }
}
grammar['start_symbol'] = grammar['start_symbol'].lower()
grammar['start_symbol'] = grammar['start_symbol'].replace("-", "_")
grammar['terminals'] = [terminal.lower() for terminal in grammar['terminals']]
# grammar['terminals'] = [terminal.replace("-","_") for terminal in grammar['terminals']]
grammar['non_terminals'] = [non_terminal.lower() for non_terminal in grammar['non_terminals']]
grammar['non_terminals'] = [non_terminal.replace("-", "_") for non_terminal in grammar['non_terminals']]
# grammar['productions'] = {non_terminal.lower(): [production.lower() for production in productions] for non_terminal, productions in grammar['productions'].items()}
# but by running the line above we get an error saying: AttributeError: 'list' object has no attribute 'lower'
# so we need to change the list to a string
grammar['productions'] = {
    non_terminal.lower(): [[symbol.lower() for symbol in production] for production in productions] for
    non_terminal, productions in grammar['productions'].items()}
# grammar['productions'] = {
#     non_terminal.replace("-","_"): [[symbol.replace("-","_") for symbol in production] for production in productions] for
#     non_terminal, productions in grammar['productions'].items()}
for non_terminal, productions in grammar['productions'].items():
    non_terminal = non_terminal.replace("-", "_")
    for production in productions:
        for symbol in production:
            if symbol != '-':
                symbol.replace("-", "_")

grammar['first_sets'] = {non_terminal.lower(): [first.lower() for first in firsts] for non_terminal, firsts in
                         grammar['first_sets'].items()}
grammar['first_sets'] = {non_terminal.replace("-", "_"): [first for first in firsts] for non_terminal, firsts in
                         grammar['first_sets'].items()}
grammar['follow_sets'] = {non_terminal.lower(): [follow.lower() for follow in follows] for non_terminal, follows in
                          grammar['follow_sets'].items()}
grammar['follow_sets'] = {non_terminal.replace("-", "_"): [follow.replace("-", "_") for follow in follows] for
                          non_terminal, follows in
                          grammar['follow_sets'].items()}
# grammar['non_terminals'] = [nt.replace("-", "_") for nt in grammar["non_terminals"]]

transition_diagrams = {
    "program": {
        ("0", "declaration_list"): "1"  # final
    },
    "declaration_list": {
        ("2", "declaration"): 3,
        ("3", "declaration_list"): 4,
        ("2", "epsilon"): 4
    },
    "declaration": {
        ("5", "declaration_initial"): 6,
        ("6", "declaration_prime"): 7

    },
    "declaration_initial": {
        ("8", "type_specifier"): 9,
        ("9", "id"): 10

    },

}
transition_diagrams = {
    "PROGRAM": [
        [(1, "DECLARATION_LIST")],
        [(2, "$")]
    ],
    "DECLARATION_LIST": [
        [(1, "DECLARATION"), (2, "epsilon")],
        [(2, "DECLARATION_LIST")]
    ],
    "DECLARATION": [
        [(1, "DECLARATION_INITIAL")],
        [(2, "DECLARATION_PRIME")]
    ],
    "DECLARATION_INITIAL": [
        [(1, "TYPE_SPECIFIER")],
        [(2, "ID")]
    ],
    "DECLARATION_PRIME": [
        [(1, "FUN_DECLARATION_PRIME"), (1, "VAR_DECLARATION_PRIME")]
    ],
    "VAR_DECLARATION_PRIME": [
        [(1, "["), (4, ";")],
        [(2, "NUM")],
        [(3, "]")],
        [(4, ";")]
    ],
    "FUN_DECLARATION_PRIME": [
        [(1, "(")],
        [(2, "PARAMS")],
        [(3, ")")],
        [(4, "COMPOUND_STMT")]
    ],
    "TYPE_SPECIFIER": [
        [(1, "int"), (1, "void")]
    ],
    "PARAMS": [
        [(1, "int"), (4, "void")],
        [(2, "ID")],
        [(3, "PARAM_PRIME")],
        [(4, "PARAM_LIST")]
    ],
    "PARAM_LIST": [
        [(1, ","), (3, "epsilon")],
        [(2, "PARAM")],
        [(3, "PARAM_LIST")]
    ],
    "PARAM": [
        [(1, "DECLARATION_INITIAL")],
        [(2, "PARAM_PRIME")]
    ],
    "PARAM_PRIME": [
        [(1, "["), (2, "epsilon")],
        [(2, "]")]
    ],
    "COMPOUND_STMT": [
        [(1, "{")],
        [(2, "DECLARATION_LIST")],
        [(3, "STATEMENT_LIST")],
        [(4, "}")]
    ],
    "STATEMENT_LIST": [
        [(1, "STATEMENT"), (2, "epsilon")],
        [(2, "STATEMENT_LIST")]
    ],
    "STATEMENT": [
        [
            (1, "EXPRESSION_STMT"),
            (1, "COMPOUND_STMT"),
            (1, "SELECTION_STMT"),
            (1, "ITERATION_STMT"),
            (1, "RETURN_STMT")
        ]
    ],
    "EXPRESSION_STMT": [
        [(1, "EXPRESSION"), (1, "break"),
         (2, ";")],
        [(2, ";")]
    ],
    "SELECTION_STMT": [
        [(1, "if")],
        [(2, "(")],
        [(3, "EXPRESSION")],
        [(4, ")")],
        [(5, "STATEMENT")],
        [(6, "else")],
        [(7, "STATEMENT")]
    ],
    "ITERATION_STMT": [
        [(1, "repeat")],
        [(2, "STATEMENT")],
        [(3, "until")],
        [(4, "(")],
        [(5, "EXPRESSION")],
        [(6, ")")]
    ],
    "RETURN_STMT": [
        [(1, "return")],
        [(2, "RETURN_STMT_PRIME")]
    ],
    "RETURN_STMT_PRIME": [
        [(1, "EXPRESSION"), (2, ";")],
        [(2, ";")]
    ],
    "EXPRESSION": [
        [(1, "ID"), (2, "SIMPLE_EXPRESSION_ZEGOND")],
        [(2, "B")]
    ],
    "B": [
        [(1, "="), (2, "["),
         (5, "SIMPLE_EXPRESSION_PRIME")],
        [(5, "EXPRESSION")],
        [(3, "EXPRESSION")],
        [(4, "]")],
        [(5, "H")]
    ],
    "H": [
        [(1, "G"), (3, "=")],
        [(2, "D")],
        [(4, "C")],
        [(4, "EXPRESSION")]
    ],
    "sIMPLE_EXPRESSION_ZEGOND": [
        [(1, "ADDITIVE_EXPRESSION_ZEGOND")],
        [(2, "C")]
    ],
    "SIMPLE_EXPRESSION_PRIME": [
        [(1, "ADDITIVE_EXPRESSION_PRIME")],
        [(2, "C")]
    ],
    "C": [
        [(1, "RELOP"), (2, "epsilon")],
        [(2, "ADDITIVE_EXPRESSION")]
    ],
    "RELOP": [
        [(1, "<"), (1, "==")]
    ],
    "ADDITIVE_EXPRESSION": [
        [(1, "TERM")],
        [(2, "D")]
    ],
    "ADDITIVE_EXPRESSION_PRIME": [
        [(1, "TERM_PRIME")],
        [(2, "D")]
    ],
    "ADDITIVE_EXPRESSION_ZEGOND": [
        [(1, "TERM_ZEGOND")],
        [(2, "D")]
    ],
    "D": [
        [(1, "ADDOP"), (3, "epsilon")],
        [(2, "TERM")],
        [(3, "D")]
    ],
    "ADDOP": [
        [(1, "+"), (1, "-")]
    ],
    "TERM": [
        [(1, "FACTOR")],
        [(2, "G")]
    ],
    "TERM_PRIME": [
        [(1, "FACTOR_PRIME")],
        [(2, "G")]
    ],
    "TERM_ZEGOND": [
        [(1, "FACTOR_ZEGOND")],
        [(2, "G")]
    ],
    "G": [
        [(1, "*"), (3, "epsilon")],
        [(2, "FACTOR")],
        [(3, "G")]
    ],
    "FACTOR": [
        [(1, "("), (3, "ID"), (4, "NUM")],
        [(2, "EXPRESSION")],
        [(4, ")")],
        [(4, "VAR_CALL_PRIME")]
    ],
    "VAR_CALL_PRIME": [
        [(1, "("), (3, "VAR_PRIME")],
        [(2, "ARGS")],
        [(3, ")")]
    ],
    "VAR_PRIME": [
        [(1, "["), (3, "epsilon")],
        [(2, "EXPRESSION")],
        [(3, "]")]
    ],
    "FACTOR_PRIME": [
        [(1, "("), (3, "epsilon")],
        [(2, "ARGS")],
        [(3, ")")]
    ],
    "FACTOR_ZEGOND": [
        [(1, "("), (3, "NUM")],
        [(2, "EXPRESSION")],
        [(3, ")")]
    ],
    "ARGS": [
        [(1, "ARG_LIST"), (1, "epsilon")]
    ],
    "ARG_LIST": [
        [(1, "EXPRESSION")],
        [(2, "ARG_LIST_PRIME")]
    ],
    "ARG_LIST_PRIME": [
        [(1, ","), (3, "epsilon")],
        [(2, "EXPRESSION")],
        [(3, "ARG_LIST_PRIME")]
    ]
}


def to_tuple(t):
    return tuple(map(to_tuple, t)) if isinstance(t, (list, tuple)) else t


def parse(grammar):
    current_token = get_next_token()


def construct_parse_table(grammar):
    parse_table = {}
    for non_terminal in grammar['non_terminals']:
        parse_table[to_tuple(non_terminal)] = {}
        for terminal in grammar['terminals']:
            # print(terminal,'this is terminals')
            parse_table[to_tuple(non_terminal)][terminal] = []

    for non_terminal, productions in grammar['productions'].items():
        # print(productions,"this is productionsn")
        for production in productions:
            if production == []:
                for terminal in grammar['follow_sets'][non_terminal]:
                    parse_table[to_tuple(non_terminal)][terminal].append(production)
            else:
                if production[0] not in grammar['terminals']:
                    # print(production,"this is production")
                    # print(production[0],non_terminal)
                    for terminal in grammar['first_sets'][production[0]]:
                        # print(terminal, production[0], grammar['first_sets'][production[0]])
                        # print(non_terminal, productions, production, terminal)
                        # print(grammar['first_sets'][production[0]])
                        parse_table[to_tuple(non_terminal)][terminal].append(production)
                else:
                    # print(non_terminal,production[0], "this is in terminals")
                    parse_table[to_tuple(non_terminal)][production[0]].append(production)

    return parse_table


parse_table = construct_parse_table(grammar)


# now we want to get the transition diagrams
def construct_transition_diagram(grammar, parse_table):
    transition_diagram = {}
    stack = [grammar['start_symbol']]
    visited = {}

    while stack:
        state = to_tuple(stack)
        if state not in visited.keys():
            visited[state] = [True]
            transition_diagram[state] = {}
            # print(to_tuple(stack.pop()))
            top = to_tuple(stack.pop())
            if top in grammar['terminals']:
                transition_diagram[state][top] = (stack.copy(), top)
                stack.append(top)
            else:
                print(top[0], top[1])
                for production in parse_table[top]:
                    # print(production,"this is production")
                    if production == []:
                        transition_diagram[state][top[1]] = (stack.copy(), top)
                        stack.append(top)
                    else:
                        for symbol in reversed(production):
                            # print(symbol,"this is symbol")
                            stack.append(symbol)
                            transition_diagram[state][symbol] = (stack.copy(), top)
                            stack.pop()

    return transition_diagram


# def construct_transition_diagram(grammar, parse_table):
#     transition_diagram = {}
#     stack = [grammar['start_symbol']]
#     visited = {}
#
#     while stack:
#         state = to_tuple(stack)
#         # state = stack
#         print("this is trans.diagram" , transition_diagram)
#         print(state)
#         print(visited)
#         if state not in visited.keys():
#         #but by running the line above we get an error saying: TypeError: unhashable type: 'list'
#
#             visited[state] = [True]
#             # visited.add(state)
#             transition_diagram[state] = {}
#             top = to_tuple(stack.pop())
#             if top in grammar['terminals']:
#                 transition_diagram[state][top] = (stack.copy(), top)
#                 stack.append(top)
#             else:
#                 # arr = [terminal,productions for terminal,productions in parse_table[top].items]
#                 print(parse_table[top].items(),"here")
#                 for terminal, productions in parse_table[top].items():
#                     if productions:
#                         production = productions[0]
#                         new_stack = stack.copy()
#                         if production != []:
#                             new_stack.extend(reversed(production))
#                         transition_diagram[state][terminal] = (new_stack, None)
#                         stack.append((new_stack, terminal))
#         else:
#             stack.pop()
#
#     return transition_diagram


transition_diagram = construct_transition_diagram(grammar, parse_table)


# def parse(input_string, grammar, transition_diagram):
#     stack = [grammar['start_symbol']]
#     input_string.append('$')
#     index = 0
#
#     while stack:
#         state = tuple(stack)
#         current_token = input_string[index]
#         if current_token not in transition_diagram[state]:
#             return False
#         new_state, action = transition_diagram[state][current_token]
#         if action == current_token:
#             index += 1
#         stack = new_state
#
#     return True
#
#
# input_string = ['int', '+', 'int', '*', 'int']
# result = parse(input_string, grammar, transition_diagram)
# print(result)  # True

# def parse(input_string, grammar, transition_diagram):
#     stack = [grammar['start_symbol']]
#     input_string.append('$')
#     index = 0
#     parse_tree = []
#
#     while stack:
#         state = tuple(stack)
#         current_token = input_string[index]
#         if current_token not in transition_diagram[state]:
#             return False
#         new_state, action = transition_diagram[state][current_token]
#         if action == current_token:
#             index += 1
#             parse_tree.append(('shift', current_token))
#         else:
#             production = find_production(grammar, state, new_state)
#             if production:
#                 parse_tree.append(('reduce', production))
#         stack = new_state
#
#     return parse_tree
#
#
# def find_production(grammar, old_state, new_state):
#     for non_terminal, productions in grammar['productions'].items():
#         for production in productions:
#             if old_state[:-1] == new_state and old_state[-1] == non_terminal:
#                 return (non_terminal, production)
#     return None
#
#
# input_string = ['int', '+', 'int', '*', 'int']
# result = parse(input_string, grammar, transition_diagram)
# print(result)

# we want to implement parse now

def parse(input_string, grammar, transition_diagram):
    stack = [grammar['start_symbol']]
    input_string += '$'
    index = 0
    parse_tree = []

    while stack:
        state = tuple(stack)
        current_token = input_string[index]
        if current_token not in transition_diagram[state]:
            return False
        new_state, action = transition_diagram[state][current_token]
        if action == current_token:
            index += 1
            parse_tree.append(('shift', current_token))
        else:
            production = find_production(grammar, state, new_state)
            if production:
                parse_tree.append(('reduce', production))
        stack = new_state

    return parse_tree


#
#
# def find_production(grammar, old_state, new_state):
#     for non_terminal, productions in grammar['productions'].items():
#         for production in productions:
#             if old_state[:-1] == new_state and old_state[-1] == non_terminal:
#                 return (non_terminal, production)
#     return None
#
#
# input_string = ['int', '+', 'int', '*', 'int']
# result = parse(input_string, grammar, transition_diagram)
# print(result)


# def parse(input_string, grammar, transition_diagram):
#     stack = [grammar['start_symbol']]
#     input_string+='$'
#     index = 0
#     parse_tree = [grammar['start_symbol']]
#
#     while stack:
#         state = tuple(stack)
#         current_token = input_string[index]
#         if current_token not in transition_diagram[state]:
#             return False
#         new_state, action = transition_diagram[state][current_token]
#         if action == current_token:
#             index += 1
#             parse_tree.append(current_token)
#         else:
#             production = find_production(grammar, state, new_state)
#             if production:
#                 non_terminal, rhs = production
#                 children = []
#                 for _ in rhs:
#                     children.append(parse_tree.pop())
#                 children.reverse()
#                 parse_tree.append([non_terminal] + children)
#         stack = new_state
#
#     return parse_tree[0]


def find_production(grammar, old_state, new_state):
    for non_terminal, productions in grammar['productions'].items():
        for production in productions:
            if old_state[:-1] == new_state and old_state[-1] == non_terminal:
                return (non_terminal, production)
    return None


def print_parse_tree(parse_tree, depth=0):
    if isinstance(parse_tree, list):
        print('\t' * depth + parse_tree[0])
        for child in parse_tree[1:]:
            print_parse_tree(child, depth + 1)
    else:
        print(parse_tree)
        print('\t' * depth)
        # but by running the line above we get an error saying: TypeError: can only concatenate str (not "bool") to str

# input_string = ['int', '+', 'int', '*', 'int']
# result = parse(input_string, grammar, transition_diagram)
# print_parse_tree(result)
