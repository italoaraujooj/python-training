class Aluno:
    
    def __init__(self, matricula, name):
        self.__matricula = matricula
        self.__name = name

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def get_matricula(self):
        return self.__matricula


