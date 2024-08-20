import sqlite3


connection=sqlite3.connect("E:\\material\\GenerativeAI\\langchain\\new_langchain\\search-engine\\sql-app-langchain\\student.db")

cursor=connection.cursor()

table_info="""
create table STUDENT(NAME VARCHAR(25),CLASS VARCHAR(25),
SECTION VARCHAR(25),MARKS INT)

"""
cursor.execute(table_info)

# Insert mmore records
cursor.execute(''' insert into STUDENT values('sharad','data science','A',90)''')
cursor.execute(''' insert into STUDENT values('sharry','data science','A',40)''')
cursor.execute(''' insert into STUDENT values('shiva','data science','B',80)''')
cursor.execute(''' insert into STUDENT values('shanu','data science','C',70)''')
cursor.execute(''' insert into STUDENT values('shivam','data science','A',60)''')
cursor.execute(''' insert into STUDENT values('krish','data science','B',80)''')
cursor.execute(''' insert into STUDENT values('sharad sisodiya','data science','A',90)''')

# display the records
print("the inserted data ")
data=cursor.execute('''select * from STUDENT''')
for row in data:
    print(row)
    
connection.commit()
connection.close()