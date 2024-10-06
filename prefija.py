
def evaluar_prefija(expresion):
    pila = []
    for token in expresion.split()[::-1]:
        if token.replace('.', '', 1).isdigit():
            pila.append(float(token))
        else:
            try:
                operando1 = pila.pop()
                operando2 = pila.pop()
                if token == '+':
                    resultado = operando1 + operando2
                elif token == '-':
                    resultado = operando1 - operando2
                elif token == '*':
                    resultado = operando1 * operando2
                elif token == '/':
                    resultado = operando1 / operando2
                elif token == '^':
                    resultado = operando1 ** operando2
                else:
                    raise ValueError(f"Operador desconocido: {token}")
                pila.append(resultado)
            except IndexError:
                raise ValueError("Expresión no válida, faltan operandos")
    if len(pila) != 1:
        raise ValueError("Expresión no válida, demasiados operandos")
    return pila.pop()


expresiones_prefija = [
    "+ 3 4",        
    "* 2 + 3 4",    
    "/ 10 ^ 3 2",   
    "- + 5 2 3",    
    "^ + 2 3 4",    
]

for expresion in expresiones_prefija:
    try:
        resultado = evaluar_prefija(expresion)
        print(f"Expresión: {expresion} = {resultado}")
    except ValueError as e:
        print(f"Error evaluando la expresión '{expresion}': {e}")

