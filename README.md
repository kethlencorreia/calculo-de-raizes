# calculo-de-raizes

Descrição do Projeto: Métodos Numéricos para Calcular Raízes de Funções

O problema de calcular as raízes reais de uma equação tem sido objeto de estudo da matemática ao longo dos séculos. Encontrar essas raízes faz parte de muitos problemas importantes das áreas relacionadas à matemática. Este projeto se concentra na implementação e análise de três métodos clássicos para encontrar raízes reais aproximadas de equações. Estes métodos são o Método da Bisseção, o Método de Newton-Raphson e o Método da Secante. O programa foi desenvolvido em Python, uma linguagem de programação versátil e amplamente utilizada para aplicações científicas e matemáticas.

# Funcionalidades

- Método da Bisseção
- Baseia-se no Teorema de Bolzano, que garante a existência de uma raiz em um intervalo fechado onde a função troca de sinal.
- O método itera dividindo o intervalo pela metade e selecionando subintervalos onde a função muda de sinal até atingir a precisão desejada.

Método de Newton-Raphson
- Usa a inclinação da tangente da função no ponto atual para iterar em direção à raiz.
- Requer a derivada da função e é eficiente, mas pode não convergir se a derivada for zero ou próxima de zero.

Método da Secante
- Semelhante ao Método de Newton-Raphson, mas não requer a derivada da função.
- Aproxima a derivada pela diferença entre dois pontos próximos, tornando-o útil quando a derivada não está disponível ou é difícil de calcular.
