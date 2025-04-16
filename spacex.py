import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space War")

# Colors
BLACK = (0, 0, 0)

# Clock
clock = pygame.time.Clock()

# Load assets
player_ship = pygame.image.load("player.png")
player_ship = pygame.transform.scale(player_ship, (50, 40))  # Apply dimensions here
enemy_ship = pygame.image.load("enemy1.png")
enemy_ship = pygame.transform.scale(enemy_ship, (50, 50))
bullet_image = pygame.image.load("bullet.png")
bullet_image = pygame.transform.scale(bullet_image, (10, 20))
 

# Player
player = player_ship.get_rect(center=(WIDTH // 2, HEIGHT - 60))
player_speed = 10

# Bullets
bullets = []
bullet_speed = -7
# Enemies
enemies = []
enemy_speed = 3
spawn_enemy_event = pygame.USEREVENT + 1
pygame.time.set_timer(spawn_enemy_event, 1000)

# Game loop
running = True
while running:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == spawn_enemy_event:
            enemy = enemy_ship.get_rect(topleft=(random.randint(0, WIDTH - enemy_ship.get_width()), 0))
            enemies.append(enemy)

    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.left > 0:
        player.x -= player_speed
    if keys[pygame.K_RIGHT] and player.right < WIDTH:
        player.x += player_speed
    if keys[pygame.K_SPACE]:
        bullets.append(bullet_image.get_rect(midbottom=player.midtop))

    # Update bullets
    for bullet in list(bullets):
        bullet.y += bullet_speed
        if bullet.bottom < 0:
            bullets.remove(bullet)

    # Update enemies
    for enemy in list(enemies):
        enemy.y += enemy_speed
        if enemy.bottom > HEIGHT:
            enemies.remove(enemy)
        for bullet in list(bullets):
            if enemy.colliderect(bullet):
                enemies.remove(enemy)
                bullets.remove(bullet) 

    # Draw player
    screen.blit(player_ship, player)

    # Draw bullets
    for bullet in bullets:
        screen.blit(bullet_image, bullet)

    # Draw enemies
    for enemy in enemies:
        screen.blit(enemy_ship, enemy)

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
sys.exit()