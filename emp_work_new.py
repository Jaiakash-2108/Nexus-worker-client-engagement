#!C:/Users/deepa/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import pymysql
import cgi, cgitb
import string,random,smtplib

cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="nexus",port=3307)
cur = con.cursor()
form = cgi.FieldStorage()
pid = form.getvalue("id")

p = """SELECT * FROM emypregister WHERE ID='%s' """ % (pid)
cur.execute(p)
res = cur.fetchall()

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
            margin-left:180px;

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
                    <a href="#">Work<span class="caret"></span></a>
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

"""% (pid,pid,pid,pid,pid))
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
"""%(pid,pid))

ename=""
for i in res:
    ename=i[1]

print("""
<form method="post">
<table class="table table-bordered" style="border: solid;">
<tr>
<th>id</th>
<th>username</th>
<th>useremail</th>
<th>userstreet</th>

</tr>
""")


q= """select * from booking_details where status="New" and Empname='%s' and customer_type="General public" """ %(ename)
cur.execute(q)
det=cur.fetchall()
bid=""
for i in det:
    bid=i[0]
    print(f"""
    <tr>
    <td>{i[0]}  </td>
    <td>{i[7]} <input type="hidden" value={i[7]} name="uname"></td>
    <td>{i[8]} <input type="hidden" value={i[8]} name="email"></td>
    <td>{i[9]}</td>   
    <input type="hidden" value={i[1]} name="ename">
    <td><input type="submit" name="accept" value="accept" class="btn btn-success">
    <input type="submit" name="reject" value="reject" class="btn btn-danger"></td>
    </form>
    </tr>
    """)
print("""</table>""")
empname=form.getvalue("ename")
username=form.getvalue("uname")
uemail=form.getvalue("email")
accepted=form.getvalue("accept")
Email=form.getvalue("email")
if accepted !=None:
    q="""update booking_details set status="Accepted" where id='%s' """%(bid)
    cur.execute(q)
    con.commit()
    fromadd = 'jaiakash.it@gmail.com'
    password2 = 'wyzv sldt djtn gwoo'
    toadd = Email
    Subject = """ xxx """
    body = f"""Your Request has been Accepted \n \n"""
    msg = f"""Subject:{Subject}\n\n{body}"""
    Server = smtplib.SMTP('smtp.gmail.com:587')
    Server.ehlo()
    Server.starttls()
    Server.login(fromadd, password2)
    Server.sendmail(fromadd, toadd, msg)
    Server.quit()
    print("""
     <script>
        alert("Accepted");
        </script>
    """)
Reject = form.getvalue("reject")
if Reject!=None:
     Email = form.getvalue("email")
     uname = form.getvalue("uname")
     status = "Reject"
     q1 = f"""update booking_details set Status='{status}' where Empname='{ename}' and Username='{uname}'"""
     cur.execute(q1)
     con.commit()
     fromadd = 'jaiakash.it@gmail.com'
     password2 = 'wyzv sldt djtn gwoo'
     toadd = Email
     Subject = """ xxx """
     body = """Your Request has been Rejected"""
     msg = f"""Subject:{Subject}\n\n{body}"""
     Server = smtplib.SMTP('smtp.gmail.com:587')
     Server.ehlo()
     Server.starttls()
     Server.login(fromadd, password2)
     Server.sendmail(fromadd, toadd, msg)
     Server.quit()
     print("""
         <script>
         alert("Rejected");
         </script>
         """)
