from minstrul.minstrul import Minstrul
from minstrul.statBudget import StatBudget

class TankMinstrul(Minstrul):
    
    def __init__(self, nickname: str, level: int, statBudget: StatBudget):
        _statModifiers = [0.35, 0.2, 0.35, 0.1]

        super().__init__(nickname, level, statBudget, _statModifiers)