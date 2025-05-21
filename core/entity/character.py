from datetime import datetime

from .entity import Entity
from .gender import Gender

class Character(Entity):
    def __init__(self, name: str, description: str,
                gender: Gender, birthdate: datetime.date):
        super().__init__(name, description)

        self.gender = gender
        self.birthdate = birthdate

def interact(self, entity: Entity):
        """
        Define the action to do when interacting with an entity.
        """
        raise NotImplementedError('Not implemented yet')


