#!C:/Users/deepa/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import pymysql
import cgi, cgitb

cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="nexus",port=3306)
cur = con.cursor()
form = cgi.FieldStorage()
work= form.getvalue("wo")
location= form.getvalue("lo")

pid = form.getvalue("id")

p = """SELECT * FROM userregister WHERE ID='%s' and customer_type="Contracter" """ % (pid)
cur.execute(p)
res = cur.fetchall()

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
            background-color:rgb(29, 55, 61);
            ;
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
            text-align:center;
            margin-left:130px;


            padding: 16px;

        }
    </style>
</head>

<body>
    <div class="container">
        <div class="sidebar">
            <h2></h2>
            <ul>
             <li>
                 <a href="contracter_dashboard.py?id=%s">Profile</a>
             </li>
                 <li>
                    <a href="contrac_dash_wrk.py?id=%s">Worker</a>
                </li>
                <li>
                    <a href="#">Booking <span class="caret"></span></a>
                    <div class="dropdown-content">
                        <a href="contrac_book_new.py?id=%s">New</a>
                        <a href="contrac_book_exis.py?id=%s">Existing</a>

                    </div>
                </li>
            """ % (pid, pid,pid,pid))
print("""
                <li>
                    <a href="#">Feedback <span class="caret"></span></a>
                    <div class="dropdown-content">
                        <a href="contrac_feedback_new.py?id=%s">New</a>
                        <a href="contrac_feedback_exis.py?id=%s">Existing</a>

                    </div>
                </li>
                 <li>
                    <a href="contrac_emp_feedback.py?id=%s">Employee feedback</a>
                </li>
                <li> <a href="nexushome.py">Log Out</a></li>
            </ul>
        </div>
        <div class="content">


    <script>
        document.addEventListener('contextmenu', function (e) {
            e.preventDefault();
        });
    </script>
</body>

</html>
"""%(pid,pid,pid))
print("""
   <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Document</title>
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/css/bootstrap.min.css">
      <script src="https://cdn.jsdelivr.net/npm/jquery@3.7.1/dist/jquery.slim.min.js"></script>
      <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.1/dist/umd/popper.min.js"></script>
      <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/js/bootstrap.bundle.min.js"></script>
    </head>
    <body>
    <div class="container-fluid">
     <div class="row">
    """)
uname = ""
uemail = ""
ucity = ""
ustreet = ""
uidd = ""
customer_type=""
for i in res:
    uname = i[1]
    uemail = i[4]
    ucity = i[8]
    ustreet = i[7]
    uidd = i[0]
    customer_type=i[11]

r = """select * from emypregister where designation='%s' and city='%s' """ % (work, location)
cur.execute(r)
re = cur.fetchall()
fid = ""
epname = ""
for f in re:
    fid = f[0]
    epname = f[1]

    print("""
            <div class="col-sm-4">
                <div class="card" style="width:300px;">
                    <img class="card-img-top" src="./media/%s" alt="Card image" height="200px">
                    <div class="card-body">
                      <h4 class="card-title">%s</h4>
                      <p class="card-text">%s</p>
                       <p class="card-text">Hours:Rs %s</p>
                      <a href="#" id="aaa"  class="btn btn-primary" data-toggle="modal"
                    data-target="#myModal%s">See Profile</a>

                    </div>
                </div>        
          </div>

        """ % (f[5], f[1], f[7], f[14], f[0]))

    print("""
                <div class="modal fade" id="myModal%s">
                    <div class="modal-dialog">
                        <div class="modal-content">
                            <div class="modal-header">
                              <h4 class="modal-title">Details</h4>
                                <button type="button" class="close" data-dismiss="modal">&times;
                                </button>

                            </div>

                            <div class="modal-body">
                                 <center>
                                 <form>
                                    <div class="form-group">  
                                    <input type="text" name="empname" id="empname" class="form-control" value='%s'>
                                    </div>
                                      <div class="form-group">  
                                    <input type="text" name="empemail" id="empemail" class="form-control" value='%s'>
                                    </div>
                                      <div class="form-group">  
                                    <input type="text" name="empdesignation" id="empdesignation" class="form-control" value='%s'>
                                    </div>
                                      <div class="form-group">  
                                    <input type="text" name="empcity" id="empcity" class="form-control" value='%s'>
                                    </div>
                                      <div class="form-group">  
                                    <input type="text" name="empstreet" id="empstreet" class="form-control" value='%s'>
                                    </div>
                                      <div class="form-group">  
                                        <label for="">Experience</label>
                                    <input type="text" name="empexperience" id="empexperience" class="form-control" value='%s'>
                                    </div>
                                      <div class="form-group">  
                                    <input type="hidden" name="username" id="username" class="form-control" value='%s'>
                                    </div>
                                      <div class="form-group">  
                                    <input type="hidden" name="useremail" id="useremail" class="form-control" value='%s'>
                                    </div>
                                      <div class="form-group">  
                                    <input type="hidden" name="userstreet" id="userstreet" class="form-control" value='%s'>
                                    </div>
                                      <div class="form-group">  
                                    <input type="hidden" name="usercity" id="usercity" class="form-control" value='%s'>
                                    </div> 
                                     <div class="form-group">  
                                      <label for="">One hour</label>
                                    <input type="text" name="amount" id="amount" class="form-control" value='%s'>
                                    </div> 
                                     <div class="form-group">  
                                      <label for="">No.of.workers</label>
                                    <input type="number" name="no_of_workers" id="no.of.workers" class="form-control" >
                                    </div> 
                                      <div class="form-group">  
                                    <input type="hidden" name="cstype" id="cstype" class="form-control" value='%s'>
                                    </div>
                                 <input type="hidden" value="%s" name="idd">
                                 <input type="submit" name="sub" class="btn btn-success" value="Book Now">
                                 </form>
                                 </center> 

                        </div>
                    </div>
                </div>
            </div>

    """ % (f[0], f[1], f[4], f[11], f[8], f[7], f[12], uname, uemail, ustreet, ucity, f[14],customer_type, uidd))

submit = form.getvalue("sub")
if submit != None:
    empname = form.getvalue("empname")
    empemail = form.getvalue("empemail")
    empdeignation = form.getvalue("empdesignation")
    empcity = form.getvalue("empcity")
    empstreet = form.getvalue("empstreet")
    empexperience = form.getvalue("empexperience")
    username = form.getvalue("username")
    useremail = form.getvalue("useremail")
    userstreet = form.getvalue("userstreet")
    usercity = form.getvalue("usercity")
    userid = form.getvalue("idd")
    empamount = form.getvalue("amount")
    no_of_worker= form.getvalue("no_of_workers")
    cstype= form.getvalue("cstype")

    q = """ INSERT INTO booking_details(Empname,Empemail, Empdesignation, Empcity, Empstreet, Empexperience, Username,Useremail,Userstreet, Usercity,status,amount,	customer_type,no_of_worker) VALUES('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s',"New",'%s','%s','%s')""" % (
    empname, empemail, empdeignation, empcity, empstreet, empexperience, username, useremail, userstreet, usercity, empamount,cstype,no_of_worker)

    cur.execute(q)
    con.commit()
    print(""""
    <script>
    alert("Booked successfully")
    location.href="contrac_dash_wrk.py?id=%s"
    </script>
    """ % (userid))