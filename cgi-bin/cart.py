import base
import model
import cgi

form = cgi.FieldStorage()
email = form.getvalue("email")
p_id = form.getvalue('p_id')
model.insertProduct(email,p_id)
d = model.showProduct(p_id)

print("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">

</head>
<body>
""")

base.header(email)

print("""
<div class ="container">
 <h1>Item added to Cart</h1>
 <hr>
 <div class ="row">
 """)
for i in d:
    print("""
    <div class="col-md-4">
            <div class="card" style="width: 18rem; margin-bottom:20px; padding:10px;">
              <img src="../product_pic/{}" class="card-img-top" alt="img" height=400>
              <div class="card-body">
                <h5 class="card-title">{}</h5>
                <p class="card-text">Price:INR {}/-</p>
              </div>
            </div>
    </div> """.format(i[-1],i[2],i[-2]))

print("""
</body>
</html>
""")

base.footer()
