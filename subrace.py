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