if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        n, k, t, m = map(int, input().split())
        # 가로 팀id, 세로 문제 번호
        matrix = [[0 for _ in range(n + 1)] for _ in range(k + 1)]
        team_count = [0 for _ in range(n + 1)]
        time = [0 for _ in range(n + 1)]
        answer = []
        for i in range(m):
            t_i, q_i, score = map(int, input().split())
            team_count[t_i] += 1
            time[t_i] = i
            if matrix[t_i][q_i] <= score:
                matrix[t_i][q_i] = score
        for i in range(1, n + 1):
            score_sum = sum(matrix[i])
            answer.append((i, score_sum))

        print(team_count)
        print(answer)




