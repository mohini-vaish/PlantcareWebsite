def header(email):

    print(f"""<nav class="navbar navbar-dark bg-dark navbar-expand-lg">
       <a class="navbar-brand" href="#">
    <img src="http://www.budapestjobs.net/wp-content/uploads/company_logos/2018/09/PlanetPlanrIdentification.png" width="30" height="30" class="d-inline-block align-top" alt="">
  </a>
       <a class="navbar-brand" href="#">Plantcare</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNavDropdown" aria-controls="navbarNavDropdown" aria-expanded="false" >
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNavDropdown">
    <ul class="navbar-nav">
  <li class="nav-item">
        <a class="nav-link" href="myProfile.py?email={email}">My Profile</a>
      </li>
   <li class="nav-item">
        <a class="nav-link" href="categories.py?email={email}">Shop Here</a>
      </li>
   <li class="nav-item">
        <a class="nav-link" href="mycart.py?email={email}">MyCart</a>
      </li>
    <li class="nav-item">
        <a class="nav-link" href="prev_Orders.py?email={email}">Previous Orders</a>
      </li>
  <li class="nav-item">
        <a class="nav-link" href="../index.html">Log Out</a>
      </li>
        </a>
      </li>
    </ul>
  </div>
   <form action="search.py?email={email}" class="form-inline my-lg-0" style="width:30%;">
      <input type="hidden" value={email} name="email">
      <input class="form-control mr-sm-2" name='q' type="search" placeholder=" Search for product, brand..." aria-label="Search" style="width:65%;">
      <button class="btn btn-outline-success my-2 my-sm-0" type="submit">Search</button>
   </form>
</nav>

""")

def footer():
    print("""
    <script
    src = "https://code.jquery.com/jquery-3.3.1.slim.min.js"
    integrity = "sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo"
    crossorigin = "anonymous" > </script>
    <script
    src = "https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js"
    integrity = "sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1"
    crossorigin = "anonymous" > </script>
    <script
    src = "https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js"
    integrity = "sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM"
    crossorigin = "anonymous" > </script>
    """)