import pygame


class Princess(pygame.sprite.Sprite):
  def __init__(self, name, x, y, img_file):
      pygame.sprite.Sprite.__init__(self)
      self.image=pygame.image.load(img_file).convert_alpha()
  
      self.rect = self.image.get_rect()
      self.rect.x = x
      self.rect.y = y
      self.name = name
'''
def background():
  grass = pygame.image.load("resources/images/grass.png")
  width, height = 640, 480
  screen=pygame.display.set_mode((width, height))
  
  for x in range(width/grass.get_width()+1):
    for y in range(height/grass.get_height()+1):
      screen.blit(grass,(x*100,y*100))
'''
