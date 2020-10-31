import sqlite3

con = sqlite3.connect("employee.db")
c = con.cursor()
#c.execute("""CREATE TABLE employee(first text, last text, pay integer)""")
c.execute("INSERT INTO employee VALUES ('SALMAN' , 'RAJ' , 100000)")
c.execute("SELECT * FROM employee")
print(c.fetchone())

con.commit()
con.close()