import pygame
import random

# Initialize pygame
pygame.init()

# Set up the display for full screen
infoObject = pygame.display.Info()
SCREEN_WIDTH = infoObject.current_w
SCREEN_HEIGHT = infoObject.current_h
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN)
pygame.display.set_caption("Shoot the Star Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (225, 225, 0)

# Clock to control the frame rate
clock = pygame.time.Clock()
FPS = 60

# Load retro font
retro_font = pygame.font.Font("retro.ttf", 36)  # Ensure "retro.ttf" is in the same directory as this script

# Load shooting sound
start_sound = pygame.mixer.Sound("Game_start.mp3")  
shoot_sound = pygame.mixer.Sound("Pop_sound.mp3")  
over_sound = pygame.mixer.Sound("Game_over.mp3")  
win_sound = pygame.mixer.Sound("Game_win.mp3")
clap_sound = pygame.mixer.Sound("Game_clap.mp3")   

# Load images
background_image = pygame.image.load("background.png").convert()  # Ensure "background.png" is in the same directory
player_image = pygame.image.load("player.png").convert_alpha()  # Ensure "player.png" is in the same directory
star_image = pygame.image.load("star.png").convert_alpha()  # Ensure "star.png" is in the same directory

# Scale images if necessary
background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
player_image = pygame.transform.scale(player_image, (150, 150))  # Adjust the size to fit your requirements
star_image = pygame.transform.scale(star_image, (70, 70))  # Adjust the size to fit your requirements

# Player class
class Player:
    def __init__(self):
        self.image = player_image
        self.rect = self.image.get_rect()
        self.rect.center = [SCREEN_WIDTH // 2, SCREEN_HEIGHT - 60]
        self.speed = 5

    def move_left(self):
        if self.rect.left > 0:
            self.rect.x -= self.speed

    def move_right(self):
        if self.rect.right < SCREEN_WIDTH:
            self.rect.x += self.speed

    def draw(self, surface):
        surface.blit(self.image, self.rect)

player = Player()

# Star class
class Star:
    def __init__(self):
        self.image = star_image
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, SCREEN_WIDTH - self.rect.width)
        self.rect.y = random.randint(-100, -50)
        self.speed = random.randint(1, 5)

    def move(self):
        self.rect.y += self.speed
        if self.rect.y > SCREEN_HEIGHT:
            self.rect.x = random.randint(0, SCREEN_WIDTH - self.rect.width)
            self.rect.y = random.randint(-100, -50)
            self.speed = random.randint(1, 5)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

# projectite class
class Projectile:
    def __init__(self, x, y):
        self.image = pygame.Surface((5, 10))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = 10

    def move(self):
        self.rect.y -= self.speed

    def draw(self, surface):
        surface.blit(self.image, self.rect)

# Create initial star list
stars = []

# List to store projectiles
projectiles = []

# shot counter
shots_hit = 0

# Function to create new star
def create_star():
    star = Star()
    stars.append(star)

# Function to display the start screen
def show_start_screen():
    start_sound.play()
    screen.blit(background_image, (0, 0))
    title_text = retro_font.render("Shoot the Star Game", True, YELLOW)
    instruction_text1 = retro_font.render("Use arrow keys to move", True, WHITE)
    instruction_text2 = retro_font.render("Press SPACE to shoot", True, WHITE)
    instruction_text3 = retro_font.render("Shoot 20 or more stars to win", True, WHITE)
    start_text = retro_font.render("Press ENTER to start or CMD + Q to Quit", True, GREEN)

    # Calculate positions with spacing
    title_pos = (SCREEN_WIDTH // 2 - title_text.get_width() // 2, SCREEN_HEIGHT // 4)
    instruction_pos1 = (SCREEN_WIDTH // 2 - instruction_text1.get_width() // 2, title_pos[1] + title_text.get_height() + 70)
    instruction_pos2 = (SCREEN_WIDTH // 2 - instruction_text2.get_width() // 2, instruction_pos1[1] + instruction_text1.get_height() + 10)
    instruction_pos3 = (SCREEN_WIDTH // 2 - instruction_text3.get_width() // 2, instruction_pos2[1] + instruction_text2.get_height() + 10)
    start_pos = (SCREEN_WIDTH // 2 - start_text.get_width() // 2, instruction_pos3[1] + instruction_text3.get_height() + 70)

    # Blit the text
    screen.blit(title_text, title_pos)
    screen.blit(instruction_text1, instruction_pos1)
    screen.blit(instruction_text2, instruction_pos2)
    screen.blit(instruction_text3, instruction_pos3)
    screen.blit(start_text, start_pos)
    pygame.display.flip()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()    
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    waiting = False
                   
# Function to display the pause screen
def show_pause_screen():
    pause_text = retro_font.render("Game Paused", True, WHITE)
    resume_text = retro_font.render("Press P to resume", True, WHITE)

    pause_pos = (SCREEN_WIDTH // 2 - pause_text.get_width() // 2, SCREEN_HEIGHT // 2 - pause_text.get_height() // 2)
    resume_pos = (SCREEN_WIDTH // 2 - resume_text.get_width() // 2, pause_pos[1] + pause_text.get_height() + 20)

    screen.blit(pause_text, pause_pos)
    screen.blit(resume_text, resume_pos)
    pygame.display.flip()

    paused = True
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    paused = False

# Main game loop
def main():
    global shots_hit
    start_time = pygame.time.get_ticks()
    game_duration = 30 * 1000  # 30 seconds in milliseconds
    game_over = False
    end_time = None
    running = True
    over_sound.stop()
    win_sound.stop()
    clap_sound.stop()
   
    while running:
        elapsed_time = pygame.time.get_ticks() - start_time
        remaining_time = max(0, (game_duration - elapsed_time) // 1000)  # Convert milliseconds to seconds

        # check if game over or not 
        if not game_over:
            if remaining_time == 0:
                game_over = True
                end_time = pygame.time.get_ticks()
            elif random.randint(0, 50) == 0:  # Random chance to create a new star
                create_star()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not game_over:
                    projectiles.append(Projectile(player.rect.centerx, player.rect.top))
                elif event.key == pygame.K_p:
                    show_pause_screen() #pause and resume game 

        # Player movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player.move_left()
        if keys[pygame.K_RIGHT]:
            player.move_right()
     
        # Move projectiles
        for projectile in projectiles:
            projectile.move()
            if projectile.rect.y < 0:
                projectiles.remove(projectile)

        # Move star
        for star in stars:
            star.move()
            # Check for collision with projectiles 
            for projectile in projectiles:
                if star.rect.colliderect(projectile.rect):
                    stars.remove(star)
                    projectiles.remove(projectile)
                    shots_hit += 1
                    shoot_sound.play()
                    break

            # Check for collision with player
            if star.rect.colliderect(player.rect):
                game_over = True
                end_time = pygame.time.get_ticks()

        # Draw everything
        screen.blit(background_image, (0, 0))
        player.draw(screen)
        for star in stars:
            star.draw(screen)
        for projectile in projectiles:
            projectile.draw(screen)

        # Display remaining time, shots fired, and shots hit
        timer_text = retro_font.render(f"Time: {remaining_time}", True, WHITE)
        shots_hit_text = retro_font.render(f"Point: {shots_hit}", True, WHITE) # Shoot hit = point 

        screen.blit(timer_text, (10, 10))
        screen.blit(shots_hit_text, (10, 90))

        pygame.display.flip()
        clock.tick(FPS)

        #game over screen 

        if game_over:
            total_elapsed_time = (end_time - start_time) // 1000  # Calculate total elapsed time in seconds

            game_over_text = retro_font.render("Times Up! Game Over...", True, RED)
            
            # Display game over message
            screen.blit(background_image, (0, 0))
            if shots_hit >= 20:
                game_result_text = retro_font.render("You are the Winner!", True, YELLOW)
                win_sound.play()
            elif shots_hit >= 15:
                game_result_text = retro_font.render("You are Good, but try again to become a winner", True, YELLOW)
                clap_sound.play()
            else:
                game_result_text = retro_font.render("You Lose... Try again....", True, RED)
                over_sound.play()
            final_shots_text = retro_font.render(f"Total Point: {shots_hit}", True, WHITE)
            total_time_text = retro_font.render(f"Total Time: {total_elapsed_time}s / 30s ", True, WHITE)
            restart_text = retro_font.render("Press R to restart or Q to quit", True, GREEN)
            
            # <---- podition game over text 
            game_over_pos = (SCREEN_WIDTH // 2 - game_over_text.get_width() // 2, SCREEN_HEIGHT // 4)
            game_result_pos = (SCREEN_WIDTH // 2 - game_result_text.get_width() // 2, game_over_pos[1] + game_over_text.get_height() + 70)
            final_shots_pos = (SCREEN_WIDTH // 2 - final_shots_text.get_width() // 2, game_result_pos[1] + game_result_text.get_height() + 10)
            total_time_pos = (SCREEN_WIDTH // 2 - total_time_text.get_width() // 2, final_shots_pos[1] + final_shots_text.get_height() + 10)
            restart_pos = (SCREEN_WIDTH // 2 - restart_text.get_width() // 2, total_time_pos[1] + total_time_text.get_height() + 70)

            # Blit the text
            screen.blit(game_over_text, game_over_pos)
            screen.blit(game_result_text, game_result_pos)
            screen.blit(final_shots_text, final_shots_pos)
            screen.blit(total_time_text, total_time_pos)
            screen.blit(restart_text, restart_pos)
            pygame.display.flip()

            waiting = True
            while waiting:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_r:
                            shots_hit = 0
                            stars.clear()
                            projectiles.clear()
                            main()
                        elif event.key == pygame.K_q:
                            pygame.quit()
                            exit()


if __name__ == "__main__":
    show_start_screen()
    main()
    pygame.quit()
