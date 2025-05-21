from .scene_entity import SceneEntity

class Scene:
    def __init__(self, name: str, description: str,
                 entities: list[SceneEntity]):
        self.name = name
        self.description = description
        self.entities = []
