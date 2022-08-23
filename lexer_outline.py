import sys

sys.path.insert(0, "../..")

tokens = ('ID',  # ID represents a variable name
          'NUM',  # NUM represents the signed integer data type
          'EXP',  # EXP represents the exponentiation operator (**)
          'STR',  # STR represents the string data type
          'VAR'  # var represents the literal string 'VAR'
          )

literals = ['=', '+', '-', '*', '/']

# create a method for parsing VAR tokens
# regex for finding VAR tokens
# return token

# create a method for parsing ID tokens
# regex for finding ID tokens
# return token

# create a method for parsing NUM tokens
# regex for finding NUM tokens
# convert token from str to int
# return token

# create a method for parsing EXP tokens
# regex for finding EXP tokens
# return token

# create a method for parsing STR tokens
# regex for finding STR tokens
# return token

t_ignore = " \t"


def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


# Build the lexer
import ply.lex as lex

lexer = lex.lex()

while True:
    code = input("Enter a line of code: ")
    lexer.input(code)

    for token in lexer:
        print(token)