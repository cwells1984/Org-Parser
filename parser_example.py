import sys
sys.path.insert(0, "../..")

tokens = ('VAR',)

literals = ['=', '+', '-', '*', '/']

def t_VAR(t):
    r'VAR '
    return t

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

# dictionary of names
names = {}

def p_expression_stmt(p):
    '''stmt : VAR'''

def p_error(p):
    if p:
        print("Syntax error at '%s'" % p.value)
    else:
        print("Syntax error at EOF")

import ply.yacc as yacc
parser = yacc.yacc()

while True:
    try:
        s = input("Enter a line of code: ")
    except EOFError:
        break
    if not s:
        continue
    yacc.parse(s)