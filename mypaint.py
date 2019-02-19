import pygame
import time
pygame.init()

display_width = 800
display_height = 600

#  COLOURS 
white = (255, 255, 255)
black = (0, 0, 0)
red = (200, 0, 0)
green = (0, 200, 0)
blue = (0, 0, 200)
bright_red = (255, 0, 0)
bright_green = (0, 255, 0)
bright_blue = (0, 0, 255)

# FONT SIZES
largeText = pygame.font.Font("freesansbold.ttf", 100)
medText = pygame.font.Font("freesansbold.ttf", 50)
smallText = pygame.font.Font("freesansbold.ttf", 20)

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Let's see if we can paint eh")
clock = pygame.time.Clock()



def textObjects(text, font):
	textSurface = font.render(text, True, white)
	return textSurface, textSurface.get_rect()
	
def button(msg, x, y, w, h, ic, ac, action = None):
	
	mouse = pygame.mouse.get_pos()
	click = pygame.mouse.get_pressed()
	if x < mouse[0] < x+w and y < mouse[1] < y+h:
		pygame.draw.rect(gameDisplay, ac, (x, y, w, h))
		pygame.draw.rect(gameDisplay, ic, (x+5, y+5, w-10, h-10))
		if click[0] == 1 and action != None:
			pygame.display.update()
			action()
	
	else:
		pygame.draw.rect(gameDisplay, ic, (x, y, w, h))
		
	textSurf, textRect = textObjects(msg, smallText)
	textRect.center = ( (x+(w/2)), (y+(h/2)) )
	gameDisplay.blit(textSurf, textRect)
	
def drawLine():
#pygame.draw.line(gameDisplay, colour, (x1, y1), (x2, y2), thickness)
# start point when first clicked, end point with second click
#get pos when keydown, get pos when keyUP make line from those two pos

	line = True
	one = False
	two = False
	order = False
	clickOne = (0,0)
	clickTwo = (0,0)
	
	while line:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
				
			button("QUIT", 120, 10, 100, 30, red, bright_red, quit_paint)
			button("Erase All", 10, 550, 100, 30, red, bright_red, eraseAll)
			button("DRAW", 10, 10, 100, 30, green, bright_green, freeDraw)
			
			mouse = pygame.mouse.get_pos()
			#click = pygame.mouse.get_pressed()
		
			if event.type == pygame.MOUSEBUTTONDOWN and one == False:
				
				clickOne = (mouse[0], mouse[1])
				one = True
				order = True
					
			elif event.type == pygame.MOUSEBUTTONUP and order == True:
				clickTwo = (mouse[0],  mouse[1])
				two = True
			
			elif one and two:	
				pygame.draw.line(gameDisplay, white, clickOne, clickTwo, 5)
				pygame.display.update()
				one = False
				two = False
				order = False
				#line = False
			
				
			
				
			pygame.display.update()
			clock.tick(500)	

def freeDraw():
	#add more functionality to colour
	loop = True
	r = 250
	g = 250
	b = 250
	while loop:	
		
		for event in pygame.event.get():
			
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
				
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					if b < 250 and r == 250 and g == 250:
						r = 0
						g = 0
						b += 50
					elif g < 250 and r == 250:
						r = 0
						g += 50
					elif r < 250:
						r += 50

				print(event)
				
				if event.key == pygame.K_RIGHT:
					if b > 0 and g >= 0 and r >= 0:
						b -= 50
					elif g > 0 and b >= 0:
						b = 250
						g -= 50
					elif r > 0:
						b = 250
						g = 250
						r -= 50
			
					
			color = (r, g, b)	
			print(color)
			mouse = pygame.mouse.get_pos()
			click = pygame.mouse.get_pressed()

			if click[0] == 1:
				pygame.draw.rect(gameDisplay, color, (mouse[0], mouse[1], 3, 3))
			elif click[2] == 1:
				pygame.draw.rect(gameDisplay, black, (mouse[0]-25, mouse[1]-25, 50, 50))
			
			button("QUIT", 120, 10, 100, 30, red, bright_red, quit_paint)
			button("Erase All", 10, 550, 100, 30, red, bright_red, eraseAll)
			button("line", 240, 10, 100, 30, blue, bright_blue, drawLine)
			pygame.display.update()
			clock.tick(500)
		
		
def eraseAll():
	gameDisplay.fill(black)

def quit_paint():
	pygame.quit()
	quit()
	
def game_loop():
	
	game = True
	while game: 
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
	
		button("DRAW", 10, 10, 100, 30, green, bright_green, freeDraw)
		button("QUIT", 120, 10, 100, 30, red, bright_red, quit_paint)

		
		pygame.display.update()
		clock.tick(10)
	

game_loop()
pygame.quit()
quit()

#make rotating dots and create patterns

	
	
	
	
	