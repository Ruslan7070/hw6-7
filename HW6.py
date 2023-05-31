import sqlite3

db = sqlite3.connect('student_db.db')

s = db.cursor()

s.execute('''CREATE TABLE IF NOT EXISTS student_db(
name text,
surname text,
b_y date,
hobby text,
view integer
)''')
#
# s.execute("INSERT INTO student_db VALUES "
#           "('Aitbek','Alymbekov',2003,'chess',11)")
# s.execute("INSERT INTO student_db VALUES "
#           "('Sanzhar','Raimkulov',2002 ,'chess',6)")
# s.execute("INSERT INTO student_db VALUES "
#           "('Azat','Zakirov',2003 ,'football',15)")
# s.execute("INSERT INTO student_db VALUES "
#           "('Mariya','Zulpuharova',2002 ,'volleyball',12)")
# s.execute("INSERT INTO student_db VALUES "
#           "('Aziz','Abdymambetov',2003 ,'football',5)")
# s.execute("INSERT INTO student_db VALUES "
#           "('Beka','Asylov',2003 ,'volleyball',10)")
# s.execute("INSERT INTO student_db VALUES "
#           "('Aida','Salamatkoeva',2002 ,'tennis',8)")
# s.execute("INSERT INTO student_db VALUES "
#           "('Samat','Sagynbekov',2001 ,'football',9)")
# s.execute("INSERT INTO student_db VALUES "
#           "('Sergei','Kolesnikov',2004 ,'hourse',11)")
# s.execute("INSERT INTO student_db VALUES "
#           "('Galym','Kokulov',2002 ,'bolleyball',7)")

s.execute("SELECT * FROM student_db WHERE LENGTH(surname)>10")
print(s.fetchall())
def print_students():
    selected_students_list = s.fetchall()
    for student in selected_students_list:
        print(student)


s.execute("UPDATE student_db SET name='genius' WHERE view > 10")


s.execute("SELECT * FROM student_db WHERE name='genius'")
print(s.fetchall())

s.execute("DELETE FROM student_db WHERE rowid %2 = 0 ")
s.execute("SELECT * FROM student_db")
print(s.fetchall())
db.commit()
db.close()



