from collections import deque

def solution(priorities, location):
    # 큐에 (우선순위, 인덱스) 튜플을 저장
    queue = deque([(priority, idx) for idx, priority in enumerate(priorities)])
    order = 0  # 실행 순서

    while queue:
        current = queue.popleft()  # 큐에서 프로세스 꺼내기
        # 큐에 현재 프로세스보다 우선순위가 높은 프로세스가 있는지 확인
        if any(current[0] < item[0] for item in queue):
            queue.append(current)  # 있다면 다시 큐에 넣기
        else:
            order += 1  # 없다면 실행 순서 증가
            if current[1] == location:  # 찾고자 하는 프로세스인지 확인
                return order