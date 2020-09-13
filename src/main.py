from game.Game import Game

def main():
	try:
		game = Game()
		game.run()
	except RuntimeError:
		print('Une erreur est survenue')

if __name__ == '__main__':
	main()