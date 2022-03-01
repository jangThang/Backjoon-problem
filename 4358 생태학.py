import sys

#입력
tree = sys.stdin.read().rstrip().split('\n')
tree_dict = dict()
for i in tree:
    #사전에 있는 나무라면 +1
    if i in tree_dict:
        tree_dict[i] += 1
    #사전에 없다면 새로 추가
    else:
        tree_dict[i] = 1

#출력
for name, num in sorted(tree_dict.items()):
    print(f"{name} {(num*100/len(tree)):.4f}")
