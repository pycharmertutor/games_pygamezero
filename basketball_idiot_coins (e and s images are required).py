#pgzero
import time
import random
a = random.randint(100, 500)
WIDTH = 800
HEIGHT = 600
coin_c = 99
player = Actor('e', (400, 300))
coins = []

def update(dt):
    global player, coins
    
    if keyboard.left:
        player.x -= 15
    elif keyboard.right:
        player.x += 15


    if keyboard.up:
        player.y -= 15
    elif keyboard.down:
        player.y += 15


    for coin in coins:
        if player.colliderect(coin):
            global coin_c
            print(coin_c)
            coin_c = coin_c + 1
            coins.remove(coin)
            print('Coin collected!')
            
    if coin_c == 100 or coin_c >= 100:
        coin_c = 0
        print("game over resseting")


    if len(coins) < 1:
        coin = Actor('s', (random.randint(0, WIDTH), random.randint(0, HEIGHT)))
        coins.append(coin)

def draw():
    screen.clear()
    player.draw()
    

    for coin in coins:
        coin.draw()
