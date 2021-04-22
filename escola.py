from aluno import Aluno
class Escola:

    def __init__(self, name):
        self.__alunos = []
        self.__matricula = 0
        self.name = name

    def get_alunos(self):
        return __alunos

    def gerar_matricula(self):
        ret = self.__matricula
        self.__matricula = self.__matricula + 1
        return ret

    def get_nome(self):
        return self.name
    
    def set_nome(self, name):
        self.name = name  

    def add_aluno(self, nome):
        aluno = Aluno(self.gerar_matricula(), nome)
        self.__alunos.append(aluno)
        print('Aluno adicionado com sucesso!')
        print(f'matricula: {aluno.get_matricula()}, nome: {aluno.get_name()}')

    def visualizar_alunos(self):
        for aluno in self.__alunos:
            print(f'{aluno.get_matricula()} - {aluno.get_name()}')

    def buscar_aluno(self, matricula):
        for aluno in self.__alunos:
            if matricula == aluno.get_matricula():
                return aluno
        return None
                
    def editar_aluno(self, matricula, aluno):
        alunoEncontrado = self.buscar_aluno(matricula)
        alunoEncontrado.set_name(aluno.get_name())

    def deletar_aluno(self, matricula):
        for aluno in self.__alunos:
            if matricula == aluno.get_matricula():
                return self.__alunos.remove(aluno)

