class Skill:
    def __init__(self, name, description, type, duration, power):
        self.name = name
        self.description = description
        self.type = type
        self.duration = duration
        self.power = power


class Entity:

    def __init__(self, name, hp, skills):
        self.name = name
        self.max_hp = hp
        self.current_hp = hp
        self.skills = skills
        self.is_alive = True

    def take_damage(self, amount):
        self.current_hp -= amount
        if self.current_hp <= 0:
            self.current_hp = 0
            self.is_alive = False



class Player(Entity):

    def __init__(self, name, hp, skills):
        super().__init__(name, hp, skills)
        self.lore = ""
        self.inventory = []




class Enemy(Entity):
    
    def __init__(self, entity_id, name, hp, skills):
        super().__init__(name, hp, skills)
        self.id = entity_id