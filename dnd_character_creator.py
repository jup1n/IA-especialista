from gender import define_gender
from alignment import define_alignment
from race import define_race
from clas import define_class
from subrace import define_subrace

class DnDCharacterCreator:
    def ask_question(self, question):
        print(question)
        return input().strip().lower()

    def create_character(self):
        gender = define_gender(self)
        alignment = define_alignment(self)
        race = define_race(self)
        classe = define_class(self)
        subrace = define_subrace(self, race)
        
        print(f"Gênero: {gender}")
        print(f"Alinhamento: {alignment}")
        if race == "Meio-Elfo" or race == "Atributo não identificado. Por favor, escolha somente um atributo.":
            print(f"Raça: {race}")
        else:
            print(f"Raça: {subrace}")
        print(f"Classe: {classe}")