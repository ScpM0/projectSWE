from tkinter import* 
import tkinter as tk
from tkinter import ttk  
from database import Database 
from tkinter import messagebox
# =================================================


root=Tk()  # إنشاء نافذة التطبيق الرئيسية
root.geometry("360x615")  # تعيي أبعاد النافذة
root.title("Employee management")  # تعيين عنوان النافذة
root.configure(bg="#003049") #تعيين لون الخلفية
root.iconbitmap(False,'Icons\\teamwork.ico') # تعيين ايقون للبرنامج
root.resizable(False,False) #(1300x515) تثبيت الحجم وعدم جعله يصغر او يكبر عن 
# =======================================================


# ==================================================

database = Database("employee.db") #اعداد قاعدة بيانات

# تعريف المتغيرات الخاصة بالحقول
name = StringVar()
age = StringVar()
gender = StringVar()
job = StringVar()
phone = StringVar()


# ===============Create Frame ============

inputsFrame = Frame(root, background='#003049') # تعيين مساحة معينه لاضافة المدخلات والازرار
inputsFrame.place(x=1, y=1, width=360, height=615) # تعيين ابعاد المساحة
title = Label(inputsFrame, text='Employee SYS', font=('Calibri', 18, 'bold'), bg="#003049", fg='white') # تسمية المساحة
title.place(x=100, y=1) # ادراج الاسم في الفريم

# ===============field Name=============

lblName = Label(inputsFrame, text='Name', font=('Calibri', 16), bg="#003049", fg='white')
lblName.place(x=15, y=50)# ادراج الاسم الحقل في الفريم
inputName = Entry(inputsFrame, textvariable=name, width=20, font=('Calibri', 16))
inputName.place(x=75, y=50)  # وضع حقل الإدخال في الشبكة

# ===============field Gender=============

lblGender = Label(inputsFrame, text='Gender', font=('Calibri', 16), bg="#003049", fg='white')
lblGender.place(x=10, y=100)
boxGender = ttk.Combobox(inputsFrame, state="readonly", textvariable=gender, width=18, font=('Calibri', 16))
boxGender['values'] = ("Male", "Female")
boxGender.place(x=80, y=100)

# ===============field Job=============

lblJob = Label(inputsFrame, text='Job', font=('Calibri', 16), bg="#003049", fg='white')
lblJob.place(x=15, y=150)
inputJob = Entry(inputsFrame, textvariable=job, width=20, font=('Calibri', 16))
inputJob.place(x=75, y=150)

# ===============field Age=============

lblAge = Label(inputsFrame, text='Age', font=('Calibri', 16), bg="#003049", fg='white')
lblAge.place(x=15, y=200)
inputAge = Entry(inputsFrame, textvariable=age, width=20, font=('Calibri', 16))
inputAge.place(x=75, y=200)

# ===============field Phone=============
lblPhone = Label(inputsFrame, text='Phone', font=('Calibri', 16), bg="#003049", fg='white')
lblPhone.place(x=15, y=250)
inputPhone = Entry(inputsFrame, textvariable=phone, width=20, font=('Calibri', 16))
inputPhone.place(x=75, y=250)


# ============field Address===============
lblAddress = Label(inputsFrame, text='Address:', font=('Calibri', 16), bg="#003049", fg='white')
lblAddress.place(x=15, y=350)
inputAddress = Text(inputsFrame, width=20, height=1.5, font=('Calibri', 16))
inputAddress.place(x=75, y=380)
# ===============================================================================



# ===========Buttons(AddData/UpdataData/RemoveData/ClearData)===========
# ==========Create Label Button=======
btnFrame = Frame(inputsFrame, bg='#003049', border=1, relief=SOLID)
btnFrame.place(x=20, y=450, width=300, height=160)

# ===========Functions Buttons================
# =========Functions Hide/Show TreeView=======
def Hide():
    root.geometry("360x615")

def Show():
    root.geometry("1300x615")
# =============================================
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
    if inputName.get() == "" or inputAge.get() == "" or inputJob.get() == "" or inputAddress.get(1.0, END) == "" or inputPhone.get() == "" or boxGender.get() == "" :
        messagebox.showerror("Error", "Please fill in the blank field")
        return
    database.update(row[0],
                    inputName.get(),
                    inputAge.get(),
                    inputJob.get(),
                    boxGender.get(),
                    inputAddress.get(1.0, END),
                    inputPhone.get(),
                    )
    messagebox.showinfo("Success", "Data updated")
    clear()
    displayAll()


# دالة لإضافة موظف جديد
def addEmployee():
    if inputName.get() == "" or inputAge.get() == "" or inputJob.get() == "" or inputAddress.get(1.0, END) == "" or inputPhone.get() == "" or boxGender.get() == "" :
        messagebox.showerror("Error", "Please fill in the blank field")
        return
    database.insert(
        inputName.get(),
        inputAge.get(),
        inputJob.get(),
        boxGender.get(),
        inputAddress.get(1.0, END),
        inputPhone.get(),
    )
    messagebox.showinfo("Success", "Added new employee!")
    clear()
    displayAll()

def searchWindow():
    # إنشاء نافذة جديدة
    searchWin = Toplevel(root)
    searchWin.geometry("800x400")
    searchWin.title("Search Employee")
    searchWin.configure(bg="#003049")
    
    # تسمية حقل البحث
    searchLabel = Label(searchWin, text="Enter Name or Phone to Search", font=('Calibri', 16), bg="#003049", fg='white')
    searchLabel.pack(pady=20)

    # حقل الإدخال للبحث
    searchEntry = Entry(searchWin, font=('Calibri', 16))
    searchEntry.pack(pady=10, padx=20, fill='x')

    # دالة للبحث عند الضغط على زر البحث
    def searchData():
        searchText = searchEntry.get()
        if searchText != "":
            # البحث في قاعدة البيانات
            results = database.search(searchText)  # إضافة دالة search في قاعدة البيانات
            if results:
                # مسح أي نتائج سابقة في جدول Treeview
                for row in show.get_children():
                    show.delete(row)
                
                # عرض نتائج البحث في Treeview
                for row in results:
                    show.insert("", END, values=row)
            else:
                messagebox.showinfo("No Results", "No employees found.")
        else:
            messagebox.showerror("Error", "Please enter something to search.")
    
    # زر البحث
    searchButton = Button(searchWin, text="Search", font=('Calibri', 16), fg='white', bg='#386641', border=0, command=searchData)
    searchButton.place(x=350, y=120)  # وضع زر البحث باستخدام place

    # إنشاء Treeview لعرض النتائج
    treeFrame = Frame(searchWin)
    treeFrame.pack(pady=35, padx=10, fill='both', expand=True)
    
    style = ttk.Style()
    style.configure("mystyle.Treeview", font=('Calibri', 12), rowheight=30, background="#14213d", foreground="#e5e5e5")
    style.configure("mystyle.Treeview.Heading", font=('Calibri', 12))

    show = ttk.Treeview(treeFrame, columns=(1, 2, 3, 4, 5, 6, 7), style="mystyle.Treeview")
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
    show.column("6", width=240)
    show.heading("7", text="Phone")
    show.column("7", width=160)
    show['show'] = 'headings'
    show.pack(fill='both', expand=True)



# ===============================================================================

# أزرار التحكم في البيانات
btnAdd = Button(btnFrame, text='Add Data', width=12, height=1, font=('Calibri', 16), fg='white', bg='#386641', border=0, command=addEmployee)
btnAdd.place(x=2, y=3)
btnDel = Button(btnFrame, text='Delete Data', width=12, height=1, font=('Calibri', 16), fg='white', bg='#e63946', border=0, command=delete)
btnDel.place(x=155, y=3)
btnUpdata = Button(btnFrame, text='Updata Data', width=12, height=1, font=('Calibri', 16), fg='white', bg='#ffc300', border=0, command=updata)
btnUpdata.place(x=2, y=50)
btnClear = Button(btnFrame, text='Clear Data', width=12, height=1, font=('Calibri', 16), fg='white', bg='#0077b6', border=0, command=clear)
btnClear.place(x=155, y=50)
# أزرار التحكم في البيانات
btnSearch = Button(btnFrame, text="Search", width=12, height=1, font=('Calibri', 16), fg='white', cursor='hand2', bg='#22577a', border=0, command=searchWindow)
btnSearch.place(x=90, y=100)

# ======================================================================

# ==========Buttons(Hide TreeView/ Show TreeView)=======================
btnHide = Button(inputsFrame, text="HIDE", command=Hide, fg='white', cursor='hand2', bg='#e63946', border=0)
btnHide.place(x=270, y=10)
btnShow = Button(inputsFrame, text="SHOW", command=Show, fg='white', cursor='hand2', bg='#386641', border=0)
btnShow.place(x=30, y=10)


# ==========Table Frame=============
tableFrame = Frame(root, background='white')

tableFrame.pack(fill='both', expand=True)
tableFrame.place(x=370, y=1, width=940, height=605)  # قلل الارتفاع قليلاً



style = ttk.Style()
style.configure("mystyle.Treeview", font=('Calibri', 12), rowheight=50,background="#14213d", foreground="#e5e5e5")
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
show.place(x=0.5,y=0.5,height=620)
show.bind("<ButtonRelease-1>", getData)

# عرض جميع البيانات عند بدء التشغيل
displayAll()

# بدء حلقة تشغيل البرنامج
root.mainloop()

root.mainloop()  # بدء الحلقة الرئيسية لتشغيل التطبيق
