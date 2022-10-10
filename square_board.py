from unittest import result
from linear_board import *
from settings import BOARD_SIZE
from list_utils import *


class SquareBoard():
    """
    Clase que representa un tablero Cuadrado
    
    Métodos para:

    1. Añadir un carácter (jugar en una columna)
    2. Detectar la victoria de un jugador
    3. Detectar el empate de 2 jugadores
    4. Detectar que el tablero está lleno
    
    """
    @classmethod
    def fromList(cls, list_of_lists):
        #esto no lo entiendo
        board = cls()
        board._columns = list(map(lambda element: LinearBoard.fromList(element, list)))
        return board

    def __init__(self):
        """
        Crea las columnas del tablero
        """
        self._columns = [LinearBoard() for i in range(BOARD_SIZE - 1)]

    def is_full(self):
        """
        Busca si cada una de las columnas está llena
        """
        all_full = True
        for board in self._columns:
            all_full = all_full and board.is_full()
        return all_full

    def as_matrix(self):
        """"Devuelve una representación en formato de matrix"""
        return list(map(lambda x: x._column, self._columns))

    def is_victory(self, char):
        return self._any_vertical_victory(char) or self._any_horizontal_victory(char) or self._any_rising_victory(char) or self._any_sinking_victory(char)
    
    def add(self, char, index):
        self._columns[index].add(char)

    def _any_vertical_victory(self, char):
        victory = False
        for board in self._columns:
            victory = victory or board.is_victory(char)
        return victory

    def _any_horizontal_victory(self, char):
        # Transponemos _columns
        transp = transpose(self.as_matrix())
        # Creamos un tablero temporal con la transpuesta
        tmp = SquareBoard.fromList(transp)
        # Comprobamos si tiene una victoria temporal

        return False
    
    def _any_rising_victory(self, char):
        return False

    def _any_sinking_victory(self, char):
        return False

    def add(self, char, index):
        pass
    
    def __repr__(self):
        return f'{self.__class__}: {self._columns}'
    