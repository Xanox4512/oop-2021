from typing import List


class VeryComplicatedService:

    def __init__(self):
        pass

    def inialize(self, config):
        # skompliowany kod
        pass

    def method1(self):
        pass

    def method2(self):
        pass

    def method3(self):
        # tak naprawdę tylko z tej metody korzystamy
        pass

    def method4(self, client_object):
        pass

    def method9(self):
        pass


class WrapperService:
    __complicatedService: VeryComplicatedService

    def __init__(self):
        pass

    def method3(self, client_provided_name: str):
        pass


class ModernWrapperService(WrapperService):
    __modern_backend_service: object

    def __init__(self):
        pass

    def method3(self, client_provided_name: str):
        pass


"""
Dokumentacja: 
- działa jak VeryComplicatedService
- ma wszystkie potrzebne metody
- nie potrzeba wogóle wiedzieć co jest w VeryComplicatedService

"""
# service = VeryComplicatedService()
# service = WrapperService()
service = ModernWrapperService()
service.method3(client_provided_name='abra kadabra')



"""
Przykład...

Allegro...



"""

class Allegro:
    pass


class AllegroWrapper:

    def get_prices_by_product_name(self, product_name: str) -> List[int]:
        pass

    def buy_product(self, auction_id: int):
        # ~ https://allegro.pl/oferta/router-mikrotik-rb5009ug-s-in-11362683574
        pass


aw = AllegroWrapper()
prices = aw.get_prices_by_product_name(product_name='Mikrotik  RB5009UG+S+IN')
# i można zrobić statystyki tych cen, histogramy itp
