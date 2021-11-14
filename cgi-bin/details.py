import cgi
import base
import model

form = cgi.FieldStorage()
category = form.getvalue("p")
email = form.getvalue("email")
data = model.product(category)

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
  background-image: url("https://images.wallpaperscraft.com/image/foliage_plants_green_120557_1280x720.jpg");
  height: auto;
  background-repeat: no-repeat;
  background-size: cover;
  overflow-x: hidden;
  } </style>
</head>
<body>
""")

base.header(email)

print("""
 <div class ="container" style="font-family:vintage; margin-left:2%" height=20%>
 <h1 style="color:white; margin-top:2%;"> {}</h1>
 </div>
 <div class ="row">
""".format(category.title()))

for i in data:
    print("""
    <div class="col-md-2" style="margin-left:2%;">
        <div class="card" style="width:12rem; margin-bottom:4px; padding:10px;">
          <img src="../product_pic/{}" alt="img" width=100% height=70%>
          <div class="card-body" >
            <h6 class="card-title">{}</h6>
            <p class="card-text">Price :INR {}/-</p>
            <a href="cart.py?p_id={}&email={}" class="btn btn-info" style="width:120px; height:10%;">Add to Cart</a>
          </div>
        </div>
        </div>
    """.format(i[-1],i[2],i[-2],i[0],email))


print("""
</div>
</div>
</body>
</html>
""")

base.footer()