from enumchoicefield import ChoiceEnum


class BetResultChoice(ChoiceEnum):
    W = "Opponent Lost"
    L = "Bettor Lost"
    T = "Everyone Lost(tied)"


class BetStateChoice(ChoiceEnum):
    C = "Completed"
    O = "Open"
    A = "Abandoned"
