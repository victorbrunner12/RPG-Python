from Monstro import Monstro

class Goblin(Monstro):
    def __init__(self, pontos_vida, pontos_ataque, nome, tipo, inteligencia):
        super().__init__(pontos_vida, pontos_ataque, nome, tipo)
        self.inteligencia = inteligencia