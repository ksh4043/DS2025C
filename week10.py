def post_order(node):
    if node:
        post_order(node.left)
        post_order(node.right)
        print(node.data, end='->')


class TreeNode:
    def __init__(self):
        self.left = None
        self.data = None
        self.right = None


def search(value):
    current = root

    if current is None:
        print("이진 트리가 비어있습니다")
        return

    while True:
        if value == current.data:
            print(f"{value}를 찾았습니다!")
            break
        elif value < current.data:
            if current.left is None:
                print(f"{value}가 해당 트리에 존재하지 않습니다!")
                break
            current = current.left
        else:
            if current.right is None:
                print(f"{value}가 해당 트리에 존재하지 않습니다!")
                break
            current = current.right


def insert(process, value):
    new_node = TreeNode()
    new_node.data = value

    if process is None:
        return new_node

    node = TreeNode()
    node.data = value
    current = process

    while True:
        if value < current.data:
            if current.left is None:
                current.left = node
                break
            current = current.left
        else:
            if current.right is None:
                current.right = node
                break
            current = current.right

    return process


if __name__ == "__main__":
    numbers = [10, 15, 8, 3, 9]
    root = None

    for number in numbers:
        root = insert(root, number)

    print("BST 구성 완료")
    post_order(root)
    print()

    number = int(input("찾는 값 입력 : "))
    search(number)