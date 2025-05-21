from .character import Character

class Player(Character):
    def __init__(self, name, description, gender, birthdate):
        super().__init__(name, description, gender, birthdate)
        