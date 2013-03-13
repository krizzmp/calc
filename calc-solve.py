
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
    'PLUS','MINUS','TIMES','DIVIDE','EQUALS','EQ',
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
t_EQ      = r'=='

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
names = {}
result ={ }

def p_error(t):
    print("Syntax error at '%s'" % t.value)

def p_solved(t):
    'statement : SOLVE LPAREN expression EQ expression COMMA NAME RPAREN'
    print 'i was called'
    result[0]=t[7]
    result[1]=sympy.solve(t[3]+'-'+t[5],t[7])
    

def p_statement_assign(t):
    'statement : NAME EQUALS expression'
    print t[3]
    names[t[1]] = t[3]
    result[1] = eval(t[3])
    

def p_statement_expr(t):
    'statement : expression'
    
    t[0] = t[1]
    print t[0]
    result[1] = eval(t[0])
    

def p_expression_binop(t):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression'''
    if t[2] == '+'  : t[0] = str(t[1]) +'+'+ str(t[3])
    elif t[2] == '-': t[0] = str(t[1]) +'-'+ str(t[3])
    elif t[2] == '*': t[0] = str(t[1]) +'*'+ str(t[3])
    elif t[2] == '/': t[0] = str(t[1]) +'/'+ str(t[3])
    

def p_expression_uminus(t):
    'expression : MINUS expression %prec UMINUS'
    t[0] = -t[2]
    

def p_expression_group(t):
    'expression : LPAREN expression RPAREN'
    t[0] = t[2]
    

def p_expression_number(t):
    'expression : NUMBER'
    
    t[0] = t[1]
    

def p_expression_name(t):
    'expression : NAME'
    try:
        t[0] = names[t[1]]
    except LookupError:
        #print("Undefined name '%s'" % t[1])
        t[0] = t[1]
        print t[0]




import ply.yacc as yacc
yacc.yacc()


s="""
solve(p*v==n*r*t , t)
solve(p*g==n*r*t , t)
a_d=6+7/(4+5)*6
a_d+4
"""

import sympy
for line in s.split("\n"):
    if line:
        yacc.parse(line)
        print '\n',line,'->'
        print result[1]