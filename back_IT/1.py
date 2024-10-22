
import heapq
def solution(N, A):
    def can_join(a, b):
        w = a + b
        return (w // 2 == a and (w + 1) // 2 == b) or ((w + 1) // 2 == a and w // 2 == b)
    pq = A.copy()
    heapq.heapify(pq)  # 최소 힙으로 변환
    while len(pq) > 1:
        a = heapq.heappop(pq)
        b = heapq.heappop(pq)

        if not can_join(a, b):
            return "false"

        heapq.heappush(pq, a + b)
    return "true"