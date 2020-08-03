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
# sprite - 적
enemy = pygame.image.load("enemy1.png")
enemy_size = enemy.get_rect().size #캐릭터 이미지의 크기
enemy_width = enemy_size[0] #캐릭터 가로크기
enemy_height = enemy_size[1] # 캐릭터 세로크기
enemy_x_pos = (screen_width-enemy_width)/2 # 캐릭터 x좌표
enemy_y_pos = (screen_height-enemy_height)/2  #캐릭터 y좌표
# 이동좌표
to_x = 0
to_y = 0
#이동속도
character_speed = 0.5
#폰트정의
game_font = pygame.font.Font(None, 40) #폰트 객체 생성 및 폰트 크기 설정

#총 시간
total_time = 10
#시작계산
start_ticks = pygame.time.get_ticks() #시작틱스 정보 받아오기

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
    char_x_minimum = 0
    char_x_maximum = screen_width-character_width
    char_y_minimum = 0
    char_y_maximum = screen_height-character_height
    
    #가로 경계값 처리
    if character_x_pos < char_x_minimum:
        character_x_pos = char_x_minimum
    elif character_x_pos > char_x_maximum:
        character_x_pos = char_x_maximum
    #세로 경계값 처리
    if character_y_pos < char_y_minimum:
        character_y_pos = char_y_minimum
    elif character_y_pos > char_y_maximum:
        character_y_pos = char_y_maximum
    
    #충동처리
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos
    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    #충돌처리 업데이트
    if character_rect.colliderect(enemy_rect):
        print("총돌")
        running = False

    #screen.fill((0,0,255))
    screen.blit(background,(0,0)) #배경그리기
    screen.blit(character,(character_x_pos, character_y_pos))#캐릭터그리기
    screen.blit(enemy,(enemy_x_pos, enemy_y_pos))#적그리기
    #타이머 그려넣기
    #경과시간 계산
    elapsed_time = (pygame.time.get_ticks()-start_ticks)/1000 #경과시간(ms->s)
    #잔여시간
    remain_time = int(total_time-elapsed_time)
    #출력내용 True 색상
    timer = game_font.render(str(remain_time), True, (255,255,255))
    screen.blit(timer, (10,10))
    # 남은시간 0이하면 게임종료(시간초과)
    if remain_time ==0:
        running = False
    #게임화면 다시그리기
    pygame.display.update() 

#잠시대기
pygame.time.delay(2000) #2000ms=2s 대기
#pygame 종료
pygame.quit()