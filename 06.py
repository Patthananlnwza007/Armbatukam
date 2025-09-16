def add_numbers(a, b):
    """
    ฟังก์ชันสำหรับบวกเลข 2 ตัว
    """
    return a + b

# ตัวอย่างการเรียกใช้งานฟังก์ชัน
result = add_numbers(5, 10)
print(f"ผลบวกของ 5 และ 10 คือ: {result}")
*---------------------------------------------------*
def square_number(a):
    """
    ฟังก์ชันสำหรับยกกำลังสอง
    """
    return a ** 2

# ตัวอย่างการเรียกใช้งานฟังก์ชัน
result = square_number(7)
print(f"ผลลัพธ์ของการยกกำลังสองของ 7 คือ: {result}")
*----------------------------------------------------*
def get_month_name(month_number):
    """
    ฟังก์ชันสำหรับแสดงชื่อเดือนจากเลขที่
    """
    month_names = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]
    
    # ตรวจสอบว่าเลขเดือนที่รับมาถูกต้องหรือไม่
    if 1 <= month_number <= 12:
        return month_names[month_number - 1]
    else:
        return "Invalid month number"

# ตัวอย่างการเรียกใช้งานฟังก์ชัน
month = get_month_name(5)
print(f"เดือนที่ 5 คือ: {month}")

month = get_month_name(15)
print(f"เดือนที่ 15 คือ: {month}")
*----------------------------------------------------*
def concatenate_strings(str1, str2, str3):
    """
    ฟังก์ชันสำหรับต่อสายอักขระ 3 สาย
    """
    return str1 + str2 + str3

# ตัวอย่างการเรียกใช้งานฟังก์ชัน
full_string = concatenate_strings("Hello, ", "World!", " How are you?")
print(f"สายอักขระที่ต่อกันคือ: {full_string}")
*------------------------------------------------------------*
def calculate_discount_price(price, discount_percent):
    """
    ฟังก์ชันสำหรับคำนวณราคาหลังหักส่วนลด
    """
    discount_amount = price * (discount_percent / 100)
    final_price = price - discount_amount
    return final_price

# ตัวอย่างการเรียกใช้งานฟังก์ชัน
original_price = 1000
discount = 20
final_price = calculate_discount_price(original_price, discount)
print(f"ราคาสินค้าเดิม: {original_price} บาท")
print(f"ส่วนลด: {discount}%")
print(f"ราคาหลังหักส่วนลด: {final_price} บาท")
