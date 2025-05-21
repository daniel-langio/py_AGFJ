from .character import Character

class NPC(Character):
    def __init__(self, name, description, gender, birthdate):
        super().__init__(name, description, gender, birthdate)

