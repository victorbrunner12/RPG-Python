from Personagem import Personagem

class Monstro(Personagem):
    def __init__(self, pontos_vida, pontos_ataque, nome, tipo):
        super().__init__(pontos_vida, pontos_ataque, nome)
        self.tipo = tipo