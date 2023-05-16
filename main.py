from ast import Pass, main
from cgitb import text
from cmath import rect
from turtle import left, right
from webbrowser import get
import pygame
import os
pygame.init()
pygame.font.init() 

FPS = 60
background_colour = (0,0,0)
(width, height) = (1100, 800)
Black = ()
clock = pygame.time.Clock()

Ball_vel = 3

VEL = 5

black = (0,0,0)
White = (255, 255, 255)

left_score = 0
right_score =0

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Pong')
screen.fill(background_colour)

class Game_state():
    def __init__(self):
        self.state = 'intro'
        self.winner = ''
    
    def intro(self):
        
        running = True
        while running:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.state = 'main_game'
                    running = False
                if event.type == pygame.QUIT:
                    running = False
                
            keys_pressed = pygame.key.get_pressed()
        
            screen.fill(black)
            font = pygame.font.Font('freesansbold.ttf', 48)
            text = font.render("Press anywhere to Start....", True, (255, 255, 255))

            textRect = text.get_rect()
            #textRect.center = (textRect.width // 2, textRect.width // 2)
            screen.blit(text, (  (width/2) - (textRect.width/2) , (height/2) - (textRect.height/2)))
                
            pygame.display.update()

    def main_game(self):
        left_score = 0
        right_score = 0
        
        
        left_score_screen = scores(20, 20)
        right_score_screen = scores(20, 20)
        
        Ball = ball(540, 390, 20)
        paddle_1 = pygame.Rect([20, 350, 20, 100])
        paddle_2 = pygame.Rect([1060, 350, 20, 100])
        line_in_center = pygame.Rect([(width//2 - 5), 0, 10, height])

        running = True
        while running:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            keys_pressed = pygame.key.get_pressed()
            
            screen.fill(black)

            if left_score != 5:
                if right_score != 5:
                    paddle_1_movement(keys_pressed, paddle_1)
                    paddle_2_movement(keys_pressed, paddle_2)
                    handle_collison(Ball, paddle_1, paddle_2)
                    Ball.move()
                    draw_stuff(Ball, paddle_1, paddle_2, line_in_center, left_score, right_score)
                    check_boundry = Ball.check_boundrys(left_score, right_score)
                    screen.fill(black)
                    if check_boundry ==  "left_score += 1":
                        left_score += 1
                    elif check_boundry == "right_score += 1":
                        right_score += 1
            
            if left_score == 5:
                self.state = 'end_screen'
                running = False
                self.winner = 'Left'
            if right_score == 5:
                self.state = 'end_screen'
                running = False
                self.winner = 'Right'

                
    def end_screen(self):
       
        running = True
       
        while running:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    
                    
                    self.state = 'main_game'
                    running = False
                    main()
                    print('mouse pressed')
                    print(self.state)
                if event.type == pygame.QUIT:
                    running = False
           
            #keys_pressed = pygame.key.get_pressed()
            #if keys_pressed[pygame.K_w] :
             #   self.state = 'main_game'
              #  main()
        
            screen.fill(black)
            font = pygame.font.Font('freesansbold.ttf', 48)
            winner = font.render(self.winner + " Wins!!!!!", True, (255, 255, 255))
            text = font.render("Click anywhere to play again!!!", True, (255, 255, 255))
            textRect = text.get_rect()
            textRect.center = (textRect.width // 2, textRect.width // 2)
            winnerRect = winner.get_rect()
            winnerRect.center = (textRect.width // 2, textRect.width // 2)
            screen.blit(winner, (  (width/2) - (winnerRect.width/2) , 200))
            screen.blit(text, (  (width/2) - (textRect.width/2) , (height/2) - (textRect.height/2)))
            
             
            pygame.display.update()
            
               
    def state_mananger(self):
        if self.state == 'intro':
            self.intro()
        if self.state == 'main_game':
            self.main_game()
        if self.state == 'end_screen':
            self.end_screen()
       
            
class scores():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def create(self, score):
        font = pygame.font.Font('freesansbold.ttf', 48)
        score_printed = font.render(str(score), True, (255, 255, 255))
        textRect = score_printed.get_rect()
        #textRect.center = (X // 2, Y // 2)
        screen.blit(score_printed, (self.x, self.y))
        
        #img = font.render(sysfont, True, White)
        #rect = img.get_rect()
        #pygame.draw.rect(img, White, rect, 1)


#Ball
class ball():
    MAX_VEL = 5
    global left_score
    global right_score
    def __init__(self, x, y, width ):
        self.x = self.x_origional = x
        self.y = self.y_origional = y
        #its a square so height = weight
        self.width = width
        self.height = width
        self.x_vel = self.MAX_VEL
        self.y_vel = 0
        self.colour = White
    
    
    def draw(self, screen):
        rect = pygame.Rect([self.x, self.y, self.width, self.height])
        pygame.draw.rect(screen, self.colour, rect) 

    def move(self):
        self.x -= self.x_vel
        self.y -= self.y_vel

    def reset(self):
        self.x = self.x_origional
        self.y = self.y_origional 
    
    def check_boundrys(self, left_score, right_score):
       # left_score_screen = scores(20, 20)
       # right_score_screen = scores(20, 200)
        #left_score_screen.create(left_score)
        #right_score_screen.create(right_score)
        #pygame.display.update()
        if self.x + (self.width//2)>= width:
            left_score += 1
            play_powerup()
            pygame.time.delay(1000)
            self.reset()
            return("left_score += 1")
         #   pygame.display.update()
            
        elif self.x - (self.width//2) <= 0:
            right_score += 1
            play_powerup()
            pygame.time.delay(1000)
            self.reset()
            return("right_score += 1")
          #  pygame.display.update()
            
#Paddles
def paddle_1_movement(keys_pressed, paddle_1):
    if keys_pressed[pygame.K_w] and paddle_1.y - VEL > 0 :
        paddle_1.y -= VEL
    if keys_pressed[pygame.K_s] and paddle_1.y + VEL < (height - 100):
        paddle_1.y += VEL

def paddle_2_movement(keys_pressed, paddle_2):
    if keys_pressed[pygame.K_UP] and paddle_2.y - VEL > 0 :
        paddle_2.y -= VEL
    if keys_pressed[pygame.K_DOWN] and paddle_2.y + VEL < (height - 100):
        paddle_2.y += VEL

def draw_stuff(Ball, paddle_1, paddle_2, line, left_score, right_score):
    pygame.draw.rect(screen, White, paddle_1)
    pygame.draw.rect(screen, White, paddle_2)
    Ball.draw(screen)
    pygame.draw.rect(screen, White, line)
    left_score_screen = scores(20, 20)
    right_score_screen = scores(1060, 20)
    left_score_screen.create(left_score)
    right_score_screen.create(right_score)
   # my_font = pygame.font.SysFont('Comic Sans MS', 30)
  ##  text_surface = my_font.render('Some Text', False, (255, 255, 255))
   # screen.blit(text_surface, (0,0))

    
    pygame.display.update()

def play_crash():
    crash_sound = pygame.mixer.Sound('Hit_Hurt.wav')
    pygame.mixer.Sound.play(crash_sound)
    pygame.mixer.music.stop()
def play_powerup():
    powerup = pygame.mixer.Sound('Powerup.wav')
    pygame.mixer.Sound.play(powerup)
    pygame.mixer.music.stop()
def play_bounce():
    bounce = pygame.mixer.Sound('bounce.wav')
    pygame.mixer.Sound.play(bounce)
    pygame.mixer.music.stop()
#Collision
def handle_collison(ball, paddle_1, paddle_2):
    if ball.y + (ball.height//2)>= height:
        ball.y_vel *= -1
        play_bounce()
        

    if ball.y - (ball.height//2) <= 0:
        ball.y_vel *= -1
        play_bounce()

    #if ball.x_vel < 0:
    if ball.y >= paddle_1.y and ball.y <= paddle_1.y + paddle_1.height:
        if ball.x - (ball.width//2) <= paddle_1.x + (paddle_1.width//2):
            ball.x_vel *= -1

            middle_y = paddle_1.y + paddle_1.height / 2
            diffrence_in_y = middle_y - ball.y
            reduction_factor = (paddle_1.height/2) / ball.MAX_VEL
            y_vel = diffrence_in_y / reduction_factor
            ball.y_vel = -1 * y_vel
            play_crash()

    if ball.y >= paddle_2.y and ball.y <= paddle_2.y + paddle_2.height:
        if ball.x + (ball.height//2) >= paddle_2.x + (paddle_2.width//2):
            ball.x_vel *= -1

            middle_y = paddle_2.y + paddle_2.height / 2
            diffrence_in_y = middle_y - ball.y
            reduction_factor = (paddle_2.height/2) / ball.MAX_VEL
            y_vel = diffrence_in_y / reduction_factor
            ball.y_vel = -1 * y_vel
            play_crash()

def print_winner(winner):
    screen.fill(black)
    font = pygame.font.Font('freesansbold.ttf', 48)
    if winner == 'left_score':
        winner_printed = font.render("Left wins!!!!",True, (255, 255, 255))
    elif winner == 'right_score':
        winner_printed = font.render("Right wins!!!!", True, (255, 255, 255))

    textRect = winner_printed.get_rect()
    #textRect.center = (textRect.width // 2, textRect.width // 2)
    screen.blit(winner_printed, ((height//2) + 50, (width//2) - (textRect.width // 2)))
    
    pygame.draw.rect(screen, White ,(550,600,100,50))
    
    pygame.display.update()
       


Game_state = Game_state()
def main():
    
    Game_state.state_mananger()
            
     
        
if __name__ == "__main__":
    main()