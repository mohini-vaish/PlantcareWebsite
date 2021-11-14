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
<style>
body {
  background-image: url("/images/back.jpg");
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

print("""<center><h1 style="color:white; margin-top:10% font-family:vintage;">Search by categories</h1>
<hr>""")

print(f"""
<div class="row" >
<div class="card-group m-4">
<div class="card mb-3 m-2 bg-light text-black" >
  <img src="https://nurserylive.com/images/stories/virtuemart/product/nurserylive-table-top-office-desk-plants-for-removing-indoor-toxins7.jpg" class="card-img" alt="..." style="width:50%; height=50%;">
  <div class="card-img-overlay ">
    <h3 class="card-title" style="font-family:vintage;">PLANTS</h3>
    <h6  style="font-style:italic; font-family:vintage; font-weight:bold; color:black;">This is a wider card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</h6>
    <a href="details.py?p=plants&email={email} " class="btn btn-success">Go</a>
 
  </div>
</div>

""")

print(f"""
<div class="card mb-3 m-2  text-black" >
  <img src="https://www.educationquizzes.com/library/KS1-Science/Seeds-and-Bulbs-1.jpg" class="card-img" alt="..." style="width:50%; height=100%;" height=100%>
  <div class="card-img-overlay ">
    <h3 class="card-title" style="font-family:vintage;">SEEDS-BULBS</h3>
    <h6  style="font-style:italic; font-family:vintage; font-weight:bold; color:black;">This is a wider card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</h6>
    <a href="details.py?p=seeds-bulbs&email={email} " class="btn btn-success" >Go</a>
 
  </div>
</div>

<div class="card mb-3 m-2  text-white" >
  <img src="https://image.made-in-china.com/2f0j00GfVRMshghvqj/Best-Selling-Plastic-Garden-Flower-Pots-Planters.jpg" class="card-img" alt="..." style="width:50%; height=100%;" height=100%>
  <div class="card-img-overlay ">
    <h3 class="card-title" style="font-family:vintage;">POTS</h3>
    <h6  style="font-style:italic; font-family:vintage; font-weight:bold; color:black;">This is a wider card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</h6>
    <a href="details.py?p=pots&email={email} " class="btn btn-success">Go</a>
 
  </div>
</div>""")


print(f"""
<div class="card mb-3 m-2 bg-info text-white" >
  <img src="https://artisanstone.com.au/blog/wp-content/uploads/2015/12/Pebbles-3-1024x683.jpg" class="card-img" alt="..." style="width:50%; height=100%;" height=100%>
  <div class="card-img-overlay ">
    <h3 class="card-title" style="font-family:vintage;" >PEBBLES</h3>
    <h6  style="font-style:italic; font-family:vintage; font-weight:bold; color:black;">This is a wider card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</h6>
    <a href="details.py?p=pebbles&email={email} " class="btn btn-success" ">Go</a>
 
  </div>
</div>
</div>
</div>""")

print(f"""<div class="row" >
<div class="card-group m-4">
<div class="card mb-3 m-2  text-black" >
  <img src="https://thumbs-prod.si-cdn.com/mo2Rg6vGYmGCiSKbqZ789ui-nqs=/800x600/filters:no_upscale()/https://public-media.si-cdn.com/filer/fd/14/fd14d1b5-d09d-4ffd-b980-df6af692c3f0/istock_49022454_medium.jpg" class="card-img" alt="..." style="width:50%; height=50%;" height=100%>
  <div class="card-img-overlay ">
    <h3 class="card-title" style="font-family:vintage; color:white;">SOILS</h3>
    <h6  style="font-style:italic; font-family:vintage; font-weight:bold; color:black;">This is a wider card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</h6>
    <a href="details.py?p=soil&email={email} " class="btn btn-success" ">Go</a>

  </div>
</div>

""")

print(f"""
<div class="card mb-3 m-2 bg-info text-white" >
  <img src="https://www.planetnatural.com/wp-content/uploads/2012/12/fertilizer-products-1.jpg" class="card-img" alt="..." style="width:50%; height=100%;" height=100%>
  <div class="card-img-overlay ">
    <h3 class="card-title" style="font-family:vintage;">FERTILIZERS</h3>
    <h6  style="font-style:italic; font-family:vintage; font-weight:bold; color:black;">This is a wider card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</h6>
    <a href="details.py?p=fertilizers&email={email} " class="btn btn-success" >Go</a>

  </div>
</div>

<div class="card mb-3 m-2  text-white" >
  <img src="https://image.made-in-china.com/2f0j00GfVRMshghvqj/Best-Selling-Plastic-Garden-Flower-Pots-Planters.jpg" class="card-img" alt="..." style="width:50%; height=100%;" height=100%>
  <div class="card-img-overlay ">
    <h3 class="card-title" style="font-family:vintage;">POTS</h3>
    <h6  style="font-style:italic; font-family:vintage; font-weight:bold; color:black;">This is a wider card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</h6>
    <a href="#" class="btn btn-success">Go</a>

  </div>
</div>""")

print(f"""
<div class="card mb-3 m-2 bg-light " >
  <img src="https://nurserylive.com/images/stories/virtuemart/category/nurserylive-pebbles-by-type-category-image.jpg" class="card-img" alt="..." style="width:50%; height=100%;" height=100%>
  <div class="card-img-overlay ">
    <h3 class="card-title" style="font-family:vintage; font-weight:bold;" >PEBBLES</h3>
    <h6  style="font-style:italic; font-family:vintage; font-weight:bold; color:black;">This is a wider card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</h6>
    <a href="#" class="btn btn-success" ">Go</a>

  </div>
</div>
</div>
</div>""")

print(f"""

</center>
</body>
</html>
""")

base.footer()