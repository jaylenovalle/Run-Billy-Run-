#Krust Krew            
#RUN BILLY, RUN!!!!
#Kerien Washington,Jaden Moya,Jaylen Ovalles
#two sentence explanation of the game's objective

from gamelib import*#import game library

#objects and initial settings
game = Game (1600,830,"run billy run!!")
bk = Image("yo.jpg",game)
bk.resizeTo(game.width, game.height)
play= Image("play.png",game)
play.resizeTo(300,300)
play.moveTo(350,350)
sea = Image("sea.gif",game)
sea.resizeTo(game.width, game.height)
game.setBackground(sea)
billy = Animation("billy.png",12,game,332/6,152/2)
billy.moveTo(50,350)
over= Image("over.jpg",game)
over.resizeTo(game.width, game.height)
mouse.visible = False
mrkrabs = Animation("wolf.png",8,game,1200/2,1536/4)
mrkrabs.moveTo(50,350)
mrkrabs.resizeTo(200,150)
gems = Image("lollolo.png",game)
#variable for jumping action        
jumping = False #Used to check to see if you are jumping
landed = False  #Used to check to see if you have landed on the "ground" (platform)
factor = 1  #Used for a slowing effect of the jumping

while not game.over:
    game.processInput()
    #game.scrollBackground("left",2)
    bk.draw()
    play.draw()
    if mouse.LeftClick:
        game.over=True
    game.update(90)
game.over = False
#Level 1 - game loop
while not game.over:
    game.processInput()
    game.scrollBackground("left",10)
    gems.moveTo(mouse.x,mouse.y)
    if billy.collidedWith(mouse) and mouse.LeftClick:
        game.score += 10
    billy.draw()
    if mrkrabs.collidedWith(mouse) and mouse.LeftClick:
        game.score += 25
    if billy.y< 350:#value of y is based on your object's y position
        landed = False#not landed

    else:
        landed = True
   
            
    if keys.Pressed[K_SPACE] and landed and not jumping:#if you have landed and are not jumping and press the space bar then jump
        jumping = True

    if jumping:
   
        billy.y -=18*factor#adjust for the drop
        #Make the character go up.  Factor creates a slowing effect to the jump
        factor*=.95#fall slowly
        landed = False
        #Since you are jumping you are no longer staying on land
        if factor < .38:
            jumping = True
            #Stop jumping once the slowing effect finishes
            factor = 1
            
    if not landed: #is jumping

        billy.y +=5#adjust for  the height of the jump - lower number higher jump
      


    if keys.Pressed[K_a]:
        billy.x-=8
    if keys.Pressed[K_d]:
        billy.x+=8
    if keys.Pressed[K_w]:
        billy.y-=0
    if keys.Pressed[K_s]:
        billy.y+=0
    mrkrabs.draw()
    if mrkrabs.y< 350:#value of y is based on your object's y position
        landed = False#not landed

    else:
        landed = True
   
            
    if keys.Pressed[K_SPACE] and landed and not jumping:#if you have landed and are not jumping and press the space bar then jump
        jumping = True

    if jumping:
   
        mrkrabs.y -=18*factor#adjust for the drop
        #Make the character go up.  Factor creates a slowing effect to the jump
        factor*=.95#fall slowly
        landed = False
        #Since you are jumping you are no longer staying on land
        if factor < .38:
            jumping = False
            #Stop jumping once the slowing effect finishes
            factor = 1
            
    if not landed: #is jumping

        mrkrabs.y +=5#adjust for  the height of the jump - lower number higher jump
    gems.draw()
    if keys.Pressed[K_LEFT]:
        mrkrabs.x-=8
    if keys.Pressed[K_RIGHT]:
        mrkrabs.x+=8
    if keys.Pressed[K_UP]:
        mrkrabs.y-=0
    if keys.Pressed[K_DOWN]:
        mrkrabs.y+=0
    if game.time <= 0:
        game.over = False
    if game.score >= 700:
        game.over = True
        over.draw()
        
    game.displayTime(150,5)
    game.displayScore()
    game.update(30)
game.quit()
