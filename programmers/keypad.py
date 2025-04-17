def solution(numbers, hand):
    keypad = {
        1: (0, 0), 2: (0, 1), 3: (0, 2),
        4: (1, 0), 5: (1, 1), 6: (1, 2),
        7: (2, 0), 8: (2, 1), 9: (2, 2),
        '*': (3, 0), 0: (3, 1), '#': (3, 2)
    }

    result = ""

    left, right = "*", "#"
    for number in numbers:
        if number in [1, 4, 7]:
            result += "L"
            left = number
        elif number in [3, 6, 9]:
            result += "R"
            right = number
        else:
            left_dist = abs(keypad[number][0] - keypad[left][0]) + abs(keypad[number][1] - keypad[left][1])
            right_dist = abs(keypad[number][0] - keypad[right][0]) + abs(keypad[number][1] - keypad[right][1])

            # 1. 왼손이 더 가까운 경우
            if left_dist < right_dist:
                result += "L"
                left = number
            # 2. 오른손이 더 가까운 경우
            elif left_dist > right_dist:
                result += "R"
                right = number
            # 3. 양손의 거리가 같은 경우
            else:
                if hand == "left":
                    result += "L"
                    left = number
                else:
                    result += "R"
                    right = number

    return result