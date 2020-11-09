# n = input("総数")
# i = input("組み合わせる数")
data = [1, 3, 4, 6, 7, 8]
n = len(data)
# ans = input("合計値")
ans = 13

# 組み合わせる数の数
combNum = 2

# for i in range(n - 2):
#     for j in range(1, n - 1):
#         for k in range(2, n):
#             if data[i] + data[j] + data[k] == ans:
#                 print(data[i], data[j], data[k])


def combinationTest(combination, depth):
    if depth == combNum + 1:
        sumNum = 0
        for i in combination:
            sumNum += data[i]
        if sumNum == ans:
            for i in combination:
                print("ans", data[i])
            print()
    else:
        s = max(combination) if combination else 0
        for i in range(s + 1, n - (combNum - depth)):
            combinationTest(combination + [i], depth + 1)

combinationTest([], 1)

print("Done")
