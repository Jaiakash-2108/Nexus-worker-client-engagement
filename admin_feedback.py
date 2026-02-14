#!C:/Users/deepa/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import pymysql
import cgi, cgitb
import smtplib
import random,string

cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="nexus",port=3306)
cur = con.cursor()
form = cgi.FieldStorage()
pid = form.getvalue("id")

p = """SELECT * FROM userregister WHERE ID='%s' """ % (pid)
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
            margin-left:180px;


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
                    <a href="#">Employee<span class="caret"></span></a>
                    <div class="dropdown-content">
                        <a href="admin_emp_new.py">New</a>
                        <a href="admin_emp_exis.py">Existing</a>

                    </div>
                </li>
                 <li>
                    <a href="admin_user.py">Public</a>
                </li>
                 <li>
                    <a href="admin_contracter.py?id=%s">Contracter</a>
                </li>
                <li>
                    <a href="admin_work.py">Work</a>
                </li>
            """)
print("""
                <li>
                    <a href="admin_feedback.py">Feedback</a>
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

""")
print("""
<table class="table table-bordered" style="border: solid;" cell-padding>
<tr>
<th>id</th>
<th>empname</th>
<th>username</th>
<th>description</th>
</tr>
""")
q= """select * from feedback_form """
cur.execute(q)
det=cur.fetchall()

for i in det:
    print(f"""
    <tr>
    <td>{i[0]}</td>
    <td>{i[1]}</td>
    <td>{i[8]}</td>
    <td>{i[4]}</td>
    </tr> 
    """)
print("""</table>""")



