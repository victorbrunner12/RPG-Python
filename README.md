# RPG-Python

A classe base "SerVivo" é definida com dois atributos inteiros: pontos_vida e pontos_ataque, que representam os pontos de vida e ataque do ser vivo.

A classe "Personagem" é uma classe derivada de "SerVivo" com um atributo adicional nome, uma string que representa o nome do personagem. Ela também possui dois métodos, "atacar" e "super_ataque", que executam um ataque básico e um ataque especial, respectivamente, em um personagem ou monstro.

O método "atacar" executa um ataque básico baseado em um dano calculado da seguinte forma:
	"self.pontos_ataque" é a quantidade de pontos de ataque do personagem atacante.
	"personagem_atacado.pontos_vida" é a quantidade de pontos de vida do personagem sendo atacado.

	A formula para o dano é simplesmente a quantidade de pontos de ataque do personagem atacante menos
	a quantidade de pontos de vida do personagem sendo atacado.
	

O método "super_ataque" executa um ataque calculado, levando em consideração o seu atributo adicional:
	
	"personagem_atacando.pontos_ataque": A quantidade de pontos de ataque que o personagem que está atacando possui.
	"personagem_atacando.inteligencia": A inteligência do personagem que está atacando.
	"personagem_atacado.forca": A força do personagem que está sendo atacado.
	
	A fórmula utiliza essas variáveis para determinar a quantidade de dano que o ataque causará ao personagem que está sendo atacado.

	--personagem_atacando.pontos_ataque * personagem_atacando.inteligencia / personagem_atacado.forca--

	OBS: Somente Lobo possui o atributo "forca" e somente o Goblin possui o atributo "inteligencia". Caso o Lobo esteja atacando o Goblin fica:
	
	--personagem_atacando.pontos_ataque * personagem_atacando.forca / personagem_atacado.inteligencia--

A classe "Monstro" é uma classe derivada de "Personagem" com um atributo adicional tipo, que representa o tipo de monstro.

A classe "Lobo" é uma classe derivada de "Monstro" com um atributo adicional forca, que representa a força do lobo.

A classe "Goblin" é uma classe derivada de "Monstro" com um atributo adicional inteligencia, que representa a inteligência do goblin.

As instâncias lobo e goblin são criadas com os atributos apropriados e seus pontos de vida iniciais são impressos na tela.
