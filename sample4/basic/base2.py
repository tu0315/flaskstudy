# 変数の応用

animal = "dog"
動物 = "cat"
print(動物)

# 定数

LEGAL_AGE = 18
age = int(input("年齢は？"))
print(age)

if age < LEGAL_AGE:  # ageが18より小さいときに処理を実行
    print("未成年")
else:
    print("成人")

# format文
print(f"age = {age}")  # 3.6
print(f"{age=}")  # 3.8
