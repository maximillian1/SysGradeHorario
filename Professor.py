class Professor():
    def __init__(self, nome, disciplinas, disponibilidade, cargaHoraria=0):
        self.idProfessor = 0
        self.nome = nome
        self.cargaHoraria = cargaHoraria
        self.disciplinas = list(Disciplina)
        self.disponibilidade = list(Disponibilidade)

        def preencherDisponibilidade():  # Esta função deve estar no main
            for h in range(0, 4):
                for d in range(0, 5):
                    disponibilidade[h][d] = int(input(f"Digite um valor: "))