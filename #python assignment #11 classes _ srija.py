# By Srija Belide
# This program represents the player's health
# and power using classes
class Character:
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power
    def __str__(self):
        return self.name + " has " + str(self.health) + str(self.power)

    def damage(self, damage_health):
        self.health = self.health - damage_health
        return self.health
        

        
player1 = Character("Chun-Li", 100, 5)
player2 = Character("Ryu", 150, 8)

player1_damage = player1.damage(8)
player2_damage = player2.damage(5)


print("Chun-Li's current health after the damage is", player1_damage)
print("Ryu's current health after the damage is", player2_damage)
        



    
       
        
        

        
      