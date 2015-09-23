class Character:
    def __init__(self, data_dict):
        self.is_enemy = data_dict["is_enemy"]
        self.name = data_dict["name"]
        if self.health <= 0:
            self.is_dead = True
        else:
            self.is_dead = False
        self.health = int(data_dict["health"])
        self.stats = data_dict["stats"]

    def take_damage(self, damage_amount, damage_dealer):
        if self.is_dead:
            print("{0} can't be damaged, he's dead!".format(self.name))
        else:
            self.health -= damage_amount
            print("{0} dealt {1} damage to {2}!\n{2} has {3} HP now.".format(damage_dealer, damage_amount,
                                                                             self.name, self.health))
            if self.health <= 0:
                self.is_dead = True
                print("{0} is dead!".format(self.name))

    def take_heal(self, heal_amount, healer):
        if self.is_dead:
            print("{0} can't be healed, he's dead!".format(self.name))
        else:
            self.health += heal_amount
            if self.name == healer:
                print("{0} healed himself by {1} HP!\n{0} has {2} health now.".format(healer, heal_amount, self.health))
            else:
                print("{0} healed {1} by {2} HP!\n{1} has {3} HP now.".format(healer, self.name,
                                                                              heal_amount, self.health))


def get_character_data():
    char_string = None
    character_data = {}
    while char_string is None:
        character_data = {'is_enemy': input("Is the character an enemy? Y or N: ").capitalize()}
        if character_data["is_enemy"] == 'Y':
            char_string = "Enemy"
            character_data["is_enemy"] = True
        elif character_data["is_enemy"] == 'N':
            char_string = "Player"
            character_data["is_enemy"] = False
        else:
            print("Invalid input! Try again.")
    character_data["name"] = input("{0} name: ".format(char_string))
    character_data["health"] = input("{0} health: ".format(char_string))
    character_data["stats"] = dict(STR=input("{0} STR: ".format(char_string)),
                                   DEX=input("{0} DEX: ".format(char_string)),
                                   CON=input("{0} CON: ".format(char_string)),
                                   INT=input("{0} INT: ".format(char_string)),
                                   WIS=input("{0} WIS: ".format(char_string)),
                                   CHA=input("{0} CHA: ".format(char_string)))
    return character_data


def main():
    char1 = Character(get_character_data())
    char2 = Character(get_character_data())
    char3 = Character(get_character_data())
    print(char1.health)
    char1.take_heal(200, char2.name)
    print(char1.health)
    char1.take_damage(300, char3.name)
    print(char1.health)
    char1.take_damage(50, char3.name)
    print(char1.health)


if __name__ == '__main__':
    main()
