import sqlite3

class Database:
    def __init__(self, data):
        # إنشاء اتصال بقاعدة البيانات وتهيئة المؤشر
        self.con = sqlite3.connect(data)
        self.cur = self.con.cursor()
        # إنشاء جدول إذا لم يكن موجودًا بالفعل
        sql = """
        CREATE TABLE IF NOT EXISTS employees (
        id INTEGER PRIMARY KEY,
        name TEXT,
        age TEXT,
        job TEXT,
        gender TEXT,
        address TEXT,
        phone TEXT
        )
        """
        self.cur.execute(sql)
        self.con.commit()  

    def insert(self, name, age, job, gender, address, phone):
        # إدراج بيانات موظف جديد في الجدول
        self.cur.execute("INSERT INTO employees VALUES (NULL, ?, ?, ?, ?, ?, ?)",
                         (name, age, job, gender, address, phone))
        self.con.commit()

    def fetch(self):
        # استرجاع جميع البيانات من الجدول
        self.cur.execute("SELECT * FROM employees")
        rows = self.cur.fetchall()
        return rows

    def remove(self, id):
        # حذف موظف من الجدول بناءً على المعرف (ID)
        self.cur.execute("DELETE FROM employees WHERE id=?", (id,))
        self.cur.execute("""
    WITH updated AS (
        SELECT id, ROW_NUMBER() OVER (ORDER BY id) AS new_id
        FROM employees
    )
    UPDATE employees
    SET id = updated.new_id
    FROM updated
    WHERE employees.id = updated.id;
    """)
        self.con.commit()

    def update(self, id, name, age, job, gender, address, phone):
        # تحديث بيانات موظف محدد في الجدول
        self.cur.execute("UPDATE employees SET name=?, age=?, job=?, gender=?, address=?, phone=? WHERE id=?",
                        (name, age, job, gender, address, phone, id))
        self.con.commit()

    def search(self, keyword):
        # البحث في الجدول باستخدام الكلمة الرئيسية
        query = f"""
        SELECT * FROM employees
        WHERE name LIKE '%{keyword}%' OR 
              age LIKE '%{keyword}%' OR 
              job LIKE '%{keyword}%' OR 
              gender LIKE '%{keyword}%' OR 
              address LIKE '%{keyword}%' OR 
              phone LIKE '%{keyword}%'
        """
        self.cur.execute(query)
        rows = self.cur.fetchall()
            return rows
