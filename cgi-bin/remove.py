import cgi
import model
import base

form = cgi.FieldStorage()
p_id = form.getvalue("p_id")
email = form.getvalue("email")
model.removeFromCart(email,p_id)

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
  background-image: url("https://www.acd-inc.com/wp-content/uploads/2018/03/checked-symbol.png?x61998");
  background-repeat: no-repeat;
  background-position: center;
  height:700px;
  background-size: 300px 300px;
  overflow-y: hidden;
  } </style>
</head>
<body>
""")

base.header(email)

print("""<b><center><h1 style="margin-top:5%;">Product Removed !!</h1></center><b>""")

print("""
</body>
</html>
""")