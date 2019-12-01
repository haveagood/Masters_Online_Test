def main():
    while True:
        print("신나는 야구 시합 \n1. 데이터 입력\n2. 데이터 출력\n메뉴 선택 ( 1 - 2 ) : ",end = "")
        menu_choice = input()
        if int(menu_choice) == 1:
            team_1_name,team_1,team_2_name,team_2 = input_data()
        elif int(menu_choice) == 2:
            output_data(team_1_name,team_1,team_2_name,team_2)
        # elif int(menu_choice) == 3:
        #     playball(team_1_name,team_1,team_2_name,team_2)
        #     break
        else:
            print("올바른 메뉴를 선택해 주세요!!")


def input_data():
    print("1번 메뉴")
    team_1,team_2 = dict(),dict()
    print("1 팀의 이름을 입력하세요> ",end = "")
    team_1_name = input()
    for i in range(1,10):
        print("%d번 타자 정보 입력> " %(i),end = "")
        name,hit = input().split(", ")
        team_1[name] = float(hit)

    print("2 팀의 이름을 입력하세요> ",end = "")
    team_2_name = input()
    for j in range(1,10):
        print("%d번 타자 정보 입력> " % (j),end = "")
        name,hit = input().split(", ")
        team_2[name] = float(hit)

    print("팀 데이터 입력이 완료되었습니다.")

    return team_1_name,team_1,team_2_name,team_2


def output_data(team_1_name,team_1,team_2_name,team_2):
    print("2번 메뉴")
    print(" ---------------------------------------------- ")
    print(team_1_name+"팀 정보")
    change_dict(team_1)
    print(" ---------------------------------------------- ")
    print(team_2_name+"팀 정보")
    change_dict(team_2)
    print(" ---------------------------------------------- ")

def change_dict(team_dict):
    name_list = list(team_dict.keys())
    hit_list = list(team_dict.values())
    for i in range(len(name_list)):
        print("%d번 %s, %0.3f" %((i+1),name_list[i],hit_list[i]))
#
# def playball(team_1_name,team_1,team_2_name,team_2):
#     print("%s VS %s의 시합을 시작합니다." % (team_1_name, team_2_name))
#

#
# def baseball():
#     game_status = ["anta","strike","ball","out"]
#     game_cnt = [0,0,0,0]
#     playball(game_status,game_cnt)
#
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