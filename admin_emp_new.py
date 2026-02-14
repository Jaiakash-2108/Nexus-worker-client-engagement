#!C:/Users/deepa/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import pymysql
import cgi, cgitb
import smtplib
import random,string

cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="nexus",port=3307)
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

print("""<table class="table table border" style="margin-left:30px">
<tr>
<th>id</th>
<th>name</th>
<th>dob</th>
<th>gender</th>
<th>email</th>
<th>proof</th>

<th>street</th>
<th>city</th>
<th>state</th>
<th>country</th>
<th>designation</th>
<th>experience</th>
<th>status</th>
</tr>""")

q="""select * from emypregister where status="new" """
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
<td> <img src="./media/{i[5]}" height=100px width=100px></td>

<td>{i[7]}</td>
<td>{i[8]}</td> 
<td>{i[9]}</td>
<td>{i[10]}</td>
<td>{i[11]}</td>
<td>{i[12]}</td>

<form method="post">
<input type="hidden" value="{i[4]}" name="email">
<td><input type="submit" name="accept" value="accept" class="btn btn-success">
<input type="submit" name="reject" value="reject" class="btn btn-danger"></td>


</tr>
</form>
""")
print("""</table>""")

def gen_password(len):
    characters=string.digits
    random_chars=random.choices(characters,k=len)
    return '' .join(random_chars)
password=gen_password(5)


Email=form.getvalue("email")
Accept=form.getvalue("accept")
if Accept!=None:
    q1 = """update emypregister set Status='confirmed', password='%s' where email='%s' """%(password,Email)
    cur.execute(q1)
    con.commit()
    fromadd = 'jaiakash.it@gmail.com'
    ppassword = 'wyzv sldt djtn gwoo'
    toadd = Email
    Subject = """ Authentication from nexus"""
    body = f"""you are selected \n \n Your Password is {password}"""
    msg = f"""Subject:{Subject}\n\n{body}"""
    Server = smtplib.SMTP('smtp.gmail.com', 587)
    Server.ehlo()
    Server.starttls()
    Server.login(fromadd, ppassword)
    Server.sendmail(fromadd, toadd, msg)
    Server.quit()
    print("""
        <script>
        alert("password updated and mail has been sent");
        </script>
        """)
Reject=form.getvalue("reject")
if Reject!=None:
    q1 = """update emypregister set Status='rejected' where email='%s' """%(Email)
    cur.execute(q1)
    con.commit()
    fromadd = 'jaiakash.it@gmail.com'
    password2 = 'wyzv sldt djtn gwoo'
    toadd = Email
    Subject = """Authentication from nexus"""
    body ="""Your Request has been Rejected"""
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


