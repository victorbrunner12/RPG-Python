from SerVivo import SerVivo

class Personagem(SerVivo):
    def __init__(self, pontos_vida, pontos_ataque, nome):
        super().__init__(pontos_vida, pontos_ataque)
        self.nome = nome

    def verifica_personagem_vivo(self, personagem_atacando, personagem_atacado):
        try:
            if personagem_atacando.pontos_vida <= 0 or personagem_atacado.pontos_vida <= 0:
                print(f"A Batalha acabou! O {personagem_atacando.nome if personagem_atacando.pontos_vida<=0 else personagem_atacado.nome} morreu!")
                return False
            return True
        except Exception as ex:
            print(ex)