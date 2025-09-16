
import tkinter as tk
from tkinter import messagebox

def show_info():
    """
    ฟังก์ชันที่จะถูกเรียกเมื่อปุ่มถูกคลิก
    แสดงกล่องข้อความที่มีข้อมูลส่วนตัว
    """
    my_name = "พัทธนัน์ ประยูร"
    my_class = "มัธยมศึกษาปีที่ 5"
    my_number = "9"
    
    info_message = f"ชื่อ: {my_name}\nชั้น: {my_class}\nเลขที่: {my_number}"
    
    # แสดงกล่องข้อความ
    messagebox.showinfo("ข้อมูลนักเรียน", info_message)

# สร้างหน้าต่างหลักของโปรแกรม
window = tk.Tk()
window.title("โปรแกรมแสดงข้อมูล")
window.geometry("300x150") # กำหนดขนาดของหน้าต่าง

# สร้างป้ายกำกับ (Label) เพื่อบอกให้ผู้ใช้กดปุ่ม
label = tk.Label(window, text="กดปุ่มด้านล่างเพื่อแสดงข้อมูล", font=("Helvetica", 12))
label.pack(pady=20)

# สร้างปุ่ม (Button) และกำหนดให้เมื่อกดแล้วให้เรียกฟังก์ชัน show_info
button = tk.Button(window, text="แสดงข้อมูล", command=show_info)
button.pack()

# เริ่มการทำงานของโปรแกรม GUI
window.mainloop()
