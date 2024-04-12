import pygame

pygame.init()

screen = pygame.display.set_mode((500,600))

GREY = (150, 150, 150)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

running = True

font = pygame.font.SysFont('sans',50)
text_1 = font.render('+',True,BLACK)
text_2 = font.render('-',True,BLACK)
text_3 = font.render('+',True,BLACK)
text_4 = font.render('-',True,BLACK)
text_5 = font.render('Start',True,BLACK)
text_6 = font.render('Reset',True,BLACK)

while running:
	screen.fill(GREY)

	mouse_x, mouse_y = pygame.mouse.get_pos()

	pygame.draw.rect(screen, BLACK, (50,50,55,55))
	pygame.draw.rect(screen, BLACK, (150,50,55,55))
	pygame.draw.rect(screen, BLACK, (150,150,55,55))
	pygame.draw.rect(screen, BLACK, (50,150,55,55))
	pygame.draw.rect(screen, BLACK, (300,50,155,55))
	pygame.draw.rect(screen, BLACK, (300,150,155,55))
	pygame.draw.rect(screen, BLACK, (50,530,405,55))

	pygame.draw.rect(screen, WHITE, (50,50,50,50))
	pygame.draw.rect(screen, WHITE, (150,50,50,50))
	pygame.draw.rect(screen, WHITE, (150,150,50,50))
	pygame.draw.rect(screen, WHITE, (50,150,50,50))
	pygame.draw.rect(screen, WHITE, (300,50,150,50))
	pygame.draw.rect(screen, WHITE, (300,150,150,50))
	pygame.draw.rect(screen, WHITE, (50,530,400,50))

	screen.blit(text_1, (65,45))
	screen.blit(text_3, (165,45))
	screen.blit(text_2, (70,145))
	screen.blit(text_4, (170,145))
	screen.blit(text_5, (330,45))
	screen.blit(text_6, (320,145))

	pygame.draw.circle(screen, BLACK, (250,400), 100)
	pygame.draw.circle(screen, WHITE, (250,400), 95)

	pygame.draw.line(screen, BLACK, (250,400),(250,310))
	pygame.draw.line(screen, BLACK, (250,400),(250,370))
	

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.MOUSEBUTTONDOWN:
			if event.button == 1:	
				print("XXX")
	pygame.display.flip()

pygame.quit()