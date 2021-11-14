import cgi
import model
import home

form = cgi.FieldStorage()

email = form.getvalue("login_email")
pwd = form.getvalue("login_pwd")

data = model.loginUser(email,pwd)


def header(email):
    print(f"""<nav class="navbar navbar-expand-lg navbar-dark bg-dark">
       <a class="navbar-brand" href="#" style="...">
            <img src="http://www.budapestjobs.net/wp-content/uploads/company_logos/2018/09/PlanetPlanrIdentification.png" width="40" height="40" class="d-inline-block align-top" alt="">  PLANTCARE</a>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
       </button>
     <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item">
        <a class="nav-link" href="myProfile.py?email={email}">MY  Profile<span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="mycart.py?email={email}">MyCart</a>
      </li>
       <li class="nav-item">
        <a class="nav-link" href="prev_Orders.py?email={email}">Previous Orders</a>
      </li>
   <li class="nav-item">
        <a class="nav-link" href="categories.py?email={email}">Shop Here</a>
      </li>
  <li class="nav-item">
        <a class="nav-link" href="../index.html">Log Out</a>
      </li>
        </a>
      </li>
    </ul>
  </div>
               <form class="form-inline" action="search.py?email={email}"  style="width:22%;">
                  <input class="form-control mr-sm-2" name='q' type="search" placeholder="Search for products" aria-label="Search" type="hidden" >
                  <button class="btn btn-outline-success my-2 my-sm-0" type="submit">Search</button>
                </form>


</nav>

""")


if data == "User do not exist":
    print("""
    <br>
    <br>
    <center><h2>Incorrect Email or Password !! Try Again !!<h2>
    <a href="../index.html" class="btn btn-primary">Back to Home Page</a></center>
    """)


else:
    home.homepage(data)
