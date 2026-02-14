#!C:/Users/deepa/AppData/Local/Programs/Python/Python311/python.exe
print("Content-Type: text/html\r\n\r\n")
import pymysql
import cgi
import cgitb

cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="nexus",port=3306)
cur = con.cursor()
form = cgi.FieldStorage()
pid = form.getvalue("id")

query = """SELECT * FROM userregister WHERE ID='%s'  """ % (pid)
cur.execute(query)
res = cur.fetchall()
uname = ""
uemail = ""
ucity = ""
ustreet = ""
uidd = ""
c_type = ""
for i in res:
    uname = i[1]
    uemail = i[4]
    ucity = i[8]
    ustreet = i[7]
    uidd = i[0]
    c_type = i[11]

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
            <div class="sidebar">
                <h2></h2>
                <ul>
                    <li><a href="userdashboard.py?id=%s">Profile</a></li>
                    <li><a href="user_workers.py?id=%s">Worker</a></li>
                    <li>
                        <a href="#">Booking <span class="caret"></span></a>
                        <div class="dropdown-content">
                            <a href="booking_new.py?id=%s">New</a>
                            <a href="booking_existing.py?id=%s">Existing</a>
                        </div>
                    </li>
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
                    <li><a href="nexushome.py">Log Out</a></li>
                </ul>
            </div>
            <div class="content">""" % (pid, pid, pid, pid, pid,pid,pid))
    print("""<h1>Feedback:</h1>""")
    print("""
    <table class="table table-bordered" style="border: solid;">
    <tr>
    <th>Id</th>
    <th>Empname</th>
    <th>Designation</th>
    <th>Description</th>
    <th>Rating</th>
    <th>Username</th>
    </tr>
    """)

q = """select * from feedback_form where  username='%s' """ %(uname)
cur.execute(q)
det = cur.fetchall()

for i in det:
        print(f"""
        <tr>
        <td>{i[0]}</td>
        <td>{i[1]}</td>
        <td>{i[2]}</td>
        <td>{i[4]}</td>
        <td>{i[5]}</td>
        <td>{i[8]}</td>
        </tr> 
        """)
print("""</table>""")

print("""<h1>Completed Works:</h1>""")
print("""
<table class="table table-bordered" style="border: solid;" cell-padding>
<tr>
<th>id</th>
<th>empname</th>
<th>empemail</th>
<th>empdesignation</th>
<th>empcity</th>
<th>empstreet</th>
<th>empexperience</th>
<th>Status</th>
<th>Cost</th>
</tr>
""")
t= """select * from booking_details where status="Completed"  and Username='%s' """ %(uname)
cur.execute(t)
rel=cur.fetchall()
for k in rel:
    print(f"""
            <tr>
            <td>{k[0]}</td>
            <td>{k[1]}</td>
            <td>{k[2]}</td>
            <td>{k[3]}</td>
            <td>{k[4]}</td>
            <td>{k[5]}</td>
            <td>{k[6]}</td>
            <td>{k[11]}</td>
            <td>{k[12]}</td>
            </tr> 
            """)
