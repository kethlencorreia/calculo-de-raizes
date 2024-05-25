import math

funcao=lambda x: math.cos(x)+2*x               #função principal
derivada=lambda x: -1*(math.sin(x))+2          #derivada da função principal


def bi(funcao, a, b, i=1, tol=10 ** -15, max=50, L=[], IT=[]):  # MÉTODO DE BISSEÇÃO
    '''Função feita para calculo de raiz através do métdo de bisseção'''
    raiz = (a + b) / 2                 #cálculo da raízes da função
    erro = abs((a - b) / 2)            #cálculo do erro
    print("{0:2d}        {1:.15f}        {2:.15f}".format(i, raiz, erro))
    if funcao(
            raiz) == 0 or erro < tol or i == max:  # tol= o numéro máximo de tolerência e max é número máximo de iterações
        return IT, L     #retorna uma lista outro com as identações  e o outro com as raízes

    if funcao(a) * funcao(raiz) < 0:
        return bi(funcao, a, raiz, i + 1, tol, max, L + [raiz], IT + [i])

    elif funcao(b) * funcao(raiz) < 0:
        return bi(funcao, raiz, b, i + 1, tol, max, L + [raiz], IT + [i])


def newton (funcao, derivada, a,i=1,tol=10**-15,max=50,L=[], IT=[]): #MÉTODO DE NEWTON-RAPSON
    '''Função feita para calculo de raiz da função pelo método de Newton-Rapson'''
    raiz = a-(funcao(a)/derivada(a))                  #cálculo da raízes da função
    erro = abs((raiz-a)/raiz)                         #cálculo do erro
    print("{0:2d}        {1:.15f}        {2:.15f}".format(i, raiz, erro))
    if funcao(raiz)==0 or erro <tol or i==max:
        return IT, L                #retorna uma lista outro com as identações  e o outro com as raízes
    else:
        return newton(funcao, derivada, raiz,i+1,tol,max,L+[raiz], IT+[i])

def secante (funcao, a,b,i=1,tol=10**-15,max=50, L=[], IT=[]): #MÉTODO SECANTE
    '''Função feita para calculo de raiz de função pelo método da secante'''
    raiz =  a - (((b-a)*funcao(a))/(funcao(b)- funcao(a)))           #cálculo da raízes da função
    erro = abs((raiz-a)/raiz)                                        #cálculo do erro
    print("{0:2d}        {1:.15f}        {2:.15f}".format(i, raiz, erro))
    if funcao(raiz)==0 or erro <tol or i==max:
        return IT, L                 #retorna uma lista outro com as identações  e o outro com as raízes
    else:
        return secante (funcao, raiz,b,i+1,tol,max, L+[raiz], IT+[i])


def main():
    '''Função feit para exibir os resultados das raízes'''
    print('Função escolhida: cos(x)+2x')
    print('Derivada da função: -sin(x)+2 ')
    print('==> MÉTODO DE BISSEÇÃO: a=-2 e b=0')
    print ('_' * 55)
    print (' i              RAIZ                      ERRO')
    print ('_' * 55)
    bi(funcao, -2,0)
    print ('_' * 55)
    print ('==> MÉTODO DE NEWTON-RAPSON:a=-2')
    print ('_' * 55)
    print (' i              RAIZ                      ERRO')
    print ('_' * 55)
    newton(funcao, derivada,-2)
    print ('_' * 55)
    print ('==> MÉTODO DA SECANTE:a=-2 e b=0')
    print ('_' * 55)
    print (' i              RAIZ                      ERRO')
    print ('_' * 55)
    secante(funcao,-2,0)
    print ('_' * 55)

main()


