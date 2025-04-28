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


def insert(root, value):
    new_node = TreeNode()
    new_node.data = value

    if root is None:
        return new_node

    node = TreeNode()
    node.data = value
    current = root

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

    return root


# def search(value):


if __name__ == "__main__":
    numbers = [10, 15, 8, 3, 9]
    root = None

    for number in numbers:
        root = insert(root, number)

    print("BST 구성 완료")
    post_order(root)