if __name__ == "__main__":
    word = input().upper()
    word_list = list(set(word))
    count = []

    for i in word_list:
        cnt = word.count(i)
        count.append(cnt)
    if count.count(max(count)) > 1:
        print("?")
    else:
        print(word_list[(count.index(max(count)))])


