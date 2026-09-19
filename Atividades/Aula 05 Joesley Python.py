def exibir_lista(cadastrados, nomes, idades):
    if cadastrados == 0:
        print("Nenhum usuario cadastrado ainda.")
        return

    print("\n========== Usuarios cadastrados ==========")

    for i in range(cadastrados):
        print(f"Nome: {nomes[i]}")
        print(f"Idade: {idades[i]}")
        print("-------------------------")


def buscar_usuario(cadastrados, nomes, idades):
    if cadastrados == 0:
        print("Nenhum usuario cadastrado ainda.")
        return

    print("\n========== Buscar Usuario ==========")
    busca = input("\nDigite o nome do usuario: ").strip().lower()

    for i in range(cadastrados):
        if busca == nomes[i].lower():
            print(f"Nome: {nomes[i]}")
            print(f"Idade: {idades[i]}")
            print(f"Posição: {i+1}")
            print("-------------------------")
            return

    print("Usuario nao encontrado!")


def remover_usuario(cadastrados, nomes, idades):
    if cadastrados == 0:
        print("Nenhum usuario cadastrado ainda.")
        return cadastrados

    nome_busca = input("Digite o nome do usuario que deseja remover: ").strip().lower()

    for i in range(cadastrados):
        if nome_busca == nomes[i].lower():
            print(f"Usuario encontrado: {nomes[i]} ({idades[i]} anos)")
            resposta = input("Deseja realmente remover este usuario? (S/N): ").strip().upper()

            if resposta == "S":
                del nomes[i]
                del idades[i]
                cadastrados -= 1
                print("Usuario removido com sucesso!")
            else:
                print("Remocao cancelada.")

            return cadastrados

    print("Usuario nao encontrado!")
    return cadastrados


def exibir_menu():
    print("\n================= Menu Principal ==================")
    print("1 - Cadastrar novo usuario")
    print("2 - Listar todos os usuarios cadastrados")
    print("3 - Buscar usuario")
    print("4 - Remover usuario")
    print("5 - Sair do sistema")


def main():
    cadastrados = 0

    limite = int(input("Quantos usuarios serao cadastrados no maximo? "))

    if limite <= 0:
        print("O limite deve ser maior que zero.")
        return

    nomes = []
    idades = []

    opcao = 0

    while opcao != 5:
        exibir_menu()
        opcao = int(input("Opcao: "))

        if opcao == 1:
            if cadastrados < limite:
                nome = input("Digite o nome do usuario: ")
                idade = int(input("Digite a idade do usuario: "))

                nomes.append(nome)
                idades.append(idade)

                cadastrados += 1

                print(
                    f"Usuario cadastrado com sucesso! "
                    f"({cadastrados}/{limite})"
                )
            else:
                print("Limite maximo de cadastros atingido!")

        elif opcao == 2:
            exibir_lista(cadastrados, nomes, idades)

        elif opcao == 3:
            buscar_usuario(cadastrados, nomes, idades)

        elif opcao == 4:
            cadastrados = remover_usuario(cadastrados, nomes, idades)

        elif opcao == 5:
            print("Encerrando o sistema...")
            return
        else:
            print("Opcao invalida! Tente novamente.")


if __name__ == "__main__":
    main()
