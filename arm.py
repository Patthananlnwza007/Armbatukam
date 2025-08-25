
import tkinter as tk

def countdown(seconds):
    """
    ฟังก์ชันสำหรับนับถอยหลังและแสดงผลบน Label
    """
    if seconds > 0:
        # แสดงตัวเลขที่นับถอยหลัง
        label_countdown.config(text=f"กำลังนับถอยหลัง: {seconds} วินาที")
        # เรียกฟังก์ชัน countdown อีกครั้งหลังจาก 1 วินาที (1000 มิลลิวินาที)
        root.after(1000, countdown, seconds - 1)
    else:
        # เมื่อนับถอยหลังครบแล้ว ให้แสดงข้อมูลส่วนตัว
        label_countdown.config(text="นับถอยหลังเสร็จสิ้น!")
        show_info()

def show_info():
    """
    ฟังก์ชันสำหรับแสดงข้อมูลส่วนตัว
    """
    info = [
        "ชื่อ - นามสกุล: พัทธนันท์ ประยูร",
        "ชื่อเล่น: อาร์ม",
        "ห้องเรียน: 5/8",
        "แผนการเรียน: วิทยาศาสตร์ - คณิตศาสตร์",
        "อยากเรียนคณะอะไร: คณะวิทยาศาสตร์"
    ]
    # แสดงข้อมูลแต่ละบรรทัดบน Label
    for i, item in enumerate(info):
        label_info = tk.Label(root, text=item, font=("Helvetica", 12))
        label_info.pack(pady=5)

# สร้างหน้าต่างหลักของโปรแกรม
root = tk.Tk()
root.title("นับถอยหลังและแสดงข้อมูล")

# สร้าง Label สำหรับแสดงตัวเลขนับถอยหลัง
label_countdown = tk.Label(root, text="กำลังจะเริ่มนับถอยหลัง...", font=("Helvetica", 16))
label_countdown.pack(pady=20)

# เริ่มต้นการนับถอยหลังที่ 10 วินาที
root.after(100, countdown, 10)

# เริ่มการทำงานของโปรแกรม
root.mainloop()
