import cgi
import base

form = cgi.FieldStorage()

email = form.getvalue("email")

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

base.header(email)

print("""<center><h1>ORDER CONFIRMATION</h1>
      <hr>
      <br>""")
print(""" <h5> Are you sure..you want to place order ?? </h5>""")
print(f"""
<br>
<a href="order.py?email={email}" class="btn btn-primary btn-lg active" role="button" aria-pressed="true">Sure</a>
<br>
<br>
<a href="mycart.py?email={email}" class="btn btn-primary btn-lg active" role="button" aria-pressed="true" >Take me back to my cart</a>""")
print("""""")
print("""
</center>
</body>
</html>""")
