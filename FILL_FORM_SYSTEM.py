from tkinter import *
import tkinter.messagebox as MessageBox
import mysql.connector as mysql


#Create tkinter window

root = Tk()
root.geometry("800x500")
root.title("Crud system")


#Inser Function
def Insert():
    id = id_entry.get()
    name = name_entry.get()
    phone = phone_entry.get()

    if (id == "" or name == "" or phone == ""):
        MessageBox.showinfo("ALERT", "Please Fill Up all after Click")
    else:
        con = mysql.connect(host="localhost", database="lapinig_web_db", user="root", password="")
        query = "INSERT INTO tb_user (ID, NAME, PHONE) VALUES ('" + id + "' , '" + name + "' , '" + phone + "')"
        cur = con.cursor()
        cur.execute(query)
        con.commit()
        cur.close()
        MessageBox.showinfo("status", "Succesfully Inserted")


#Delete Function
def Delete():

    if (id_entry.get() == ""):
       MessageBox.showinfo("ALERT", "Please enter ID to Delete row")
    else:
       con = mysql.connect(host="localhost", database="lapinig_web_db", user="root", password="")
       query = ("DELETE FROM tb_user WHERE ID='" + id_entry.get() +"'")
       cur = con.cursor()
       cur.execute(query)
       con.commit()

       id_entry.delete(0, 'end')
       name_entry.delete(0, 'end')
       phone_entry.delete(0, 'end')

       MessageBox.showinfo("status", "Succesfully Delete")
       cur.close()



#Update Function
def Update():
    id = id_entry.get()
    name = name_entry.get()
    phone = phone_entry.get()

    if (id == "" or name == "" or phone == ""):
        MessageBox.showinfo("ALERT", "Please Fill Up all after Click")
    else:
        con = mysql.connect(host="localhost", database="lapinig_web_db", user="root", password="")
        cur = con.cursor()
        cur.execute("UPDATE tb_user SET name='" + name +"', phone='" + phone +"' WHERE ID  ='" + id +"'")
        con.commit()
        cur.close()
        MessageBox.showinfo("status", "Succesfully Update")


#Select Function
def Select():

        if (id_entry.get() == ""):
            MessageBox.showinfo("ALERT", "ID is required to select row!")
        else:
            con = mysql.connect(host="localhost", database="lapinig_web_db", user="root", password="")
            cur = con.cursor()
            cur.execute("select * from tb_user where id='" + id_entry.get() +"'")
            rows = cur.fetchall()

            for row in rows:
                name_entry.insert(0, row[1])
                phone_entry.insert(0, row[2])

            con.close()



# Create label and entry box
id = Label(root, text="Enter ID:", font=("verdana 15"))
id.place(x=50, y=30)
id_entry = Entry(root, font=("verdana 15"))
id_entry.place(x=150, y=30)


name = Label(root, text="Name:", font=("verdana 15"))
name.place(x=50, y=80)
name_entry = Entry(root, font=("verdana 15"))
name_entry.place(x=150, y=80)


phone = Label(root, text="Phone:", font=("verdana 15"))
phone.place(x=50, y=130)
phone_entry = Entry(root, font=("verdana 15"))
phone_entry.place(x=150, y=130)



btnInsert = Button(root, text="Insert", command=Insert,  font=("verdana 15")).place(x=100, y=180)
btnDelete = Button(root, text="Delete", command=Delete,  font=("verdana 15")).place(x=200, y=180)
btnUpdate = Button(root, text="Update", command=Update,  font=("verdana 15")).place(x=320, y=180)
btnSelect = Button(root, text="Select", command=Select,  font=("verdana 15")).place(x=200, y=240)


root.mainloop()



