
# 定義一個函數來計算BMI
def calculate_bmi(height, weight):
    height_m = height / 100  # 將身高轉換為公尺
    bmi = weight / (height_m ** 2)  # 計算BMI
    return bmi

# 輸入身高和體重
height = float(input("請輸入您的身高（公分）："))
weight = float(input("請輸入您的體重（公斤）："))

# 計算BMI
bmi = calculate_bmi(height, weight)

# 輸出BMI
print("您的BMI是：", bmi)