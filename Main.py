from Lobo import Lobo
from Goblin import Goblin

if __name__=='__main__':
    lobo = Lobo(pontos_vida=3, pontos_ataque=45, nome='Lobo Mau', tipo='Lobo Grande', forca=45)
    goblin = Goblin(pontos_vida=950, pontos_ataque=3, nome='Goblin', tipo='Goblin Ancião', inteligencia=55)

    print(f"Vida goblin: {goblin.pontos_vida}\nVida Lobo: {lobo.pontos_vida}\n")


    lobo.super_ataque(personagem_atacado=goblin)
    goblin.super_ataque(personagem_atacado=lobo)

    lobo.atacar(personagem_atacado=goblin)
    goblin.atacar(personagem_atacado=lobo)