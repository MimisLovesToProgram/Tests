import pygame

pygame.init()

red = (255, 0, 0)

display_surface = pygame.display.set_mode((0, 0), pygame.NOFRAME)

font = pygame.font.Font('freesansbold.ttf', 32)
bacon = font.render('Μπεικον. Απειρο μπεικον, αλλα καθολου παιχνιδια, H...', False, red)
games = font.render('Παιχνιδια. Απειρα παιχνιδια, αλλα καθολου παιχνιδια?', False, red)
baconPos = (0, 0)
gamesPos = (0, 200)

display_surface.blit(bacon, baconPos)
display_surface.blit(games, gamesPos)
pygame.display.update()
pygame.time.wait(5000)
pygame.quit()
