import base
import cgi
import model

form = cgi.FieldStorage()
email = form.getvalue("email")
data = model.mycart(email)

print("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <link rel="icon" href="http://www.budapestjobs.net/wp-content/uploads/company_logos/2018/09/PlanetPlanrIdentification.png">
    <title>Plantcare</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
</head>
<body>
""")

sum = 0
delivery = 50

base.header(email)

print("""<center><h1 style="font-family:vintage; background-color:green; color:white;">MY CART</h1>
<hr>""")

for i in data:
     d = model.showProduct(i[1])
     print("""
     <div class="card mb-3" style="width: 45rem;margin-bottom:200px; padding:10px;">
      <div class="row no-gutters">
        <div class="col-md-4">
       <img src="../product_pic/{}" class='w-50' alt="...">
     </div>
     <div class="col-md-8">
     <div class="card-body">
        <h5 class="card-title">{}</h5>
        <p class="card-text">Price:INR {}/-</p>
        <a href="remove.py?p_id={}&email={}" class="btn btn-info">Remove from cart</a>
     </div>
     </div>
     </div>
     </div>""".format(d[0][-1], d[0][2], d[0][-2],d[0][0],email))
     sum += int(d[0][-2])

if sum == 0:
     print(""" <center><img src="https://iticsystem.com/img/empty-cart.png" width = '450' height = '400' alt="..."><center> """)

else:
     print(f"""
     <h2>Your Bill</h2>
     <b><h5>Items Total:Rs.{sum}</h5><b>""")
     print(f"""<b><h5>Delivery Charges:Rs.{delivery}</h5><b>""")
     print(f"""<b><h5>Total Bill:Rs.{sum + delivery}</h5></b>
     <a href="orderConfirmation.py?email={email}" class="btn btn-info btn-lg active" role="button" aria-pressed="true">Order now >> </a>
     """)

print("""
</center>
</div>
</body>
</html>
""")

base.footer()