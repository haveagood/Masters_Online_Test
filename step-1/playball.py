import random

def main():
    print("신나는 야구 게임!")
    print("첫 번째 타자가 타석에 입장했습니다.")
    baseball()

def baseball():
    game_status = ["anta","strike","ball","out"]
    game_cnt = [0,0,0,0]
    playball(game_status,game_cnt)

def playball(game_status,game_cnt):

    while True:

        now_status = random.choice(game_status)
        print(" ")

        if now_status == "anta":
            game_cnt = anta(game_cnt)
        elif now_status == "strike":
            game_cnt = strike(game_cnt)
        elif now_status == "ball":
            game_cnt = ball(game_cnt)
        elif now_status == "out":
            game_cnt = out(game_cnt)

        print("%dS %dB %dO" % (game_cnt[1], game_cnt[2], game_cnt[3]))

        if game_cnt[3] == 3:
            print(" ")
            break


    print("최종 안타수 : %d" %(game_cnt[0]))
    print("GAME OVER")


def next_player(game_cnt):
    print("다음 타자가 타석에 입장했습니다.")
    game_cnt[1], game_cnt[2] = 0, 0
    return game_cnt


def anta(game_cnt):
    game_cnt[0] += 1
    print("안타!", end = " ")
    game_cnt = next_player(game_cnt)
    return game_cnt


def strike(game_cnt):
    game_cnt[1] += 1
    print("스트라이크!")
    if game_cnt[1] == 3:
        game_cnt = out(game_cnt)

    return game_cnt


def ball(game_cnt):
    game_cnt[2] += 1
    if game_cnt[2] == 4:
        game_cnt[0] += 1
        print("포볼!", end = " ")
        game_cnt = next_player(game_cnt)
    else:
        print("볼!")
    return game_cnt


def out(game_cnt):
    game_cnt[3] += 1
    if game_cnt[3] == 3:
        game_cnt[1],game_cnt[2] = 0,0
        print("아웃!")
        return game_cnt

    else:
        print("아웃!", end = " ")
        game_cnt = next_player(game_cnt)
        return game_cnt


main()