import pygame
import random

screen_size = [360, 600]
screen = pygame.display.set_mode(screen_size)
pygame.font.init()

score = 0

def random_offset():
  return -1*random.randint(100, 1500)

def update_chicken_pos(idx):
  global score
  if chicken_y[idx]> 600:
    chicken_y[idx] = random_offset()
    score = score + 50
    print ('score', score)
  else:
    chicken_y[idx] = chicken_y[idx] + 5


def crashed(idx):
  global score
  global keep_alive
  score = score - 50
  chicken_y[idx] = random_offset()
  if score < - 200:
    keep_alive = False


def display_score(score):
  font = pygame.font.SysFont('Uniblock',50)
  score_text = 'Score: ' + str(score)
  text_img = font.render(score_text, True, (0, 255, 0)) 
  screen.blit(text_img, [20,10])



background = pygame.image.load('background.png')
user = pygame.image.load('user.png')
chicken = pygame.image.load('chicken.png')
chicken_y = [random_offset(), random_offset(), random_offset()]
user_x = 150


keep_alive = True
clock = pygame.time.Clock()



while keep_alive:
  pygame.event.get()
  keys = pygame.key.get_pressed()
  if keys[pygame.K_RIGHT] and user_x < 300:
    user_x = user_x + 5
  elif keys[pygame.K_LEFT] and user_x > 0:
    user_x = user_x - 5
    
  update_chicken_pos(0)
  update_chicken_pos(1)
  update_chicken_pos(2)
  
  screen.blit(background, [0, 0])
  screen.blit(user, [user_x, 520])
  screen.blit(chicken, [0, chicken_y[0]])
  screen.blit(chicken, [140, chicken_y[1]])
  screen.blit(chicken, [280, chicken_y[2]])

  if chicken_y[0] > 500 and user_x <70:
    crashed(0)


  if chicken_y[1] > 500 and user_x > 100 and user_x <200:
    crashed(1)  

  if chicken_y[2] > 500 and user_x >220:
    crashed(2)  


  display_score(score)



  pygame.display.update()
  clock.tick(100)


