from Monstro import Monstro

class Lobo(Monstro):
    def __init__(self, pontos_vida, pontos_ataque, nome, tipo, forca):
        super().__init__(pontos_vida, pontos_ataque, nome, tipo)
        self.forca = forca