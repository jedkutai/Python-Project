import pygame
import math
import random
from pygame import mixer

def play_haters(z):
    pygame.init()


    screen = pygame.display.set_mode((800, 600))

    # Background
    background = pygame.image.load("\\\\wsl.localhost\\Ubuntu\\home\\jedkutai\\code\\projects\\haters modes\\stars background.jpg")

    # Background sound
    music_list = ["\\\\wsl.localhost\\Ubuntu\\home\\jedkutai\\code\\projects\\haters modes\\Default\\soundtrack.wav", 
    "\\\\wsl.localhost\\Ubuntu\\home\\jedkutai\\code\\projects\\haters modes\\Nicki vs Remy\\soundtrack.mp3",
    "\\\\wsl.localhost\\Ubuntu\\home\\jedkutai\\code\\projects\\haters modes\\Drake vs Meek\\soundtrack.mp3"
    ]
    mixer.music.load(music_list[z])
    mixer.music.play(-1)

    # Title & Icon
    title_list = ["Space Invaders",
    "Remy Ma vs Nicki Minaj",
    "Drake vs Meek Mill"
    ]
    pygame.display.set_caption(title_list[z])
    icon_list = ["\\\\wsl.localhost\\Ubuntu\\home\\jedkutai\\code\\projects\\haters modes\\Default\\bullet.png", 
    "\\\\wsl.localhost\\Ubuntu\\home\\jedkutai\\code\\projects\\haters modes\\Nicki vs Remy\\bullet.png",
    "\\\\wsl.localhost\\Ubuntu\\home\\jedkutai\\code\\projects\\haters modes\\Drake vs Meek\\bullet.png"
    ]
    icon = pygame.image.load(icon_list[z])
    pygame.display.set_icon(icon)

    # Player Image
    player_list = ["\\\\wsl.localhost\\Ubuntu\\home\\jedkutai\\code\\projects\\haters modes\\Default\\pro.png",
    "\\\\wsl.localhost\\Ubuntu\\home\\jedkutai\\code\\projects\\haters modes\\Nicki vs Remy\\pro.png",
    "\\\\wsl.localhost\\Ubuntu\\home\\jedkutai\\code\\projects\\haters modes\\Drake vs Meek\\pro.png"
    ]
    playerImg = pygame.image.load(player_list[z])
    playerX = 368
    playerY = 480
    playerX_change = 0


    # Enemy Image
    enemyImg = []
    enemyX = []
    enemyY = []
    enemyX_change = []
    enemyY_change = []
    num_of_enemies = 6
    enemy_list = ["\\\\wsl.localhost\\Ubuntu\\home\\jedkutai\\code\\projects\\haters modes\\Default\\enemy.png",
    "\\\\wsl.localhost\\Ubuntu\\home\\jedkutai\\code\\projects\\haters modes\\Nicki vs Remy\\enemy.png",
    "\\\\wsl.localhost\\Ubuntu\\home\\jedkutai\\code\\projects\\haters modes\\Drake vs Meek\\enemy.png"
    ]

    for i in range(num_of_enemies):
        enemyImg.append(pygame.image.load(enemy_list[z]))
        enemyX.append(random.randint(0, 736))
        enemyY.append(random.randint(50,150))
        enemyX_change.append(.5)
        enemyY_change.append(40)

    # bullet
    bullet_list = ["\\\\wsl.localhost\\Ubuntu\\home\\jedkutai\\code\\projects\\haters modes\\Default\\bullet.png",
    "\\\\wsl.localhost\\Ubuntu\\home\\jedkutai\\code\\projects\\haters modes\\Nicki vs Remy\\bullet.png",
    "\\\\wsl.localhost\\Ubuntu\\home\\jedkutai\\code\\projects\\haters modes\\Drake vs Meek\\bullet.png"
    ]
    bulletImg = pygame.image.load(bullet_list[z])
    bulletX = 0
    bulletY = 480
    bulletY_change = 1.3
    global bullet_state
    bullet_state = "ready"

    # Font
    score_value = 0
    font = pygame.font.Font("freesansbold.ttf",32)

    textX = 10
    textY = 10

    # Game Over Text
    over_font = pygame.font.Font("freesansbold.ttf",64)

    def show_score(x,y):
        score = font.render("Score: " + str(score_value), True, (255,255,255))
        screen.blit(score, (x, y))

    def game_over_text():
        over_text = over_font.render("GAME OVER", True, (255,255,255))
        screen.blit(over_text, (200, 275))

    def player(x, y):
        screen.blit(playerImg, (x, y))

    def enemy(x, y, i):
        screen.blit(enemyImg[i], (x, y))

    def fire_bullet(x,y):
        global bullet_state
        bullet_state = "fire"
        screen.blit(bulletImg, (x+16, y+10))

    def isCollision(enemyX, enemyY, bulletX, bulletY):
        distance = math.sqrt(math.pow(enemyX - bulletX,2) + math.pow(enemyY - bulletY,2))
        if distance < 27:
            return True
        else:
            return False

    

    # Game Loop
    running = True
    while running:
        screen.fill((0,0,0))
        screen.blit(background, (0,0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Right or Left
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    playerX_change = -1.5
                if event.key == pygame.K_RIGHT:
                    playerX_change = 1.5
                if event.key == pygame.K_SPACE:
                    if bullet_state == "ready":
                        bullet_sound = mixer.Sound("\\\\wsl.localhost\\Ubuntu\\home\\jedkutai\\code\\projects\\haters modes\\laser.wav")
                        bullet_sound.play()
                        bulletX = playerX
                        fire_bullet(bulletX, bulletY)

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or pygame.K_RIGHT:
                    playerX_change = 0

        
        # Player Movement
        playerX += playerX_change

        if playerX <=0:
            playerX = 0
        elif playerX >= 736:
            playerX = 736
        
        # Enemy Movement
        for i in range(num_of_enemies):
            
            # Game Over
            if enemyY[i] > 480:
                for j in range(num_of_enemies):
                    enemyY[j] = 2000
                game_over_text()
                break

            enemyX[i] += enemyX_change[i]
            if enemyX[i] <=0:
                enemyX_change[i] = .5
                enemyY[i] += enemyY_change[i]
            elif enemyX[i] >= 736:
                enemyX_change[i] = -.5
                enemyY[i] += enemyY_change[i]

            # Collision
            collision = isCollision(enemyX[i],enemyY[i],bulletX,bulletY)
            collision_list = ["\\\\wsl.localhost\\Ubuntu\\home\\jedkutai\\code\\projects\\haters modes\\Default\\contact.wav",
            "\\\\wsl.localhost\\Ubuntu\\home\\jedkutai\\code\\projects\\haters modes\\Nicki vs Remy\\contact.mp3",
            "\\\\wsl.localhost\\Ubuntu\\home\\jedkutai\\code\\projects\\haters modes\\Drake vs Meek\\contact.mp3"
            ]
            if collision:
                explosion_sound = mixer.Sound(collision_list[z])
                explosion_sound.play()
                bulletY = 480
                bullet_state = "ready"
                score_value += 1
                enemyX[i] = random.randint(0, 736)
                enemyY[i] = random.randint(50,150)

            enemy(enemyX[i], enemyY[i], i)
        # Bullet Movement
        if bulletY <= 0:
            bulletY = 480
            bullet_state = "ready"

        if bullet_state == "fire":
            fire_bullet(bulletX, bulletY)
            bulletY -= bulletY_change

        
            

        player(playerX, playerY)
        show_score(textX, textY)
        pygame.display.update()


print("WARNING: THIS GAME WILL PLAY LOUD MUSIC AND OPEN IN THE BACKGROUND\nWhat version of the game would you like to play? Enter:\n")
print("0 for Default\n1 for Remy Ma vs Nicki Minaj\n2 for Drake vs Meek Mill")
game_type = int(input("Version: "))
play_haters(game_type)