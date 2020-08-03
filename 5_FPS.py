import pygame

pygame.init() #초기화

#화면크기설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width,screen_height))
#타이틀
pygame.display.set_caption("pygame")
#FPS설정
clock = pygame.time.Clock()
# 배경이미지불러오기
background = pygame.image.load("background1.png")
# sprite -캐릭터- 불러오기
character = pygame.image.load("character1.png")
character_size = character.get_rect().size #캐릭터 이미지의 크기
character_width = character_size[0] #캐릭터 가로크기
character_height = character_size[1] # 캐릭터 세로크기
character_x_pos = (screen_width-character_width)/2 # 캐릭터 x좌표
character_y_pos = screen_height-character_height #캐릭터 y좌표
# 이동좌표
to_x = 0
to_y = 0
#이동속도
character_speed = 0.5
#이벤트루프
running = True #게임진행 중인지
while running:
    dt = clock.tick(30) # 게임화면의 초당 프레임수
    #print("fps:"+str(clock.get_fps()))
    for event in pygame.event.get():#어떤 이벤트가 발생했는가
        if event.type == pygame.QUIT: #창 닫히는 이벤트의 발생
            running = False #게임 진행중이 아님
        if event.type == pygame.KEYDOWN: #키 눌러짐 확인
            # 키
            left = event.key == pygame.K_LEFT
            right = event.key == pygame.K_RIGHT
            up = event.key == pygame.K_UP
            down = event.key == pygame.K_DOWN
            if left: #방향키 좌
                to_x -= character_speed
            if right:# 방향키 우
                to_x += character_speed
            if up: # 방향키 위
                to_y -= character_speed
            if down: #방향키 아래
                to_y += character_speed
        if event.type == pygame.KEYUP:
            if left or right:
                to_x = 0
            if up or down:
                to_y = 0
    
    #좌표변경
    character_x_pos += to_x*dt
    character_y_pos += to_y*dt
    # 캐릭터의 위치범위
    character_x_minimum = 0
    character_x_maximum = screen_width-character_width
    character_y_minimum = 0
    character_y_maximum = screen_height-character_height
    
    #가로 경계값 처리
    if character_x_pos < character_x_minimum:
        character_x_pos = character_x_minimum
    elif character_x_pos > character_x_maximum:
        character_x_pos = character_x_maximum
    #세로 경계값 처리
    if character_y_pos < character_y_minimum:
        character_y_pos = character_y_minimum
    elif character_y_pos > character_y_maximum:
        character_y_pos = character_y_maximum
    
    #screen.fill((0,0,255))
    screen.blit(background,(0,0)) #배경그리기
    screen.blit(character,(character_x_pos, character_y_pos))
    pygame.display.update() #게임화면 다시그리기


#pygame 종료
pygame.quit()