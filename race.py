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
                question_atributo = "Escolha um atributo dentre os seguintes: forca, destreza, constituicao, inteligencia, sabedoria ou carisma"
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