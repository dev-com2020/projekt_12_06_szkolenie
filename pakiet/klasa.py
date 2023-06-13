from abc import abstractmethod, ABC


class Dom(ABC):
    __metraz = 100
    __ilosc_okien = 5
    __ilosc_drzwi = 2
    __ilosc_pieter = 1

    def pokaz_metraz(self):
        print(f'Metraz: {self.__metraz}')

    @abstractmethod
    def pokaz_ilosc_okien(self):
        pass

class Dom2(Dom):

    def __init__(self, metraz, ilosc_okien=5, ilosc_drzwi=2, ilosc_pieter=1):
        self.metraz = metraz
        self.__ilosc_okien = ilosc_okien
        self.__ilosc_drzwi = ilosc_drzwi
        self.__ilosc_pieter = ilosc_pieter

    def pokaz_metraz(self):
        print(f'Metraz: {self.metraz}')

    def pokaz_ilosc_okien(self):
        print(f'Ilosc okien: {self.__ilosc_okien}')

class Dom3(Dom2):
    def __init__(self, metraz, ilosc_okien=5, ilosc_drzwi=2, ilosc_pieter=1, kolor_elewacji='szary'):
        super().__init__(metraz, ilosc_okien, ilosc_drzwi, ilosc_pieter)
        self.kolor_elewacji = kolor_elewacji

    def pokaz_metraz(self):
        print(f'Metraz: {self.metraz}')
        print(f'Kolor elewacji: {self.kolor_elewacji}')

    def pokaz_kolor(self):
        print(f'Kolor elewacji: {self.kolor_elewacji}')




dom2 = Dom2(300)
dom2.pokaz_metraz()
dom3 = Dom3(400)
dom3.pokaz_metraz()
dom3.pokaz_kolor()
dom3.ilosc_okien = "nie ma okien"
dom3.ilosc_okien = 10
dom3.pokaz_ilosc_okien()
print((Dom3).mro())