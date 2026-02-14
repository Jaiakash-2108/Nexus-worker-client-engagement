#!C:/Users/deepa/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import cgi, cgitb, pymysql, os

cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="nexus",port=3306)
cur = con.cursor()
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
    <div class="col-md-4"></div>
    <div class="col-md-4" style="padding-top:50px;">
        <form method="post" enctype="multipart/form-data">
            <fieldset>
                <div class="form-group">
                    <label for="name">NAME</label>
                    <input type="text" id="name" name="name" placeholder="name" class="form-control">

                </div>
                <div class="form-group">
                    <label for="DOB">DOB</label>
                    <input type="date" id="dob" name="dob" placeholder="DOB" class="form-control">

                </div>
                <div class="form-group">
                    <label for="gender">Gender</label>
                    <input type="radio" name="Gender" id="male" value="Male">
                    <label for="male">male</label> 
                    <input type="radio" name="Gender" id="female" value="Female">
                    
                    <label for="female">female</label>
                </div>

                <div class="form-group">
                    <label for="email">E-mail</label>
                    <input type="email" name="email" id="email" placeholder="name" class="form-control">

                </div>
                <div>
                    <label for="Aadhar">ID proof</label>
                    <input type="file" name="proof" id="proof">
                </div>
                <br>
                        
                <div class="form-group">
                <label for="street">street</label>
                <input type="text"u8 name="street" id="" placeholder="" class="form-control">
                 </div>               
                 <div class="form-group">
                 <label for="">city</label>
            <select name="city" id="" class="form-control">
            <option disabled selected>select your city</option>
            <option value="Salem">Salem</option>
            <option value="Erode">Erode</option>
            <option value="Chennai">Chennai</option>
            <option value="Namakkal">Namakkal</option>
            <option value="Karur">Karur</option>
            <option value="Trichy">Trichy</option>
            <option value="Madurai">Madurai</option>
            <option value="Covai">Covai</option>
            <option value="Theni">Theni</option>

                </select> 
                 </div>  
                 <div class="form-group">
                <label for="">state</label>
                <input type="text" name="state" id="state" value="Tamil Nadu" readonly class="form-control">  
               </div> 
                 <div class="form-group">
                <label for="">country</label>  
                <input type="text" name="country" id="country" value="India" readonly class="form-control"> <br>
                 </div> 
                 <div class="form-group">
                <label for="">designation</label>  
                <input type="text" name="designation" id="designation" value=""  class="form-control"> <br>
                 </div> 
                 <div class="form-group">
                <label for="">Experience</label>  
                <input type="text" name="experience" id="experience" value=""  class="form-control"> <br>
                 </div>
                    <div class="form-group">
                <label for="">Amount</label>  
                <input type="number" name="amount" id="amount" value="" placeholder="one hour"  class="form-control"> <br>
                 </div> 
                <div class="form-group">
                    <input type="submit" name="sub" id="submit" value="register" class="btn btn-success">
                    <input type="reset" name="cancel" id="cancel" value="cancel" class="btn btn-danger">

                </div>
            </fieldset>
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


</html>
""")
form = cgi.FieldStorage()
if len(form) != 0:
    submit = form.getvalue("sub")
    if submit != None:
        pname = form.getvalue("name")
        pdob = form.getvalue("dob")
        pgender = form.getvalue("Gender")
        pemail = form.getvalue("email")
        proof = form['proof']

        pstreet = form.getvalue("street")
        pcity = form.getvalue("city")
        pstate = form.getvalue("state")
        pcountry = form.getvalue("country")
        pdesignation=form.getvalue("designation")
        pexperience = form.getvalue("experience")
        pamount = form.getvalue("amount")
        status="new"
        if proof.filename:
            fn = os.path.basename(proof.filename)
            open("media/" + fn, "wb").write(proof.file.read())
            q = """insert into emypregister(name,dob,Gender,email,proof,street,city,state,country,designation,experience,Status,amount) 
            values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"""%(pname,pdob,pgender,pemail,fn,pstreet,pcity,pstate,pcountry,pdesignation,pexperience,status,pamount)

            cur.execute(q)
            con.commit()
            print("""
            <script>
            alert("values inserted successfully");
            </script>
            """)
