#Requisitos:
#✅ Use uma estrutura homogênea (vetor) com 20 posições
#✅ Implemente as funções abaixo:

#• Empilhar: adiciona um elemento no topo da pilha
#• Desempilhar: remove e retorna o elemento do topo da pilha
#• Limpar: remove todos os elementos da pilha
#• Listar: exibe todos os elementos armazenados na pilha
#• Vazia: retorna verdadeiro se a pilha estiver vazia e falso se não estiver

#⚠️ Faça todos os tratamentos necessários para evitar o estouro do vetor. Por exemplo: 
# empilhar com a pilha cheia ou desempilhar com a pilha vazia.
TAMANHO = 20

def exibir_menu():
    print("\n================= Menu Principal ==================")
    print("1 - Empilhar: adiciona um elemento no topo da pilha")
    print("2 - Desempilhar: remove e retorna o elemento do topo da pilha")
    print("3 - Limpar: remove todos os elementos da pilha")
    print("4 - Listar: exibe todos os elementos armazenados na pilha")
    print("5 - Vazia: verifica se a pilha está vazia")
    print("6 - Sair do sistema")

def empilhar(pilha, topo, nome):
    # Se o topo for igual o tamanho -1: pilha cheia entao nao adicionar maiss
    if topo == TAMANHO - 1:
        print("Erro: a pilha está cheia!")
        return topo
    # Avança o topo e adiciona o elemento
    topo += 1
    pilha[topo] = nome
    print("Elemento empilhado com sucesso!")
    return topo

def desempilhar(pilha, topo):
    # se -1: pilha vazia
    if topo == -1:
        print("Erro: a pilha está vazia!")
        return topo, None
    # Guarda o elemento do topo para exibgir posteriormente
    elemento = pilha[topo]
    pilha[topo] = None
    # Move o topo para baixo
    topo -= 1
    print(f"Elemento removido: {elemento}")
    return topo, elemento

def limpar(pilha, topo):
    if topo == -1:
        print("A pilha já está vazia!")
        return topo
    # Remove todos os elementos 
    while topo >= 0:
        pilha[topo] = None
    # Traz o topo pra baixo
        topo -= 1
    print("Pilha limpa com sucesso!")
    return topo

def listar(pilha, topo):
    if topo == -1:
        print("A pilha está vazia!")
        return
    print("\nElementos da pilha (do topo para a base):")
    # Percorrer do topo até a base
    for i in range(topo, -1, -1):
        print(f"[{i}] {pilha[i]}")

def vazia(topo):
    if topo == -1:
        print("Pilha vazia!")
        return True

    print("Pilha com elementos!")
    return False

def main():
    pilha = [None] * TAMANHO
    # Iniciar topo (p´recisa iniciar como -1 para as checagens)
    topo = -1
    while True:
        exibir_menu()
        try:
            opcao = int(input("Opção: "))
        except ValueError:
            print("Digite uma opção válida!")
            continue

        if opcao == 1:
            nome = input("Digite o nome do usuário: ")
            topo = empilhar(pilha, topo, nome)

        elif opcao == 2:
            topo, elemento = desempilhar(pilha, topo)

        elif opcao == 3:
            topo = limpar(pilha, topo)

        elif opcao == 4:
            listar(pilha, topo)

        elif opcao == 5:
            vazia(topo)

        elif opcao == 6:
            print("Encerrando o sistema...")
            break

        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()
