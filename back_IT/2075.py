import heapq

if __name__ == "__main__":
    N = int(input())
    # 최소 힙을 사용해서 가장 큰 5개의 수만 유지
    heap = []

    for _ in range(N):
        # 한 줄씩 처리
        row = map(int, input().split())
        for num in row:
            if len(heap) < N:
                heapq.heappush(heap, num)
            else:
                if heap[0] < num:
                    heapq.heapreplace(heap, num)

    # heap[0]가 5번째로 큰 수
    print(heap[0])