import sys

sys.path.insert(0, "../..")

# SCANNER CODE HERE
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
def t_VAR(t):
    r'VAR'
    return t

# create a method for parsing ID tokens
# regex for finding ID tokens
# return token
def t_ID(t):
    r'[a-zA-Z][a-zA-Z0-9]*'
    return t

# create a method for parsing NUM tokens
# regex for finding NUM tokens
# convert token from str to int
# return token
def t_NUM(t):
    r'[-]?[0-9]+'
    t.value = int(t.value)
    return t

# create a method for parsing EXP tokens
# regex for finding EXP tokens
# return token
def t_EXP(t):
    r'\*\*'
    return t

# create a method for parsing STR tokens
# regex for finding STR tokens
# return token
def t_STR(t):
    r'"[a-zA-Z. ]+"'
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

# END SCANNER CODE
# PARSER CODE HERE

def p_expression_stmt(p):
    '''stmt : assign
            | declare
            | binop'''

def p_expression_declare(p):
    '''declare : var id
               | var assign'''

def p_expression_assign(p):
    '''assign : id '=' term
              | id '=' str'''

def p_expression_binop(p):
    '''binop : term literal term
             | term exp term
             | str '+' str'''

def p_expression_term(p):
    '''term : id
            | num
            | binop'''

def p_term_literal(p):
    '''literal : '+'
               | '-'
               | '*'
               | '/' '''

def p_term_id(p):
    'id : ID'
    p[0] = p[1]

def p_term_num(p):
    'num : NUM'
    p[0] = p[1]

def p_term_exp(p):
    'exp : EXP'
    p[0] = p[1]

def p_term_str(p):
    'str : STR'
    p[0] = p[1]

def p_term_var(p):
    '''var : VAR'''

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