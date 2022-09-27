# Hangman Game (Jogo da Forca) 
# Programação Orientada a Objetos

# Import
import random

# Board (tabuleiro)
board = ['''

>>>>>>>>>>Hangman<<<<<<<<<<

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
		print("@iniciado com sucesso@")
		
		
	# Método para adivinhar a letra
	def guess(self, letter):
		self.letter=letter
		if (self.letter) in self.word:
			ind=self.word.index(self.letter)
			self.letras_certas.append(self.letter + " ")
			self.palavraSecreta[ind]=self.letter
		else:
			self.tentativas+=1
			self.letras_erradas.append((self.letter + " "))
			
		
		
	# Método para verificar se o jogo terminou
	def hangman_over(self):
		if self.tentativas>=6:
			acabou_jogo=False
			return acabou_jogo
		elif (self.palavraSecreta==self.word):
			acabou_jogo=False
			return acabou_jogo
		
	# Método para verificar se o jogador venceu
	def hangman_won(self):
		return True if (self.palavraSecreta==self.word) else False
	

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
		print("\n Letras corretas: ", self.letras_certas)
		print("\n Palavras erradas:  ", self.letras_erradas)
		


		

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
		game.guess(letra_in)


	# Verifica o status do jogo
	game.print_game_status()	

	# De acordo com o status, imprime mensagem na tela para o usuário
	if game.hangman_won():
		print ('\nParabéns! Você venceu!!')

	else:
	 	print("\nGame over! Você perdeu.")
		#print("A palavra era " + game.word)
	
		
	print ('\nFoi bom jogar com você! Agora vá estudar!\n')

# Executa o programa		
if __name__ == "__main__":
	main()

