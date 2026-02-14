#!C:/Users/deepa/AppData/Local/Programs/Python/Python311/python.exe
print("Content-Type: text/html\r\n\r\n")
import pymysql
import cgi
import cgitb
cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="nexus",port=3307)
cur = con.cursor()
form = cgi.FieldStorage()
pid = form.getvalue("id")

query = """SELECT * FROM userregister WHERE id='%s'  """ % (pid)
cur.execute(query)
res = cur.fetchall()
uname=""
uemail=""
ucity=""
ustreet=""
uidd=""
c_type=""
for i in res:
    uname=i[1]
    uemail=i[4]
    ucity=i[8]
    ustreet=i[7]
    uidd=i[0]
    c_type=i[11]

    print("""
    <!DOCTYPE html>
    <html lang="en">
    
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Dashboard</title>
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.7.1/jquery.min.js"></script>
        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>
        <style>
            body,
            ul {
                margin: 0;
                padding: 0;
            }
    
            .container {
                display: flex;
            }
    
            .sidebar {
                width: 250px;
                background-color: rgb(29, 55, 61);
                overflow-y: auto;
                height: 100vh;
                position: fixed;
                top: 0;
                left: 0;
            }
    
            .sidebar h2 {
                color: white;
                text-align: center;
                padding: 10px;
                margin: 0;
            }
    
            .sidebar ul {
                list-style: none;
                padding: 0;
            }
    
            .sidebar ul li {
                padding: 10px;
                text-align: left;
            }
    
            .sidebar ul li a {
                color: white;
                text-decoration: none;
                display: block;
                transition: background-color 0.3s, color 0.3s;
                font-size: 20px;
            }
    
            .sidebar ul li a:hover {
                background-color: #555;
                color: #fff;
            }
    
            .dropdown-content {
                display: none;
                padding-left: 20px;
                font-size: 15px;
            }
    
            .sidebar ul li:hover .dropdown-content {
                display: block;
            }
    
            .content {
                flex-grow: 1;
                text-align: center;
                margin-left: 250px;
                /* Adjust to match the sidebar width */
                padding: 16px;
            }
        </style>
    </head>
    
    <body>
        <div class="container">
            """)
    print("""
            <div class="content">
                <form method="post" enctype="multipart/form-data">
                    <fieldset>
                        <div class="form-group">
                            <label for="name">Name</label>
                            <input type="text" id="name" name="name" class="form-control">
                        </div>
                        <div class="form-group">
                            <label for="designation">Designation</label>
                            <input type="text" id="designation" name="designation" class="form-control">
                        </div>
                        <div class="form-group">
                            <label for="workingdays">Working Days</label>
                            <input type="number" name="workingdays" id="workingdays" class="form-control">
                        </div>
                        <div class="form-group">
                            <label for="description">Description</label>
                            <input type="text" name="description" id="description" class="form-control">
                        </div>
                        <div class="form-group">
                            <label for="rating">Rating</label>
                            <select name="rating" id="rating" class="form-control">
                                <option value="1">1</option>
                                <option value="2">2</option>
                                <option value="3">3</option>
                                <option value="4">4</option>
                                <option value="5">5</option>
                            </select>
                        </div>
                        <div class="form-group">
                            <label for="street">Street</label>
                            <input type="text" name="street" id="street" class="form-control">
                        </div>
                        <div class="form-group">
                            <label for="city">City</label>
                            <select name="city" id="city" class="form-control">
                                <option disabled selected>Select your city</option>
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
                            <input type="hidden" name="username" id="username" class="form-control" value='%s'>
                            <input type="hidden" name="useremail" id="useremail" class="form-control" value='%s'>
                            <input type="hidden" name="userstreet" id="userstreet" class="form-control" value='%s'>
                            <input type="hidden" name="usercity" id="usercity" class="form-control" value='%s'>
                            <input type="hidden" value="%s" name="idd">
                        </div>
                        <div class="form-group">
                            <input type="hidden" name="customer_type" id="cs_type" value='%s' class="form-control">
                        </div>
                        <input type="submit" name="sub" class="btn btn-success" value="Submit">
                    </fieldset>
                </form>
            </div>
        </div>
        <script>
            document.addEventListener('contextmenu', function (e) {
                e.preventDefault();
            });
        </script>
    </body>
    
    </html>
    """ % (uname,uemail,ustreet,ucity,pid,c_type))

submit=form.getvalue("sub")
if submit !=None:
    name=form.getvalue("name")
    designation = form.getvalue("designation")
    workingdays=form.getvalue("workingdays")
    description = form.getvalue("description")
    rating = form.getvalue("rating")
    street = form.getvalue("street")
    city = form.getvalue("city")
    username = form.getvalue("username")
    useremail = form.getvalue("useremail")
    userstreet = form.getvalue("userstreet")
    usercity = form.getvalue("usercity")
    userid = form.getvalue("idd")
    cs_type= form.getvalue("customer_type")

    q=""" INSERT INTO feedback_form(name, designation, workingdays, description, rating, street, city, username, useremail, userstreet, usercity,customer_type) VALUES('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s') """ % (name,designation,workingdays,description,rating,street,city,username,useremail,userstreet,usercity, cs_type)
    cur.execute(q)
    con.commit()
    print(""""
      <script>
      alert("Submit successfully")
      location.href="feedback_form.py?id=%s"
      </script>
      """%(userid))


