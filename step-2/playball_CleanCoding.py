import random

def main():
    # team_1_name = "aaaa"
    # team_2_name = "bbbb"
    # team_1 = {'최석원': 0.423, '김민수': 0.433, '강만식': 0.344, '김도일': 0.342, '공한직': 0.454, '갈마인': 0.236, '안성기': 0.498,
    #           '임채룡': 0.435, '한성옥': 0.223}
    # team_2 = {'최석': 0.423, '민수': 0.433, '강식': 0.344, '도일': 0.342, '공직': 0.454, '마인': 0.446, '성기': 0.498,
    #           '임룡': 0.435, '한성': 0.423}
    while True:
        print("신나는 야구 시합 \n1. 데이터 입력\n2. 데이터 출력\n3. 게임 시작\n메뉴 선택 ( 1 - 3 ) : ",end = "")
        menu_choice = input()
        if int(menu_choice) == 1:
            team_1_name,team_1,team_2_name,team_2# = input_data()
        elif int(menu_choice) == 2:
            output_data(team_1_name,team_1,team_2_name,team_2)
        elif int(menu_choice) == 3:
            playball(team_1_name,team_1,team_2_name,team_2)
            break
        else:
            print("올바른 메뉴를 선택해 주세요!!")


def input_data():
    print("1번 메뉴")
    team_1,team_2 = dict(),dict()
    print("1 팀의 이름을 입력하세요> ",end = "")
    team_1_name = input()
    team_1 = input_team_data(team_1)
    print("2 팀의 이름을 입력하세요> ",end = "")
    team_2_name = input()
    team_2 = input_team_data(team_2)
    print("팀 데이터 입력이 완료되었습니다.")
    return team_1_name, team_1, team_2_name, team_2


def input_team_data(team):
    cnt = 1
    while cnt < 10:
        print("%d번 타자 정보 입력> " %(cnt),end = "")
        name,hit = input().split(", ")
        if name in team.keys():
            print("이미 존재하는 선수 입니다.")
        elif len(hit) > 5:
            print("소숫점 자릿수를 확인하여 주세요")
        elif 0.1 > float(hit) or float(hit) > 0.5:
            print("선수의 타율이 잘못 입력되었습니다.")
        else:
            team[name] = float(hit)
            cnt += 1
    return team


def output_data(team_1_name,team_1,team_2_name,team_2):
    print("2번 메뉴")
    print(" ---------------------------------------------- ")
    print(team_1_name+"팀 정보")
    team_1_name,team_1_hit = change_dict(team_1)
    player_print(team_1_name,team_1_hit)
    print(" ---------------------------------------------- ")
    print(team_2_name+"팀 정보")
    team_2_name,team_2_hit = change_dict(team_2)
    player_print(team_2_name,team_2_hit)
    print(" ---------------------------------------------- ")


def change_dict(team_dict):
    name_list = list(team_dict.keys())
    hit_list = list(team_dict.values())
    return name_list,hit_list


def player_print(name,hit):
    for i in range(len(name)):
        print("%d번 %s, %0.3f" %((i+1),name[i],hit[i]))


def playball(team_1_name,team_1,team_2_name,team_2):
    team1_idx,team2_idx = 0,0
    score_board = [[0]*7 for _ in range(2)]
    print("%s VS %s의 시합을 시작합니다.\n" % (team_1_name, team_2_name))
    for i in range(1,7):
        print("%d회 초 %s의 공격" %(i,team_1_name))
        score_board[0][i],team1_idx = ining(team_1,team1_idx)
        print("%d회 말 %s의 공격" % (i, team_2_name))
        score_board[1][i],team2_idx = ining(team_2, team1_idx)

    final_score(team_1_name,team_2_name,score_board)


def final_score(team_1_name,team_2_name,score_board):
    print("-------------------------")
    print("경기 종료")
    print("%s VS %s" %(team_1_name,team_2_name))
    print("%d : %d" %(sum(score_board[0]),sum(score_board[1])))
    print("Thank You!!")


def ining(team,team_idx):
    name_list, hit_list = change_dict(team)
    game_cnt = [0,0,0,0]
    get_point = 0
    while True:
        team_idx += 1
        print("%d 번 %s" %(team_idx,name_list[team_idx-1]))
        game_cnt = now_play(game_cnt,hit_list[team_idx-1])
        if team_idx == 9:
            team_idx = 0
        if game_cnt[3] == 3:
            break

    if game_cnt[0] - 4 > 0:
        get_point = game_cnt[0] - 4
    return get_point,team_idx


def now_play(game_cnt,hit):

    while True:
        now = choice(hit)
        if now == "anta":
            game_cnt = anta(game_cnt)
            break
        elif now == "strike":
            game_cnt = strike(game_cnt)
            if game_cnt[1] == 3:
                break
        elif now == "ball":
            game_cnt = ball(game_cnt)
            if game_cnt[2] == 4:
                break
        elif now == "out":
            game_cnt = out(game_cnt)
            break
    game_cnt[1],game_cnt[2] = 0,0
    return game_cnt


def anta(game_cnt):
    game_cnt[0] += 1
    print("안타!")
    print("%dS %dB %dO" % (game_cnt[1], game_cnt[2], game_cnt[3]))
    return game_cnt


def strike(game_cnt):
    game_cnt[1] += 1
    print("스트라이크!")
    print("%dS %dB %dO" % (game_cnt[1], game_cnt[2], game_cnt[3]))
    if game_cnt[1] == 3:
        game_cnt[3] += 1
        print("아웃!")
    return game_cnt


def ball(game_cnt):
    game_cnt[2] += 1
    if game_cnt[2] == 4:
        game_cnt[0] += 1
        print("포볼!")
    else:
        print("볼!")
    print("%dS %dB %dO" % (game_cnt[1], game_cnt[2], game_cnt[3]))
    return game_cnt


def out(game_cnt):
    game_cnt[3] += 1
    print("아웃!")
    print("%dS %dB %dO" % (game_cnt[1], game_cnt[2], game_cnt[3]))
    return game_cnt


def choice(hit):
    player_status = [hit, ((1 - hit) / 2 - 0.05), ((1 - hit) / 2 - 0.05), 0.1]
    for i in range(4):
        player_status[i] *= 1000
    r = random.randrange(1,1001)
    if r <= player_status[0]:
        return "anta"
    elif player_status[0] < r <= (player_status[0] + player_status[1]):
        return "strike"
    elif (player_status[0] + player_status[1]) < r <= (player_status[0] + player_status[1] + player_status[2]):
        return "ball"
    else:
        return "out"

'''
야구 경기에 대한 부분을 구현하였습니다.

- playball()
    
    우선 경기가 시작되면 playball 이라는 함수로 들어가게 됩니다.
    
    해당 함수의 team1_idx,team2_idx는 각 팀의 타자의 순번을 저장하는 변수 입니다.
    
    score_board라는 2차원 배열의 경우 각 이닝마다의 점수를 기록하기 위해 설정하였습니다.
    
    경기가 시작되게 되면, for문을 활용하여 1~6이닝까지의 경기를 하게 됩니다.
    
    각 이닝별로의 경기 진행 상황의 경우에는 ining이라는 함수를 활용하여 따로 구현 하였습니다.

- ining()
    
    한 이닝을 구현하였습니다. team_1,team_2 딕셔너리에 들어있는 선수정보와 타율 정보를 활용하기 위해서 changedict라는 함수를 활용하였습니다.
    
    Key값과 Value값을 리스트로 변경하여 인덱스를 해당 타자의 타자번호, key값을 이름, value값을 타율로 활용하였습니다.
    
    game_cnt라는 ([0,0,0,0]) 배열에는 [안타, 스트라이크, 볼, 아웃]의 정보를 저장하기 위해 선언하였습니다.
    
    game_point 변수는 해당 이닝이 끝났을 때, 안타의 갯수가 4개 이상일 경우 점수를 저장하기 위해 선언하였습니다.
    
    하나의 이닝을 while문으로 실행하였습니다.
    
    team_idx 값을 하나씩 증가시키고, 만약 값이 9를 초과할 경우 0으로 다시 초기화를 시켰습니다.
    
    선수 개별의 플레이에 대해서는 now_play()함수로 별도 구현 하였습니다.
    
    아웃카운트가 3개가 될 경우 while문을 중단시키고 해당 이닝의 점수를 계산하여 해당 이닝의 최종점수와 타순번호를 playball함수로 돌려주었습니다.
    
- now_play()

    한명의 타자가 게임을 하는것을 while문을 통해서 구현하였습니다.
    
    안타, 스트라이크, 볼, 아웃 4가지 상황중 어떤 상황을 가지게 되는지는 choice함수에서 값을 돌려받아 now라는 변수에 저장하였습니다.
    
    각 상황별로 if문을 활용하여 구현하였고, 3스트라이크, 4볼의 경우에는 아웃, 안타의 경우와 동일하게 처리하였습니다.
    
    1. anta()
        안타를 치게 될 경우에는 game_cnt[0] 값을 1 증가시키고, break문을 활용하여 출루하는것처럼 while문을 빠져나왔습니다.
        
    2. strike()
        스트라이크를 치게 될 경우에는 game_cnt[1]값을 1 증가시키고, game_cnt값을 return 하여 다시 while문으로 경기를 진행했습니다.
        
        만약 스트라이크가 3개일 경우에는 아웃!이라는 메세지를 별도로 뜨게 하고, game_cnt[3]값을 1 증가시켜 아웃과 동일하게 처리하고
        
        break문을 통해서 while문을 빠져나왔습니다.
        
    3. ball()
        볼의 경우는 스트라이크와 비슷하였습니다. game_cnt[2]값을 1증가시키고, 4볼의 경우에는 포볼 메세지를 추가로 띄우고,
        
        game_cnt[0]값을 1 증가시켜 안타와 동일하게 처리하였습니다.
        
    4. out()
        아웃은 game_cnt[3]의 값을 1 증가시키고 아웃이라는 메세지 출력 후 빠져나오게 하였습니다.
        
    각 상황별로 별도의 print문을 활용하여 현재 이닝의 진행상황을 지속적으로 식별 가능하게 하였습니다.
    
- choice()

    [안타 확률, 스트라이크 확률, 볼 확률, 아웃 확률] 값을 받아왔습니다.
    
    해당 값에 각 1000씩 곱하였습니다. 모든 숫자를 더하면 1000이 되도록 하였습니다.
    
    random라이브러리를 활용하여 1~1000사이의 범위를 지정하고 임의의 수 하나를 뽑도록 하였습니다.
    
    if문을 활용하여 낮은수 부터 차례대로 if문을 통과하여 확률을 계산하였습니다.
    
    해당 부분의 코드 입니다.
    
    if r <= player_status[0]: # 안타의 확률
        return "anta"
    elif player_status[0] < r <= (player_status[0] + player_status[1]): # 스트라이크의 확률
        return "strike"
    elif (player_status[0] + player_status[1]) < r <= (player_status[0] + player_status[1] + player_status[2]): # 볼의 확률
        return "ball"
    else:
        return "out" # 나머지는 아웃의 확률로 계산하였습니다.
     
'''


# def playball(game_status,game_cnt):
#
#     while True:
#
#         now_status = random.choice(game_status)
#         print(" ")
#
#         if now_status == "anta":
#             game_cnt = anta(game_cnt)
#         elif now_status == "strike":
#             game_cnt = strike(game_cnt)
#         elif now_status == "ball":
#             game_cnt = ball(game_cnt)
#         elif now_status == "out":
#             game_cnt = out(game_cnt)
#
#         print("%dS %dB %dO" % (game_cnt[1], game_cnt[2], game_cnt[3]))
#
#         if game_cnt[3] == 3:
#             print(" ")
#             break
#
#
#     print("최종 안타수 : %d" %(game_cnt[0]))
#     print("GAME OVER")
#
#
# def next_player(game_cnt):
#     print("다음 타자가 타석에 입장했습니다.")
#     game_cnt[1], game_cnt[2] = 0, 0
#     return game_cnt
#
#
# def anta(game_cnt):
#     game_cnt[0] += 1
#     print("안타!", end = " ")
#     game_cnt = next_player(game_cnt)
#     return game_cnt
#
#
# def strike(game_cnt):
#     game_cnt[1] += 1
#     print("스트라이크!")
#     if game_cnt[1] == 3:
#         game_cnt = out(game_cnt)
#
#     return game_cnt
#
#
# def ball(game_cnt):
#     game_cnt[2] += 1
#     if game_cnt[2] == 4:
#         print("포볼!", end = " ")
#         game_cnt = next_player(game_cnt)
#     else:
#         print("볼!")
#     return game_cnt
#
#
# def out(game_cnt):
#     game_cnt[3] += 1
#     if game_cnt[3] == 3:
#         game_cnt[1],game_cnt[2] = 0,0
#         print("아웃!")
#         return game_cnt
#
#     else:
#         print("아웃!", end = " ")
#         game_cnt = next_player(game_cnt)
#         return game_cnt
#

main()