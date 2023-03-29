#pgzero
import random

WIDTH = 800
HEIGHT = 600

player = Actor('e', (400, 300))
coins = []

def update(dt):
    global player, coins
    
    # Move the player left or right when the arrow keys are pressed
    if keyboard.left:
        player.x -= 15
    elif keyboard.right:
        player.x += 15

    # Move the player up or down when the arrow keys are pressed
    if keyboard.up:
        player.y -= 15
    elif keyboard.down:
        player.y += 15

    # Check for collisions between the player and any coins
    for coin in coins:
        if player.colliderect(coin):
            coins.remove(coin)
            print('Coin collected!')

    # Spawn a new coin randomly on the screen
    if len(coins) < 1:
        coin = Actor('s', (random.randint(0, WIDTH), random.randint(0, HEIGHT)))
        coins.append(coin)

def draw():
    screen.clear()
    player.draw()
    
    # Draw all of the coins on the screen
    for coin in coins:
        coin.draw()
