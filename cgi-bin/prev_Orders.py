import cgi
import model
import base

form = cgi.FieldStorage()

email = form.getvalue("email")
data = model.prev_orders(email)

print("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <link rel="icon" href="http://www.budapestjobs.net/wp-content/uploads/company_logos/2018/09/PlanetPlanrIdentification.png">
    <title>Plantcare</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
<style>
body {
  background-image: url("https://img.freepik.com/free-vector/different-elements-online-shopping_1085-848.jpg?size=338&ext=jpg");
  background-repeat: no-repeat;
  height:650px;
  background-position: center;
  overflow-x: hidden;
  } 
  </style>
</head>
<body>
""")

base.header(email)

print("""<center><h1>PREVIOUS ORDERS</h1></center>
      <hr>""")

for i in data:
   d = model.showProduct(i[2])
   print(f"""<p style="margin-left:10%;">OrderID:{i[-1]}</p>""")
   print("""<p style="margin-left:10%;">Date:{}</p>""".format(i[-2]))
   print(f"""<p style="margin-left:10%;">Time:{i[-1]}</p>""")
   print("""
        <div class="card mb-2" style="width:25rem; margin-bottom:200px; padding:5px; margin-left:10%">
         <div class="row no-gutters">
           <div class="col-md-4">
          <img src="../product_pic/{}" class='w-50' alt="...">
        </div>
        <div class="col-md-8">
        <div class="card-body">
           <h5 class="card-title">{}</h5>
           <p class="card-text">Price:INR {}/-</p>
        </div>
        </div>
        </div>
        </div>""".format(d[0][-1], d[0][2], d[0][-2],d[0][0]))

print("""

</body>
</html>
""")

base.footer()