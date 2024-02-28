import math

G = 6.67408E-11

# 화성
# name = "화성"
# M = 6.42E23
# r = 3396.2 * 1000
# V = math.sqrt(2 * G * M / r)
# print(f"{name}의 탈출 속도: {V}")
print("화성의 탈출 속도:", math.sqrt(2 * 6.67408E-11 * 6.42E23 / (3396.2 * 1000)))
name = "달"
M = 7.3E22
r = 1737.5 * 1000
V = math.sqrt(2 * G * M / r)
print(f"{name}의 탈출 속도: {V}")