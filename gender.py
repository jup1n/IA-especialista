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