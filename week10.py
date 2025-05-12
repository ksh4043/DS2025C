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

    while True:
        if value == current.data:
            return True
        elif value < current.data:
            if current.left is None:
                return False
            current = current.left
        else:
            if current.right is None:
                return False
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


def delete(node, value):
    if node is None:
        return None

    if value < node.data:
        node.left = delete(node.left, value)
    elif value > node.data:
        node.right = delete(node.right, value)
    else: # 삭제할 노드 발견
        if node.right is None:
            return node.left
        elif node.left is None:
            return node.right
        # 자식 노드가 2개인 경우
        min_larger_node = node.right
        while min_larger_node.left:
            min_larger_node = min_larger_node.left # move
        node.data = min_larger_node.data
        node.right = delete(node.right, min_larger_node.data)
    return node


if __name__ == "__main__":
    numbers = [10, 15, 8, 3, 9, 14]
    root = None

    for number in numbers:
        root = insert(root, number)

    print("BST 구성 완료")
    post_order(root)
    print()

    find_number = int(input("찾는 값 입력 : "))
    if search(find_number) :
        print(f"{find_number}를 찾았습니다!")
    else:
        print(f"{find_number}가 해당 트리에 존재하지 않습니다!")

    delete_number = int(input("제거할 값 입력 : "))
    root = delete(root, delete_number)

    post_order(root)
    print()