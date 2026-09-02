from .minstrul import Minstrul
from .minstrulFactory import MinstrulFactory
from.statBudget import StatBudget

def CreateMinstrul(nickname: str, archetype, level: int, statBudget) -> Minstrul:
    return MinstrulFactory.CreateMinstrul(nickname, archetype, level, statBudget)

__all__ = ['Minstrul', 'CreateMinstrul']

__all__ = ['Minstrul', 'StatBudget', 'CreateMinstrul']
