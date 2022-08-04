
import pygame,sys
from network import Network


pygame.init()
c = Network()
window  = pygame.display.set_mode((700,500))

bar1 = pygame.transform.scale(pygame.image.load("bar.png"),(100,50))
bar2 = pygame.transform.scale(pygame.image.load("bar.png"),(100,50))

bar1_x = 0
bar2_x = 0

def parse_data(data):
    try:
        d = data.split(",")
        return [int(d[0]), int(d[1])]
    except:
        return 0,0

def send_data():
        data =  str(bar1_x) + "," + str(bar2_x)
        reply = c.send(data)
        return reply


while True:
    window.fill(pygame.Color(255,255,255))
    # bar1 = pygame.draw.rect(window,pygame.Color(255,0,0),(int(bar1_x),100,70,40),0)
    # bar2 = pygame.draw.rect(window,pygame.Color(0,255,0),(int(bar2_x),400,70,40),0)

    window.blit(bar1,(bar1_x,100))
    window.blit(bar2,(bar2_x,400))


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                print("A")
                bar1_x += 5
            if event.key == pygame.K_d:
                print("d")
                bar1_x -= 5
            if event.key == pygame.K_LEFT:
                bar2_x += 5
            if event.key == pygame.K_RIGHT:
                bar2_x -= 5

    bar1_x,bar2_x = parse_data(send_data())
        
    pygame.time.Clock().tick(50)
    pygame.display.update()
