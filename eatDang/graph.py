import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.font_manager as fm

# 한글 폰트 설정
plt.rc('font', family='AppleGothic')  # Mac 사용자의 경우
plt.rc('axes', unicode_minus=False)  # 마이너스 기호 깨짐 방지

# 가상의 데이터 (PDF에서 추출한 내용을 기반으로 재구성)
age_groups = ["남", "여"]
zero_sugar_preference = [43.1, 56.9]  # 일부 제로/저당 식품 선호 비율
colors = ["#1f77b4", "#aec7e8"]


exercise_types = ["주 1~2회", "주 3~4회", "주 5~6회", "매일","전혀 운동을 하지 않음"]
check_ingredients = [0, 100, 0, 0, 0]  # 성분 확인 비율



# 나이대별 저당/제로 식품 선호도 그래프
plt.figure(figsize=(15, 6))
plt.pie(zero_sugar_preference, labels=age_groups, autopct="%1.1f%%", colors=colors, startangle=90, wedgeprops={'edgecolor': 'white', 'linewidth': 2})
plt.title("성별 별 선호도(일부) 비율 (%)")
plt.show()

# 운동 종류별 성분 확인 비율 그래프
plt.figure(figsize=(12, 6))
sns.barplot(x=exercise_types, y=check_ingredients, palette="Greens")
plt.title("운동 횟수별 선호도(아주 가끔) 비율 (%)")
plt.xlabel("운동 횟수")
plt.ylabel("선호도(아주 가끔) 비율 (%)")
plt.show()
