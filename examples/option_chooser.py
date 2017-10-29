import sys
sys.path.append("..")
import pygame
from PyGameWidgets import core
from PyGameWidgets import widgets

# Option chooser example.

WINDOW_WIDTH = 1024
WINDOW_HEIGHT = 728

pygame.init()
pygame.font.init
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()
FPS = 60
running = True

if __name__ == "__main__":	
	panel = widgets.Panel(core.Grid((3, 20), (WINDOW_WIDTH, WINDOW_HEIGHT)), None, None, (0, 0))
	panel.set_color((155, 155, 155, 255))
	opt = widgets.OptionChooser(panel, (0, 5), ["Blue", "Orange", "Black", "White", "Red"])
	opt.set_span((2, 3))
	opt.set_border(core.BLACK, 16)
	opt.text_color = core.RED
	opt.bold = True
	opt.italic = True
	opt.update_text()

	def redraw():
		pygame.display.flip()
		screen.fill((0, 0, 0))
		panel.draw(screen)
		opt.draw(screen)

while (running):
	clock.tick(FPS)
	redraw()
	for e in pygame.event.get():
		if e.type == pygame.QUIT:
			sys.exit()
		opt.activate(e)