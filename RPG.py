class SerVivo:
    def __init__(self, pontos_vida, pontos_ataque):
        self.pontos_vida = pontos_vida
        self.pontos_ataque = pontos_ataque
    
class Personagem(SerVivo):
    def __init__(self, pontos_vida, pontos_ataque, nome):
        super().__init__(pontos_vida, pontos_ataque)
        self.nome = nome

    def atacar(self, personagem_atacado):
        try:
            if self.verifica_personagem_vivo(personagem_atacado):
                if personagem_atacado.nome.lower() == 'goblin':
                    personagem_atacado.pontos_vida -= self.pontos_ataque
                    print(f"{self.nome} atacou {personagem_atacado.nome} com {self.pontos_ataque} pontos de ataque.\n{personagem_atacado.nome} agora tem {personagem_atacado.pontos_vida} de pontos de vida.\n")
                elif personagem_atacado.nome.lower() == 'lobo mau':
                    personagem_atacado.pontos_vida -= self.pontos_ataque 
                    print(f"{self.nome} atacou {personagem_atacado.nome} com {self.pontos_ataque} pontos de ataque.\n{personagem_atacado.nome} agora tem {personagem_atacado.pontos_vida} de pontos de vida.\n")
        except Exception as ex:
            print(ex)

    def super_ataque(self, personagem_atacando, personagem_atacado):
        try:
            if self.verifica_personagem_vivo(personagem_atacado):
                if personagem_atacado.nome.lower() == 'goblin':
                    dano = personagem_atacando.pontos_ataque*personagem_atacando.forca / personagem_atacado.inteligencia
                    personagem_atacado.pontos_vida -= dano
                    print(f"{self.nome} atacou {personagem_atacado.nome} com super poder.\n{personagem_atacado.nome} agora tem {personagem_atacado.pontos_vida} de pontos de vida.\n")
                elif personagem_atacado.nome.lower() == 'lobo mau':
                    dano = personagem_atacando.pontos_ataque*personagem_atacando.inteligencia / personagem_atacado.forca
                    personagem_atacado.pontos_vida -= dano
                    print(f"{self.nome} atacou {personagem_atacado.nome} com super poder.\n{personagem_atacado.nome} agora tem {personagem_atacado.pontos_vida} de pontos de vida.\n")
        except Exception as ex:
            print(ex)

    def verifica_personagem_vivo(self, personagem_atacado):
        try:
            if self.pontos_vida <= 0 or personagem_atacado.pontos_vida <= 0:
                print(f"A Batalha acabou! O {self.nome if self.pontos_vida==0 else personagem_atacado.nome} morreu!")
                return False
            return True
        except Exception as ex:
            print(ex)

class Monstro(Personagem):
    def __init__(self, pontos_vida, pontos_ataque, nome, tipo):
        super().__init__(pontos_vida, pontos_ataque, nome)
        self.tipo = tipo

class Lobo(Monstro):
    def __init__(self, pontos_vida, pontos_ataque, nome, tipo, forca):
        super().__init__(pontos_vida, pontos_ataque, nome, tipo)
        self.forca = forca

class Goblin(Monstro):
    def __init__(self, pontos_vida, pontos_ataque, nome, tipo, inteligencia):
        super().__init__(pontos_vida, pontos_ataque, nome, tipo)
        self.inteligencia = inteligencia

lobo = Lobo(pontos_vida=100, pontos_ataque=45, nome='Lobo Mau', tipo='Lobo Grande', forca=100)
goblin = Goblin(pontos_vida=950, pontos_ataque=3, nome='Goblin', tipo='Goblin Ancião', inteligencia=100)

print(f"Vida goblin: {goblin.pontos_vida}\nVida Lobo: {lobo.pontos_vida}\n")

lobo.super_ataque(personagem_atacando=lobo, personagem_atacado=goblin)
goblin.super_ataque(personagem_atacando=goblin, personagem_atacado=lobo)
lobo.atacar(personagem_atacado=goblin)
goblin.atacar(personagem_atacado=lobo)

