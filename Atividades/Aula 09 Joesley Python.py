# 1. Contextualização
# Após o sucesso nas implementações das estruturas de dados Pilha e Fila, o estudante foi solicitado pela
# empresa para desenvolver uma última implementação necessária ao projeto.
# Nesta nova demanda, será utilizada uma estrutura homogênea (vetor) contendo 20 elementos, que deverá
# ser ordenada por meio de dois algoritmos diferentes:
# • BubbleSort: algoritmo de ordenação mais simples, destinado à implementação inicial do serviço para o
# cliente.
# • MergeSort: algoritmo de ordenação mais eficiente, destinado a uma futura otimização do sistema.
# Para o desenvolvimento da atividade, será utilizado o seguinte vetor de números inteiros:
# Vetor original:
# [1, 7, 10, 9, 2, 3, 20, 18, 33, 90, 44, 34, 30, 21, 27, 5, 8, 99, 54, 68]


def exibir_menu():
    print("\n================= Menu Principal ==================")
    print("1 - Ordenar em BubbleSort")
    print("2 - Ordenar em MergeSort")
    print("3 - Listar: Exibe a lista")
    print("4 - Resetar Vetor")
    print("5 - Sair do sistema")

def bubbleSort(vetor):
    # aparentemente no python se passar sem o .copy o vetor original é modificado (pesquisar o motivo)
    ordenado = vetor.copy()
    n = len(ordenado)
    # repetição para inverter as posições
    for i in range(n-1):
        for j in range(n-i-1):
            if ordenado[j] > ordenado[j+1]:
                ordenado[j], ordenado[j+1] = ordenado[j+1], ordenado[j]
    return ordenado

def mergeSort(vetor):
  # checar se o vetor tem como ser dividido
  if len(vetor) <= 1:
    return vetor    
  # dividindo o vetor ao meio
  meio = len(vetor) // 2
  metadeEsquerda = vetor[:meio]
  metadeDireita = vetor[meio:]

  esquerdaOrganizada = mergeSort(metadeEsquerda)
  direitaOrganizada = mergeSort(metadeDireita)

  return merge(esquerdaOrganizada, direitaOrganizada)

def merge(esquerda, direita):
  resultado = []
  i = j = 0

  while i < len(esquerda) and j < len(direita):
    if esquerda[i] < direita[j]:
      resultado.append(esquerda[i])
      i += 1
    else:
      resultado.append(direita[j])
      j += 1

  resultado.extend(esquerda[i:])
  resultado.extend(direita[j:])

  return resultado

def main():
    vetor = [1, 7, 10, 9, 2, 3, 20, 18, 33, 90, 44, 34, 30, 21, 27, 5, 8, 99, 54, 68]
    ordenado = []    

    while True:
        exibir_menu()
        try:
            opcao = int(input("Opção: "))
        except ValueError:
            print("Digite uma opção válida!")
            continue

        if opcao == 1:
            ordenado = bubbleSort(vetor)
            print("Vetor ordenado com Bubble:", ordenado)
            
        elif opcao == 2:
            ordenado = mergeSort(vetor)
            print("Vetor ordenado com merge:", ordenado)            

        elif opcao == 3:
            print("Vetor:", vetor)
            print("Vetor organizado", ordenado)
        
        elif opcao == 4:
            vetor = [1, 7, 10, 9, 2, 3, 20, 18, 33, 90, 44, 34, 30, 21, 27, 5, 8, 99, 54, 68]

        elif opcao == 5:
            print("Encerrando o sistema...")
            break
        else:
            print("Opção inválida! Tente novamente.")


if __name__ == "__main__":
    main()