#!/usr/bin/env python3
print("content-type:text/html \r\n\r\n")
import pymysql
import cgi
import cgitb

cgitb.enable()

form = cgi.FieldStorage()
error = form.getvalue("error")

con = pymysql.connect(host="localhost", user="root", password="", database="nexus", port=3306)
cur = con.cursor()

print("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>User Login - Nexus</title>
    
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
    <link rel="stylesheet" href="./css/style.css">
    
    <style>
        body {
            background: linear-gradient(135deg, #1D373D 0%, #00897B 100%);
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 20px;
        }
        
        .login-wrapper {
            width: 100%;
            max-width: 450px;
        }
        
        .login-card {
            background: white;
            border-radius: 10px;
            box-shadow: 0 10px 40px rgba(0,0,0,0.2);
            overflow: hidden;
        }
        
        .login-header {
            background: linear-gradient(135deg, #1D373D 0%, #00897B 100%);
            color: white;
            padding: 40px 30px;
            text-align: center;
        }
        
        .login-header img {
            height: 60px;
            margin-bottom: 15px;
            border-radius: 50%;
        }
        
        .login-header h2 {
            margin: 0;
            font-size: 28px;
            font-weight: 700;
        }
        
        .login-header p {
            margin: 10px 0 0 0;
            opacity: 0.9;
            font-size: 14px;
        }
        
        .login-body {
            padding: 40px 30px;
        }
        
        .form-group {
            margin-bottom: 20px;
        }
        
        .form-group label {
            font-weight: 500;
            color: #2C3E50;
            margin-bottom: 8px;
            display: block;
        }
        
        .form-group input {
            width: 100%;
            padding: 12px 15px;
            border: 1px solid #ECF0F1;
            border-radius: 5px;
            font-size: 14px;
            transition: border-color 0.3s ease;
        }
        
        .form-group input:focus {
            outline: none;
            border-color: #00897B;
            box-shadow: 0 0 0 3px rgba(0, 137, 123, 0.1);
        }
        
        .form-group input::placeholder {
            color: #AED6E1;
        }
        
        .remember-forgot {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 20px;
            font-size: 14px;
        }
        
        .remember-forgot a {
            color: #00897B;
            text-decoration: none;
        }
        
        .remember-forgot a:hover {
            text-decoration: underline;
        }
        
        .btn-login {
            width: 100%;
            padding: 12px;
            background: linear-gradient(135deg, #1D373D 0%, #00897B 100%);
            color: white;
            border: none;
            border-radius: 5px;
            font-size: 16px;
            font-weight: 600;
            cursor: pointer;
            transition: transform 0.2s ease, box-shadow 0.2s ease;
        }
        
        .btn-login:hover {
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(0, 137, 123, 0.3);
        }
        
        .divider {
            text-align: center;
            margin: 30px 0;
            position: relative;
        }
        
        .divider::before {
            content: "";
            position: absolute;
            left: 0;
            right: 0;
            top: 50%;
            height: 1px;
            background: #ECF0F1;
        }
        
        .divider span {
            background: white;
            padding: 0 10px;
            color: #7F8C8D;
            font-size: 14px;
            position: relative;
        }
        
        .signup-link {
            text-align: center;
            margin-top: 20px;
            padding-top: 20px;
            border-top: 1px solid #ECF0F1;
        }
        
        .signup-link p {
            color: #7F8C8D;
            margin: 0;
        }
        
        .signup-link a {
            color: #00897B;
            font-weight: 600;
            text-decoration: none;
        }
        
        .signup-link a:hover {
            text-decoration: underline;
        }
        
        .nav-options {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(100px, 1fr));
            gap: 10px;
            margin-top: 30px;
        }
        
        .nav-options a {
            padding: 10px;
            text-align: center;
            background: #F5F9FB;
            border-radius: 5px;
            text-decoration: none;
            color: #00897B;
            font-size: 12px;
            font-weight: 500;
            transition: background 0.3s ease;
        }
        
        .nav-options a:hover {
            background: #E8F4F8;
        }
        
        .alert {
            border: none;
            border-left: 4px solid #E74C3C;
            background: #F8D7DA;
            color: #721C24;
            padding: 12px 15px;
            border-radius: 5px;
            margin-bottom: 20px;
        }
        
        .alert.success {
            border-left-color: #27AE60;
            background: #D4EDDA;
            color: #155724;
        }
    </style>
</head>
<body>
    <div class="login-wrapper">
        <div class="login-card">
            <div class="login-header">
                <img src="./image/logo.jpg" alt="Nexus Logo">
                <h2>Nexus</h2>
                <p>Worker Engagement Platform</p>
            </div>
            
            <div class="login-body">
                <h3 style="text-align: center; color: #2C3E50; margin-bottom: 30px; font-weight: 600;">
                    Client Login
                </h3>
""")

if error:
    print(f'<div class="alert">{error}</div>')

print("""
                <form method="POST" action="">
                    <div class="form-group">
                        <label for="username">
                            <i class="fa fa-user"></i> Email or Username
                        </label>
                        <input type="text" id="username" name="username" class="form-control" 
                               placeholder="Enter your email or username" required>
                    </div>
                    
                    <div class="form-group">
                        <label for="password">
                            <i class="fa fa-lock"></i> Password
                        </label>
                        <input type="password" id="password" name="password" class="form-control" 
                               placeholder="Enter your password" required>
                    </div>
                    
                    <div class="remember-forgot">
                        <label style="margin: 0;">
                            <input type="checkbox" name="remember"> Remember me
                        </label>
                        <a href="#forgot-password">Forgot password?</a>
                    </div>
                    
                    <button type="submit" class="btn-login">
                        <i class="fa fa-sign-in"></i> Login
                    </button>
                </form>
                
                <div class="divider">
                    <span>Don't have an account?</span>
                </div>
                
                <div class="signup-link">
                    <p>New here? Create your free account</p>
                    <a href="userregister.py" style="display: inline-block; padding: 10px 20px; 
                       background: #F5F9FB; border-radius: 5px; color: #00897B; text-decoration: none; 
                       margin-top: 10px; font-weight: 600;">
                        <i class="fa fa-user-plus"></i> Sign Up
                    </a>
                </div>
                
                <div class="divider" style="margin: 30px 0;">
                    <span>Other Logins</span>
                </div>
                
                <div class="nav-options">
                    <a href="contracter_login.py">
                        <i class="fa fa-user-tie"></i><br>Contractor
                    </a>
                    <a href="Emplogin.py">
                        <i class="fa fa-briefcase"></i><br>Employee
                    </a>
                    <a href="Adminlogin.py">
                        <i class="fa fa-shield"></i><br>Admin
                    </a>
                </div>
                
                <div style="text-align: center; margin-top: 30px; color: #7F8C8D; font-size: 12px;">
                    <p>By logging in, you agree to our Terms of Service and Privacy Policy</p>
                </div>
            </div>
        </div>
    </div>
    
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.7.1/jquery.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>
</body>
</html>
""")

con.close()
