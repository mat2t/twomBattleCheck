from minstrul.minstrul import Minstrul
from minstrul.statBudget import StatBudget

class CannonMinstrul(Minstrul):
    
    def __init__(self, nickname: str, level: int, statBudget: StatBudget):
        _statModifiers = [0.2, 0.375, 0.175, 0.25]

        super().__init__(nickname, level, statBudget, _statModifiers)