from eta_project.src.models.ice_cream_stand import IceCreamStand


class TestIceCreamStand:

    def test_flavors_available(self):
        sorveteria = IceCreamStand("Sorveteria Gelato", "Sorvetes Artesanais", ["Chocolate", "Baunilha"])
        expected = "\nNo momento temos os seguintes sabores de sorvete disponíveis:\t-Chocolate\t-Baunilha"

        result = sorveteria.flavors_available()

        assert expected == result

    def test_flavors_available_empty(self):
        sorveteria = IceCreamStand("Sorveteria Gelato", "Sorvetes Artesanais", [])
        expected = "Estamos sem estoque atualmente!"

        result = sorveteria.flavors_available()

        assert expected == result

    def test_find_flavor_exists(self):
        sorveteria = IceCreamStand("Sorveteria Gelato", "Sorvetes Artesanais", ["Chocolate", "Baunilha"])
        expected = "Temos no momento ['Chocolate', 'Baunilha']!"

        result = sorveteria.find_flavor("Chocolate")

        assert expected == result

    def test_find_flavor_not_exists(self):
        sorveteria = IceCreamStand("Sorveteria Gelato", "Sorvetes Artesanais", ["Chocolate", "Baunilha"])
        expected = "Não temos no momento ['Chocolate', 'Baunilha']!"

        result = sorveteria.find_flavor("Morango")

        assert expected == result

    def test_add_flavor_new(self):
        sorveteria = IceCreamStand("Sorveteria Gelato", "Sorvetes Artesanais", ["Chocolate", "Baunilha"])
        expected = "Morango adicionado ao estoque!"

        result = sorveteria.add_flavor("Morango")

        assert expected == result
        assert "Morango" in sorveteria.flavors

    def test_add_flavor_existing(self):
        sorveteria = IceCreamStand("Sorveteria Gelato", "Sorvetes Artesanais", ["Chocolate", "Baunilha"])
        expected = "\nSabor já disponivel!"

        result = sorveteria.add_flavor("Chocolate")

        assert expected == result

    def test_add_flavor_empty_stock(self):
        sorveteria = IceCreamStand("Sorveteria Gelato", "Sorvetes Artesanais", [])
        expected = "Estamos sem estoque atualmente!"

        result = sorveteria.add_flavor("Morango")

        assert expected == result
