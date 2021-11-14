import cgi
import model
import home

form = cgi.FieldStorage()

name = form.getvalue('reg_name')
email = form.getvalue('reg_email')
pwd = form.getvalue('reg_pwd')
address = form.getvalue('reg_address')
gender = form.getvalue('gender')
mobile = form.getvalue('reg_mobile')

user = model.register(name,email,pwd,address,mobile,gender)
home.registration()