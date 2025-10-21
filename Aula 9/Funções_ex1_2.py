def soma(n1,n2):
    return n1+n2

def subtracao(n1,n2):
    return n1-n2

def multiplicacao(n1,n2):
    return n1*n2

def divisao(n1,n2):
    return n1/n2

def par_ou_impar(x):
    if x % 2 == 0:
        return "par"
    else:
        return "impar"
    
def máximo(x,y):
    return max(x,y)

def minimo(x,y):
    return min(x,y)

def múltiplos(x,y):
    return x % y == 0
        
def área_quadrado(L):
    return L**2

def área_triângulo(b,h):
    return (b*h)/2