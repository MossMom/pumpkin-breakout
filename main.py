# Import pygame & random library and initialize the game engine
import pygame, random, math

pygame.init()

# Open new window, caption it "Breakout"
(width, height) = (600, 800)
screen = pygame.display.set_mode((width, height)) # creates pygame screen
pygame.display.set_caption("Breakout")

# Here's the variable that runs our game loop
doExit = False

# The clock will be used to control how fast the screen updates
clock = pygame.time.Clock()

# Variables hold paddle position & color
# These go above game loop
p1x = 250
p1y = 750
p1Color = 100
p1Speed = 0

# Ball variables
bVxStart = random.randint(0,1)
bVyStart = 1
bx = 250 # X position
by = 400 # Y position

# Random starting velocity, decides beginning player confirm as well
  
if bVxStart == 1:
    bVx = -5 # X velocity (horizontal speed)
if  bVxStart == 0:
    bVx = +5 # X velocity (horizontal speed)

if bVyStart == 1:
    bVy = 5 # X velocity (vertical speed)
    p1Confirm = True

class pumpkin: # BALL OBJECT CLASS --------------------------------------------------------------------------
    def __init__(self, x, y, choice):
        self.x = x
        self.y = y
        if choice <= 3: # orange pumpkin
            self.color = (138 +random.randint(-10,10), 23 +random.randint(-10,10), 17 +random.randint(-10,10))
            self.color2 = (138-22, 23-12, 17-10)
        elif choice <= 7: # red pumpkin
            self.color = (186 +random.randint(-10,10), 93 +random.randint(-10,10), 17 +random.randint(-10,10))
            self.color2 = (186-25, 93-18, 17-10)
        elif choice <= 9: # white pumpkin
            self.color = (181 +random.randint(-10,10), 160 +random.randint(-10,10), 150 +random.randint(-10,10))
            self.color2 = (181-20, 160-25, 150-25)
        elif choice <= 10: # blue pumpkin
            self.color = (72 +random.randint(-10,10), 81 +random.randint(-10,10), 122 +random.randint(-10,10))
            self.color2 = (72-12, 81-13, 122-15)
        else:
            print("! Error in color assignment !")
        
    def collide(self, ballX, ballY):
        if math.sqrt(((self.x-ballX) * (self.x-ballX)) + ((self.y-ballY) * (self.y-ballY))) < (90 + 10):
            return True
        else:
            return False
        
        
    def draw(self):
        pygame.draw.ellipse(screen, self.color, (self.x, self.y, 100, 80))
        pygame.draw.arc(screen, self.color2, (self.x+10, self.y-16, 110, 115), (5*math.pi)/6, (7*math.pi)/6, 5)
        pygame.draw.arc(screen, self.color2, (self.x+30, self.y-36, 110, 150), (5*math.pi)/6, (7*math.pi)/6, 5)
        pygame.draw.arc(screen, self.color2, (self.x-22, self.y-16, 110, 115), (11*math.pi)/6, (math.pi)/6, 5)
        pygame.draw.arc(screen, self.color2, (self.x-42, self.y-36, 110, 150), (11*math.pi)/6, (math.pi)/6, 5)
        pygame.draw.arc(screen, ((22, 100, 8)), (self.x+45, self.y-51, 110, 115), (5*math.pi)/6, (math.pi), 8)
        pygame.draw.ellipse(screen, ((0, 0, 0)), (self.x, self.y, 100, 80), 5)


# CREATE A SET AMOUNT OF PUMPKINS ----------------------------------------------------------------------------------
patch = [] # creates empty pumpkin list

for i in range(5): # makes a grid of pumpkins
    for j in range(3):
        x = 10+(i*120)
        y = 40+(j*120)
        choice = random.randint(1, 10)
        patch.append(pumpkin(x, y, choice))


while not doExit: #GAME LOOP----------------------------------------------------

    # Event queue stuff
    clock.tick(60)

    for event in pygame.event.get(): # Check if user did something
        if event.type == pygame.QUIT: # Check if user clicked close
            doExit = True # Flag that we are done so we exit the game loop
    
    # Game logic will go here-----------------------------------------------------
    
    if p1Confirm == True:
        p1Color = 255
    else:
        p1Color = 100


    # Move paddles, don't let them go off screen
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] and p1x > 5:
        p1x-=7
    if keys[pygame.K_d] and p1x < 495:
        p1x+=7

    # Reflect ball off of paddle, check if inside paddle, increase speed by score
    if by >= p1y - 20 and by <= p1y and bx + 20 > p1x and bx < p1x + 100 and p1Confirm == True:
        bVy *= -1
    if bVy > 0:
        p1Confirm = True
    else:
        p1Confirm = False

    # Ball movement
    bx += bVx
    by += bVy

    # Reflect ball of sides of screen, set score to 0 for 1 player, allow other player to recieve points for their next hit
    if bx < 5 or bx + 20 > 595:
        bVx *= -1
    if by < 5 or by + 20 > 795:
        bVy *= -1
        
    # Render section will go here ------------------------------------------------
    screen.fill((0,0,0)) # Wipe screen black

    # Draw a rectangle
    pygame.draw.rect(screen, (p1Color,p1Color,p1Color), (p1x, p1y, 100, 20), 1)

    # Draw a ball
    pygame.draw.ellipse(screen, (255,255,255), (bx, by, 20, 20), 1)
    
    # Show Controls
    font = pygame.font.Font(None, 20) # Use default font
    text = font.render(str("Player 1 Controls: A / D"), 1, (100, 100, 100))
    screen.blit(text, (8,780))
    
    for i, pumpkin in enumerate(patch):
        pumpkin.draw() # draws all pumpkins in the patch
        if pumpkin.collide(bx, by):
            bVx *= -1
            bVy *= -1
            patch.remove(pumpkin)

    # Update the screen
    pygame.display.flip()


# END GAME LOOP ----------------------------------------------------------------

pygame.quit() # When game is done close down pygame
