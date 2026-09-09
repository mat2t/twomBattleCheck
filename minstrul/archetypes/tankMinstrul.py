from minstrul.minstrul import Minstrul
from minstrul.statBudget import StatBudget
from minstrul.minstrul import Faction

class TankMinstrul(Minstrul):
    
    def __init__(self, nickname: str, faction: Faction, level: int, statBudget: StatBudget):
        _statModifiers = [0.35, 0.2, 0.35, 0.1]

        super().__init__(nickname, faction, level, statBudget, _statModifiers)