from abc import ABC, abstractmethod


# abstrakt osztály
class Szoba(ABC):

    @abstractmethod
    def __init__(self, ar, szobaszam):
        self._ar = ar
        self.szobaszam = szobaszam
