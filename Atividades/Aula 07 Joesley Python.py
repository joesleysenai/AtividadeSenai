# Foi demandado ao estudante a implementação de novas funcionalidades no sistema da empresa Ozzy.
# A atividade consiste em realizar a implementação de duas estruturas de dados que serão utilizadas em um novo projeto 
# que está em desenvolvimento. As estruturas de dados são uma fila e uma Fila, as quais devem seguir os princípios 
# de desenvolvimento conhecidos pelo estudante. Como estas estruturas deverão armazenar nomes de pessoas, devem, 
# portanto, possuir um tipo de dado correspondente a esta necessidade.

# Etapa 02
# Agora você deverá implementar a estrutura de Fila, lembrando que esta estrutura segue o conceito de que o primeiro a entrar 
# é o primeiro a sair. A fila deverá ser implementada utilizando uma estrutura homogênea com 25 posições, 
# e as seguintes funções deverão ser implementadas para a manipulação da fila:
# Adicionar (insere um elemento no final da fila);
# Remover (remove e retorna o elemento do início da fila);
# Limpar (remove todos os elementos da fila na ordem correta);
# Listar (lista todos os elementos existentes na fila);
# Vazia (retorna verdade se a fila estiver vazia, e falso caso contrário).
# Lembre-se de realizar todos os tratamentos necessários para que não aconteça o estouro da estrutura homogênea.

TAMANHO = 25

def exibir_menu():
    print("\n================= Menu Principal ==================")
    print("1 - Adicionar (insere um elemento no final da fila);")
    print("2 - Remover (remove e retorna o elemento do início da fila);")
    print("3 - Limpar (remove todos os elementos da fila na ordem correta);")
    print("4 - Listar: exibe todos os elementos armazenados na fila")
    print("5 - Vazia: verifica se a fila está vazia")
    print("6 - Sair do sistema")

def adicionar(fila, frente, fim, quantidade, nome):
    # Verifica se a fila está cheia
    if quantidade == TAMANHO:
        print("Erro: a fila está cheia!")
        return frente, fim, quantidade
    # Insere o nome no fim da fila e incrementa o fim (Testando fila circular)
    fila[fim] = nome
    fim = (fim + 1) % TAMANHO
    # Aumentaa a quantidade de elementos
    quantidade += 1
    print("Elemento enfileirado com sucesso!")
    return frente, fim, quantidade

def remover(fila, frente, fim, quantidade):
    # Verificar se a fila está vazia
    if quantidade == 0:
        print("Erro: a fila está vazia!")
        return frente, fim, quantidade, None
    # Guarda o elemento que será removido
    elemento = fila[frente]
    #remove o elemento 
    fila[frente] = None
    # Avança o inicio da fila (Circular)
    frente = (frente + 1) % TAMANHO
    # Diminui a quantidade
    quantidade -= 1    
    # Se a fila ficou vazia, reinicia os índices
    if quantidade == 0:
        frente = 0
        fim = 0
    print(f"Elemento removido: {elemento}")
    return frente, fim, quantidade, elemento

def limpar(fila, frente, fim, quantidade):
    if quantidade == 0:
        print("A fila já está vazia!")
        return 0, 0, 0
    # Remove todos os elementos 
    for i in range(TAMANHO):
        fila[i] = None

    print("Fila limpa com sucesso!")
    return 0 ,0 ,0

def listar(fila, frente, fim, quantidade):
    if quantidade == 0:
        print("A fila está vazia!")
        return
    print("\nElementos da fila (Do inicio ao fim):")
    posicao = frente
    # Percorrer do inicioo até o final
    for i in range(quantidade):
        print(f"[{posicao}] {fila[posicao]}")
        # Avança posição forma circular
        posicao = (posicao + 1) % TAMANHO

def vazia(quantidade):
    if quantidade == 0:
        print("Fila vazia!")
        return True

    print("Fila com elementos!")
    return False

def popular(fila, frente, fim, quantidade):
    nomes = ["João","Maria","Carlos","Ana","Pedro"]
    for nome in nomes:
        frente, fim, quantidade = adicionar(fila, frente, fim, quantidade, nome)
    return frente, fim, quantidade

def main():
    fila = [None] * TAMANHO
    # INdices do frente e fim (p´recisa iniciar como 0 para as checagens)
    frente = 0
    fim = 0
    quantidade = 0

    while True:
        exibir_menu()
        try:
            opcao = int(input("Opção: "))
        except ValueError:
            print("Digite uma opção válida!")
            continue

        if opcao == 1:
            nome = input("Digite o nome do usuário: ")
            frente, fim, quantidade = adicionar(fila, frente, fim, quantidade, nome)

        elif opcao == 2:
            frente, fim, quantidade, elemento = remover(fila, frente, fim, quantidade)

        elif opcao == 3:
            frente, fim, quantidade = limpar(fila, frente, fim, quantidade)

        elif opcao == 4:
            listar(fila, frente, fim, quantidade)

        elif opcao == 5:
            vazia(quantidade)

        elif opcao == 6:
            print("Encerrando o sistema...")
            break
        elif opcao == 7:
            frente, fim, quantidade = popular(fila, frente, fim, quantidade)
            print("Fila populada para testes!")
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()
