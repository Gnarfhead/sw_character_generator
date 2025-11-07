from sw_character_generator.classes.playerclass import PlayerClass
from sw_character_generator.classes.profession.ranger import Ranger
from sw_character_generator.classes.race.human import Human
from sw_character_generator.functions import save_character

def main():
    character = PlayerClass(
        player_name="Test Player",
        character_name="Aragorn",
        profession="ranger",
        race="human",
        alignment="good"
    )
    print(character)

save_character(character)

if __name__ == "__main__":
    main()