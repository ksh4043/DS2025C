import random

randInt = random.randint(1, 100)
win = False
for i in range(1, 8):
    term = int(input("정수 입력 : "))

    if randInt == term :
        win = True
        break
    elif randInt > term :
        print("조금 더 커용")
    elif randInt < term :
        print("작아용")

    print(f"앞으로 {7 - i}의 기회가 남았어요")

if win :
    print("정답입니다! 당신이 이겼습니다!")
else :
    print("패배했네용 ㅠㅠ 힘내서 다시 해보세요!")