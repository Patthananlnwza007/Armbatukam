hour = int(input("กรุณาใส่จำนวนชั่วโมง: "))
minute = int(input("กรุณาใส่นาที: "))

if hour < 0 or minute < 0:
    print("โปรดใส่ข้อมูลที่ไม่ติดลบ")
else:
    # ถ้ามีนาทีเกิน 0 ให้นับเป็นชั่วโมงเพิ่มอีก 1
    if minute > 0:
        hour += 1
    
    # ชั่วโมงแรกจอดฟรี
    if hour <= 1:
        fee = 0
    else:
        fee = (hour - 1) * 30
    
    print(f"ค่าจอดรถ {fee} บาท")
*-------------------------------------------------*
def calculate_operations():
    try:
        m = int(input("กรอกตัวเลขตัวที่ 1: "))
        n = int(input("กรอกตัวเลขตัวที่ 2: "))

        print("ผลบวก =", m + n)
        print("ผลลบ =", m - n)
        print("ผลคูณ =", m * n)

        if n != 0:
            print("ผลหาร =", m / n)
        else:
            print("ไม่สามารถหารด้วยศูนย์ได้")

    except ValueError:
        print("โปรดใส่ข้อมูลที่เป็นตัวเลขจำนวนเต็มเท่านั้น")

# เรียกใช้งานฟังก์ชัน
calculate_operations()
-------------------------------------------
# รับค่า a และ b จากผู้ใช้
a = int(input("กรอกค่า a: "))
b = int(input("กรอกค่า b: "))

# สลับค่า
a, b = b, a

# แสดงผลลัพธ์หลังสลับ
print("a =", a)
print("b =", b)
-----------------------------------------
i = 0
while i <= 100:
    print(i)
    i += 1
  ---------------------------------------
i = 1000
while i >= 0:
    print(i)
    i -= 1
*--------------------------------------------------------------------------------*
min_value = None

while True:
    user_input = input("กรอกจำนวนจริง (หรือหยุดด้วยค่าที่ไม่ใช่จำนวน): ")
    try:
        num = float(user_input)
        if min_value is None or num < min_value:
            min_value = num
    except ValueError:
        break

if min_value is not None:
    print("ค่าที่น้อยที่สุดคือ:", min_value)
else:
    print("ไม่มีจำนวนจริงที่รับเข้ามาเลย")
*--------------------------------------------------------------------------------*
scores = []
i = 0

while i < 5:
    try:
        score = float(input(f"กรอกคะแนนตัวที่ {i+1}: "))
        scores.append(score)
        i += 1
    except ValueError:
        print("โปรดกรอกตัวเลขเท่านั้น")

average = sum(scores) / len(scores)
print("ค่าเฉลี่ยของคะแนนทั้งหมดคือ:", average)
