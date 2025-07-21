
chest = float(input("กรุณากรอกขนาดหน้าอก (นิ้ว): "))

if chest <= 34:
    print("ได้เสื้อขนาด XS")
elif chest <= 36:
    print("ได้เสื้อขนาด S")
elif chest <= 38:
    print("ได้เสื้อขนาด M")
elif chest <= 40:
    print("ได้เสื้อขนาด L")
else:
    print("ได้เสื้อขนาด XL")
*------------------------------*
income = float(input("กรุณากรอกรายได้ต่อเดือน (บาท): "))

if income < 15000:
    print("รายได้ไม่ถึงเกณฑ์สำหรับสมัครบัตรเครดิต")
elif income < 30000:
    print("ผ่านเกณฑ์ แต่ยังไม่มีคะแนนเครดิต")
elif income < 90000:
    print("คุณได้รับบัตรเครดิตประเภท เงิน")
elif income < 100000:
    print("คุณได้รับบัตรเครดิตประเภท ทอง")
else:
    print("คุณได้รับบัตรเครดิตประเภท Platinum")
*------------------------------*
score = float(input("กรุณากรอกคะแนน (0-100): "))

if score >= 80:
    print("เกรด A")
elif score >= 70:
    print("เกรด B")
elif score >= 60:
    print("เกรด C")
elif score >= 50:
    print("เกรด D")
else:
    print("เกรด F")
*------------------------------*
username = input("Username: ")
password = input("Password: ")

if username == "admin" and password == "Ad13n@23t":
    print("Welcome, admin")
else:
    print("You are not admin")
