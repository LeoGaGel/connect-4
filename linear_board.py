from settings import BOARD_SIZE, VICTORY_STRIKE
from list_utils import find_streak

class LinearBoard:
    """
    Representa un tablero con una sola columna.
    x representa al jugador 1
    o representa al jugador 2
    None reprersenta un espacio vacío
    """
    
    def __init__(self):
        """
        Inicializa el tablero vacío. usease, lleno de None
        """
        self._column = [None] * BOARD_SIZE

    @classmethod
    def fromList(cls, list):
        board = cls()
        board._column = list
        return board
        
    def is_full(self):
        """
        Devuelve True si el tablero está lleno
        """
        # si el último elemento es None, NO está lleno
        if self._column[-1] == None:
            return False
        else:
            return True

 
    def add(self, char):
        """
        Añade una 'ficha' en dicha columna, en el primer espacio disponible
        """
        # si no está lleno
        if not self.is_full():
            # averiguo donde está el primer None
            i = self._column.index(None)
            # lo cambio por un char
            self._column[i] = char


    def is_victory(self, char):
        return find_streak(self._column,char, VICTORY_STRIKE)

    def is_tie(self, char1, char2):
        # si no hay victoria de nadie, pues hay empate
        if (self.is_victory(char1) == False) and (self.is_victory(char2) == False) and self.is_full:
            return True
        else:
            return False



