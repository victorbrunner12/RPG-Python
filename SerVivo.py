class SerVivo:
    def __init__(self, pontos_vida, pontos_ataque):
        self.pontos_vida = pontos_vida
        self.pontos_ataque = pontos_ataque

    def atacar(self, personagem_atacado):
        try:
            if self.verifica_personagem_vivo(self, personagem_atacado):
                if personagem_atacado.nome.lower() == 'goblin':
                    personagem_atacado.pontos_vida -= self.pontos_ataque
                    print(
                        f"{self.nome} atacou {personagem_atacado.nome} com {self.pontos_ataque} pontos de ataque.\n{personagem_atacado.nome} agora tem {personagem_atacado.pontos_vida} de pontos de vida.\n")
                elif personagem_atacado.nome.lower() == 'lobo mau':
                    personagem_atacado.pontos_vida -= self.pontos_ataque
                    print(
                        f"{self.nome} atacou {personagem_atacado.nome} com {self.pontos_ataque} pontos de ataque.\n{personagem_atacado.nome} agora tem {personagem_atacado.pontos_vida} de pontos de vida.\n")
        except Exception as ex:
            print(ex)

    def super_ataque(self, personagem_atacado):
        try:
            if self.verifica_personagem_vivo(self, personagem_atacado):
                if personagem_atacado.nome.lower() == 'goblin':
                    dano = self.pontos_ataque * self.forca / personagem_atacado.inteligencia * 1.5
                    personagem_atacado.pontos_vida -= dano
                    print(
                        f"{self.nome} atacou {personagem_atacado.nome} com super poder.\n{personagem_atacado.nome} agora tem {personagem_atacado.pontos_vida} de pontos de vida.\n")
                elif personagem_atacado.nome.lower() == 'lobo mau':
                    dano = self.pontos_ataque * self.inteligencia / personagem_atacado.forca * 1.5
                    personagem_atacado.pontos_vida -= dano
                    print(
                        f"{self.nome} atacou {personagem_atacado.nome} com super poder.\n{personagem_atacado.nome} agora tem {personagem_atacado.pontos_vida} de pontos de vida.\n")
        except Exception as ex:
            print(ex)

