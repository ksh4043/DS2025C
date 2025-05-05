def is_queue_full() -> bool :
    global SIZE, rear
    if rear == SIZE - 1:
        return True
    else:
        return False


def is_queue_empty() -> bool :
    global SIZE, front, rear
    if front == rear:
        return True
    else:
        return False


def en_queue(data):
    global rear
    if is_queue_full():
        print("큐가 꽉 찼습니다")
        return None
    rear = rear + 1
    queue[rear] = data


def de_queue():
    global front
    if is_queue_empty():
        print("큐가 비어있습니다")
        return None
    front = front + 1
    data = queue[front]
    queue[front] = None
    return data

def peek():
    global front
    if is_queue_empty():
        print("큐가 비어있습니다")
        return None
    return queue[front+1]


SIZE = int(input("큐 사이즈 입력 : "))
queue = [None for _ in range(SIZE)]
front = rear = -1

if __name__ == "__main__":
    while True:
        menu = input("삽입(i), 추출(e), 확인(v), 종료(x) : ")
        if menu == 'x' or menu == 'X':
            print("프로그램을 종료합니다")
            break
        elif menu == 'i' or menu == 'I':
            en_queue(input("입력할 데이터 : "))
            print(queue)
        elif menu == 'e' or menu == 'E':
            print(f"추출된 데이터 {de_queue()}")
            print(queue)
        elif menu == 'v' or menu == 'V':
            print(f"확인된 데이터 {peek()}")
            print(queue)
        else:
            print(f"{menu}는 잘못된 입력입니다.")
