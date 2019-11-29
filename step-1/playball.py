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

'''
일차적으로 큰 틀을 작성하였습니다.

기본적으로 step-1 단계에서 주어진 요건은 함수형으로 코딩을 하고, 함수의 이름과 매개변수, 반환값을 고려하여 코딩을 하는 것입니다.

첫번째 단계로서 크게 3가지의 함수로 프로그램을 구성했습니다.

1. main()
    야구 게임을 실행하게 하는 함수입니다. 초기 출력값과 baseball이라는 함수를 실행하게 하였습니다.
    
2. baseball()
    야구 게임이 여러 이닝이 진행 될 경우를 생각하여 한 게임을 플레이 할 때, 사용하기 위하여 baseball이라는 함수를 별도로 만들었습니다.
    해당 함수에는 게임의 기록과 야구에서 등장하는 4가지의 경우의 수를 리스트로 설정하였습니다.
    
3. playball()
    실질적으로 각 이닝의 플레이가 이루어지는 함수입니다.
    now_status라는 변수에 game_status리스트에서 random 라이브러리를 사용하여 임의의 상태를 하나 갖도록 하였습니다.
'''
