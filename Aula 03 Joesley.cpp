#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void exibirLista(int cadastrados, char nome[][50], int idade[]) {
    if (cadastrados == 0) {
        printf("Nenhum usuario cadastrado ainda.\n");
        return;
    }

    printf("\n========== Usuarios cadastrados ==========\n");

    for (int i = 0; i < cadastrados; i++) {
        printf("Nome: %s\n", nome[i]);
        printf("Idade: %d\n", idade[i]);
        printf("-------------------------\n");
    }
}

void exibirMenu() {
    printf("\n================= Menu Principal ==================\n");
    printf("1 - Cadastrar novo usuario\n");
    printf("2 - Listar todos os usuarios cadastrados\n");
    printf("3 - Sair do sistema\n");
    printf("Opcao: ");
}

int main() {
    int limite;
    int cadastrados = 0;
    int opcao = 0;

    printf("Quantos usuarios serao cadastrados no maximo? ");
    scanf("%d", &limite);

    if (limite <= 0) {
        printf("O limite deve ser maior que zero.\n");
        return 1;
    }

    char nome[limite][50];
    int idade[limite];

    do {
        exibirMenu();
        scanf("%d", &opcao);

        switch (opcao) {
            case 1:
                if (cadastrados < limite) {
                    printf("Digite o nome do usuario: ");
                    scanf(" %49[^\n]", nome[cadastrados]);

                    printf("Digite a idade do usuario: ");
                    scanf("%d", &idade[cadastrados]);

                    cadastrados++;

                    printf("Usuario cadastrado com sucesso! (%d/%d)\n",
                           cadastrados, limite);
                } else {
                    printf("Limite maximo de cadastros atingido!\n");
                }
                break;

            case 2:
                exibirLista(cadastrados, nome, idade);
                break;

            case 3:
                printf("Encerrando o sistema...\n");
                break;

            default:
                printf("Opcao invalida! Tente novamente.\n");
                break;
        }

    } while (opcao != 3);

    return 0;
}

