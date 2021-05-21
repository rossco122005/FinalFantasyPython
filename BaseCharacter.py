class BaseCharacter:
    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.mp = 0
        self.attack = 5
        self.defense = 0

    def attack(self):
        return self.attack

    def be_attacked(self, damage):
        self.hp = self.hp - damage
        if self.hp <= 0:
            self.hp = 0

    def be_healed(self, amount_healed):
        self.hp = self.hp + amount_healed

    def get_name(self):
        return self.name

    def get_hp(self):
        return self.hp
