import pygame,sys,time,random
from pygame.locals import *

redColour = pygame.Color(255,0,0)
blackColour = pygame.Color(0,0,0)
whiteColour = pygame.Color(255,255,255)

#---定義遊戲結束
def gameOver():
    pygame.quit()
    sys.exit()

#---定義主函數及各種初始化
def main():
    pygame.init()
    fpsClock = pygame.time.Clock()
    playSurface = pygame.display.set_mode((640,480))
    pygame.display.set_caption('貪食蛇')
    snakePosition = [80,100]
    snakeBody = [[80,100],[100,100],[120,100]]
    targetPosition = [300,300]
    targetFlag = 1
    direction = 'right'
    changeDirection = direction

    while True:

        #---檢查鍵盤事件
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            #---判斷鍵盤事件
            elif event.type == KEYDOWN:
                if event.key == K_RIGHT:
                    changeDirection = 'right'
                if event.key == K_LEFT:
                    changeDirection = 'left'
                if event.key == K_UP:
                    changeDirection = 'up'
                if event.key == K_DOWN:
                    changeDirection = 'down'
                if event.key == K_ESCAPE:
                    pygame.event.post(pygame.event.Event(QUIT))

        #---判斷反方向
        if changeDirection == 'right' and not direction == 'left':
            direction = changeDirection
        if changeDirection == 'left' and not direction == 'right':
            direction = changeDirection
        if changeDirection == 'up' and not direction == 'down':
            direction = changeDirection
        if changeDirection == 'down' and not direction == 'up':
            direction = changeDirection

        #---移動
        if direction == 'right':
            snakePosition[0] += 20
        if direction == 'left':
            snakePosition[0] -= 20
        if direction == 'up':
            snakePosition[1] -= 20
        if direction == 'down':
            snakePosition[1] += 20

        #---增加長度
        snakeBody.insert(0,list(snakePosition))

        #---判斷重疊
        if snakePosition[0] == targetPosition[0] and snakePosition[1] == targetPosition[1]:
            targetFlag = 0
        else:
            snakeBody.pop()

        #---隨機生成
        if targetFlag == 0:
            x = random.randrange(1,32)
            y = random.randrange(1,24)
            targetPosition = [int(x*20),int(y*20)]
            targetFlag = 1

        #---繪製邊界
        playSurface.fill(blackColour)
        for position in snakeBody:
            pygame.draw.rect(playSurface,whiteColour,Rect(position[0],position[1],20,20))
            pygame.draw.rect(playSurface,redColour,Rect(targetPosition[0], targetPosition[1],20,20))

        #---刷新顯示
        pygame.display.flip()

        #---超越邊界
        if snakePosition[0] > 620 or snakePosition[0] < 0:
            gameOver(playSurface)
        if snakePosition[1] > 460 or snakePosition[1] < 0:
            for snakeBody in snakeBody[1:]:
                if snakePosition[0] == snakeBody[0] and snakePosition[1] == snakeBody[1]:
                    gameOver(playSurface)

        #---遊戲速度                
        fpsClock.tick(3)

#---啟動遊戲
if __name__ == "__main__":
    main()