import cgi
import model
import base

form = cgi.FieldStorage()

email = form.getvalue("email")

data = model.myProfile(email)

print("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
<style>
body {
  background-image: url("https://www.thespruce.com/thmb/KgSmJlEnCvtlRNGPLjURbDrw3JA=/960x0/filters:no_upscale():max_bytes(150000):strip_icc()/Chinese-lantern-pods-big-5961769d5f9b583f180ca93e.jpg");
  height: auto;
  background-repeat: no-repeat;
  background-size: cover;
  overflow-x: hidden;
  } 
</style>
</head>
<body>
""")

base.header(email)

print("""<center><h1 style="color:white; font-family:vintage; margin-top:5%;">MY PROFILE</h1></center>
<hr>
<br>""")

print("""<center>
<div class="froster-card text-white" style="max-width:40rem;">
  <div class="card-body" >
    <p class="card-text" style="font-size:25px; font-family:vinatge;">Name: {}</p>
    <p class="card-text" style="font-size:25px; font-family:vinatge;">Email: {}</p>
    <p class="card-text" style="font-size:25px; font-family:vinatge;">Address: {}</p>
    <p class="card-text" style="font-size:25px; font-family:vinatge;">Mobile No.: {}</p>
  </div>
</div>
<br>
<a href="editProfile.py?email={}" class="btn btn-warning btn-lg active" role="button" aria-pressed="true" >Edit Profile</a>
</center>
""".format(data[0][0],data[0][1],data[0][3],data[0][4],email))



print("""
</body>
</html>
""")