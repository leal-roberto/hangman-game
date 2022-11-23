# Hangman Game (Jogo da Forca) 
# Programação Orientada a Objetos

# Import
import random
import os

# Board (tabuleiro)
board = ['''

>>>>>>>>>>FORCA<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']


# Classe
class Hangman:
	
	# Método Construtor
	def __init__(self, word):
		self.word = word
		self.palavraSecreta=[]
		self.tentativas=0
		self.letras_certas=[]
		self.letras_erradas=[]
		self.palavraResposta=[]
		print("..:: BEM VINDO AO JOGO DA FORCA ::..\n")
		
		
	# Método para adivinhar a letra
	def guess(self, letter):
		self.letter=letter.lower()
		


		if (self.letter) in self.word:
			self.letras_certas.append(self.letter)
			for y in range(len(self.word)):
				if (self.letter==self.word[y]):
					self.palavraSecreta[y]=self.letter					
			
		else:
			self.letras_erradas.append((self.letter))
			if self.tentativas <6:
				self.tentativas+=1
			else:
				self.tentativas=6
		
		self.palavraResposta=("".join(self.palavraSecreta))
		
			
		
		
	# Método para verificar se o jogo terminou
	def hangman_over(self):
		if self.tentativas>=6:
			acabou_jogo=False
			return acabou_jogo
		elif (self.palavraResposta==self.word):
			acabou_jogo=False
			return acabou_jogo
		else:
			return True
		
	# Método para verificar se o jogador venceu
	def hangman_won(self):
		return True if (self.palavraResposta==self.word) else False
	


	# Método para não mostrar a letra no board
	def hide_word(self):
		palavra_temp=[]
		for y in self.word:
			palavra_temp.append(" _ ")

		#palavraSecreta= ' '.join(palavraSecreta)
		self.palavraSecreta=palavra_temp
		return self.palavraSecreta
		
	# Método para checar o status do game e imprimir o board na tela
	def print_game_status(self):
		print(board[self.tentativas])
		print("\n " + ' '.join(self.palavraSecreta))
		print("\n Letras corretas: ", " ".join(self.letras_certas))
		print("\n Palavras erradas:  ", " ".join(self.letras_erradas))
			


		

# Função para ler uma palavra de forma aleatória do banco de palavras
def rand_word():
        with open("palavras.txt", "rt") as f:
                bank = f.readlines()
        return bank[random.randint(0,len(bank))].strip()


# Função Main - Execução do Programa
def main():
	

	# Objeto
	game = Hangman(rand_word())
	game.hide_word()
		
	
	# Enquanto o jogo não tiver terminado, print do status, solicita uma letra e faz a leitura do caracter
	acabou_jogo=True
	while acabou_jogo:
		game.print_game_status()

		letra_in = input("\n Escolha uma letra:  ")
		if (letra_in in game.letras_certas or letra_in in game.letras_erradas):

			print(" Erro: Letra ja escolhida")
			input ("Pressione qualquer tecla para continuar...")
			
		else:
			game.guess(letra_in)
			acabou_jogo= game.hangman_over()
		
		os.system('cls' if os.name== 'nt' else 'clear')


	# Verifica o status do jogo
	game.print_game_status()	

	# De acordo com o status, imprime mensagem na tela para o usuário
	if game.hangman_won():
		print ('\nParabéns! Você venceu!!')

	else:
	 	print("\nGame over! Você perdeu.\n A palavra era:  " + game.word)	
		
	print ('\nFoi bom jogar com você! Agora vá estudar!\n')

# Executa o programa
if __name__ == "__main__":
	main()

