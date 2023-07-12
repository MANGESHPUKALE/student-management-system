# ******************  STUDENT MANAGEMENT SYSTEM   **************************** 



# _____________________importing library's_____________________________________

from tkinter import *
from tkinter.messagebox import * 
from tkinter.scrolledtext import * 
from mysql.connector import *
import pandas as pd
import numpy as np



# ______________________main to add employee__________________________________

def f1():
	root.withdraw()
	aw.deiconify()

# ____________________add employee to main___________________________________

def f2():
	aw.withdraw()
	root.deiconify()

# _____________________main to view employee_________________________________

def f3():
	root.withdraw()
	vw.deiconify()
	vw_st_data.delete(1.0,END)
	con =None
	try:
		con = connect(host="localhost",user="root",password="Mangesh@123",database="smsdb")
		cursor = con.cursor()
		sql = "select * from student"
		cursor.execute(sql)
		data = cursor.fetchall()
		info =""
		for d in data:
			info = info + "rno = " +str(d[0])+ "\nName= " +str(d[1]) +"\nMobile No. = "+str(d[2]) +"\nEmail ID = " + str(d[3]) + "\n" + ("_"*30) + "\n"
		vw_st_data.insert(INSERT,info)
	except Exception as e:
		print("Issue", e)
	finally:
		if con is not None:
			con.close()

# _______________________view to main page_______________________________________

def f4():
	vw.withdraw()
	root.deiconify()


# _______________________main to update page____________________________________

def f5():
	root.withdraw()
	uw.deiconify()

# _______________________update to main page____________________________________

def f6():
	uw.withdraw()
	root.deiconify()

#_________________________ main to delete page___________________________________

def f7():
	root.withdraw()
	dw.deiconify()


# __________________________delete to main page___________________________________

def f8():
	dw.withdraw()
	root.deiconify()



# ______________________for add employee page_____________________________________

def add():
	con = None
	try:
		con = connect(host="localhost",user="root",password="Mangesh@123",database="smsdb")
		rno = int(aw_ent_rno.get())
		name = aw_ent_name.get()
		phone = int(aw_ent_phone.get())
		email = aw_ent_email.get()
		cursor = con.cursor()
		sql = "insert into student values('%d','%s','%d','%s')"
		cursor.execute(sql%(rno,name,phone,email))
		con.commit()
		showinfo("Success", "Record created")
	except Exception as e:
		if con is not None:
			con.rollback()
			showerror("Issue", e)
	finally:
		if con is not None:
			con.close()
		aw_ent_rno.delete(0,END)
		aw_ent_name.delete(0,END)
		aw_ent_phone.delete(0,END)
		aw_ent_email.delete(0,END)
		aw_ent_rno.focus()

# _______________________for delete student_________________________________________

def delete():
	con = None

	try:
		con = connect(host = "localhost", user = "root", password = "Mangesh@123",			database = "smsdb")
		cursor = con.cursor()
		sql = "delete from student where rno = '%d'"
		rno = int(dw_ent_rno.get())
		cursor.execute(sql % (rno))
		if cursor.rowcount == 1:
			con.commit()
			showinfo("Deleted", "Record Deleted")
		else:
			showinfo("Failed", "Record does not exists")

	except Exception as e:
		if con is not None:
			con.rollback()
			showerror("Issue", e)
	finally:
		if con is not None:
			con.close()
		dw_ent_rno.delete(0,END)
		dw_ent_rno.focus()

# ___________________________here update student_________________________________

def update():
	con = None
	try:
		con = connect(host = "localhost", user = "root", password = "Mangesh@123",			database = "smsdb")
		cursor = con.cursor()
		sql = "update student set name ='%s',phone ='%d',email = 's%' where rno = '%d'"
		rno = int(uw_ent_rno.get())
		name = uw_ent_name.get()
		phone = int(uw_ent_phone.get())
		email = uw_ent_email.get()
		cursor.execute(sql % (name,phone,email,rno))
		if cursor.rowcount == 1:
			con.commit()
			showinfo("Updated", "Record Updated")
		else:
			showinfo("Failed", "Record does not exists")

	except Exception as e:
		if con is not None:
			con.rollback()
			showerror("Issue", e)
	finally:
		if con is not None:
			con.close()
		uw_ent_rno.delete(0,END)
		uw_ent_name.delete(0,END)
		uw_ent_phone.delete(0,END)
		uw_ent_email.delete(0,END)
		uw_ent_rno.focus()




# _________________________________Main page_____________________________________

root = Tk()
root.title("Employee Management System")
root.geometry("600x700+50+50")
root.iconbitmap("student.ico")
f =("Arial",25,"bold")
root.configure(bg ="lightgreen")

lab_head = Label(root,text="Student Management System",fg = "red",font=('Times', 35,"bold"))
lab_head.config(bg="lightgreen")
lab_head.pack(pady=20)
btn_add = Button(root,text ="Add Student",font=('Times', 35,"bold"), width= 15,command = f1)
btn_add.pack(pady=20)
btn_view = Button(root,text ="View Students",font=('Times', 35,"bold"), width= 15,command = f3)
btn_view.pack(pady=20)
btn_update = Button(root,text ="Update Student",font=('Times', 35,"bold"), width= 15,command = f5)
btn_update.pack(pady=20)
btn_delete = Button(root,text ="Delete Student",font=('Times', 35,"bold"), width= 15,command = f7)
btn_delete.pack(pady=20)



#______________________________________Add student page________________________________

aw = Toplevel(root)
aw.title("Add Student")
aw.geometry("600x700+50+50")

aw_lab_rno = Label(aw,text ="Enter rno", font = f)
aw_ent_rno = Entry(aw,font = f, bd = 2)
aw_lab_name = Label(aw, text = "Enter Name", font = f)
aw_ent_name = Entry(aw, font = f, bd = 2)
aw_lab_phone = Label(aw, text = "Enter Phone", font = f)
aw_ent_phone = Entry(aw, font = f, bd = 2)
aw_lab_email = Label(aw, text = "Enter Email", font = f)
aw_ent_email = Entry(aw, font = f, bd = 2)

aw_btn_save = Button(aw, text = "Add", font = f,command = add)
aw_btn_back = Button(aw, text = "Back", font = f,command = f2)

aw_lab_rno.pack(pady = 10)
aw_ent_rno.pack(pady = 10)
aw_lab_name.pack(pady = 10)
aw_ent_name.pack(pady = 10)
aw_lab_phone.pack(pady = 10)
aw_ent_phone.pack(pady = 10)
aw_lab_email.pack(pady = 10)
aw_ent_email.pack(pady = 10)
aw_btn_save.pack(pady = 10)
aw_btn_back.pack(pady = 10)

aw.withdraw()




# _____________________________View student page_________________________________________

vw = Toplevel(root)
vw.title("View Students")
vw.geometry("600x700+50+50")
f1 = ("Arial",20)

vw_st_data = ScrolledText(vw, height = 17, font = f1, bd = 6)
vw_btn_back = Button(vw, text = "Back", font = f, command = f4)
vw_st_data.pack(pady = 10)
vw_btn_back.pack(pady = 10)

vw.withdraw()





#______________________________update Student________________________________________

uw = Toplevel(root)
uw.title("Update student")
uw.geometry("600x700+50+50")

uw_lab_rno = Label(uw, text = "Enter rno", font = f)
uw_ent_rno = Entry(uw, font = f, bd = 2)
uw_lab_name = Label(uw, text = "Enter Name", font = f)
uw_ent_name = Entry(uw, font = f, bd = 2)
uw_lab_phone = Label(uw, text = "Enter Phone", font = f)
uw_ent_phone = Entry(uw, font = f, bd = 2)
uw_lab_email = Label(uw, text = "Enter Email", font = f)
uw_ent_email = Entry(uw, font = f, bd = 2)

uw_btn_save = Button(uw, text = "Update", font = f, command = update)
uw_btn_back = Button(uw, text = "Back", font = f, command = f6)

uw_lab_rno.pack(pady = 10)
uw_ent_rno.pack(pady = 10)
uw_lab_name.pack(pady = 10)
uw_ent_name.pack(pady = 10)
uw_lab_phone.pack(pady = 10)
uw_ent_phone.pack(pady = 10)
uw_lab_email.pack(pady = 10)
uw_ent_email.pack(pady = 10)
uw_btn_save.pack(pady = 10)
uw_btn_back.pack(pady = 10)

uw.withdraw()




#____________________________Delete Student__________________________________________

dw = Toplevel(root)
dw.title("Delete Student")
dw.geometry("600x700+50+50")

dw_lab_rno = Label(dw, text = "Enter rno", font = f)
dw_ent_rno = Entry(dw, font = f, bd = 2)

dw_btn_save = Button(dw, text = "Delete", font = f,command = delete)
dw_btn_back = Button(dw, text = "Back", font = f, command = f8)

dw_lab_rno.pack(pady = 10)
dw_ent_rno.pack(pady = 10)
dw_btn_save.pack(pady = 10)
dw_btn_back.pack(pady = 10)
dw.withdraw()



#________________if user exit then showing message to use_________________________________

def f9():
	answer = askyesno(title='confirmation', message = 'tussi ja rahe ho?')
	if answer:
		root.destroy()
root.protocol("WM_DELETE_WINDOW",f9)



root.mainloop()















































