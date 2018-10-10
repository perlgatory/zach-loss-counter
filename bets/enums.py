from enum import Enum

class BetResultChoice(Enum):
    W = "Opponent Lost"
    L = "Bettor Lost"
    T = "Everyone Lost(tied)"

class BetStateChoice(Enum):
    C = "Completed"
    O = "Open"
    A = "Abandoned"
