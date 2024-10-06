def quadtree(x, arrlist):
    s = 0
    for l in arrlist:
        s += sum(l)

    if s == x ** 2:
        return '1'
    if s == 0:
        return '0'

    half = x // 2
    temp = '('
    temp += quadtree(half, [l[:half] for l in arrlist[:half]])
    temp += quadtree(half, [l[:half] for l in arrlist[half:]])
    temp += quadtree(half, [l[half:] for l in arrlist[:half]])
    temp += quadtree(half, [l[half:] for l in arrlist[half:]])
    temp += ')'

    return temp


if __name__ == "__main__":
    n = int(input())
    arr = [list(map(int, input())) for _ in range(n)]

    print(quadtree(n, arr))
