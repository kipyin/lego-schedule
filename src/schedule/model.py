""""""
from datetime import date
from typing import List
import enum

import attr

class Role(enum.Enum):
    WORSHIP_LEADER = "WORSHIP_LEADER"
    KEYBOARD = "KEYBOARD"
    DRUMS = "DRUMS"
    GUITAR = "GUITAR"
    PAD = "PAD"
    PROJECTION = "PROJECTION"


@attr.s(auto_attribs=True)
class Person:
    name: str
    blockout: List[date]
    roles: Role
    served_dates: List[date]


if __name__ == "__main__":
    kip = Person(
        name='Kip',
        roles = [Role.WORSHIP_LEADER],
        blockout=[],
        served_dates = []
    )
    
