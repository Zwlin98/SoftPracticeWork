import psycopg2

conn = psycopg2.connect(database='zwlin', user='zwlin', password='zwldbzwl', host='120.24.91.195', port='5432')
print("Open database Successful")

cur = conn.cursor()

# cur.execute('''CREATE TABLE COMPANY
#        (ID INT PRIMARY KEY     NOT NULL,
#        NAME           TEXT    NOT NULL,
#        AGE            INT     NOT NULL,
#        ADDRESS        CHAR(50),
#        SALARY         REAL);''')
#
# cur.execute("insert into company (ID,NAME ,AGE,ADDRESS,SALARY) values (1,'AAAA',15,'BeiJing',20000.00)")
# cur.execute("insert into company (ID,NAME ,AGE,ADDRESS,SALARY) values (2,'BBBB',30,'BeiJing',18000.00)")
# cur.execute("insert into company (ID,NAME ,AGE,ADDRESS,SALARY) values (3,'CCCC',45,'BeiJing',30000.00)")
# cur.execute("insert into company (ID,NAME ,AGE,ADDRESS,SALARY) values (4,'DDDD',60,'BeiJing',25000.00)")
#
# cur.execute("select * from company")
# rows = cur.fetchall()
# for row in rows:
#     print(row[1])

# cur.execute('''
# create table Employee
# (
# 	EmployeeID char(6) not null primary key,
# 	Name char(10) not null,
# 	Birthday date not null,
# 	Sex bit not null,
# 	Address Char(20),
# 	Zip char(6),
# 	PhoneNumber char(12),
# 	EmailAdderss char(30),
# 	DepartmentID char(3) not null
# );
# create table Departments
# (
# 	DepartmentID char(3) not null primary key,
# 	DepartmentName char(20) not null,
# 	Note text
# );
# create table Salary
# (
# 	EmployeeID char(6) not null ,
# 	DepartmentName char(20) not null,
# 	Note text
# );
# ''')

cur.execute('''
CREATE TABLE Employee
(
EmployeeID  char(6) not null primary key,
Name char(10) not null,
Birthday char(8) not null,
Sex bit not null,
Address char(20),
Zip char(6),
PhoneNumber char(12),
EmailAddress char(30),
DepartmentID char(3)
);

CREATE TABLE Departments
(
DepartmentID char(3) not null primary key,
DepartmentName char(20) not null,
Note Text
);
CREATE TABLE Salary
(
EmployeeID char(6) not null,
Income float(8) not null,
OutCome float(8) not null
);

insert into Departments values('1','财务部','财务部');
insert into Departments values('2','研发部','研发部');
insert into Departments values('3','人力资源部','人力资源部');
insert into Employee values('1001','李勇','78-3-12','0','河南','475001','3880378','ly@henu.edu.cn','1');
insert into Employee values('1002','王敏','80-11-2','1','河南','475002','0378311','wm@henu.edu.cn','1');
insert into Employee values('1003','刘晨','78-6-22','0','河南','475003','0378322','lc@henu.edu.cn','1');
insert into Employee values('2001','张立','78-8-1','0','河南','475004','0378333','zl@henu.edu.cn','2');
insert into Employee values('2002','刘毅','82-1-23','0','河南','475005','0378344','ly@henu.edu.cn','2');
insert into Employee values('2003','张玫','81-3-15','1','河南','475006','0378355','zm@henu.edu.cn','2');
insert into Employee values('3001','徐静','76-8-12','1','河南','475007','0378366','xj@henu.edu.cn','3');
insert into Employee values('3002','赵军','79-2-19','0','河南','475008','0378377','zj@henu.edu.cn','3');
insert into Salary values('1001',3600,1500);
insert into Salary values('1002',3300,1000);
insert into Salary values('1003',3700,1200);
insert into Salary values('2001',4000,1600);
insert into Salary values('2002',3800,1800);
insert into Salary values('2003',3800,1500);
insert into Salary values('3001',4200,2000);
insert into Salary values('3002',4100,1800);
''')

print("create successful")
conn.commit()

conn.close()
