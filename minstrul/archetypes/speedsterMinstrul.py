from minstrul.minstrul import Minstrul
from minstrul.statBudget import StatBudget
from minstrul.faction import Faction

class SpeedsterMinstrul(Minstrul):
    
    def __init__(self, nickname: str, faction: Faction, level: int, statBudget: StatBudget):
        _statModifiers = [0.225, 0.275, 0.175, 0.325]

        super().__init__(nickname, faction, level, statBudget, _statModifiers)