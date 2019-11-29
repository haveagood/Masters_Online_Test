import random

def main():
    print("신나는 야구 게임!")
    print("첫 번째 타자가 타석에 입장했습니다.")
    baseball()

def baseball():
    game_status = ["anta","strike","ball","out"]
    game_cnt = [0,0,0,0]
    playball(game_status,game_cnt)

def playball(game_status, game_cnt):
    now_status = random.choice(game_status)

    while True:
        now_status = random.choice(game_status)
        print(" ")
        if now_status == "anta":
            game_cnt[0] += 1
            game_cnt[1], game_cnt[2] = 0, 0
            print("안타! 다음 타자가 타석에 입장했습니다.")
        elif now_status == "strike":
            game_cnt[1] += 1
            print("스트라이크!")
            if game_cnt[1] == 3:
                print("아웃! 다음 타자가 타석에 입장했습니다.")
                game_cnt[3] += 1
                game_cnt[1], game_cnt[2] = 0, 0
                if game_cnt[3] == 3:
                    break
        elif now_status == "ball":
            game_cnt[2] += 1
            print("볼!")
            if game_cnt[2] == 4:
                game_cnt[0] += 1
                print("포볼! 다음 타자가 타석에 입장했습니다.")
                game_cnt[1], game_cnt[2] = 0, 0
        elif now_status == "out":
            if game_cnt[3] == 3:
                break
            game_cnt[3] += 1
            game_cnt[1], game_cnt[2] = 0, 0
            print("아웃! 다음 타자가 타석에 입장했습니다.")

        print("%dS %dB %dO" % (game_cnt[1], game_cnt[2], game_cnt[3]))
    print("최종 안타수 : %d" % (game_cnt[0]))
    print("GAME OVER")