class Character:
    """Base class for all game characters with common attributes and methods."""
    
    def __init__(self, name, health, level=1):
        self.name = name
        self.max_health = health
        self.current_health = health
        self.level = level
        self.is_alive = True
    
    def take_damage(self, amount):
        """Reduces character health when taking damage."""
        self.current_health = max(0, self.current_health - amount)
        if self.current_health == 0:
            self.is_alive = False
            print(f"{self.name} has been defeated!")
        else:
            print(f"{self.name} takes {amount} damage! Health: {self.current_health}/{self.max_health}")
    
    def heal(self, amount):
        """Restores character health."""
        if not self.is_alive:
            print(f"{self.name} cannot be healed because they are defeated!")
            return
        
        self.current_health = min(self.max_health, self.current_health + amount)
        print(f"{self.name} heals for {amount}! Health: {self.current_health}/{self.max_health}")
    
    def level_up(self):
        """Increases character level and enhances stats."""
        self.level += 1
        self.max_health = int(self.max_health * 1.1)  # 10% health increase per level
        self.current_health = self.max_health
        print(f"{self.name} levels up to level {self.level}! Max health increased to {self.max_health}")
    
    def __str__(self):
        """String representation of the character."""
        status = "Alive" if self.is_alive else "Defeated"
        return f"{self.name} (Lvl {self.level}) - HP: {self.current_health}/{self.max_health} - Status: {status}"


class Warrior(Character):
    """Warrior class specializing in physical combat and defensive abilities."""
    
    def __init__(self, name, health=150, strength=10, armor=5, level=1):
        super().__init__(name, health, level)
        self.strength = strength
        self.armor = armor
        self.rage = 0
    
    def take_damage(self, amount):
        """Warriors reduce incoming damage with their armor."""
        reduced_damage = max(1, amount - self.armor)
        self.rage += 5  # Warriors gain rage when taking damage
        print(f"{self.name}'s armor absorbs {amount - reduced_damage} damage!")
        super().take_damage(reduced_damage)
    
    def attack(self, target):
        """Basic warrior attack."""
        damage = self.strength + (self.level * 2)
        print(f"{self.name} attacks {target.name} with their weapon for {damage} damage!")
        target.take_damage(damage)
        self.rage += 3
    
    def execute(self, target):
        """Powerful attack that consumes rage."""
        if self.rage >= 20:
            damage = (self.strength * 2) + (self.level * 3)
            print(f"{self.name} executes a devastating blow on {target.name} for {damage} damage!")
            target.take_damage(damage)
            self.rage -= 20
        else:
            print(f"{self.name} doesn't have enough rage to execute! (Current: {self.rage}/20)")
    
    def level_up(self):
        """Warriors gain additional benefits when leveling up."""
        super().level_up()
        self.strength += 2
        self.armor += 1
        print(f"{self.name}'s strength increased to {self.strength} and armor to {self.armor}!")
    
    def __str__(self):
        """Extended string representation with warrior-specific attributes."""
        base_str = super().__str__()
        return f"{base_str} - STR: {self.strength} - ARM: {self.armor} - RAGE: {self.rage}"


class Mage(Character):
    """Mage class focusing on magical abilities and spellcasting."""
    
    def __init__(self, name, health=100, intelligence=15, mana=100, level=1):
        super().__init__(name, health, level)
        self.intelligence = intelligence
        self.max_mana = mana
        self.current_mana = mana
        self.spells = ["Fireball", "Ice Shard", "Arcane Missile"]
    
    def cast_spell(self, spell_name, target):
        """Cast a spell on a target if enough mana is available."""
        mana_costs = {"Fireball": 20, "Ice Shard": 15, "Arcane Missile": 10, "Teleport": 30}
        
        if spell_name not in self.spells:
            print(f"{self.name} doesn't know the spell '{spell_name}'!")
            return
        
        if spell_name not in mana_costs:
            print(f"Unknown spell: {spell_name}")
            return
            
        mana_cost = mana_costs[spell_name]
        
        if self.current_mana < mana_cost:
            print(f"{self.name} doesn't have enough mana to cast {spell_name}! (Current: {self.current_mana}/{mana_cost})")
            return
            
        self.current_mana -= mana_cost
        
        # Different spell effects
        if spell_name == "Fireball":
            damage = (self.intelligence * 2) + (self.level * 3)
            print(f"{self.name} casts Fireball, engulfing {target.name} in flames for {damage} damage!")
            target.take_damage(damage)
        elif spell_name == "Ice Shard":
            damage = self.intelligence + (self.level * 2)
            print(f"{self.name} casts Ice Shard, piercing {target.name} for {damage} damage!")
            target.take_damage(damage)
        elif spell_name == "Arcane Missile":
            damage = int(self.intelligence * 0.8) + self.level
            print(f"{self.name} casts Arcane Missile, striking {target.name} for {damage} damage!")
            target.take_damage(damage)
        
        print(f"{self.name}'s remaining mana: {self.current_mana}/{self.max_mana}")
    
    def meditate(self):
        """Recover mana through meditation."""
        recover_amount = int(self.max_mana * 0.3)
        self.current_mana = min(self.max_mana, self.current_mana + recover_amount)
        print(f"{self.name} meditates and recovers {recover_amount} mana. Current mana: {self.current_mana}/{self.max_mana}")
    
    def learn_spell(self, spell_name):
        """Learn a new spell if it's valid."""
        valid_spells = ["Fireball", "Ice Shard", "Arcane Missile", "Teleport", "Polymorph", "Arcane Intellect"]
        
        if spell_name in self.spells:
            print(f"{self.name} already knows {spell_name}!")
            return
            
        if spell_name in valid_spells:
            self.spells.append(spell_name)
            print(f"{self.name} has learned the spell: {spell_name}!")
        else:
            print(f"{spell_name} is not a valid spell to learn!")
    
    def level_up(self):
        """Mages gain additional benefits when leveling up."""
        super().level_up()
        self.intelligence += 3
        self.max_mana += 20
        self.current_mana = self.max_mana
        print(f"{self.name}'s intelligence increased to {self.intelligence} and max mana to {self.max_mana}!")
    
    def __str__(self):
        """Extended string representation with mage-specific attributes."""
        base_str = super().__str__()
        return f"{base_str} - INT: {self.intelligence} - MANA: {self.current_mana}/{self.max_mana} - SPELLS: {len(self.spells)}"
if __name__ == "__main__":
    # Create character instances
    warrior = Warrior("Thorgar", health=200, strength=12)
    mage = Mage("Elindra", health=120, intelligence=18, mana=150)

    # Print character information
    print("===== Initial Character Stats =====")
    print(warrior)
    print(mage)
    print()

    # Test interactions
    print("===== Combat Simulation =====")
    warrior.attack(mage)
    mage.cast_spell("Fireball", warrior)
    
    print("\n===== Special Abilities =====")
    warrior.execute(mage)  # Not enough rage yet
    warrior.take_damage(30)  # Building rage
    warrior.execute(mage)  # Now has enough rage
    
    print("\n===== Character Development =====")
    mage.meditate()
    mage.learn_spell("Teleport")
    warrior.level_up()
    mage.level_up()
    
    print("\n===== Updated Character Stats =====")
    print(warrior)
    print(mage)