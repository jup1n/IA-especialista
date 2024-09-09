def define_class(self):
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
            return "Bardo"