from minstrul.minstrul import Minstrul
from minstrul.statBudget import StatBudget
from minstrul.faction import Faction

class BalancedMinstrul(Minstrul):
    
    def __init__(self,nickname: str, faction: Faction, level: int, statBudget: StatBudget):
        _statModifiers = [0.25, 0.25, 0.25, 0.25]

        super().__init__(nickname, faction, level, statBudget, _statModifiers)