def solution(distance, rocks, n):
    rocks.sort()
    rocks.append(distance)

    left, right = 1, distance
    answer = 0

    while left <= right:
        mid = (left + right) // 2
        current = 0
        removed = 0
        min_distance = float('inf')

        for rock in rocks:
            if rock - current < mid:
                removed += 1
            else:
                min_distance = min(min_distance, rock - current)
                current = rock

        if removed > n:
            right = mid - 1
        else:
            answer = max(answer, min_distance)
            left = mid + 1
    return answer