class DnDCharacterCreator:
    def ask_question(self, question):
        print(question)
        return input().strip().lower()
    
    def define_gender(self):
        print("O seu personagem se define com o genero: ")
        question = "a) Feminino\n b) Masculino\n c) Indefinido"
        answer = self.ask_question(question)
        
        gender = answer
        
        return gender
        

    def define_alignment(self):
        print('Voce consideraria o seu personagem: ')
        question_LC = "a) Benevolente, preocupado em fazer o certo\nb) egoísta, não se importa em prejudicar os outros para ganho próprio\nc) ponderado, não se importa em ajudar ou prejudicar os outros dependendo do caso."
        answer_LC = self.ask_question(question_LC)

        print('Ele precisa que: ')
        question_GE = "a) que tudo funcione adequadamente, de forma lógica, para atingir um fim\nb) seguir o fluxo\nc) quebrar a rotina com frequência, sua e dos outros, mudando a forma como tudo acontece"
        answer_GE = self.ask_question(question_GE)

        alignment = "Indefinido"  # Valor padrão para alinhamento

        if answer_LC == "a" and answer_GE == "a":
            alignment = "Leal e Bom"
        elif answer_LC == "a" and answer_GE == "b":
            alignment = "Leal e Mal"
        elif answer_LC == "a" and answer_GE == "c":
            alignment = "Leal e Neutro"
        elif answer_LC == "b" and answer_GE == "a":
            alignment = "Caotico e Bom"
        elif answer_LC == "b" and answer_GE == "b":
            alignment = "Caotico e Mal"
        elif answer_LC == "b" and answer_GE == "c":
            alignment = "Caotico e Neutro"
        elif answer_LC == "c" and answer_GE == "a":
            alignment = "Neutro e Bom"
        elif answer_LC == "c" and answer_GE == "b":
            alignment = "Neutro e Mal"
        elif answer_LC == "c" and answer_GE == "c":
            alignment = "Neutro"
        else:
            print("Respostas inválidas. Por favor, tente novamente.")

        return alignment
    
    def define_race(self):
        print("Responda as seguintes questões com 'sim' ou 'não'")
        question_melee = "Seu personagem é voltado para combate corpo a corpo?"
        answer_melee = self.ask_question(question_melee) == "sim"
        
        question_ranged = "Seu personagem tem habilidades de combate à distância?"
        answer_ranged = self.ask_question(question_ranged) == "sim"
        
        question_caster = "Seu personagem será focado em lançar feitiços?"
        answer_caster = self.ask_question(question_caster) == "sim"
        
        question_sneaking = "Seu personagem terá habilidades de furtividade?"
        answer_sneaking = self.ask_question(question_sneaking) == "sim"
        
        question_detective = "Ele terá habilidades para investigações ou habilidades de detetive?"
        answer_detective = self.ask_question(question_detective) == "sim"
        
        question_speaching = "Ele terá boas habilidades de oratória ou negociação?"
        answer_speaching = self.ask_question(question_speaching) == "sim"
        
        question_tank = "O seu personagem pode atuar como tanque, absorvendo dano?"
        answer_tank = self.ask_question(question_tank) == "sim"

        if answer_melee and answer_ranged and not answer_caster and not answer_sneaking and not answer_detective and not answer_speaching and answer_tank:
            return "Guerreiro"
        elif answer_melee and answer_ranged and not answer_caster and answer_sneaking and not answer_detective and not answer_speaching and not answer_tank:
            return "Ladino"
        elif answer_melee and not answer_ranged and answer_caster and not answer_sneaking and not answer_detective and not answer_speaching and not answer_tank:
            return "Feiticeiro"
        elif answer_melee and not answer_ranged and answer_caster and not answer_sneaking and not answer_detective and answer_speaching and answer_tank:
            return "Paladino"
        elif answer_melee and not answer_ranged and answer_caster and not answer_sneaking and not answer_detective and answer_speaching and answer_tank:
            return "Clerico"
        elif answer_melee and not answer_ranged and answer_caster and not answer_sneaking and not answer_detective and not answer_speaching and answer_tank:
            return "Druida"
        elif answer_melee and not answer_ranged and not answer_caster and not answer_sneaking and not answer_detective and not answer_speaching and answer_tank:
            return "Barbario"
        elif not answer_melee and answer_ranged and answer_caster and not answer_sneaking and not answer_detective and not answer_speaching and not answer_tank:
            return "Bruxo"
        elif not answer_melee and answer_ranged and answer_caster and not answer_sneaking and not answer_detective and answer_speaching and not answer_tank:
            return "Warlock"
        elif answer_melee and not answer_ranged and not answer_caster and not answer_sneaking and not answer_detective and not answer_speaching and not answer_tank:
            return "Monge"
        elif not answer_melee and answer_ranged and not answer_caster and answer_sneaking and not answer_detective and not answer_speaching and not answer_tank:
            return "Ranger"
        elif not answer_melee and not answer_ranged and answer_caster and answer_sneaking and not answer_detective and answer_speaching and not answer_tank:
            return "Bardo"
        else:
            return "Classe indefinida. Respostas não coincidem com uma classe específica."

        
    def create_character(self):
        alignment = self.define_alignment()
        print(f"Alinhamento: {alignment}")

# Uso da classe
creator = DnDCharacterCreator()
creator.create_character()