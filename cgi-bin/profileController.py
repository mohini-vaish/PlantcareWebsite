import cgi
import model
import base

form = cgi.FieldStorage()

email = form.getvalue('email')
name = form.getvalue('reg_name')
address = form.getvalue('reg_address')
mobile = form.getvalue('reg_mobile')

model.editProfile(name,address,mobile,email)
print("""
    <!doctype html>
    <html lang="en">
    <head>
        <!-- Required meta tags -->
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        <!-- Bootstrap CSS -->
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
        <link rel="icon" href="http://www.budapestjobs.net/wp-content/uploads/company_logos/2018/09/PlanetPlanrIdentification.png">
        <title>Plantcare</title>
        <link rel="stylesheet" href="styles.css">
    </head>
    <body>
    """)

base.header(email)

print("""
<br>
<br>
<br>
<center><h1>Profile Updated!!</h1></center>""")

print("""
</body>
</html>""")

base.footer()

