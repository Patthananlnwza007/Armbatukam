
import random

target = 85

for i in range(0, 101):
    if i == target:
        print(f"เจอเป้าหมายแล้วคือ {i}")
        break
    elif i < target:
        print(f"{i} ยังไม่ใช่เป้าหมาย")
    else:
        print("เลยเป้าหมายแล้ว")
*-------------*
students = ["ชื่อนักเรียน1", "ชื่อนักเรียน2", "ชื่อนักเรียน3", ..., "ชื่อนักเรียน39"]

for name in students:
    print(f"รายชื่อ: {name}")
*-------------*
# 1. ลำดับเลขคี่ 1, 3, 5, ..., 21
i = 1
while i <= 21:
    print(i, end=", ")
    i += 2
# 2. ลำดับเลข 2, 2.5, 8, 11.3, 13, 14, 17 (ใช้ list)
lst = [2, 2.5, 8, 11.3, 13, 14, 17]
i = 0
while i < len(lst):
    print(lst[i], end=", ")
    i += 1
# 3. 100, 90, 80, ..., -100 (ลดลงทีละ 10)
i = 100
while i >= -100:
    print(i, end=", ")
    i -= 10
# 4. -30, -20, -10, 0, 10, 20, 30
i = -30
while i <= 30:
    print(i, end=", ")
    i += 10
# 5. 15, 23, 31, 39, 47, 55
i = 15
while i <= 55:
    print(i, end=", ")
    i += 8
*-------------*
num = int(input("กรุณาใส่เลขที่ต้องการดูสูตรคูณ: "))

for i in range(1, 13):
    print(f"{num} x {i} = {num * i}")
