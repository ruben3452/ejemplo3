#Importamos la Libreria PLY Lex
import ply.lex as lexico

#*********************************************************************************************

tokens = (
          # Palabras Reservadas
          'PALABRARESERVADA', 'NUMERO',
          # Simbolos
          'CORCHETEIZQ', 'CORCHETEDER', 'PARENTESISIZQ', 'PARENTESISDER', 'PUNTO', 'MENOS',
          'EXCLAMACION', 'MULTIPLICACION', 'DIVISION', 'PORCENTAJE', 'SUMA', 'MENORQUE',
          'MENORIGUAL', 'MAYORQUE', 'MAYORIGUAL', 'ESIGUAL', 'ESDIFERENTE', 'Y', 'O',
          'ASIGNACION', 'COMILLADOBLE', 'COMILLASIMPLE', 'PUNTOCOMA', 'COMA', 'DOSPUNTOS',
          # Otros
          'IDENTIFICADOR', 'COMENTARIOML', 'CADENACARACTERES', 'COMENTARIOL'
          )

#*********************************************************************************************

#Tokens
t_CORCHETEIZQ = r'\['
t_CORCHETEDER = r'\]'
t_PARENTESISIZQ = r'\('
t_PARENTESISDER = r'\)'
t_PUNTO = r'\.'
t_MENOS = r'\-'
t_EXCLAMACION = r'!'
t_MULTIPLICACION = r'\*'
t_DIVISION = r'/'
t_PORCENTAJE = r'%'
t_SUMA = r'\+'
t_MENORQUE = r'<'
t_MENORIGUAL = r'[<]\='
t_MAYORQUE = r'>'
t_MAYORIGUAL = r'[>]\='
t_ESIGUAL = r'[\=]\='
t_ESDIFERENTE = r'[!]\='
t_Y = r'[&]&'
t_O = r'\|'
t_ASIGNACION = r'\='
t_COMILLADOBLE = r'\"'
t_COMILLASIMPLE = r'\''
t_PUNTOCOMA = r';'
t_COMA = r','
t_DOSPUNTOS = r'\:'



#*********************************************************************************************

def t_CADENACARACTERES(t):
    r'\"[a-zA-Z0-9_]+\"' # Duda... Por que no se puede \w
    return t

#*********************************************************************************************

def t_COMENTARIOML(t):
    r'/*(.|\n)*?\*/'
    t.lexer.lineno += t.value.count('\n')
    return t

#*********************************************************************************************

def t_COMENTARIOL(t):
    r'//(.)*(\n)?'
    t.lexer.lineno += 1
    return t

#*********************************************************************************************
    
def t_IDENTIFICADOR(t):
    r'(int|void|string|boolean)\s[a-zA-Z_][a-zA-Z0-9_]+'
    return t

#*********************************************************************************************

# Para limitar una cadena de caracteres a cirto numero
def cortar(t):
    t = t[0:10]
    print t

#*********************************************************************************************

def t_PALABRARESERVADA(t):
    r'class|extend|void|int|boolean|string|return|if|else|while|break|continue|this|new|length|true|false|null'
    return t

#*********************************************************************************************

def t_NUMERO(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("El valor no es correcto %d", t.value)
        t.value = 0
    return t

#*********************************************************************************************

# Caracteres que se van a Ignorar
t_ignore = " \t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

#*********************************************************************************************

def t_error(t):
    print("No se reconoce el caracter '%s'" % t.value[0])
    t.lexer.skip(1)
    
#*********************************************************************************************
    
def leerArchivo():
    analizador = lexico.lex()
    archi = open('datos.txt','r')
    linea = archi.readline()
    while linea != "":
        analizador.input(linea)
        linea = archi.readline()
        #print linea
        #analizador.input(linea)
        while True:
            tok = analizador.token()
            if not tok: break      #fin de la lista
            print tok
    archi.close()

#*********************************************************************************************

#cortar("Hola")
leerArchivo()
