from eta_project.src.models.restaurant import Restaurant
from eta_project.src.models.ice_cream_stand import IceCreamStand


def main():
    # Criando instâncias
    restaurant_name = "Restaurante Gourmet"
    cuisine_type = "Comida Internacional"
    ice_cream_name = "Sorveteria Gelato"
    ice_cream_type = "Sorvetes Artesanais"
    initial_flavors = ["Chocolate", "Baunilha", "Morango"]

    restaurant = Restaurant(restaurant_name, cuisine_type)
    ice_cream_stand = IceCreamStand(ice_cream_name, ice_cream_type, initial_flavors)

    while True:
        print("\nMenu Principal:")
        print("1. Funcionalidades do Restaurante")
        print("2. Funcionalidades da Sorveteria")
        print("3. Sair")

        main_choice = input("Escolha uma opção (1-3): ")

        if main_choice == "1":
            while True:
                print("\nFuncionalidades do Restaurante:")
                print("1. Descrever o restaurante")
                print("2. Abrir o restaurante")
                print("3. Fechar o restaurante")
                print("4. Definir número de clientes atendidos")
                print("5. Incrementar número de clientes atendidos")
                print("6. Voltar ao menu principal")

                choice = input("Escolha uma opção (1-6): ")

                if choice == "1":
                    print(restaurant.describe_restaurant())
                elif choice == "2":
                    print(restaurant.open_restaurant())
                elif choice == "3":
                    print(restaurant.close_restaurant())
                elif choice == "4":
                    total_customers = int(input("Digite o total de clientes atendidos: "))
                    print(restaurant.set_number_served(total_customers))
                elif choice == "5":
                    more_customers = int(input("Digite o número de clientes a adicionar: "))
                    print(restaurant.increment_number_served(more_customers))
                elif choice == "6":
                    break
                else:
                    print("Opção inválida. Por favor, escolha novamente.")

        elif main_choice == "2":
            while True:
                print("\nFuncionalidades da Sorveteria:")
                print("1. Ver sabores disponíveis")
                print("2. Verificar se um sabor está disponível")
                print("3. Adicionar um novo sabor")
                print("4. Voltar ao menu principal")

                choice = input("Escolha uma opção (1-4): ")

                if choice == "1":
                    print(ice_cream_stand.flavors_available())
                elif choice == "2":
                    flavor = input("Digite o sabor que deseja verificar: ")
                    print(ice_cream_stand.find_flavor(flavor))
                elif choice == "3":
                    new_flavor = input("Digite o sabor que deseja adicionar: ")
                    print(ice_cream_stand.add_flavor(new_flavor))
                elif choice == "4":
                    break
                else:
                    print("Opção inválida. Por favor, escolha novamente.")

        elif main_choice == "3":
            print("Obrigado por visitar nosso sistema! Até logo!")
            break

        else:
            print("Opção inválida. Por favor, escolha novamente.")


if __name__ == "__main__":
    main()
