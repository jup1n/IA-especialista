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

        
    def define_race(self):
        print("Responda as seguintes questões com 'sim' ou 'não'")
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

        if answer_resistencia and answer_velocidade and not answer_armas and answer_idiomas and not answer_habilidades and not answer_tamanho_pequeno and not answer_visao_escuro:
            return "Humano"
        elif answer_resistencia and answer_velocidade and answer_armas and answer_idiomas and not answer_habilidades and not answer_tamanho_pequeno and answer_visao_escuro:
            return "Anão"
        elif not answer_resistencia and answer_velocidade and answer_armas and not answer_idiomas and not answer_habilidades and not answer_tamanho_pequeno and answer_visao_escuro:
            return "Elfo"
        elif not answer_resistencia and not answer_velocidade and answer_armas and not answer_idiomas and not answer_habilidades and answer_tamanho_pequeno and not answer_visao_escuro:
            return "Halfling"
        elif not answer_resistencia and answer_velocidade and answer_armas and not answer_idiomas and not answer_habilidades and not answer_tamanho_pequeno and answer_visao_escuro:
            return "Meio-Orc"
        elif not answer_resistencia and not answer_velocidade and not answer_armas and answer_idiomas and answer_habilidades and answer_tamanho_pequeno and answer_visao_escuro:
            return "Gnomo"
        elif not answer_resistencia and answer_velocidade and answer_armas and not answer_idiomas and answer_habilidades and not answer_tamanho_pequeno and answer_visao_escuro:
            return "Meio-Elfo"
        elif not answer_resistencia and answer_velocidade and answer_armas and not answer_idiomas and answer_habilidades and not answer_tamanho_pequeno and answer_visao_escuro:
            return "Draconato"
        else:
            question_habilidade = "Seu personagem se destaca em algum atributo?"
            answer_habilidade = self.ask_question(question_habilidade)

            if not answer_habilidade.lower():
                return "Humano"
            else:
                question_atributo = "Qual atributo? (forca, destreza, constituicao, inteligencia, sabedoria ou carisma)"
                answer_atributo = self.ask_question(question_atributo).lower()

                if answer_atributo == "forca":
                    return "Meio-Orc"
                elif answer_atributo == "destreza":
                    return "Meio-Elfo"
                elif answer_atributo == "constituicao":
                    return "Anão"
                elif answer_atributo == "inteligencia":
                    return "Gnomo"
                elif answer_atributo == "sabedoria":
                    return "Elfo"
                elif answer_atributo == "carisma":
                    return "Draconato"
                else:
                    return "Atributo não identificado. Por favor, escolha somente um atributo."

    def define_subrace(self, race):
        if race == "Humano":
            print("Seu personagem possui um talento especial desde o nível 1, ou prefere ser versátil em todos os atributos?")
            question = "a) Talento\nb) Versátil"
            answer = self.ask_question(question)
            
            if answer == "a":
                return "Humano Variante"
            elif answer == "b":
                return "Humano Padrão"
            else:
                print("Resposta inválida. Por favor, tente novamente.")
        
        elif race == "Anão":
            print("Seu personagem é mais resistente e duradouro, ou prefere ter força e habilidades de combate?")
            question = "a) Resistente\nb) Forte"
            answer = self.ask_question(question)
            
            if answer == "a":
                return "Anão da Colina"
            elif answer == "b":
                return "Anão da Montanha"
            else:
                print("Resposta inválida. Por favor, tente novamente.")
        
        elif race == "Elfo":
            print("Seu personagem tem uma conexão maior com a magia ou prefere se misturar com a natureza?")
            question = "a) Magia\nb) Natureza"
            answer = self.ask_question(question)
            
            if answer == "a":
                return "Alto-Elfo"
            elif answer == "b":
                return "Elfo da Floresta"
            else:
                print("Resposta inválida. Por favor, tente novamente.")
        
        elif race == "Halfling":
            print("Seu personagem é mais furtivo e prefere se esconder, ou é mais robusto e resiliente?")
            question = "a) Furtivo\nb) Robusto"
            answer = self.ask_question(question)
            
            if answer == "a":
                return "Halfling Pés-Leves"
            elif answer == "b":
                return "Halfling Robusto"
            else:
                print("Resposta inválida. Por favor, tente novamente.")
        
        elif race == "Meio-Orc":
            print("Seu personagem prefere usar sua força bruta em combate ou desenvolveu habilidades sociais para sobreviver nas cidades?")
            question = "a) Força Bruta\nb) Habilidades Sociais"
            answer = self.ask_question(question)
            
            if answer == "a":
                return "Meio-Orc Selvagem"
            elif answer == "b":
                return "Meio-Orc Urbano"
            else:
                print("Resposta inválida. Por favor, tente novamente.")
        
        elif race == "Gnomo":
            print("Seu personagem é um inventor e engenheiro ou tem uma conexão especial com a natureza?")
            question = "a) Inventor\nb) Conexão com a Natureza"
            answer = self.ask_question(question)
            
            if answer == "a":
                return "Gnomo das Rochas"
            elif answer == "b":
                return "Gnomo Florestal"
            else:
                print("Resposta inválida. Por favor, tente novamente.")

        
    def create_character(self):
        gender = self.define_gender()
        alignment = self.define_alignment()
        race = self.define_race()
        classe = self.define_class()
        subrace = self.define_subrace(race)
        
        print(f"Genero: {gender}")
        print(f"Alinhamento: {alignment}")
        print(f"Raça: {subrace}")
        print(f"Classe: {classe}")

creator = DnDCharacterCreator()
creator.create_character()