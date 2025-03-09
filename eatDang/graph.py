import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.font_manager as fm

# 한글 폰트 설정
plt.rc('font', family='AppleGothic')  # Mac 사용자의 경우
plt.rc('axes', unicode_minus=False)  # 마이너스 기호 깨짐 방지

# 가상의 데이터 (PDF에서 추출한 내용을 기반으로 재구성)
age_groups = ["일부 제로 식품을 선호한다.", "가능하면 항상 제로 식품만 먹는다.", "관심 없다.(상관없이 먹는다.)","저당 식품 아주 드물게 먹음 ", "제로/저당식품을 먹지 않는다."]
zero_sugar_preference = [44.44, 27.78, 23.61, 1.39, 2.78]  # 일부 제로/저당 식품 선호 비율

exercise_types = ["주 1~2회", "주 3~4회", "주 5~6회", "매일","전혀 운동을 하지 않음"]
check_ingredients = [0, 100, 0, 0, 0]  # 성분 확인 비율



# 나이대별 저당/제로 식품 선호도 그래프
plt.figure(figsize=(15, 6))
sns.barplot(x=age_groups, y=zero_sugar_preference, palette="Blues")
plt.title("제로/저당 상품 선호도 별 성분 확인 비율 (%)")
plt.xlabel("상품 선호도")
plt.ylabel("성분 확인 비율  (%)")
plt.show()

# 운동 종류별 성분 확인 비율 그래프
plt.figure(figsize=(12, 6))
sns.barplot(x=exercise_types, y=check_ingredients, palette="Greens")
plt.title("운동 횟수별 선호도(아주 가끔) 비율 (%)")
plt.xlabel("운동 횟수")
plt.ylabel("선호도(아주 가끔) 비율 (%)")
plt.show()
