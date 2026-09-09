from .minstrul import Minstrul
from .faction import Faction, FACTION_EFFECTIVENESS
from .minstrulFactory import MinstrulFactory
from.statBudget import StatBudget

def CreateMinstrul(nickname: str, faction: Faction, archetype, level: int, statBudget) -> Minstrul:
    return MinstrulFactory.CreateMinstrul(nickname, faction, archetype, level, statBudget)

__all__ = ['Minstrul', 'StatBudget', 'Faction', 'FACTION_EFFECTIVENESS', 'CreateMinstrul']
