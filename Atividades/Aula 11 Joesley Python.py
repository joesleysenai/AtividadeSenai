'''
- Então crie uma classe denominada “Reserva” com os seguintes atributos: número do avião e nome do passageiro. 
- Na sequência, no método principal do algoritmo, primeiro defina um array de objetos do tipo “Reserva”.
- Observe que este é um array de referências e não de objetos reais. Em seguida, crie objetos reais para a classe “Reserva”.
'''

class Aviao:
    def __init__(self, codigo):
        self.codigo = codigo


def numerar_avioes(cod_aviao):
    print("\n--- Cadastro dos aviões ---")

    for i in range(4):
        while True:
            try:
                numero = int(input(f"Digite o número do avião {i + 1}: "))

                if numero in cod_aviao:
                    print("Este número de avião já foi cadastrado!")
                else:
                    cod_aviao[i] = numero
                    break

            except ValueError:
                print("Digite um número inteiro válido!")

    print("Aviões cadastrados com sucesso!")


def cadastrar_assentos(cod_aviao, assentos):
    if 0 in cod_aviao:
        print("Cadastre primeiro os quatro aviões na opção 1!")
        return

    print("\n--- Cadastro de assentos ---")

    for i in range(4):
        while True:
            try:
                quantidade = int(
                    input(
                        f"Quantos assentos estão disponíveis "
                        f"no avião {cod_aviao[i]}? "
                    )
                )

                if quantidade < 0:
                    print("A quantidade não pode ser negativa!")
                else:
                    assentos[i] = quantidade
                    break

            except ValueError:
                print("Digite uma quantidade inteira válida!")

    print("Assentos cadastrados com sucesso!")


class Reserva:
    def __init__(self, cod_aviao, nome_passageiro):
        self.cod_aviao = cod_aviao
        self.nome_passageiro = nome_passageiro


def reservar_passagem(cod_aviao, assentos, reservas, total_reservas):
    if 0 in cod_aviao:
        print("Cadastre primeiro os quatro aviões na opção 1!")
        return total_reservas

    if total_reservas >= 20:
        print("Limite de 20 reservas atingido!")
        return total_reservas

    try:
        numero = int(input("Informe o número do avião: "))
    except ValueError:
        print("Digite um número de avião válido!")
        return total_reservas

    if numero not in cod_aviao:
        print("Este avião não existe!")
        return total_reservas

    indice = cod_aviao.index(numero)

    if assentos[indice] <= 0:
        print("Não há assentos disponíveis para este avião!")
        return total_reservas

    nome = input("Digite o nome do passageiro: ").strip()

    if not nome:
        print("O nome do passageiro não pode ficar vazio!")
        return total_reservas

    # Criação do objeto real
    reserva = Reserva(numero, nome)

    # Armazenamento da referência no array
    reservas[total_reservas] = reserva

    assentos[indice] -= 1

    print("Reserva realizada com sucesso!")

    return total_reservas + 1


def consultar_por_aviao(cod_aviao, reservas):
    if 0 in cod_aviao:
        print("Cadastre primeiro os quatro aviões na opção 1!")
        return

    try:
        numero = int(input("Informe o número do avião: "))
    except ValueError:
        print("Digite um número de avião válido!")
        return

    if numero not in cod_aviao:
        print("Este avião não existe!")
        return

    encontrou = False

    print(f"\n--- Reservas do avião {numero} ---")

    for reserva in reservas:
        if reserva.cod_aviao == numero:
            print("Passageiro:", reserva.nome_passageiro)
            encontrou = True

    if not encontrou:
        print("Não há reservas realizadas para este avião!")


def consultar_por_passageiro(reservas):
    nome = input("Informe o nome do passageiro: ").strip()

    encontrou = False

    print(f"\n--- Reservas de {nome} ---")

    for reserva in reservas:
        if reserva.nome_passageiro.casefold() == nome.casefold():
            print("Número do avião:", reserva.cod_aviao)
            encontrou = True

    if not encontrou:
        print("Não há reservas realizadas para este passageiro!")


def exibir_menu():
    print("\n========== Sweet Flight ==========")
    print("1 - Registrar o número de cada avião")
    print("2 - Registrar os assentos disponíveis")
    print("3 - Reservar passagem aérea")
    print("4 - Consultar reservas por avião")
    print("5 - Consultar reservas por passageiro")
    print("6 - Sair do sistema")
    print("==================================")


def main():
    # Vetores com quatro posições
    cod_aviao = [0, 0, 0, 0]
    assentos = [0, 0, 0, 0]

    # Array com 20 posições para referências de objetos Reserva
    reservas = [None] * 20

    # Controla a quantidade de reservas realizadas
    total_reservas = 0

    while True:
        exibir_menu()

        try:
            opcao = int(input("Escolha uma opção: "))
        except ValueError:
            print("Digite uma opção válida!")
            continue

        if opcao == 1:
            numerar_avioes(cod_aviao)

        elif opcao == 2:
            cadastrar_assentos(cod_aviao, assentos)

        elif opcao == 3:
            if total_reservas < 20:
                # Cria a reserva e armazena sua referência
                total_reservas = reservar_passagem(
                cod_aviao,
                assentos,
                reservas,
                total_reservas)
            else:
                print("Limite de 20 reservas atingido!")

        elif opcao == 4:
            consultar_por_aviao(
                cod_aviao,
                reservas[:total_reservas]
            )

        elif opcao == 5:
            consultar_por_passageiro(
                reservas[:total_reservas]
            )

        elif opcao == 6:
            print("Encerrando Sweet Flight...")
            break

        else:
            print("Opção inválida! Tente novamente.")


if __name__ == "__main__":
    main()
