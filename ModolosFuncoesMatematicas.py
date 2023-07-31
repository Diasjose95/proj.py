def somar(*valores: int) -> int:
    """
    estes comando visa realizar a soma de numeros!
    """
   
    resultado = 0
    for v in valores:
        resultado = resultado+v
    return resultado 

def subitrair(*valores: int) -> int:
    """
    este comando visa realizar a subitraçao de dois ou mais numeros
    """
   
    resultado = 0
    for v in valores:
        resultado = resultado-v
    return resultado 

def dividir(*valores: float) -> float:
    """
    este comando visa realizar a divisao de dois ou mais valores com resultado real!
    """
   
    resultado = 0
    for v in valores:
        resultado = resultado/v
    return resultado 

def multiplicar(*valores: int) -> int:
    """
    este comando visa realizar a multiplicaçao dos valores!
    """
   
    resultado = 0
    for v in valores:
        resultado = resultado+v
    return resultado 

def potencia(*valores: int) -> int:
    """
    .......
    """
   
    resultado = 0
    for v in valores:
        resultado = resultado**v
    return resultado 

def divisao_int(*valores: int) -> int:
    """
    este comando visa realizar a divisão inteira
    """
   
    resultado = 0
    for v in valores:
        resultado = resultado//v
    return resultado 

def resto_divisao(*valores: int) -> int:
    """
    este comando retorna o resto da divisão inteira!
    """
   
    resultado = 0
    for v in valores:
        resultado = resultado%v
    return resultado 

def raizq(*valores: float) -> float:
    """
    este comando encontra encontra a raiz quadrada de um numero!
    """
   
    resultado = 0
    for v in valores:
        resultado = v**(1/2)
    return resultado 

def raizc(*valores: float) -> float:
    """
   este comando encontra encontra a raiz cubica de um numero!
    """
   
    resultado = 0
    for v in valores:
        resultado = v**(1/3)
    return resultado 
