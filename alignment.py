def define_alignment(self):
        print('Voce consideraria o seu personagem: ')
        question_LC = "a) Benevolente, preocupado em fazer o certo\nb) egoísta, não se importa em prejudicar os outros para ganho próprio\nc) ponderado, não se importa em ajudar ou prejudicar os outros dependendo do caso."
        answer_LC = self.ask_question(question_LC)

        print('Ele precisa que: ')
        question_GE = "a) que tudo funcione adequadamente, de forma lógica, para atingir um fim\nb) seguir o fluxo\nc) quebrar a rotina com frequência, sua e dos outros, mudando a forma como tudo acontece"
        answer_GE = self.ask_question(question_GE)

        if answer_LC == "a" and answer_GE == "a":
            return "Leal e Bom"
        elif answer_LC == "a" and answer_GE == "b":
            return "Leal e Mal"
        elif answer_LC == "a" and answer_GE == "c":
            return "Leal e Neutro"
        elif answer_LC == "b" and answer_GE == "a":
            return "Caotico e Bom"
        elif answer_LC == "b" and answer_GE == "b":
            return "Caotico e Mal"
        elif answer_LC == "b" and answer_GE == "c":
            return "Caotico e Neutro"
        elif answer_LC == "c" and answer_GE == "a":
            return "Neutro e Bom"
        elif answer_LC == "c" and answer_GE == "b":
            return "Neutro e Mal"
        elif answer_LC == "c" and answer_GE == "c":
            return "Neutro"
        else:
            return "Respostas inválidas. Por favor, tente novamente."
