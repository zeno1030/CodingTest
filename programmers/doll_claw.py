from collections import defaultdict
from collections import deque


def solution(board, moves):
    answer = 0

    #   defaultdict로 몇 번칸에 무슨 인형 있는지 파악
    board_dict = defaultdict(deque)

    for toy in board:
        for i in range(len(toy)):
            if toy[i] != 0:
                board_dict[i + 1].append(toy[i])
    print(board_dict)

    #   moves를 통해 popleft를 하여 뽑은 인형 list에 넣는다.

    picked_up = []

    for i in moves:
        if len(board_dict[i]) == 0:
            continue
        else:
            current_toy = board_dict[i].popleft()
            if picked_up and picked_up[-1] == current_toy:
                picked_up.pop()
                answer += 2
            else:
                picked_up.append(current_toy)

    return answer
