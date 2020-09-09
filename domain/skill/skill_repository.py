from abc import abstractmethod
from typing import List

from sqlalchemy.testing.plugin.plugin_base import ABC

from domain.skill.skill import Skill


class SkillRepository(ABC):
    @abstractmethod
    def get_skill(self, name: str) -> Skill:
        pass

    @abstractmethod
    def get_all_skills(self) -> List[Skill]:
        pass
