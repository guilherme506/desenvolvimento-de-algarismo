# Tecnicas Desenvolvimento Algaritmo(UDF)
## Estruturas-Condicionais 
O exercicio proposto desse repositório consiste me criar um programa em Python que simule um sistema de verificação de idade para entrada em eventos.

O programa Funciona da seguinte maneira:

passo 1: O programa pergunta quantos anos o usuário tem

passo 2: De acordo com a idade colocada o programa irá verificar se a entrada sera inválida, proibida, precisa de responsavel ou permitida
    A verificação e feita com a utilização de if, elif e else sendo que:
    
        if: vai ser usado para caso a idade seja menor do que 0 o resultado irá dar inválido
        
        elif: sera usado em dois casos:
        
            - No primerio caso se o usuário tenha 14 anos ou menos a entrada será proibida
            - No segundo caso se o usuário tenha menos de 18 anos a entrada será precisa de um responsavel
            
        elif: Vai ser usado se a idade passar pelos if e os dois elif, dando o resultado entrada permitida 

passo 3: No final o programa irá dar o resultado da verificação feita.

### Exemplo 

Usuário coloca que tem 15 anos 
-Ele passa pela condição if pois o valor indicado e maior do que 0

-Ele passa pelo primeiro elif pois o valor indicado e maior do que 14 

-Ele e barrado pelo segundo elif pois o valor indicado esta entre 15 e 18

O resultado vai dar precisa de responsavel para entrar no evento 
