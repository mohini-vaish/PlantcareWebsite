import base
import cgi
import model
import random
from datetime import datetime

form = cgi.FieldStorage()
email = form.getvalue("email")
payment = form.getvalue("payment")

data = model.mycart(email)
details = model.details(email)
model.clearCart(email)

d = datetime.now()
date = d.strftime("%d/%m/%y,%a")
time = d.strftime("%H:%M:%S %p")

print("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
<style>
body {
  background-image: url("https://img.freepik.com/free-photo/black-friday-composition-with-four-bags-cart_23-2147709334.jpg?size=626&ext=jpg");
  background-repeat: no-repeat;
  background-size: cover;
  overflow-x: hidden;
  } </style>
</head>
<body>
""")

base.header(email)
order_id = random.randint(1000,9999)

print(""" 
  <br>
  <h3 style="font-family:vintage; margin-left:6%;">Delivery Details</h3>
  <hr>
  <div class="card-body" style="margin-left:5%;">
    <h5 class="card-title" style="font-family:vintage; color:green; font-weight:bold;">NAME: {}</h5>
    <h5 class="card-title" style="font-family:vintage; color:green; font-weight:bold;">ADDRESS: {}</h5>
    <h5 class="card-title" style="font-family:vintage; color:green; font-weight:bold;">MOBILE NO.: {}</h5>
  </div>""".format(details[0][0],details[0][1],details[0][2]))

print("""
  <center><h1 style="margin-top:6%;">Thank you for shopping with us !!</h1>
  <br>
  <h5><b>***Order will be delivered in 4-5 working days***</b></h5><center>
   """)

for i in data:
    model.orders(order_id,i[0],i[1],date,time)

print("""
</body>
</html>
""")

base.footer()
