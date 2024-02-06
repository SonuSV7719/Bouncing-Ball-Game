import pygame
import sys

pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Bouncing Ball Game")

# colors
black = (0, 0, 0)
ball_color = (255, 0, 0)
red = (255, 0, 0)
white = (255, 255, 255)

# ball
ball_radius = 20
ball_speed = [6, 6]
ball_position = [width // 2, height // 2]

# Surface
sur_x1, sur_y1 = width // 2 - 70, height - 30
sur_x2, sur_y2 = width // 2 + 70, height - 30
sur_wid = 10
reachedBoundryLeft = False
reachedBoundryRight = False
leftButtonPressed = False
rightButtonPressed = False

# Restart Btn 
re_btn_x1, re_btn_y1 = width // 2 - 30, height // 2 + 50
re_btn_wid = 70
re_btn_height = 30

# txt
font = pygame.font.Font(None, 64)  
game_over_text = font.render("Game Over", True, white)
game_over_rect = game_over_text.get_rect(center=(width // 2, height // 2))

# Restart button
re_font = pygame.font.Font(None, 20) 
restart_button_text = re_font.render("Restart", True, white)
restart_button_rect = restart_button_text.get_rect(center=(width // 2 + 5, height // 2 + 65))

# score
highscore = 0
score = 0
sco_font = pygame.font.Font(None, 25) 
score_txt = sco_font.render(f"Score : {score}", True, white)
score_txt_rect = restart_button_text.get_rect(right=width - 100, top=10)
hi_score_txt = sco_font.render(f"Highscore : {score}", True, white)
hi_score_txt_rect = restart_button_text.get_rect(right=width - 100, top=35)

# game loop
clock = pygame.time.Clock()
is_running = True

# game over
game_over = False

game_start = False
hit = False

def reset_game():
    global ball_position, reachedBoundaryLeft, reachedBoundaryRight, game_over, game_start,ball_speed , sur_x1, sur_x2, sur_y1, score, sur_y2
    game_start = False
    ball_position = [width // 2, height // 2]
    reachedBoundaryLeft = False
    reachedBoundaryRight = False
    game_over = False
    sur_x1, sur_y1 = width // 2 - 70, height - 30
    sur_x2, sur_y2 = width // 2 + 70, height - 30
    ball_speed = [6, 6]
    score = 0


while is_running:
    score_txt = sco_font.render(f"Score : {score}", True, white)
    score_txt_rect = restart_button_text.get_rect(right=width - 100, top=10)
    hi_score_txt = sco_font.render(f"Highscore : {score}", True, white)
    hi_score_txt_rect = restart_button_text.get_rect(right=width - 100, top=35)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
        if event.type == pygame.KEYDOWN:
            game_start = True
            if event.key == pygame.K_LEFT and not reachedBoundryLeft:
                leftButtonPressed = True
                reachedBoundryRight = False
            if event.key == pygame.K_RIGHT and not reachedBoundryRight:
                rightButtonPressed = True
                reachedBoundryLeft = False

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                leftButtonPressed = False
            if event.key == pygame.K_RIGHT:
                rightButtonPressed = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if restart_button_rect.collidepoint(event.pos):
                reset_game()
                
    # Move surface
    if leftButtonPressed and not reachedBoundryLeft:
        sur_x1 -= 10
        sur_x2 -= 10
    if rightButtonPressed and not reachedBoundryRight:
        sur_x1 += 10
        sur_x2 += 10
          
    if game_start:
        ball_position[0] += ball_speed[0]
        ball_position[1] += ball_speed[1]

    # Bounce off the walls
    if ball_position[0] - ball_radius <= 0 or ball_position[0] + ball_radius >= width:
        ball_speed[0] = -ball_speed[0]
    if ball_position[1] - ball_radius <= 0 :
        ball_speed[1] = -ball_speed[1]
        
    if (abs(sur_y1 - ball_position[1]) <= 18) and (ball_position[0] >= sur_x1 - 19 and ball_position[0] <= sur_x2 + 19):
        ball_speed[1] = -ball_speed[1]
        score += 10
        highscore = max(score, highscore)
        
    if ball_position[1] + ball_radius >= height:
        game_over = True
        # print(game_over)

    # surface boundaries
    if sur_x1 <= 0:
        reachedBoundryLeft = True
    elif sur_x2 >= width:
        reachedBoundryRight = True
    else:
        reachedBoundryLeft = False
        reachedBoundryRight = False

    screen.fill(black)
    if not game_over:
        pygame.draw.circle(screen, ball_color, (int(ball_position[0]), int(ball_position[1])), ball_radius)
        pygame.draw.line(screen, red, (sur_x1, sur_y1), (sur_x2, sur_y2), sur_wid)
    else:
        screen.blit(game_over_text, game_over_rect)
        screen.blit(restart_button_text, restart_button_rect)
     
    screen.blit(score_txt, score_txt_rect)   
    screen.blit(hi_score_txt, hi_score_txt_rect)  
   
    pygame.display.flip()
    clock.tick(60)

# Quit Pygame
pygame.quit()
sys.exit()
