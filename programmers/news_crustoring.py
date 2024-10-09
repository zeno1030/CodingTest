def solution(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()

    # 문자 쌍을 저장할 리스트
    pairs1 = []
    pairs2 = []

    # 첫 번째 문자열의 문자 쌍 생성
    for i in range(len(str1) - 1):
        pair = str1[i:i + 2]
        if pair.isalpha():  # 알파벳 쌍만 추가
            pairs1.append(pair)

    # 두 번째 문자열의 문자 쌍 생성
    for i in range(len(str2) - 1):
        pair = str2[i:i + 2]
        if pair.isalpha():  # 알파벳 쌍만 추가
            pairs2.append(pair)

    # 쌍의 교집합과 합집합 계산
    intersection = 0
    union = len(pairs1) + len(pairs2)

    for pair in set(pairs1):
        if pair in pairs2:
            count1 = pairs1.count(pair)
            count2 = pairs2.count(pair)
            intersection += min(count1, count2)

    # 유사도 계산
    if union == 0:
        return 65536  # 두 문자열 모두 쌍이 없으면 65536 반환
    else:
        similarity_score = int((intersection / (union - intersection)) * 65536)
        return similarity_score
