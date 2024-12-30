import modulo_personagem

"""Classe orquestradora do jogo"""
class Jogo:
    def __init__(self):
        self.heroi = modulo_personagem.Heroi(nome="Herói", vida=100, nivel=5, habilidade="Super Força")
        self.inimigo = modulo_personagem.Inimigo(nome="Morcego", vida=80, nivel=5, tipo="Voador")

    def iniciar_batallha(self):
        print("Iniciando a batalha!")
        while self.heroi.get_vida() > 0 and self.inimigo.get_vida() > 0:
            print("\nDetalhes dos Personagens:")
            print(self.heroi.exibir_detalhes())
            print(self.inimigo.exibir_detalhes())

            input("Pressione Enter para atacar....")
            escolha = input("\nTipos de Ataque Disponíveis \n1. Ataque Normal \n2. Ataque Especial \nEscolha: ")

            if escolha == '1':
                self.heroi.atacar(self.inimigo)
            elif escolha == '2':
                self.heroi.ataque_especial(self.inimigo)
            else:
                print("Escolha inválida. Escolha novamente.")

            if self.inimigo.get_vida() > 0:
                self.inimigo.atacar(self.heroi)

        if self.heroi.get_vida() > 0:
            print("\nParabéns, você venceu a batalha!\n")
        else:
            print("\nVocê foi derrotado!\n")