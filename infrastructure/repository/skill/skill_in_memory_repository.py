from enum import Enum
from typing import List

from domain.skill.skill import Skill
from domain.skill.skill_repository import SkillRepository
from infrastructure.repository.skill.in_memory_skills import InMemorySkills
from infrastructure.repository.skill.skill_to_domain import to_domain


class SkillInMemoryRepository(SkillRepository):
    def __init__(self, skills: Enum = InMemorySkills):
        self.skills = [skill.value for skill in skills]

    def get_skill(self, name: str) -> Skill:
        skill = [skill for skill in self.skills if skill['name'] == name][0]
        return to_domain(skill)

    def get_all_skills(self) -> List[Skill]:
        return self.skills
