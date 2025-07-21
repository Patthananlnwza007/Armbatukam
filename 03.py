products = {
    "1. หมูสับกิโล": 150.00,
    "2. เนื้ออกไก่": 105.00,
    "3. ไก่บ้าน": 120.00,
    "4. มาม่าต้มยำ": 6.50,
    "5. หัวหอม": 15.00,
    "6. ข้าวสาร": 35.00,
    "7. น้ำปลา": 10.00,
    "8. ซอสหอยนางรม": 18.00,
    "9. ยาสระผม": 120.00,
    "10. ไข่ไก่": 120.25,
    "11. ผักชี": 21.50,
    "12. เป๊ปซี่": 20.50,
    "13. กาแฟ": 15.75,
    "14. หมูปิ้งเสียบไม้": 19.00,
    "15. ชาไทย": 17.50,
    "16. น้ำเปล่า": 10.00
}

print("งบประมาณ: 1000 บาท\n")
print("รายการสินค้า:")
for key, value in products.items():
    print(f"{key} - {value:.2f} บาท")

total = 0
print("\nกรุณาเลือกสินค้าจำนวน 5 รายการ (ใส่หมายเลข):")
for i in range(5):
    choice = input(f"เลือกสินค้าหมายเลขที่ {i+1}: ")
    item = list(products.items())[int(choice)-1]
    total += item[1]

print(f"\nยอดรวมที่ซื้อ: {total:.2f} บาท")
if total > 1000:
    print("เกินงบ 1000 บาท!")
else:
    print(f"เหลือเงิน: {1000 - total:.2f} บาท")
*----------------------------------------------*
# รับค่าความถี่สัมพัทธ์ และจำนวนกลุ่ม
relative_frequency = float(input("กรุณากรอกความถี่สัมพัทธ์ (เช่น 0.25): "))
classes = float(input("กรุณากรอกจำนวนกลุ่ม: "))

result = relative_frequency * classes
print(f"ผลลัพธ์ = {result}")

# กำหนดเซต a และ b
a = {10, 20, 30, 40, 50, 60}
b = {30, 40, 50, 60, 70, 80}
*----------------------------------------------*
celsius = float(input("กรุณากรอกอุณหภูมิ (องศาเซลเซียส): "))

fahrenheit = (9/5) * celsius + 32
kelvin = celsius + 273.15
*----------------------------------------------*
print(f"แปลงเป็นฟาเรนไฮต์: {fahrenheit:.2f} °F")
print(f"แปลงเป็นเคลวิน: {kelvin:.2f} K")

# 1. Union (ผลรวมของสมาชิกทั้งหมดใน a และ b)
result_union = a | b
print("ผลลัพธ์ของ a | b =", result_union)

# 2. Intersection (ค่าที่มีในทั้ง a และ b)
result_intersection = a & b
print("ผลลัพธ์ของ a & b =", result_intersection)

# 3. Difference (ค่าที่มีใน a แต่ไม่มีใน b)
result_difference = a - b
print("ผลลัพธ์ของ a - b =", result_difference)

# 4. Symmetric Difference (ค่าที่ไม่ซ้ำกันใน a และ b)
result_sym_diff = a ^ b
print("ผลลัพธ์ของ a ^ b =", result_sym_diff)
