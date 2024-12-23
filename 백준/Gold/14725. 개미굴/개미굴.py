def add_to_tree(tree, path):
    current = tree
    for level in path:
        if level not in current:
            current[level] = {} # 새 계층 추가
        current = current[level] # 현재 계층 이동

def print_tree(tree, depth=0):
 for key in sorted(tree.keys()): # 사전 순서로 출력
     print("--" * depth + key)
     print_tree(tree[key], depth + 1) # 하위 계층 출력

if __name__ == '__main__':
    # 입력 처리
    N = int(input()) # 경로 개수
    tree = {}

    for _ in range(N):
        path = input().split()[1:] # 경로 정보
        add_to_tree(tree, path)

    # 출력 처리
    print_tree(tree)