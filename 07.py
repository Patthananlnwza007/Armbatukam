
import tkinter as tk
from tkinter import messagebox

def calculate_area():
    """
    ฟังก์ชันสำหรับคำนวณพื้นที่สามเหลี่ยม
    """
    try:
        base = float(entry_base.get())
        height = float(entry_height.get())
        
        area = 0.5 * base * height
        
        # แสดงผลลัพธ์ใน Label
        result_label.config(text=f"พื้นที่สามเหลี่ยมคือ: {area:.2f} ตารางหน่วย")
        
    except ValueError:
        # หากผู้ใช้กรอกข้อมูลที่ไม่ใช่ตัวเลข
        messagebox.showerror("ข้อผิดพลาด", "กรุณาป้อนข้อมูลเป็นตัวเลขเท่านั้น")

# สร้างหน้าต่างหลัก
window = tk.Tk()
window.title("โปรแกรมคำนวณพื้นที่สามเหลี่ยม")
window.geometry("400x250")

# สร้าง Label และ Entry สำหรับความยาวฐาน
label_base = tk.Label(window, text="ความยาวฐาน (Base):", font=("Helvetica", 12))
label_base.pack(pady=5)
entry_base = tk.Entry(window)
entry_base.pack(pady=5)

# สร้าง Label และ Entry สำหรับความสูง
label_height = tk.Label(window, text="ความสูง (Height):", font=("Helvetica", 12))
label_height.pack(pady=5)
entry_height = tk.Entry(window)
entry_height.pack(pady=5)

# สร้างปุ่มสำหรับคำนวณ
calculate_button = tk.Button(window, text="คำนวณพื้นที่", command=calculate_area)
calculate_button.pack(pady=10)

# สร้าง Label สำหรับแสดงผลลัพธ์
result_label = tk.Label(window, text="ผลลัพธ์จะแสดงที่นี่", font=("Helvetica", 14, "bold"))
result_label.pack(pady=10)

# เริ่มต้นการทำงานของโปรแกรม GUI
window.mainloop()
