from minstrul.minstrul import Minstrul, StatBudget, Faction
from minstrul.archetypes import *


class MinstrulFactory:
    _registry = {
            Archetype.BALANCED: BalancedMinstrul,
            Archetype.CANNON: CannonMinstrul,
            Archetype.TANK: TankMinstrul,
            Archetype.SPEEDSTER: SpeedsterMinstrul
        }

    @classmethod
    def CreateMinstrul(self, nickname: str, faction: Faction, level: int, archetype: Archetype,
                       statBudget: StatBudget) -> Minstrul:
        if archetype not in self._registry:
            raise ValueError(f"Unknown type: {archetype}")
            
        minstrul = self._registry[archetype]
        return minstrul(nickname, faction, level, statBudget)
