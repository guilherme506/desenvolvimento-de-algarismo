/*
Escreva um programa em linguagem C que solicite ao usuário a média para aprovação
em um curso e em seguida solicite ao usuário o nome, sexo e as 03 notas do aluno e ao
final imprima a frase: "O aluno XXXXX foi aprovado com media YY" considerando o gênero
do(a) aluno(a) e se foi aprovado(a) ou reprovado(a)
*/
#include <stdio.h>

int main(){
    float nota1, nota2, nota3, media;
    char nome[255];
    char sexo[2];

    printf("Digite o nome do aluno\n");
    scanf("%s,", &*nome);

    printf("Digite seu gêneco(F/M)\n");
    scanf("%1s", &*sexo);
    
    printf("Digite a primeira nota\n");
    scanf("%f", &nota1);

    printf("Digite a segunda nota\n");
    scanf("%f", &nota2);

    printf("Digite a terceira nota\n");
    scanf("%f", &nota3);
    
    media = (nota1+nota2+nota3)/3;

    char* aprovacao;
    if(media >= 7){
        aprovacao = "aprovado";
    } else if (media > 7){
        aprovacao = "reprovado";
    }
    
    printf("O aluno %s foi %s com media %.2f", nome, aprovacao, media);


    return 0;
}