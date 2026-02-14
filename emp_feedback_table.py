#!C:/Users/deepa/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import pymysql
import cgi, cgitb

cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="nexus",port=3306)
cur = con.cursor()
form = cgi.FieldStorage()
pid = form.getvalue("id")

p = """SELECT * FROM emypregister WHERE ID='%s' """ % (pid)
cur.execute(p)
res = cur.fetchall()
name=""
for i in res:
    name=i[1]
print(f"""
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
        ul {{
            margin: 0;
            padding: 0;
        }}

        /* Container for sidebar and content */
        .container {{
            display: flex;
        }}

        /* Sidebar styles */
        .sidebar {{
            width: 250px;
            background-color:rgb(29, 55, 61);
            ;
            overflow-y: auto;
            height: 100vh;
            position: fixed;
            top: 0;
            left: 0;
        }}

        .sidebar h2 {{
            color: white;
            text-align: center;
            padding: 10px;
            margin: 0;
        }}

        .sidebar ul {{
            list-style: none;
            padding: 0;
        }}

        .sidebar ul li {{
            padding: 10px;
            text-align: left;
        }}

        .sidebar ul li a {{
            color: white;
            text-decoration: none;
            display: block;
            transition: background-color 0.3s, color 0.3s;
            font-size: 20px;
        }}

        /* Hover effect for links */
        .sidebar ul li a:hover {{
            background-color: #555;
            color: #fff;
        }}

        /* Dropdown submenu */
        .dropdown-content {{
            display: none;
            padding-left: 20px;
            font-size: 15px;
        }}

        /* Show dropdown content on hover */
        .sidebar ul li:hover .dropdown-content {{
            display: block;
        }}

        /* Content styles */
        .content {{
            flex-grow: 1;
            text-align:center;
            margin-left:120px;


            /* Adjust this to match the sidebar width */
            padding: 16px;

        }}
    </style>
</head>

<body>
    <div class="container">
        <div class="sidebar">
            <h2></h2>
            <ul>
            <li><a href="Empdashboard.py?id=%s">Profile</a></li>
                <li>
                    <a href="#">User_Work<span class="caret"></span></a>
                    <div class="dropdown-content">
                        <a href="emp_work_new.py?id=%s">New</a>
                        <a href="emp_wrk_exs.py?id=%s">Existing</a>

                    </div>
                </li>
                 <li>
                    <a href="#">contracter_worker<span class="caret"></span></a>
                    <div class="dropdown-content">
                        <a href="emp_c_new.py?id=%s">New</a>
                        <a href="emp_c_exis.py?id=%s">Existing</a>

                    </div>
                </li>

"""%(pid,pid,pid,pid,pid))
print("""
                <li>
                    <a href="emp_feedback_table.py?id=%s">Feedback</a>
                </li>
                       <li>
                    <a href="emp_working_history.py?id=%s">Working history</a>
                </li>

                <li> <a href="nexushome.py">Log Out</a></li>
            </ul>
        </div>
        <div class="content">


    <script>
        document.addEventListener('contextmenu', function (e) {{
            e.preventDefault();
        }});
    </script>
</body>

</html>
 <div class="content">""" %(pid,pid))

print("""<h1>Feedback:</h1>""")
print("""
    <table class="table table-bordered" style="border: solid;">
    <tr>
    <th>username</th>
    <th>Useremail</th>
    <th>Userstreet</th>
    <th>Usercity</th>
    <th>Customertype</th>
    <th>Feedback</th>
    </tr>
    """)

q = """select * from feedback_form where  name='%s' """ %(name)
cur.execute(q)
det = cur.fetchall()

for i in det:
        print(f"""
        <tr>
        <td>{i[8]}</td>
        <td>{i[9]}</td>
        <td>{i[10]}</td>
        <td>{i[11]}</td>
        <td>{i[12]}</td>
        <td>{i[4]}</td>
        </tr> 
        """)
print("""</table>""")

