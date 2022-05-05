class Disponibilidade():
    def __init__(self, idProfessor, horariosDispProf):
        self.idDisponibilidade = 0
        self.idProfessor = idProfessor
        self.horariosDispProf = [[0, 0, 0, 0, 0],
                                 [0, 0, 0, 0, 0],
                                 [0, 0, 0, 0, 0],
                                 [0, 0, 0, 0, 0]]