#!C:/Users/deepa/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import pymysql
import cgitb
cgitb.enable()
con=pymysql.connect(host="localhost",user="root",password="",database="nexus",port=3307)
cur=con.cursor()
print("""
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Nexus</title>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.7.1/jquery.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
</head>

<body>
    <style>
        #www {
            margin-top: 30px;
            margin-left: 20px;
        }

        #ccc {
            background-color: aliceblue;
            font-weight: 600;
            padding-left: 10px;
        }

        #ii {
            font-weight: 800;
        }

        #ooo {
            margin-left: 30px;
        }

        #yyy {
            font-size: 50px;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            color: maroon;
            text-shadow:4px 4px;
        }
        nav ul li a{
            font-weight: 800;
            font-size: 15px;
        }

      
    </style>
    <div class="container-fluid" >
    <div class="row">
    <div class="col-lg-5 col-xs-3"></div>
     <div class="col-xs-6">
        <h1 style="font-weight: 900; color: teal;"> 
     <img src="./image/logo.jpg" alt="" height="60px" width="80px" style="border-radius: 50%;">
         Nexus</h1>
            </div>
            </div>
            </div>
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
        <div class="container-fluid">
        
            <div class="navbar-header">
                <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#mynavbar">
                    <span class="icon-bar" style="background-color: darkcyan;"></span>
                    <span class="icon-bar" style="background-color: darkcyan;"></span>
                    <span class="icon-bar" style="background-color: darkcyan;"></span>
                </button>
               
              
            </div>
            <div class="collapse navbar-collapse" id="mynavbar">
            
                <ul class="nav navbar-nav">
                    <li class="dropdown">
                        <a class="dropdown-toggle" data-toggle="dropdown" href="#"></a>
                    </li>
                    <li><a href="#"></a></li>
                    <li><a href="#"></a></li>
                    <li><a href="userregister.py"><span class="glyphicon glyphicon-user"></span>Reg-User</a></li>
                     <li>
                    <a href="" data-toggle="dropdown">Login-User <span class="caret"></span></a>
                    <div class="dropdown-menu">
                    <ul role="menu">
                      <li style="display: block;">  <a href="userlogin.py">public</a></li>
                        <li style="display: block;">   <a href="contracter_login.py">contracter</a></li>
</ul>
                    </div>
                </li>
                </ul>
                <ul class="nav navbar-nav navbar-right">
                    <li><a href="Adminlogin.py"><span class="glyphicon glyphicon-user"></span>Admin</a></li>
                    <li><a href="EmpRegister.py"><span class="glyphicon glyphicon-log-in"></span>Reg-Employee</a></li>
                    <li><a href="Emplogin.py"><span class="glyphicon glyphicon-log-in"></span>Login-Employee</a></li>

                </ul>

            </div>

        </div>

    </nav>

    <div class="container">

        <div id="mycarousel" class="carousel slide" data-ride="carousel">



            <ol class="carousel-indicators">
                <li data-target="#mycarousel" data-slide-to="0" class="active"></li>
                <li data-target="#mycarousel" data-slide-to="1"></li>
                <li data-target="#mycarousel" data-slide-to="2"></li>
                <li data-target="#mycarousel" data-slide-to="3"></li>
            </ol>


            <div class="carousel-inner">
                <div class="item active">
                    <img src="./image/elec.jpg" alt="" style="width: 100%;height: 550px;">

                    <div class="carousel-caption">
                        <h1 style="font-family: cursive;font-size: 30px;font-weight: 800;color:white;">Electrician</h1>
                        <p></p>

                    </div>

                </div>
                <div class="item">
                    <img src="./image/painter.jpg" alt="" style="width: 100%;height: 550px;">
                    <div class="carousel-caption">
                        <h3 style="font-family: cursive;font-size: 30px;font-weight: 800;color:white;">Painter</h3>
                        <p></p>

                    </div>

                </div>
                <div class="item">
                    <img src="./image/n4pl.jpg" alt="" style="width: 100%;height: 550px;">
                    <div class="carousel-caption">
                        <h3 style="font-family: cursive;font-size: 30px;font-weight: 800;color:white;">Plumber</h3>
                        <p></p>

                    </div>

                </div>
                <div class="item">
                    <img src="./image/n1.jpg" alt="" style="width: 100%;height: 550px;">
                    <div class="carousel-caption">
                        <h3 style="font-family: cursive;font-size: 30px;font-weight: 800;color:white;">Carpenter</h3>
                        <p></p>

                    </div>

                </div>


            </div> 

            <a class="left carousel-control" href="#mycarousel" data-slide="prev">
                <span class="glyphicon glyphicon-chevron-left"></span>
                <span class="sr-only">previous</span>
            </a>
            <a class="right carousel-control" href="#mycarousel" data-slide="next">
                <span class="glyphicon glyphicon-chevron-right"></span>
                <span class="sr-only">next</span>
            </a>



        </div>

    </div> <br><br>

    <div class="container">
        <div class="row">
            <div class="col-sm-3"> <center>
                <a href=""><img src="./image/car.jpeg" alt="" width="200px" height="200px" class="img-circle"></a>
                <h3 style="text-align: center; color: black; font-weight: bolder;">CARPENTER</h3>
           </center> </div>
            <div class="col-sm-3"> <center>
                <a href=""><img src="./image/elect.jpeg" alt="" width="200px" height="200px" class="img-circle"></a>
                <h3 style="text-align: center; color: black; font-weight: bolder;">ELECTRICIAN</h3>
                        
            </center> </div>
            <div class="col-sm-3"> <center>
                <a href=""><img src="./image/pain.jpeg" alt="" width="200px" height="200px" class="img-circle"></a>
                <h3 style="text-align: center; color: black; font-weight: bolder;">PAINTER</h3>
            </center> </div>
            <div class="col-sm-3"> <center>
                <a href=""><img src="./image/plum.jpg" alt="" width="200px" height="200px" class="img-circle"></a>
                <h3 style="text-align: center; color: black; font-weight: bolder;">PLUMBER</h3>
           </center>  </div>
        </div>
    </div>
    <hr>

    <center>
        <h1 id="yyy"><em>Local Workers In Your Pocket !</em></h1>
    </center>

   
    <pre style="background-color: rgb(211, 199, 185);"><h4 >             We know how hard it is to find qualified local workers for a home or office.
             And random workers you find through random sources may not perform as per your requirement. 
             And internet won't help as Good workers are not good at technology. 
             Nexus will help you reach the qualified workers faster, in your area as per your requirements and budget.
             Whether you need a Carpenter, Plumber, Electrician or Painter, Don't just get a random workers. 
             Get a Neuxs verified by Nexus team.!</h4></pre>
   




</body>

<footer>
    <div class="row">
        <div class="container-fluid">
            <div class="col-md-2">
            </div>

            <div class="col-md-3">
            </div>
            <div class="col-md-3">
                 <a href=""><p>2024 - All rights reserved.</p></a>
                <P>
                  <a href=""><span class="fa fa-instagram"></span></a>
                   <a href=""><span class="fa fa-facebook"></span></a>
                   <a href=""><span class="fa fa-twitter"></span></a>
                   <a href=""><span class="fa fa-whatsapp"></span></a>
                    <a href=""><span class="fa fa-youtube"></span></a>
                    <a href=""><span class="fa fa-linkedin"></span></a>

                </p>

            </div>
            <div class="col-md-3">
            </div>
        </div>
    </div>


</footer>


</html>
""")