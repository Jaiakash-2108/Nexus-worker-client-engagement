#!C:/Users/deepa/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import pymysql
import cgi, cgitb

cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="nexus",port=3307)
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

idd = ""
for i in res:
    idd = i[0]
    print("""
                    <form>   
                <div class="row">
                    <div class="col-md-2">
                     <input type="hidden" name="uid" id="uid"  class="form-control" autofocus  value="%s"></div>


                    <div class="col-md-4">
                       """ % (idd))
    print("""
                        <input type="text" name="worker" id="wor"  class="form-control" autofocus  placeholder="Designation"></div>
                        <div class="col-md-4">

                        <input type="text" name="location" id="loc"  autofocus class="form-control"  placeholder="Location"></div>
                            <div class="col-md-2">
                        <input type="submit" name="submit" id="sub" value="submit" class="btn btn-success"  style="width:100%"></div>
                        </form>   
                        </div>

                """)
userid = form.getvalue("uid")
worker = form.getvalue("worker")
location = form.getvalue("location")
submit = form.getvalue("submit")

if submit != None:
    h = """select * from emypregister where designation='%s' and city='%s'""" % (worker, location)
    cur.execute(h)
    rec = cur.fetchall()
    print("""
        <script>
        location.href="contract_dash_submit.py?wo=%s&lo=%s&id=%s"
        </script>
        """ % (worker, location, userid))