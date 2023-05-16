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
       