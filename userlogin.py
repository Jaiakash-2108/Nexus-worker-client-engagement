#!C:/Users/deepa/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import pymysql
import cgi,cgitb
cgitb.enable()
con=pymysql.connect(host="localhost",user="root",password="",database="nexus",port=3306)
cur=con.cursor()
print("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.7.1/jquery.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
    <title>Document</title>
</head>
<body>
    <style>
        body{
            background-color: black;
            background-repeat: no-repeat;
            background-size: cover;
        }
        label{
            color: white;
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
            
            
     <div class="container-fluid" >
    <div class="row">
    <div class="col-sm-4"></div>
    <div class="col-sm-4" style="border: solid 1px rgb(255, 255, 255); margin-top: 50px;">
        <p style="font-weight: bolder; font-size: 30px;text-align: center;color: white;">Login Form</p>
        <form method="post" enctype="multipart/form-data">
            <div class="form-group">
                <label for="Email">Email</label>
                <input type="Email" name="email" id="email" class="form-control">
            </div>
            <div class="form-group">
                <label for="password">Password</label>
                <input type="password" name="password" id="password" class="form-control">
            </div>
            <div>
                <input type="submit" name="submit" id="submit" value="Submit" class="btn btn-success">
                <input type="submit" name="submit" id="submit" value="Cancel" class="btn btn-danger">
            </div>
            <br>
        </form>
    </div>
    </div>

<footer style="margin-top:330px;">
    <div class="row">
        <div class="container-fluid">

            <div class="col-md-4">
            </div>
            <div class="col-md-4">
            <center>
                 <a href=""><p>2024 - All rights reserved.</p></a>
                <P>
                  <a href=""><span class="fa fa-instagram"></span></a>
                   <a href=""><span class="fa fa-facebook"></span></a>
                   <a href=""><span class="fa fa-twitter"></span></a>
                   <a href=""><span class="fa fa-whatsapp"></span></a>
                    <a href=""><span class="fa fa-youtube"></span></a>
                    <a href=""><span class="fa fa-linkedin"></span></a>

                </p>
                </center>
            </div>
            <div class="col-md-4">
            </div>
        </div>
    </div>


</footer>



</body>

</html> """)

form=cgi.FieldStorage()
email=form.getvalue("email")
password=form.getvalue("password")
submit=form.getvalue("submit")
if submit !=None:
        q = """select id from userregister where email='%s' and password='%s' and customer_type="General Public" """%(email,password)
        cur.execute(q)
        rec=cur.fetchone()
        if rec !=None:
            print("""
            <script>
            alert("login successfully");
            location.href="userdashboard.py?id=%s"
            </script>
            """ %rec[0])
        else:
            print("""
            <script>
            alert("user not found")
            </script>
            """)
