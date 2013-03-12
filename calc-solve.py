
# -----------------------------------------------------------------------------
# calc.py
#
# A simple calculator with variables -- all in one file.
# -----------------------------------------------------------------------------
reserved = {
    'solve' : 'SOLVE',
}
tokens = [
    'NAME','NUMBER',
    'PLUS','MINUS','TIMES','DIVIDE','EQUALS',
    'LPAREN','RPAREN',
    'COMMA',
    ]+ list(reserved.values())

# Tokens

t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_EQUALS  = r'='
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_COMMA   = r','

def t_NAME(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value,'NAME')
    return t

def t_NUMBER(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t

# Ignored characters
t_ignore = " \t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")
    
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)
    
# Build the lexer
import ply.lex as lex
lex.lex()

# Parsing rules

precedence = (
    ('left','PLUS','MINUS'),
    ('left','TIMES','DIVIDE'),
    ('right','UMINUS'),
    )

# dictionary of names
names = []
result ={ }

def p_solved(t):
    'solved : SOLVE LPAREN eq EQUALS eq COMMA NAME RPAREN'
    result[0]=t[7]
    result[1]=sympy.solve(t[3]+'-'+t[5],sympy.symbols(t[7]))



def p_eq_name(t):
    'eq : NAME'
    t[0]=sympy.symbols(t[1])
    names.append(t[1])

def p_eq_binop(t):
    '''eq : eq PLUS eq
          | eq MINUS eq
          | eq TIMES eq
          | eq DIVIDE eq'''
    t[0]=str(t[1])+t[2]+str(t[3])

def p_expression_binop(t):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression'''
    if t[2] == '+'  : t[0] = t[1] + t[3]
    elif t[2] == '-': t[0] = t[1] - t[3]
    elif t[2] == '*': t[0] = t[1] * t[3]
    elif t[2] == '/': t[0] = t[1] / t[3]


def p_expression_uminus(t):
    'expression : MINUS expression %prec UMINUS'
    t[0] = -t[2]
def p_expression(t):
    'eq : expression'
    t[0] = t[1]

def p_expression_group(t):
    'expression : LPAREN expression RPAREN'
    t[0] = t[2]

def p_expression_number(t):
    'expression : NUMBER'
    t[0] = t[1]

def p_error(t):
    print("Syntax error at '%s'" % t.value)

import ply.yacc as yacc
yacc.yacc()


s="""
solve(p*v=n*r*t , t)
solve(p*g=n*r*t , t)
"""

print [x**2 for x in range(1,9) if x%2]
import sympy
for line in s.split("\n"):
    if line:
        yacc.parse(line)
        print '\n',line,'->'
        print result[0],'=',result[1][0]