from sw_character_generator.classes.playerclass import PlayerClass
from sw_character_generator.functions.save_character import save_character
from sw_character_generator.classes.profession.assassin import apply_assassin_dependent_modifiers as assassin_mods

def main():

    Blubb = PlayerClass(
        player_name="Test Player",
        character_name="Aragorn",
        gender="Male",
        age=30,
    )
    #save_character(Blubb)
    
    print(Blubb)
    assassin_mods(Blubb)
    print("After applying assassin modifiers:")
    print(Blubb)    

    #save_character(Blubb)


if __name__ == "__main__":
    main()