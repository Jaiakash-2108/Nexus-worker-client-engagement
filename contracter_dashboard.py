#!C:/Users/deepa/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import pymysql
import cgi, cgitb

cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="nexus",port=3306)
cur = con.cursor()
form = cgi.FieldStorage()
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
                    <a href="contrac_dash_wrk.py?id=%s">Worker</a>
                </li>
                <li>
                    <a href="#">Booking <span class="caret"></span></a>
                    <div class="dropdown-content">
                        <a href="contrac_book_new.py?id=%s">New</a>
                        <a href="contrac_book_exis.py?id=%s">Existing</a>

                    </div>
                </li>
            """ % (pid, pid,pid))
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

for y in res:
    userid = y[0]
    print("""
     <center>
      <img src="./media/%s" width="100px" height"100px" style="border-radius:200px";>
      <table>
      <tr>
      <th>Name:</th>
      <td>%s</td>
      </tr><br>
      <tr>
      <th>E-mail:</th>
      <td>%s</td>
      </tr>
      <tr>
      <th>city:</th>
      <td>%s</td>
      </tr>
      <tr>
      <td>
        <button type="button" class="btn btn-info btn-md" style="position:relative; top:50px; left:40px;" data-toggle="modal"
                    data-target="#myModal%s">Change Password</button>
                    </td>
                    </tr>
    </center>
    """ % (y[5], y[1], y[4], y[8], userid))

    print("""
      <div class="row">
        <div class="col-sm-4"></div>
         <div class="col-sm-4" style="text-align: left;">
            <div class="container"> 
                <br>
                <div class="modal fade" id="myModal%s">
                    <div class="modal-dialog">
                        <div class="modal-content">
                            <div class="modal-header">
                                <button type="button" class="close" data-dismiss="modal">&times;
                                </button>
                                <h4 class="modal-title">Create Your New Password</h4>
                            </div>

                            <div class="modal-body">
                                 <form method="post" enctype="multipart/form-data">
                                 <div class="form-group">  
                                    <input type="hidden" name="idd" id="pass" class="form-control" value='%s'>
                                    </div>

                                    <div class="form-group>
                                    <input type="hidden" name="nnn" id="pass" class="form-control" value='%s'>
                                    </div>
                                    <div class="form-group">
                                        <label for="new password">New password</label>
                                        <input type="password" name="pass" id="pass" class="form-control">
                                    </div>
                                    <div class="form-group">
                                        <label for="Re-type password">Re-type password</label>
                                        <input type="password" name="repass" id="repass" class="form-control">
                                    </div>
                                       <div class="form-group">
                                <input type="hidden" class="form-control" name="oldpass" id="oldpass" value='%s'>
                            </div>
                            </div>
                            <div class="modal-footer">
                                <input type="submit" class="btn btn-success" name="upd" value="change">
                            </div>
                          </form>
                        </div>
                    </div>
                </div>
            </div>
        </div>

    </div> 
    """ % (userid, y[4], userid, y[6]))

new = form.getvalue("pass")
renew = form.getvalue("repass")
email = form.getvalue("idd")
uid = form.getvalue("nnn")

old = form.getvalue("oldpass")
upd = form.getvalue("upd")

if upd != None:
    if new == renew:
        if old != new:
            n = """update userregister set password='%s'  where email='%s'""" % (new, email)
            cur.execute(n)

            con.commit()
            print("""
            <html>
            <body>
            <script>
            alert("Your password has been changed successfully");
            location.href="nexushome.py"
            </script>
            </body>
            </html>
            """)
        else:
            print("""
            <html>
            <body>
            <script>
            alert("New password and old password are the same");
            </script>
            </body>
            </html>
            """)
    else:
        print("""
        <html>
        <body>
        <script>
        alert("New password and confirm password are different");
        </script>
        </body>
        </html>
        """)
print("""
    <script>
        document.addEventListener('contextmenu', function (e) {
            e.preventDefault();
        });
    </script>
</body>
</html>
""")