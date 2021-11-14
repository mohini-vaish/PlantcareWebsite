import pymysql
import os

connection = pymysql.connect(host='localhost',port=3306,user='root',
                             database='socialnetwork',autocommit=True)

cursor = connection.cursor()

class User():
    def __init__(self, name, email, pwd, address,mobile, gender):
        self.name = name
        self.email = email
        self.pwd = pwd
        self.address = address
        self.mobile = mobile
        self.gender = gender

    def __str__(self):
        return self.name + "," + self.email + "," + self.pwd + "," + self.address + "," + self.mobile + "," + self.gender


def register(name,email,pwd,address,mobile,gender):
    try:
        user = User(name,email, pwd,address,mobile,gender)
        query = "insert into users values (%s, %s, %s, %s, %s,%s)"
        cursor.execute(query, (user.name,user.email,user.pwd, user.address,user.mobile,user.gender))
        return user

    except pymysql.IntegrityError:
        return "Email ID Already Exist"


def loginUser(email,pwd):
    query = "select * from users where email=%s and pwd = %s"
    cursor.execute(query, (email, pwd))
    data = cursor.fetchall()
    if len(data) < 1:
        return "User do not exist"
    else:
        return data

def addProduct(p_id,p_category,p_name,p_brand,p_price,p_pic):
    if p_pic:
        fn = os.path.basename(p_pic)
        image = p_pic.file.read()
        file = open('product_pic/'+fn,'wb')
        file.write(image)
        file.close()
    query = "insert into products values (%s,%s,%s,%s,%s,%s)"
    cursor.execute(query,(p_id,p_category,p_name,p_brand,p_price,p_pic))

def product(p_category):
    query = "select * from products where p_category = %s"
    cursor.execute(query, (p_category))
    data = cursor.fetchall()
    return data

def insertProduct(email,p_id):
    query = "insert into cart values (%s,%s)"
    cursor.execute(query,(email,p_id))

def showProduct(p_id):
    query = "select * from products where p_id = %s"
    cursor.execute(query, (p_id))
    d = cursor.fetchall()
    return d

def mycart(email):
    query = "select * from cart where email = %s"
    cursor.execute(query, (email))
    data = cursor.fetchall()
    return data

def allUsers():
    query = "select * from users"
    cursor.execute(query)
    data = cursor.fetchall()
    return data

def details(email):
    query = "select name,address,mobile from users where email = %s"
    cursor.execute(query,(email))
    details = cursor.fetchall()
    return details

def editProfile(name,address,mobile,email):
    query = "update users SET name = %s , address = %s , mobile = %s where email = %s "
    cursor.execute(query, (name,address,mobile,email))

def orders(order_id,email,p_id,date,time):
    query = "insert into orders values (%s,%s,%s,%s,%s)"
    cursor.execute(query, (order_id,email,p_id,date,time))

def prev_orders(email):
    query = "select * from orders where email = %s order by date"
    cursor.execute(query,(email))
    data = cursor.fetchall()
    return data

def searchProduct():
    query = "select * from products"
    cursor.execute(query)
    data = cursor.fetchall()
    return data

def removeFromCart(email,p_id):
    query = "DELETE FROM cart WHERE email =%s and p_id = %s"
    cursor.execute(query, (email,p_id))

def clearCart(email):
    query = "DELETE FROM cart WHERE email =%s"
    cursor.execute(query,(email))

def myProfile(email):
    query = "select * from users where email = %s"
    cursor.execute(query,(email))
    data = cursor.fetchall()
    return data
