import random


def main():
    while True:
        print("신나는 야구 시합 \n1. 데이터 입력\n2. 데이터 출력\n3. 게임 시작\n메뉴 선택 ( 1 - 3 ) : ", end="")
        menu_choice = input()
        if int(menu_choice) == 1:
            team_1_name, team_1, team_2_name, team_2 = input_data()
        elif int(menu_choice) == 2:
            output_data(team_1_name, team_1, team_2_name, team_2)
        elif int(menu_choice) == 3:
            playball(team_1_name, team_1, team_2_name, team_2)
            break
        else:
            print("올바른 메뉴를 선택해 주세요!!")


def input_data():
    print("1번 메뉴")
    team_1, team_2 = dict(), dict()
    print("1 팀의 이름을 입력하세요> ", end="")
    team_1_name = input()
    team_1 = input_team_data(team_1)
    print("2 팀의 이름을 입력하세요> ", end="")
    team_2_name = input()
    team_2 = input_team_data(team_2)
    print("팀 데이터 입력이 완료되었습니다.")
    return team_1_name, team_1, team_2_name, team_2


def input_team_data(team):
    cnt = 1
    while cnt < 10:
        print("%d번 타자 정보 입력> " % (cnt), end="")
        name, hit = input().split(", ")
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


def output_data(team_1_name, team_1, team_2_name, team_2):
    print("2번 메뉴")
    print(" ---------------------------------------------- ")
    print(team_1_name + "팀 정보")
    team_1_name, team_1_hit = change_dict(team_1)
    player_print(team_1_name, team_1_hit)
    print(" ---------------------------------------------- ")
    print(team_2_name + "팀 정보")
    team_2_name, team_2_hit = change_dict(team_2)
    player_print(team_2_name, team_2_hit)
    print(" ---------------------------------------------- ")


def change_dict(team_dict):
    name_list = list(team_dict.keys())
    hit_list = list(team_dict.values())
    return name_list, hit_list


def player_print(name, hit):
    for i in range(len(name)):
        print("%d번 %s, %0.3f" % ((i + 1), name[i], hit[i]))


def playball(team_1_name, team_1, team_2_name, team_2):
    team1_idx, team2_idx = 0, 0
    score_board = [[0] * 7 for _ in range(2)]
    print("%s VS %s의 시합을 시작합니다.\n" % (team_1_name, team_2_name))
    for i in range(1, 7):
        print("%d회 초 %s의 공격" % (i, team_1_name))
        score_board[0][i], team1_idx = ining(team_1, team1_idx)
        print("%d회 말 %s의 공격" % (i, team_2_name))
        score_board[1][i], team2_idx = ining(team_2, team1_idx)

    final_score(team_1_name, team_2_name, score_board)


def final_score(team_1_name, team_2_name, score_board):
    print("-------------------------")
    print("경기 종료")
    print("%s VS %s" % (team_1_name, team_2_name))
    print("%d : %d" % (sum(score_board[0]), sum(score_board[1])))
    print("Thank You!!")


def ining(team, team_idx):
    name_list, hit_list = change_dict(team)
    game_cnt = [0, 0, 0, 0]
    get_point = 0
    while True:
        team_idx += 1
        print("%d 번 %s" % (team_idx, name_list[team_idx - 1]))
        game_cnt = now_play(game_cnt, hit_list[team_idx - 1])
        if team_idx == 9:
            team_idx = 0
        if game_cnt[3] == 3:
            break

    if game_cnt[0] - 4 > 0:
        get_point = game_cnt[0] - 4
    return get_point, team_idx


def now_play(game_cnt, hit):
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
    game_cnt[1], game_cnt[2] = 0, 0
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
    r = random.randrange(1, 1001)
    if r <= player_status[0]:
        return "anta"
    elif player_status[0] < r <= (player_status[0] + player_status[1]):
        return "strike"
    elif (player_status[0] + player_status[1]) < r <= (player_status[0] + player_status[1] + player_status[2]):
        return "ball"
    else:
        return "out"


# team_1_name = "aaaa"
# team_2_name = "bbbb"
# team_1 = {'최석원': 0.423, '김민수': 0.433, '강만식': 0.344, '김도일': 0.342, '공한직': 0.454, '갈마인': 0.236, '안성기': 0.498,
#           '임채룡': 0.435, '한성옥': 0.223}
# team_2 = {'최석': 0.423, '민수': 0.433, '강식': 0.344, '도일': 0.342, '공직': 0.454, '마인': 0.446, '성기': 0.498,
#           '임룡': 0.435, '한성': 0.423}

#---------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------

def Score_board():

    if len(team_1_name) < len(team_2_name):
        name_length = len(team_2_name)

    print("+--------------------------------+")
    print("| "+" "*name_length+" " * (10-name_length)+"1 2 3 4 5 6 | TOT    |")
    team_score_print(team_1_name,name_length,score_board[0])
    team_score_print(team_2_name,name_length,score_board[1])
    print("|  " + " " * 28 + "  |")
    print("|     " +team_1_name+" "*(24-(name_length*2))+team_2_name+ "   |")
    team_player_print(team_1,team_2)
    print("|  " + " " * 28 + "  |")
    print("+--------------------------------+")



def team_score_print(team_name,name_length,score_board):
    print("| "+team_name+" "*(10-name_length),end="")
    for i in range(len(score_board)):
        print(score_board[i],end=" ")
    print("|"+" "*8 + "|")


def team_player_print(team_1,team_2):
    team1_name = list(team_1.keys())
    team2_name = list(team_2.keys())

    team1_name = namelength_check(team1_name)
    team2_name = namelength_check(team2_name)

    for i in range(9):
        print("|  ",end = "")
        print("%d. %s" %(i+1,team1_name[i]),end = "")
        print(" "*13,end="")
        print("%d. %s" %(i+1,team2_name[i]),end = "")
        print("  |")



def namelength_check(name_list):
    for i in range(len(name_list)):
        if len(name_list[i]) > 3:
            name_list[i] = name_list[i][:3]
        elif len(name_list[i]) < 3:
            n = 3 - len(name_list[i])
            name_list[i] = name_list[i]+" "*(n+1)
    return name_list

#main()

Score_board()