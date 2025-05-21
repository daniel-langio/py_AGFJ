from .entity import Entity

class Object(Entity):
    def __init__(self, name: str, description: str):
        super().__init__(name, description)


    