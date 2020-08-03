import pygame

pygame.init() #초기화

#화면크기설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width,screen_height))
#타이틀
pygame.display.set_caption("pygame")

#이벤트루프
running = True #게임진행 중인지
while running:
    for event in pygame.event.get():#어떤 이벤트가 발생했는가
        if event.type == pygame.QUIT: #창 닫히는 이벤트의 발생
            running = False #게임 진행중이 아님


#pygame 종료
pygame.quit()