from eta_project.src.models.restaurant import Restaurant


class IceCreamStand(Restaurant):
    """Um tipo especializado de restaurante."""

    def __init__(self, restaurant_name, cuisine_type, flavors_list):
        """
        Inicialize os atributos da classe pai.
        Em seguida, inicialize os atributos específicos de uma sorveteria.
        """
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors_list

    def flavors_available(self):
        """
        Percorra a lista de sabores disponíveis e imprima.

        BUG 1: Os sabores não estavam separados por linhas na mensagem.
        CORREÇÃO: Adicionada quebra de linha entre os sabores na mensagem final.
        """
        if self.flavors:
            result = "\nNo momento temos os seguintes sabores de sorvete disponíveis:\n"
            for flavor in self.flavors:
                result += f"\t-{flavor}\n"
            return result
        else:
            return "Estamos sem estoque atualmente!"

    def find_flavor(self, flavor):
        """
        Verifica se o sabor informado está disponível.

        BUG 2: A mensagem de confirmação e ausência mostrava uma lista completa de sabores ao invés de apenas confirmar ou negar.
        CORREÇÃO: Ajustadas as mensagens para indicar apenas se o sabor está ou não disponível.
        """
        if self.flavors:
            if flavor in self.flavors:
                return f"Temos no momento o sabor {flavor}!"
            else:
                return f"Não temos no momento o sabor {flavor}!"
        else:
            return "Estamos sem estoque atualmente!"

    def add_flavor(self, flavor):
        """
        Adiciona o sabor informado ao estoque.

        BUG 3: Ao tentar adicionar um sabor quando a lista de sabores estava vazia, o método retornava "Estamos sem estoque atualmente!".
        CORREÇÃO: Adicionado suporte para inicializar a lista de sabores caso esteja vazia.
        """
        if self.flavors is None or not self.flavors:  # Refatoração: Verifica lista vazia ou None
            self.flavors = [flavor]
            return f"{flavor} adicionado ao estoque!"
        elif flavor in self.flavors:
            return "\nSabor já disponível!"
        else:
            self.flavors.append(flavor)
            return f"{flavor} adicionado ao estoque!"
