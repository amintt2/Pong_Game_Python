import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the screen
screen = pygame.display.set_mode((1440, 920))
pygame.display.set_caption("Pong Game")

# Define colors
black = (0, 0, 0)
white = (255, 255, 255)
gray = (128, 128, 128)
green = (0, 255, 0)
gray_green = (128, 128, 0)

# Add this code after defining the colors
clock = pygame.time.Clock() # Create a clock object
FPS = 560 # Desired frame rate (560 FPS)

# Paddle positions and dimensions
player_paddle = pygame.Rect(80, 250, 11, 132)
opponent_paddle = pygame.Rect(1330, 250, 11, 132)

# Paddle movement
paddle_speed = 2

# Ball properties
ball = pygame.Rect(395, 295, 15, 15)
ball_speed = [1, 1]

# Game state
game_over = False
player_score = 0

# Create a file to save the best score if it doesn't exist
try:
best_score_file = open("best_score.txt", "r")
best_score_file.close()
except FileNotFoundError:
best_score_file = open("best_score.txt", "w")
best_score_file.write("0")
best_score_file.close()

# Game loop (modify your existing game loop)
while True:
for event in pygame.event.get():
if event.type == pygame.QUIT:
pygame.quit()
sys.exit()

if not game_over:
# Fill the background with black
screen.fill(black)

# Draw the paddles and ball
pygame.draw.rect(screen, white, player_paddle)
pygame.draw.rect(screen, white, opponent_paddle)
pygame.draw.ellipse(screen, white, ball)

# Move the paddles
keys = pygame.key.get_pressed()
if keys[pygame.K_z] and player_paddle.top > 0:
player_paddle.y -= paddle_speed
if keys[pygame.K_s] and player_paddle.bottom < 920:
player_paddle.y += paddle_speed
if keys[pygame.K_UP] and opponent_paddle.top > 0:
opponent_paddle.y -= paddle_speed
if keys[pygame.K_DOWN] and opponent_paddle.bottom < 920:
opponent_paddle.y += paddle_speed

# Move the ball
ball.x += ball_speed[0]
ball.y += ball_speed[1]

# Ball collisions with top and bottom
if ball.top <= 0 or ball.bottom >= 920:
ball_speed[1] = -ball_speed[1]

# Ball collisions with paddles and top and bottom of the paddles
if ball.colliderect(player_paddle) or ball.colliderect(opponent_paddle):
ball_speed[0] = -ball_speed[0]
player_score += 1
if ball.colliderect(player_paddle) and ball.top <= player_paddle.top:
ball_speed[1] = -ball_speed[1]
if ball.colliderect(player_paddle) and ball.bottom >= player_paddle.bottom:
ball_speed[1] = -ball_speed[1]
if ball.colliderect(opponent_paddle) and ball.top <= opponent_paddle.top:
ball_speed[1] = -ball_speed[1]
if ball.colliderect(opponent_paddle) and ball.bottom >= opponent_paddle.bottom:
ball_speed[1] = -ball_speed[1]


# Check if the ball exits the screen
if ball.left <= 0:
game_over = True
elif ball.right >= 1440:
game_over = True

# Display player score in gray_green and the player best score in gray
font = pygame.font.Font(None, 36)
score_text = font.render(f"Score: {
    player_score
}", True, gray_green)
screen.blit(score_text, (20, 20))
best_score_file = open("best_score.txt", "r")
best_score = int(best_score_file.read())
best_score_file.close()
best_score_text = font.render(f"Best Score: {
    best_score
}", True, gray)
screen.blit(best_score_text, (20, 50))

# Update the display
pygame.display.update()
else :
# Display "Game Over" message and restart button and score. Also, stop the quit button
# displaying the best score
font = pygame.font.Font(None, 72)
text = font.render("Game Over", True, white)
text_rect = text.get_rect(center = (720, 200))
restart_text = font.render("Press R to Restart", True, white)
restart_rect = restart_text.get_rect(center = (720, 300))
score_text = font.render(f"Score: {
    player_score
}", True, green)
quit_text = font.render("Press Q to Quit", True, white)
quit_rect = quit_text.get_rect(center = (720, 400))
best_score_file = open("best_score.txt", "r")
best_score = int(best_score_file.read())
best_score_file.close()
best_score_text = font.render(f"Best Score: {
    best_score
}", True, gray)
best_score_rect = best_score_text.get_rect(center = (1000, 800))
screen.blit(best_score_text, best_score_rect)
screen.blit(quit_text, quit_rect)
screen.blit(score_text, (600, 600))
screen.blit(text, text_rect)
screen.blit(restart_text, restart_rect)
pygame.display.update()

# Event handling for restart
keys = pygame.key.get_pressed()
if keys[pygame.K_r]:
# Reset the game state and score save the best score in a file
if player_score > best_score:
best_score = player_score
game_over = False
player_score = 0
ball = pygame.Rect(395, 295, 15, 15)
ball_speed = [1, 1]
best_score_file = open("best_score.txt", "w")
best_score_file.write(str(best_score))
best_score_file.close()
elif keys[pygame.K_q]:
# quit the game and save the best score in a file
if player_score > best_score:
best_score = player_score

best_score_file = open("best_score.txt", "w")
best_score_file.write(str(best_score))
best_score_file.close()
pygame.quit()
sys.exit()

clock.tick(FPS)