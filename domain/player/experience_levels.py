from enum import Enum


class ExperienceLevel(Enum):
    level_1 = {
        'level': 1,
        'min': 0,
        'max': 99,
    }
    level_2 = {
        'level': 2,
        'min': 100,
        'max': 199,
    }

    level_3 = {
        'level': 3,
        'min': 200,
        'max': 399,
    }

    level_4 = {
        'level': 4,
        'min': 400,
        'max': 799,
    }

    level_5 = {
        'level': 5,
        'min': 800,
        'max': 1599,
    }

    level_6 = {
        'level': 6,
        'min': 1600,
        'max': 3199,
    }

    level_7 = {
        'level': 7,
        'min': 3200,
        'max': 6399,
    }

    level_8 = {
        'level': 8,
        'min': 6400,
        'max': 12799,
    }

    level_9 = {
        'level': 9,
        'min': 12800,
        'max': 25599,
    }

    level_10 = {
        'level': 10,
        'min': 25600,
        'max': 51199,
    }
