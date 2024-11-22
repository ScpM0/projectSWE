from datetime import date
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from database import Database

# إنشاء الاتصال بقاعدة البيانات
database = Database("employee.db")

# إعداد نافذة التطبيق الرئيسية
root = Tk()
root.title("Employee Management System")
root.geometry("1300x515")
root.resizable(False, False)
root.configure(bg="#000814")

# تعريف المتغيرات الخاصة بالحقول
name = StringVar()
age = StringVar()
gender = StringVar()
job = StringVar()
phone = StringVar()

# ==========Frames==========
inputsFrame = Frame(root, background='#000814')
inputsFrame.place(x=1, y=1, width=360, height=515)

# إضافة العنوان وبعض الحقول
title = Label(inputsFrame, text='Employee SYS', font=('Calibri', 18, 'bold'), bg="#000814", fg='white')
title.place(x=100, y=1)

lblName = Label(inputsFrame, text='Name', font=('Calibri', 16), bg="#000814", fg='white')
lblName.place(x=15, y=50)
inputName = Entry(inputsFrame, textvariable=name, width=20, font=('Calibri', 16))
inputName.place(x=75, y=50)

lblJob = Label(inputsFrame, text='Job', font=('Calibri', 16), bg="#000814", fg='white')
lblJob.place(x=15, y=100)
inputJob = Entry(inputsFrame, textvariable=job, width=20, font=('Calibri', 16))
inputJob.place(x=75, y=100)

lblGender = Label(inputsFrame, text='Gender', font=('Calibri', 16), bg="#000814", fg='white')
lblGender.place(x=10, y=150)
boxGender = ttk.Combobox(inputsFrame, state="readonly", textvariable=gender, width=18, font=('Calibri', 16))
boxGender['values'] = ("Male", "Female")
boxGender.place(x=80, y=150)

lblAge = Label(inputsFrame, text='Age', font=('Calibri', 16), bg="#000814", fg='white')
lblAge.place(x=15, y=200)
inputAge = Entry(inputsFrame, textvariable=age, width=20, font=('Calibri', 16))
inputAge.place(x=75, y=200)

lblPhone = Label(inputsFrame, text='Phone', font=('Calibri', 16), bg="#000814", fg='white')
lblPhone.place(x=15, y=250)
inputPhone = Entry(inputsFrame, textvariable=phone, width=20, font=('Calibri', 16))
inputPhone.place(x=75, y=250)

lblAddress = Label(inputsFrame, text='Address:', font=('Calibri', 16), bg="#000814", fg='white')
lblAddress.place(x=15, y=300)
inputAddress = Text(inputsFrame, width=20, height=1.5, font=('Calibri', 16))
inputAddress.place(x=75, y=330)

# ========Function Show/Hide====
def Hide():
    root.geometry("360x515")


def Show():
    root.geometry("1300x515")


# دالة لجلب البيانات من الجدول
def getData(event):
    selectedRow = show.focus()
    info = show.item(selectedRow)
    global row
    row = info["values"]
    name.set(row[1])
    age.set(row[2])
    job.set(row[3])
    gender.set(row[4])
    inputAddress.delete(1.0, END)
    inputAddress.insert(END, row[5])
    phone.set(row[6])


# دالة لعرض جميع البيانات في الجدول
def displayAll():
    show.delete(*show.get_children())
    for row in database.fetch():
        show.insert("", END, values=row)


# دالة لمسح البيانات من الحقول
def clear():
    name.set("")
    age.set("")
    job.set("")
    phone.set("")
    gender.set("")
    inputAddress.delete(1.0, END)


# دالة لحذف بيانات الموظف
def delete():
    database.remove(row[0])
    clear()
    displayAll()


# دالة لتحديث بيانات الموظف
def updata():
    if inputName.get() == "" or inputAge.get() == "" or inputJob.get() == "" or inputAddress.get(1.0, END) == "" or inputPhone.get() == "" or boxGender.get() == "":
        messagebox.showerror("Error", "Please fill in the blank field")
        return
    database.update(row[0],
                    inputName.get(),
                    inputAge.get(),
                    inputJob.get(),
                    boxGender.get(),
                    inputAddress.get(1.0, END),
                    inputPhone.get()
                    )
    messagebox.showinfo("Success", "Data updated")
    clear()
    displayAll()


# دالة لإضافة موظف جديد
def addEmployee():
    if inputName.get() == "" or inputAge.get() == "" or inputJob.get() == "" or inputAddress.get(1.0, END) == "" or inputPhone.get() == "" or boxGender.get() == "":
        messagebox.showerror("Error", "Please fill in the blank field")
        return
    database.insert(
        inputName.get(),
        inputAge.get(),
        inputJob.get(),
        boxGender.get(),
        inputAddress.get(1.0, END),
        inputPhone.get()
    )
    messagebox.showinfo("Success", "Added new employee!")
    clear()
    displayAll()


# ====== إضافة أزرار إظهار/إخفاء ======
btnHide = Button(inputsFrame, text="HIDE", command=Hide, fg='white', cursor='hand2', bg='#e63946', border=0)
btnHide.place(x=270, y=10)
btnShow = Button(inputsFrame, text="SHOW", command=Show, fg='white', cursor='hand2', bg='#386641', border=0)
btnShow.place(x=30, y=10)

# ===========Buttons=============
btnFrame = Frame(inputsFrame, bg='#000814', border=1, relief=SOLID)
btnFrame.place(x=10, y=400, width=300, height=100)

# أزرار التحكم في البيانات
btnAdd = Button(btnFrame, text='Add Data', width=12, height=1, font=('Calibri', 16), fg='white', bg='#386641', border=0, command=addEmployee)
btnAdd.place(x=2, y=3)
btnDel = Button(btnFrame, text='Delete Data', width=12, height=1, font=('Calibri', 16), fg='white', bg='#e63946', border=0, command=delete)
btnDel.place(x=155, y=3)
btnUpdata = Button(btnFrame, text='Updata Data', width=12, height=1, font=('Calibri', 16), fg='white', bg='#ffc300', border=0, command=updata)
btnUpdata.place(x=2, y=50)
btnClear = Button(btnFrame, text='Clear Data', width=12, height=1, font=('Calibri', 16), fg='white', bg='#0077b6', border=0, command=clear)
btnClear.place(x=155, y=50)

# ==========Table Frame=============
tableFrame = Frame(root, background='white')
tableFrame.place(x=370, y=1, width=940, height=510)

style = ttk.Style()
style.configure("mystyle.Treeview", font=('Calibri', 12), rowheight=50)
style.configure("mystyle.Treeview.Heading", font=('Calibri', 12))

show = ttk.Treeview(tableFrame, columns=(1, 2, 3, 4, 5, 6, 7), style="mystyle.Treeview")
show.heading("1", text="ID")
show.column("1", width=40)
show.heading("2", text="Name")
show.column("2", width=180)
show.heading("3", text="Age")
show.column("3", width=40)
show.heading("4", text="Job")
show.column("4", width=160)
show.heading("5", text="Gender")
show.column("5", width=130)
show.heading("6", text="Address")
show.column("6", width=230)
show.heading("7", text="Phone")
show.column("7", width=160)

show['show'] = 'headings'
show.pack()
show.bind("<ButtonRelease-1>", getData)

# عرض جميع البيانات عند بدء التشغيل
displayAll()

# بدء حلقة تشغيل البرنامج
root.mainloop()
