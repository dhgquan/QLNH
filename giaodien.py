from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
import tkinter

from utils import (
    safe_input,
    get_products,
    get_employees,
    get_sales
)

from actions import (
    register_sale,
    register_product_arrival,
    query_inventory_data,
    employees_with_most_sales,
    most_sold_items
)


windown = Tk()
windown.geometry()
windown.title("Quản lí nhà hàng")

lbl= tkinter.Label(windown, text="Chọn hành động", fg = "blue", font=("Arial", 32))
lbl.grid(column=0, row=1)

def handleButton():
    windown = Tk()
    windown.geometry()
    windown.title("Bán hàng")
    lbl = tkinter.Label(windown, text="Nhân viên bán hàng", fg="blue", font=("Arial", 32))
    lbl.grid(column=0, row=1)
    txt = Entry(windown, width=20)
    txt.grid()
    BT = Button(windown, text="Đăng nhập",command=DN)
    BT.grid()
    return

def DN():
    windown = Tk()
    windown.geometry()
    windown.title("Bán hàng")
    lbl = tkinter.Label(windown, text="Món ăn", fg="red")
    lbl.grid(column=0, row=4)
    combo = Combobox(windown)
    combo['values']=("Cà phê đen","Cà phê sữa","Bánh mì","Sinh tố","Pizza")
    combo.current()
    combo.grid(column=1,row=4)
    lbl = tkinter.Label(windown, text="Số lượng", fg="red")
    lbl.grid(column=0, row=6)
    txt = Entry(windown, width=22)
    txt.grid(column=1,row=6)
    BT = Button(windown, text="Đặt món",command=DM)
    BT.grid(column=2,row=10)
    return

def DM():
    messagebox.showinfo("Thong bao","Thanh cong")

def handleButton2():
    windown = Tk()
    windown.geometry("600x400")
    windown.title("Thêm món")
    lbl = tkinter.Label(windown, text="Món ăn", fg="red")
    lbl.grid(column=0, row=4)
    combo = Combobox(windown)
    combo['values'] = ("Cà phê đen", "Cà phê sữa", "Bánh mì", "Sinh tố", "Pizza")
    combo.current()
    combo.grid(column=1, row=4)
    lbl = tkinter.Label(windown, text="Số lượng", fg="red")
    lbl.grid(column=0, row=6)
    txt = Entry(windown, width=22)
    txt.grid(column=1, row=6)
    BT = Button(windown, text="Thêm")
    BT.grid(column=2, row=10)
    return

def handleButton3():
    windown = Tk()
    windown.geometry("600x400")
    windown.title("Xem món")
    lbl = tkinter.Label(windown, text="Món ăn", fg="red")
    lbl.grid(column=0, row=4)
    combo = Combobox(windown)
    combo['values'] = ("Cà phê đen", "Cà phê sữa", "Bánh mì", "Sinh tố", "Pizza")
    combo.current()
    combo.grid(column=1, row=4)
    return

def handleButton4():
    windown = Tk()
    windown.geometry("600x400")
    windown.title("Năng suát bán hàng")
    return

BT = Button(windown, text="Bán hàng", command=handleButton)
BT.grid()

BT2 = Button(windown, text="Thêm món", command=handleButton2)
BT2.grid()

BT3 = Button(windown, text="Xem món", command=handleButton3)
BT3.grid()

BT4 = Button(windown, text="Năng suát bán hàng", command=handleButton4)
BT4.grid()

windown.mainloop()