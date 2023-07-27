def verificar(valor: str) -> int:
    contador = 0
    for v in valor:
        if v in "123456789":
            contador = contador+1
            
    return contador


    

def he_numero(valor: str) -> bool:
    return True if len(valor) == verificar(valor) else False

def ler_int(texto: str) -> int:
    numero = input(texto)
    return int(numero) if he_numero(numero) else 0



def colorir (texto: str, cor: str) -> None:
    """
    Esta função exibe o texto colorido no terminal 
    
    Parâmentros:
    texto(str) : o que será colorido
    cor (str) : a cor do texto 
    
    Retorno:
    none
    
    """
    cores = {
        'branco': '30',
        'vermelho': '31',
        'verde': '32',
        'amarelo': '33',
        'azul': '34',
        'roxo': '35',
        'ciano': '36',
        'cinza': '37',
                 
    }
    
    
    
    if cor.lower() in cores:
        print(f"\033[{cores [cor.lower()]}m{texto}\33[m")
    else:
        print(texto)
