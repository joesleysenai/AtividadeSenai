#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct Usuario {
    char nome[50];
    int idade;
    struct Usuario* proximo;
};

void adicionarUsuario(struct Usuario** inicio, char* nome, int idade) {
    struct Usuario* novoUsuario = (struct Usuario*) malloc(sizeof(struct Usuario));
    if (novoUsuario == NULL) {
        printf("Erro ao alocar memória!\n");
        return;
    }
    strcpy(novoUsuario->nome, nome);
    novoUsuario->idade = idade;
    novoUsuario->proximo = *inicio;
    *inicio = novoUsuario;
}

void exibirLista(struct Usuario* inicio) {
    struct Usuario* atual = inicio;
    printf("\n--- Lista de Usuarios ---\n");
    if (atual == NULL) {
        printf("Nenhum usuario cadastrado ainda.\n");
        return;
    }
    while (atual != NULL) {
        printf("Nome: %s\n", atual->nome);
        printf("Idade %d\n", atual->idade);
        atual = atual->proximo;
    }
    printf("-------------------------\n");
}

void exibirMenu() {
    printf("\n================= Menu Principal ==================\n");
    printf("1 - Cadastrar novo usuario\n");
    printf("2 - Listar todos os usuarios cadastrados\n");
    printf("3 - Sair do sistema\n");
    printf("Opcao: ");
}

void liberarMemoria(struct Usuario* inicio) {
    struct Usuario* atual = inicio;
    while (atual != NULL) {
        struct Usuario* temp = atual;
        atual = atual->proximo;
        free(temp);
    }
}

int main(int argc, char *argv[]) {
    struct Usuario* lista = NULL;
    int limite = 0;
    int cadastrados = 0;
    int opcao = 0;
    char nome[50];
    int idade;
    printf("Quantos usuarios serao cadastrados no maximo? ");
    scanf("%d", &limite);

    do {
        exibirMenu();
        scanf("%d", &opcao);

        switch (opcao) {
            case 1:
                if (cadastrados < limite) {
                    printf("Digite o nome do usuario: ");
                    scanf(" %[^\n]", nome);
                    printf("Digite a idade do usuario: ");
                    scanf(" %d", &idade);
                    adicionarUsuario(&lista, nome, idade);
                    cadastrados++;
                    printf("Usuario cadastrado com sucesso! (%d/%d)\n", cadastrados, limite);
                } else {
                    printf("Limite maximo de cadastros atingido!\n");
                }
                break;
            
            case 2:
                exibirLista(lista);
                break;

            case 3:
                printf("Encerrando o sistema...\n");
                break;

            default:
                printf("Opcao invalida! Tente novamente.\n");
                break;
        }

    } while (opcao != 3); // && cadastrados < limite);

    
    exibirLista(lista);

    
    liberarMemoria(lista);

    return 0;
}
