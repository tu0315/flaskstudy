# リスト
list_a = [1, 2, 3, 4]
# 空リスト
list_b = []

print(list_a)
# 後ろから2番目
print(list_a[-2])

list_a = [1, [1, 2, "apple"], 3, "banana"]

print(list_a[1][2])
print(list_a)
list_a[1][2] = "lemon"
print(list_a)
# 逆から
list_a.reverse()
print(list_a)

# リスト関数

list_a = [1, 2, 3, 4, 5]
list_b = list_a[:3]
# 3つまで表示
print(list_b)
# 0〜5までを1つ飛ばしで表示
print(list_a[0:5:2])

# append, extend, insert, clear
# リスト追加
list_a.append("apple")
print(list_a)
# 複数追加
list_a.extend(["banana", "lemon"])
print(list_a)
# 1番目に追加する
list_a.insert(1, "grape")
print(list_a)
# リストを空にする
list_a.clear()
print(list_a)

# remove, pop, count
list_a = [1, 2, 3, 4, 5]
# 3番目を削除する
list_a.remove(3)
print("3番目を削除する")
print(list_a)
# 1番目を削除する
value = list_a.pop(1)
print(list_a)
# リストの個数
print(value)
# 引数の数を表示する
print(list_a.count(1))
# print(list_a.index("banana"))

# copy
# list_b = list_a.copy()
# print(list_a)
# list_b[0]='AAAAA'
# print(list_a)

# sort reverse
# list_a = ['banana', 'lemon', 'apple', 'grape']
# print(list_a)
# list_a = sorted(list_a)
# list_a.reverse()
# print(list_a)
