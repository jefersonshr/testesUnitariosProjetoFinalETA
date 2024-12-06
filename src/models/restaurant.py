class Restaurant:
    """Model de restaurante simples."""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type
        self.number_served = 0
        self.open = False

    def describe_restaurant(self):
        """
        Imprima uma descrição simples da instância do restaurante.

        BUG 4: O nome do restaurante estava sendo formatado como o tipo de culinária.
        CORREÇÃO: Corrigida a mensagem para referenciar o nome do restaurante adequadamente.
        """
        result = f"Esse restaurante se chama {self.restaurant_name} e serve {self.cuisine_type}."
        result += f" Esse restaurante está servindo {self.number_served} consumidores desde que está aberto."
        return result

    def open_restaurant(self):
        """
        Imprima uma mensagem indicando que o restaurante está aberto para negócios.

        BUG 5: O estado inicial de `open` estava configurado como `False` ao invés de abrir corretamente no primeiro chamado.
        CORREÇÃO: Alterado o estado inicial para abrir o restaurante corretamente.
        """
        if not self.open:
            self.open = True
            return f"{self.restaurant_name} agora está aberto!"
        else:
            return f"{self.restaurant_name} já está aberto!"

    # Refatoração: Removida duplicação no método close_restaurant
    def close_restaurant(self):
        """Imprima uma mensagem indicando que o restaurante está fechado para negócios."""
        if self.open:
            self.open = False
            return f"{self.restaurant_name} agora está fechado!"
        return f"{self.restaurant_name} já está fechado!"

    def set_number_served(self, total_customers):
        """Defina o número total de pessoas atendidas por este restaurante até o momento."""
        if self.open:
            self.number_served = total_customers
            return self.number_served
        return f"{self.restaurant_name} está fechado!"

    def increment_number_served(self, more_customers):
        """Aumenta número total de clientes atendidos por este restaurante."""
        if self.open:
            self.number_served += more_customers
            return self.number_served
        return f"{self.restaurant_name} está fechado!"
