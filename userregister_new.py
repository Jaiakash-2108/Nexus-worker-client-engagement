#!/usr/bin/env python3
print("content-type:text/html \r\n\r\n")
import pymysql
import cgi
import cgitb

cgitb.enable()

form = cgi.FieldStorage()
success = form.getvalue("success")
error = form.getvalue("error")

con = pymysql.connect(host="localhost", user="root", password="", database="nexus", port=3306)
cur = con.cursor()

print("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>User Registration - Nexus</title>
    
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
    <link rel="stylesheet" href="./css/style.css">
    
    <style>
        .registration-container {
            max-width: 600px;
            margin: 40px auto;
            background: white;
            padding: 40px;
            border-radius: 10px;
            box-shadow: 0 2px 15px rgba(0,0,0,0.1);
        }
        
        .registration-header {
            text-align: center;
            margin-bottom: 40px;
            padding-bottom: 20px;
            border-bottom: 2px solid #ECF0F1;
        }
        
        .registration-header h2 {
            color: #1D373D;
            font-size: 32px;
            font-weight: 700;
            margin: 0;
        }
        
        .registration-header p {
            color: #7F8C8D;
            margin: 10px 0 0 0;
        }
        
        .form-group label {
            font-weight: 500;
            color: #2C3E50;
        }
        
        .form-group input,
        .form-group select,
        .form-group textarea {
            border: 1px solid #ECF0F1;
            border-radius: 5px;
            transition: border-color 0.3s ease;
        }
        
        .form-group input:focus,
        .form-group select:focus,
        .form-group textarea:focus {
            outline: none;
            border-color: #00897B;
            box-shadow: 0 0 0 3px rgba(0, 137, 123, 0.1);
        }
        
        .form-row {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 20px;
        }
        
        .form-row.full {
            grid-template-columns: 1fr;
        }
        
        .file-upload {
            position: relative;
            display: inline-block;
            width: 100%;
        }
        
        .file-upload input[type="file"] {
            display: none;
        }
        
        .file-upload-label {
            display: block;
            padding: 12px 15px;
            background: #F5F9FB;
            border: 2px dashed #00897B;
            border-radius: 5px;
            text-align: center;
            cursor: pointer;
            transition: all 0.3s ease;
            color: #00897B;
            font-weight: 500;
        }
        
        .file-upload-label:hover {
            background: #E8F4F8;
            border-color: #00897B;
        }
        
        .file-upload input[type="file"]:focus ~ label {
            background: #E8F4F8;
        }
        
        .terms-checkbox {
            padding: 15px;
            background: #F5F9FB;
            border-radius: 5px;
            margin: 20px 0;
        }
        
        .terms-checkbox input[type="checkbox"] {
            margin-right: 10px;
        }
        
        .terms-checkbox label {
            margin: 0;
            font-weight: normal;
        }
        
        .terms-checkbox a {
            color: #00897B;
            text-decoration: none;
        }
        
        .btn-register {
            width: 100%;
            padding: 12px;
            background: linear-gradient(135deg, #1D373D 0%, #00897B 100%);
            color: white;
            border: none;
            border-radius: 5px;
            font-size: 16px;
            font-weight: 600;
            cursor: pointer;
            margin-top: 20px;
            transition: transform 0.2s ease;
        }
        
        .btn-register:hover {
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(0, 137, 123, 0.3);
        }
        
        .login-link {
            text-align: center;
            margin-top: 20px;
            color: #7F8C8D;
        }
        
        .login-link a {
            color: #00897B;
            font-weight: 600;
            text-decoration: none;
        }
        
        .alert {
            border: none;
            border-left: 4px solid;
            border-radius: 5px;
            padding: 12px 15px;
            margin-bottom: 20px;
        }
        
        .alert.success {
            border-left-color: #27AE60;
            background: #D4EDDA;
            color: #155724;
        }
        
        .alert.error {
            border-left-color: #E74C3C;
            background: #F8D7DA;
            color: #721C24;
        }
        
        @media (max-width: 768px) {
            .form-row {
                grid-template-columns: 1fr;
            }
            
            .registration-container {
                margin: 20px;
                padding: 20px;
            }
        }
    </style>
</head>
<body style="background-color: #F5F9FB;">
    <div class="registration-container">
        <div class="registration-header">
            <h2><i class="fa fa-user-plus"></i> Register as Client</h2>
            <p>Create your account and start finding workers</p>
        </div>
        
        <!-- Alerts -->
""")

if success:
    print(f'<div class="alert success"><i class="fa fa-check"></i> {success}</div>')
if error:
    print(f'<div class="alert error"><i class="fa fa-times"></i> {error}</div>')

print("""
        <form method="POST" action="" enctype="multipart/form-data">
            <!-- Full Name -->
            <div class="form-row">
                <div class="form-group">
                    <label for="fname">
                        <i class="fa fa-user"></i> First Name *
                    </label>
                    <input type="text" id="fname" name="fname" class="form-control" 
                           placeholder="First name" required>
                </div>
                <div class="form-group">
                    <label for="lname">
                        <i class="fa fa-user"></i> Last Name *
                    </label>
                    <input type="text" id="lname" name="lname" class="form-control" 
                           placeholder="Last name" required>
                </div>
            </div>
            
            <!-- Email & Phone -->
            <div class="form-row">
                <div class="form-group">
                    <label for="email">
                        <i class="fa fa-envelope"></i> Email *
                    </label>
                    <input type="email" id="email" name="email" class="form-control" 
                           placeholder="your@email.com" required>
                </div>
                <div class="form-group">
                    <label for="phone">
                        <i class="fa fa-phone"></i> Phone Number
                    </label>
                    <input type="tel" id="phone" name="phone" class="form-control" 
                           placeholder="(555) 123-4567">
                </div>
            </div>
            
            <!-- Date of Birth & Gender -->
            <div class="form-row">
                <div class="form-group">
                    <label for="dob">
                        <i class="fa fa-calendar"></i> Date of Birth *
                    </label>
                    <input type="date" id="dob" name="dob" class="form-control" required>
                </div>
                <div class="form-group">
                    <label for="gender">
                        <i class="fa fa-mars"></i> Gender *
                    </label>
                    <select id="gender" name="gender" class="form-control" required>
                        <option value="">-- Select --</option>
                        <option value="Male">Male</option>
                        <option value="Female">Female</option>
                        <option value="Other">Other</option>
                    </select>
                </div>
            </div>
            
            <!-- Address -->
            <div class="form-row">
                <div class="form-group">
                    <label for="street">
                        <i class="fa fa-road"></i> Street Address *
                    </label>
                    <input type="text" id="street" name="street" class="form-control" 
                           placeholder="Street address" required>
                </div>
                <div class="form-group">
                    <label for="city">
                        <i class="fa fa-map-marker"></i> City *
                    </label>
                    <input type="text" id="city" name="city" class="form-control" 
                           placeholder="City" required>
                </div>
            </div>
            
            <!-- State & Country -->
            <div class="form-row">
                <div class="form-group">
                    <label for="state">
                        <i class="fa fa-map"></i> State/Province
                    </label>
                    <input type="text" id="state" name="state" class="form-control" 
                           placeholder="State">
                </div>
                <div class="form-group">
                    <label for="country">
                        <i class="fa fa-globe"></i> Country *
                    </label>
                    <input type="text" id="country" name="country" class="form-control" 
                           placeholder="Country" required>
                </div>
            </div>
            
            <!-- ID Proof -->
            <div class="form-row full">
                <div class="form-group">
                    <label>
                        <i class="fa fa-file"></i> Identity Proof Document *
                    </label>
                    <div class="file-upload">
                        <input type="file" id="proof" name="proof" accept="image/*,.pdf" required>
                        <label for="proof" class="file-upload-label">
                            <i class="fa fa-cloud-upload"></i><br>
                            Click to upload or drag file (PDF, JPG, PNG)
                        </label>
                    </div>
                    <small style="color: #7F8C8D; display: block; margin-top: 5px;">
                        Max file size: 5MB
                    </small>
                </div>
            </div>
            
            <!-- Password -->
            <div class="form-row">
                <div class="form-group">
                    <label for="password">
                        <i class="fa fa-lock"></i> Password *
                    </label>
                    <input type="password" id="password" name="password" class="form-control" 
                           placeholder="Create a strong password" required>
                    <small style="color: #7F8C8D;">
                        At least 8 characters, including uppercase, lowercase, and numbers
                    </small>
                </div>
                <div class="form-group">
                    <label for="confirm_password">
                        <i class="fa fa-lock"></i> Confirm Password *
                    </label>
                    <input type="password" id="confirm_password" name="confirm_password" 
                           class="form-control" placeholder="Confirm password" required>
                </div>
            </div>
            
            <!-- Bio -->
            <div class="form-row full">
                <div class="form-group">
                    <label for="bio">
                        <i class="fa fa-pencil"></i> About You
                    </label>
                    <textarea id="bio" name="bio" class="form-control" 
                              placeholder="Tell us about yourself (optional)" rows="3"></textarea>
                </div>
            </div>
            
            <!-- Terms & Conditions -->
            <div class="terms-checkbox">
                <input type="checkbox" id="terms" name="terms" required>
                <label for="terms">
                    I agree to the <a href="#" target="_blank">Terms of Service</a> and 
                    <a href="#" target="_blank">Privacy Policy</a>
                </label>
            </div>
            
            <!-- Submit Button -->
            <button type="submit" class="btn-register">
                <i class="fa fa-user-plus"></i> Create Account
            </button>
            
            <!-- Login Link -->
            <div class="login-link">
                Already have an account? 
                <a href="userlogin.py">Login here</a>
            </div>
        </form>
    </div>
    
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.7.1/jquery.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>
    
    <script>
        // Drag and drop file upload
        const fileUpload = document.querySelector('.file-upload-label');
        const fileInput = document.querySelector('#proof');
        
        fileUpload.addEventListener('dragover', (e) => {
            e.preventDefault();
            fileUpload.style.background = '#E8F4F8';
        });
        
        fileUpload.addEventListener('dragleave', () => {
            fileUpload.style.background = '#F5F9FB';
        });
        
        fileUpload.addEventListener('drop', (e) => {
            e.preventDefault();
            fileUpload.style.background = '#F5F9FB';
            fileInput.files = e.dataTransfer.files;
        });
        
        // Form validation
        document.querySelector('form').addEventListener('submit', function(e) {
            const password = document.querySelector('#password').value;
            const confirmPassword = document.querySelector('#confirm_password').value;
            
            if(password !== confirmPassword) {
                e.preventDefault();
                alert('Passwords do not match!');
                return false;
            }
            
            if(password.length < 8) {
                e.preventDefault();
                alert('Password must be at least 8 characters long!');
                return false;
            }
        });
    </script>
</body>
</html>
""")

con.close()
