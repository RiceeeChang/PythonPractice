#---------------------------------------
#
# SqlYacc.py - small DB yacc
#
#---------------------------------------
import ply.yacc as yacc

# Get the token map from the lexer. This is required
from SqlLex import tokens

start = 'command'

def p_command(p):
    '''command : define_cmd
               | set_cmd
               | create_cmd
               | insert_cmd
               | delete_cmd
               | update_cmd
               | select_cmd'''

def p_define_cmd(p):
    # define relation <relation_name>
    'define_cmd : DEFINE RELATION WORD'

def p_set_cmd(p):
    # set attribute character <char_number> <attribute_name>
    # set attribute integer <attribute_name> range <front_number> <rear_number>
    # set attribute integer <attribute_name>
    # set primary key <attribute_name>
    '''set_cmd : SET ATTRIBUTE CHARACTER NUMBER WORD
           | SET ATTRIBUTE INTEGER WORD RANGE NUMBER NUMBER
           | SET ATTRIBUTE INTEGER WORD
           | SET PRIMARY KEY  WORD'''

def p_create_cmd(p):
    # create table <relation_name> <table_name>
    'create_cmd : CREATE TABLE WORD WORD'

def p_insert_cmd(p):
    # insert <table_name> (<attribute_value>)+
    'insert_cmd : INSERT WORD attribute_expr'

def p_attribute_expr(p):
    # <attribute_value> <attribute_expr>
    '''attribute_expr : WORD attribute_expr
                      | NUMBER attribute_expr
                      |'''

def p_delete_cmd(p):
    # delete <table_name> <primary_key_value>
    'delete_cmd : DELETE WORD NUMBER'

def p_update_cmd(p):
    # update <table_name> <primary_key_value> (<attribute_value>)+
    'update_cmd : UPDATE WORD NUMBER attribute_expr'

def p_select_cmd(p):
    # select <attribute_name> from <table_name> where <expr>
    'select_cmd : SELECT WORD FROM WORD WHERE expr'

def p_expr(p):
    # <attribute_name> [=|>|<] <value>
    '''expr : WORD EQUAL NUMBER
          | WORD GREATER NUMBER
          | WORD LESS NUMBER'''

# Error rule for syntax errors
def p_error(p):
    print("Syntax error in " + p.value)

# Build the parser
parser = yacc.yacc()


while True:
    try:
        s = input('parser > ')
    except EOFError:
        break

    if not s: continue
    result = parser.parse(s)
    print(result)
