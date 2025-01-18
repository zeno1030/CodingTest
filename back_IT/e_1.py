def decrypt_cipher(ciphertext, mappings):
    # 매핑 정보를 딕셔너리로 변환
    match_dict = {key: value for key, value in mappings}
    print(match_dict)

    def decode_char(char):
        visited = set()  # 방문한 문자 추적
        while char in match_dict:
            print(char)
            if char in visited:  # 무한 루프 탐지
                return '?'  # 무한 루프 발생 시 '?' 반환
            visited.add(char)
            char = match_dict[char]
        return char

    # 암호문의 각 문자를 변환
    decoded_text = ''.join(decode_char(char) if char != ' ' else ' ' for char in ciphertext)
    return decoded_text

# 입력 처리
ciphertext = input().strip()  # 암호문 입력
n = int(input().strip())  # 매핑 개수 입력
mappings = [input().split() for _ in range(n)]  # 매핑 정보 입력

# 복호화 실행 및 결과 출력
result = decrypt_cipher(ciphertext, mappings)
print(result)