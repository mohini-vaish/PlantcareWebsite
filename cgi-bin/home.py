import base

print("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <link rel="icon" href="http://www.budapestjobs.net/wp-content/uploads/company_logos/2018/09/PlanetPlanrIdentification.png">
        <title>Plantcare</title>
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
    """)

def homepage(data):
    base.header(data[0][1])
    print("""<style>
    body{
    background-color: white;
  overflow-x: hidden;}
  
</style><body>
<h2 style="color:green; margin-left:15px; margin-top: 15px">Indoor plants</h2>
<div class="row">
<div class="card-group m-4">
<div class="col-sm-2">
  <div class=" frosted-card border-warning text-black bg-info">
    <img class="card-img-top " src="https://cdn.nurserylive.com/images/stories/virtuemart/product/resized/nurserylive-money-plant-green-2_280x280.jpg" alt="Card image cap" >
    <div class="card-body ">
    <h6 class="card-text" style="font-style:italic;">Money Plant, Scindapsus (Green) - Plant</h6>
    <a href="https://dengarden.com/gardening/Significance-of-growing-money-plant-in-your-house" class="card-link" style="color:white;">Read more..</a>
    </div>
    </div>
    </div>
  <div class="col-sm-2">
  <div class="frosted-card text-black" >
    <img class="card-img-top" src="https://cdn.nurserylive.com/images/stories/virtuemart/product/resized/nurserylive-Schefflera-green_280x280.jpg" alt="Card image cap" >
    <div class="card-body">
    <h6 class="card-text" >Schefflera - Plant</h6>
    <a href="https://www.nature-and-garden.com/gardening/schefflera.html" class="card-link">Read more..</a>

    </div>
    </div>
    </div>
  <div class="col-sm-2">
  <div class="frosted-card text-black bg-success" style="height:95%;">
    <img class="card-img-top" src="https://cdn.nurserylive.com/images/stories/virtuemart/product/resized/nurserylive-jade-plant-elephant-bush-1_280x280.jpg" alt="Card image cap" >
    <div class="card-body">
    <h6 class="card-text" >Elephantbush, Portulacaria afra(Green) - Succulent Plant</h6>
    <a href="#" class="card-link" style="color:white;">Read more..</a>
    </div>
    </div>
    </div>
  <div class="col-sm-2">
  <div class="frosted-card text-black" >
    <img class="card-img-top" src="https://cdn.nurserylive.com/images/stories/virtuemart/product/resized/nurserylive-dracaena-surculosa-aurea-golddust-dracaenaplant-1_280x280.jpg" alt="Card image cap" >
    <div class="card-body">
    <h6 class="card-text" >Dracaena surculosa Aurea, Golddust Dracaena-Plant</h6>
    <a href="#" class="card-link">Read more..</a>
    </div>
    </div>
    </div>
    <div class="col-sm-2">
  <div class="frosted-card text-black bg-info" >
    <img class="card-img-top" src="https://cdn.nurserylive.com/images/stories/virtuemart/product/resized/nurserylive-schefflera-variegated-1_280x280.jpg" alt="Card image cap" >
    <div class="card-body">
    <h6 class="card-text" >Schefflera Variegated - Plant</h6>
    <a href="http://jogindernursery.com/index.php?route=product/product&product_id=563" class="card-link" style="color:white;">Read more..</a>
    </div>
    </div>
    </div>
 <div class="col-sm-2">
  <div class="frosted-card text-black" >
    <img class="card-img-top" src="https://cdn.nurserylive.com/images/stories/virtuemart/product/resized/nurserylive-pleomele-song-of-india-green-plant_280x280.jpg" alt="Card image cap" >
    <div class="card-body">
    <h6 class="card-text" >Pleomele, Song of India (Green)-Plant</h6>
    <a href="#" class="card-link">Read more..</a>
    </div>
    </div>
    </div>
</div>""")

    print("""
<div class="row" >
<div class="card-group m-4">
<div class="col-sm-2">
  <div class="frosted-card text-black" >
    <img class="card-img-top" src="https://cdn.nurserylive.com/images/stories/virtuemart/product/resized/nurserylive-ledebouria-socialis_280x280.jpg" alt="Card image cap" >
    <div class="card-body">
    <h6 class="card-text" >Silver Squill, Ledebouria socialis-Plant</h6>
    <a href="#" class="card-link">Read more..</a>
    </div>
    </div>
    </div>
  <div class="col-sm-2">
  <div class="frosted-card text-black" >
    <img class="card-img-top" src="https://cdn.nurserylive.com/images/stories/virtuemart/product/resized/nurserylive-syngonium-variegated-small-plant-23_280x280.jpg" alt="Card image cap" >
    <div class="card-body">
    <h6 class="card-text" >Syngonium variegated - Plant</h6>
    <a href="#" class="card-link">Read more..</a>
    </div>
    </div>
    </div>
  <div class="col-sm-2">
  <div class="frosted-card text-black" >
    <img class="card-img-top" src="https://cdn.nurserylive.com/images/stories/virtuemart/product/resized/nurserylive-syngonium-pink-1_280x280.jpg" alt="Card image cap" >
    <div class="card-body">
    <h6 class="card-text" >Syngonium ( Pink ) - Plant</h6>
    <a href="#" class="card-link">Read more..</a>
    </div>
    </div>
    </div>
  <div class="col-sm-2">
  <div class="frosted-card text-black" >
    <img class="card-img-top" src="https://cdn.nurserylive.com/images/stories/virtuemart/product/resized/nurserylive-peace-lily-spathiphyllum-124_280x280.jpg" alt="Card image cap" >
    <div class="card-body">
    <h6 class="card-text" >Peace Lily, Spathiphyllum - Plant</h6>
    <a href="#" class="card-link">Read more..</a>
    </div>
    </div>
    </div>
    <div class="col-sm-2">
  <div class="frosted-card text-white" >
    <img class="card-img-top" src="https://cdn.nurserylive.com/images/stories/virtuemart/product/resized/nurserylive-pleomele-song-of-india-golden-1_280x280.jpg" data-src="https://cdn.nurserylive.com/images/stories/virtuemart/product/resized/nurserylive-pleomele-song-of-india-golden-1_280x280.jpg" data-jchll="true" alt="nurserylive-pleomele-song-of-india-golden-1" class="img-front lazy-loaded" alt="Card image cap" >
    <div class="card-body">
    <h6 class="card-text" >Pleomele, Song of India (Golden) - Plant</h6>
    <a href="#" class="card-link">Read more..</a>
    </div>
    </div>
    </div>
 <div class="col-sm-2">
  <div class="frosted-card text-white" >
    <img class="card-img-top" src="https://cdn.nurserylive.com/images/stories/virtuemart/product/resized/nurserylive-nephrolepis-exaltata-aurea-golden-fern-pivla-fern-main_280x280.jpg" alt="Card image cap" >
    <div class="card-body">
    <h6 class="card-text" >Nephrolepis exaltata aurea, Golden Fern, Pivla Fern - Plant</h6>
    <a href="#" class="card-link">Read more..</a>
    </div>
    </div>
    </div>  
</div>
""")
    print("""
    <div class="row2" >
    <div class="card-group ">
    <div class="col-sm-2">
      <div class="frosted-card text-white" >
        <img class="card-img-top" src="https://cdn.nurserylive.com/images/stories/virtuemart/product/resized/nurserylive-ledebouria-socialis_280x280.jpg" alt="Card image cap" >
        <div class="card-body">
        <h6 class="card-text" >Silver Squill, Ledebouria socialis-Plant</h6>
        <a href="#" class="card-link">Read more..</a>
        </div>
        </div>
        </div>
      <div class="col-sm-2">
      <div class="frosted-card text-white" >
        <img class="card-img-top" src="https://cdn.nurserylive.com/images/stories/virtuemart/product/resized/nurserylive-syngonium-variegated-small-plant-23_280x280.jpg" alt="Card image cap" >
        <div class="card-body">
        <h6 class="card-text" >Syngonium variegated - Plant</h6>
        <a href="#" class="card-link">Read more..</a>
        </div>
        </div>
        </div>
      <div class="col-sm-2">
      <div class="frosted-card text-white" >
        <img class="card-img-top" src="https://cdn.nurserylive.com/images/stories/virtuemart/product/resized/nurserylive-syngonium-pink-1_280x280.jpg" alt="Card image cap" >
        <div class="card-body">
        <h6 class="card-text" >Syngonium ( Pink ) - Plant</h6>
        <a href="#" class="card-link">Read more..</a>
        </div>
        </div>
        </div>
      <div class="col-sm-2">
      <div class="frosted-card text-white" >
        <img class="card-img-top" src="https://cdn.nurserylive.com/images/stories/virtuemart/product/resized/nurserylive-peace-lily-spathiphyllum-124_280x280.jpg" alt="Card image cap" >
        <div class="card-body">
        <h6 class="card-text" >Peace Lily, Spathiphyllum - Plant</h6>
        <a href="#" class="card-link">Read more..</a>
        </div>
        </div>
        </div>
        <div class="col-sm-2">
      <div class="frosted-card text-white" >
        <img class="card-img-top" src="https://cdn.nurserylive.com/images/stories/virtuemart/product/resized/nurserylive-pleomele-song-of-india-golden-1_280x280.jpg" data-src="https://cdn.nurserylive.com/images/stories/virtuemart/product/resized/nurserylive-pleomele-song-of-india-golden-1_280x280.jpg" data-jchll="true" alt="nurserylive-pleomele-song-of-india-golden-1" class="img-front lazy-loaded" alt="Card image cap" >
        <div class="card-body">
        <h6 class="card-text" >Pleomele, Song of India (Golden) - Plant</h6>
        <a href="#" class="card-link">Read more..</a>
        </div>
        </div>
        </div>
     <div class="col-sm-2">
      <div class="frosted-card text-white" >
        <img class="card-img-top" src="https://cdn.nurserylive.com/images/stories/virtuemart/product/resized/nurserylive-nephrolepis-exaltata-aurea-golden-fern-pivla-fern-main_280x280.jpg" alt="Card image cap" >
        <div class="card-body">
        <h6 class="card-text" >Nephrolepis exaltata aurea, Golden Fern, Pivla Fern - Plant</h6>
        <a href="#" class="card-link">Read more..</a>
        </div>
        </div>
        </div>  
    </div>
    """)


def registration():
    print("""
        <center><img src="http://ssipgujarat.in/gih/img/thanks.jpg" width ='300' height = '130' alt="..." style="margin-top:10%;">
        <div class="card-text text-success">You have successfully registered! Login to continue.</div><center>
        <br>
        <br>
        <a href="../index.html" class="btn btn-primary btn-lg active" role="button" aria-pressed="true">Login</a>
        """)

print("""
        </body>
        </html>  
    """)

base.footer()