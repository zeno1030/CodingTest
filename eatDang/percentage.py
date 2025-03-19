import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder

# CSV 파일 불러오기
file_path = '응답.csv'  # 파일 경로 설정
df = pd.read_csv(file_path)

# 컬럼명 공백 제거 (혹시 있을 수 있는 숨겨진 공백 처리)
df.columns = df.columns.str.strip()

# "성분확인" 컬럼에서 "확인하는 편이다." 정확히 필터링
filtered_df = df[df['제로/저당 식품을 선호하는 편인가요?'].str.strip() == '저당 식품 아주 드물게 먹음']

# "어떤 운동" 컬럼별 비율 계산
exercise_ratio = filtered_df['성별'].str.strip().value_counts(normalize=True) * 100

# 결과 출력
print('저당 식품 아주 드물게 먹음 라고 답한 사람들의 성별 비율:')
print(exercise_ratio)

# === 범주형 데이터를 수치화 (Label Encoding) ===
label_encoder = LabelEncoder()

# '성분확인'과 '어떤 운동' 컬럼 수치화
df['선호도_코드'] = label_encoder.fit_transform(df['제로/저당 식품을 선호하는 편인가요?'].str.strip())
df['성별_코드'] = label_encoder.fit_transform(df['성별'].str.strip())

# === 상관 관계수 계산 ===
correlation = df['선호도_코드'].corr(df['성별_코드'])
print('선호도(항상)과 성별 간 상관 관계수:', correlation)

