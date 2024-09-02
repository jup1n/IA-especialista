class DnDCharacterCreator:
    def ask_question(self, question):
        print(question)
        return input().strip().lower()
    
    def define_gender(self): # Definição do genero do personagem
        print("Responda das sequintes perguntas com a sua letra de identificação (a/b/c)")
        print("O seu personagem se define com o genero: ")
        question = "a) Feminino\nb) Masculino"
        answer = self.ask_question(question) == "a"
        
        if answer:
            gender = "Feminino"
        elif not answer:
            gender = "Masculino"
        
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
    
    def define_class(self):
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

        
    def define_race(self):
        print("Responda as seguintes questões com 'sim' ou 'não'")

        question_forca = "Seu personagem tem aumento de força?"
        answer_forca = self.ask_question(question_forca) == "sim"
        
        question_destreza = "Seu personagem tem aumento de destreza?"
        answer_destreza = self.ask_question(question_destreza) == "sim"
        
        question_constituicao = "Seu personagem tem aumento de constituição?"
        answer_constituicao = self.ask_question(question_constituicao) == "sim"
        
        question_inteligencia = "Seu personagem tem aumento de inteligência?"
        answer_inteligencia = self.ask_question(question_inteligencia) == "sim"
        
        question_sabedoria = "Seu personagem tem aumento de sabedoria?"
        answer_sabedoria = self.ask_question(question_sabedoria) == "sim"
        
        question_carisma = "Seu personagem tem aumento de carisma?"
        answer_carisma = self.ask_question(question_carisma) == "sim"
        
        question_resistencia = "Seu personagem tem resistência a dano?"
        answer_resistencia = self.ask_question(question_resistencia) == "sim"
        
        question_velocidade = "Seu personagem tem velocidade base de 30 pés?"
        answer_velocidade = self.ask_question(question_velocidade) == "sim"
        
        question_armas = "Seu personagem possui proficiência com armas?"
        answer_armas = self.ask_question(question_armas) == "sim"
        
        question_idiomas = "Seu personagem sabe idiomas adicionais?"
        answer_idiomas = self.ask_question(question_idiomas) == "sim"
        
        question_habilidades = "Seu personagem possui habilidades únicas?"
        answer_habilidades = self.ask_question(question_habilidades) == "sim"
        
        question_tamanho_pequeno = "Seu personagem tem tamanho pequeno?"
        answer_tamanho_pequeno = self.ask_question(question_tamanho_pequeno) == "sim"
        
        question_visao_escuro = "Seu personagem possui visão no escuro?"
        answer_visao_escuro = self.ask_question(question_visao_escuro) == "sim"

        if answer_forca and answer_destreza and answer_constituicao and not answer_inteligencia and not answer_sabedoria and answer_carisma and not answer_resistencia and answer_velocidade and not answer_armas and answer_idiomas and not answer_habilidades and not answer_tamanho_pequeno and not answer_visao_escuro:
            return "Humano"
        elif not answer_forca and not answer_destreza and answer_constituicao and not answer_inteligencia and answer_sabedoria and not answer_carisma and answer_resistencia and answer_velocidade and answer_armas and answer_idiomas and not answer_habilidades and not answer_tamanho_pequeno and answer_visao_escuro:
            return "Anão"
        elif not answer_forca and answer_destreza and not answer_constituicao and answer_inteligencia and answer_sabedoria and not answer_carisma and not answer_resistencia and answer_velocidade and answer_armas and not answer_idiomas and not answer_habilidades and not answer_tamanho_pequeno and answer_visao_escuro:
            return "Elfo"
        elif not answer_forca and answer_destreza and not answer_constituicao and not answer_inteligencia and not answer_sabedoria and answer_carisma and not answer_resistencia and not answer_velocidade and answer_armas and not answer_idiomas and not answer_habilidades and answer_tamanho_pequeno and not answer_visao_escuro:
            return "Halfling"
        elif answer_forca and not answer_destreza and answer_constituicao and not answer_inteligencia and not answer_sabedoria and not answer_carisma and not answer_resistencia and answer_velocidade and answer_armas and not answer_idiomas and not answer_habilidades and not answer_tamanho_pequeno and answer_visao_escuro:
            return "Meio-Orc"
        elif not answer_forca and answer_destreza and not answer_constituicao and answer_inteligencia and not answer_sabedoria and not answer_carisma and not answer_resistencia and not answer_velocidade and not answer_armas and answer_idiomas and answer_habilidades and answer_tamanho_pequeno and answer_visao_escuro:
            return "Gnomo"
        elif not answer_forca and answer_destreza and not answer_constituicao and not answer_inteligencia and answer_sabedoria and answer_carisma and not answer_resistencia and answer_velocidade and answer_armas and not answer_idiomas and answer_habilidades and not answer_tamanho_pequeno and answer_visao_escuro:
            return "Meio-Elfo"
        elif answer_forca and not answer_destreza and answer_constituicao and not answer_inteligencia and not answer_sabedoria and answer_carisma and not answer_resistencia and answer_velocidade and answer_armas and not answer_idiomas and answer_habilidades and not answer_tamanho_pequeno and answer_visao_escuro:
            return "Draconato"
        else:
            return "Raça indefinida. Respostas não coincidem com uma raça específica."

        
    def create_character(self):
        gender = self.define_gender()
        alignment = self.define_alignment()
        race = self.define_race()
        classe = self.define_class()
        
        print(f"Genero: {gender}")
        print(f"Alinhamento: {alignment}")
        print(f"Raça: {race}")
        print(f"Classe: {classe}")

creator = DnDCharacterCreator()
creator.create_character()