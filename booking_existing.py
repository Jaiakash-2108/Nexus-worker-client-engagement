#!C:/Users/deepa/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import pymysql
import cgi, cgitb

cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="nexus",port=3307)
cur = con.cursor()
form = cgi.FieldStorage()
work=form.getvalue("wo")
location=form.getvalue("lo")
pid = form.getvalue("id")

p = """SELECT * FROM userregister WHERE ID='%s' and customer_type="General public"  """ % (pid)
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
        /* Reset some default styles */
        body,
        ul {
            margin: 0;
            padding: 0;
        }

        /* Container for sidebar and content */
        .container {
            display: flex;
        }

        /* Sidebar styles */
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

        /* Hover effect for links */
        .sidebar ul li a:hover {
            background-color: #555;
            color: #fff;
        }

        /* Dropdown submenu */
        .dropdown-content {
            display: none;
            padding-left: 20px;
            font-size: 15px;
        }

        /* Show dropdown content on hover */
        .sidebar ul li:hover .dropdown-content {
            display: block;
        }

        /* Content styles */
        .content {
            flex-grow: 1;
            text-align:center;
            margin-left:180px;

            /* Adjust this to match the sidebar width */
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
                    <a href="userdashboard.py?id=%s">Profile</a>
                </li>
                 <li>
                    <a href="user_workers.py?id=%s">Worker</a>
                </li>
                <li>
                    <a href="#">Booking <span class="caret"></span></a>
                    <div class="dropdown-content">
                        <a href="booking_new.py?id=%s">New</a>
                        <a href="booking_existing.py?id=%s">Existing</a>

                    </div>
                </li>""" % (pid,pid,pid,pid))
print("""
                <li>
                    <a href="#">Feedback <span class="caret"></span></a>
                    <div class="dropdown-content">
                        <a href="feedback_form.py?id=%s">New</a>
                        <a href="feedback_existing.py?id=%s">Existing</a>

                    </div>
                </li>
                <li>
                    <a href="user_emp_feedback.py?id=%s">Employee feedback</a>
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
<table class="table table-bordered" style="border: solid;" cell-padding>
<tr>
<th>Id</th>
<th>Empname</th>
<th>Empemail</th>
<th>Empdesignation</th>
<th>Empcity</th>
<th>Empstreet</th>
<th>Empexperience</th>
<th>Status</th>
<th>Amount</th>
</tr>
""")
uname = ""
for j in res:
    uname = j[1]
    q= """select * from booking_details where status="Accepted" and Username='%s' """ %(uname)
    cur.execute(q)
    det=cur.fetchall()

    for i in det:
        print(f"""
        <tr>
        <td>{i[0]}</td>
        <td>{i[1]}</td>
        <td>{i[2]}</td>
        <td>{i[3]}</td>
        <td>{i[4]}</td>
        <td>{i[5]}</td>
        <td>{i[6]}</td>
        <td>{i[11]}</td>
        <td>{i[12]}</td>
        </tr> 
        """)
    print("""</table>""")