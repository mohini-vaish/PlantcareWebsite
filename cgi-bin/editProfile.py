import base
import cgi

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

print("<div class='container'>")
print("""<center><h1>Edit Details </h1></center>
<hr>""")

print(f"""
<form action="profileController.py?email={email}" method = post>
 <div class="form-group">
    <label for="exampleInputName">Enter name</label>
    <input type="text" class="form-control" name="reg_name" id="exampleInputName" placeholder="Enter Name">
 </div>
 <div class="form-group">
    <label for="exampleInputAddress2">Address</label>
    <input type="text" class="form-control" name="reg_address" id="exampleInputAddress2" placeholder="Address">
 </div>
 <div class="form-group">
    <label for="exampleInputmobile2">Mobile No.</label>
    <input type="text" class="form-control" name="reg_mobile" id="exampleInputmobile2" placeholder="MobileNo.">
 </div> 
 <button type="submit" class="btn btn-primary">Submit</button>
</form>
""")

print("""
   </div>
   </body>
   </html>
""")

base.footer()
