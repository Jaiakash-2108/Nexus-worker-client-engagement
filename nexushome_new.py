#!/usr/bin/env python3
#!C:/Users/deepa/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import pymysql
import cgitb
cgitb.enable()

con = pymysql.connect(host="localhost", user="root", password="", database="nexus", port=3306)
cur = con.cursor()

print("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Nexus - Worker & Client Engagement Platform</title>
    
    <!-- Bootstrap -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
    <!-- Font Awesome -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
    <!-- Custom CSS -->
    <link rel="stylesheet" href="./css/style.css">
    
    <style>
        .navbar-header {
            display: flex;
            align-items: center;
        }
        
        .navbar-brand {
            display: flex;
            align-items: center;
            gap: 10px;
        }
        
        .navbar-brand img {
            height: 50px;
            border-radius: 50%;
        }
    </style>
</head>
<body>
    <!-- Navigation Bar -->
    <nav class="navbar navbar-default">
        <div class="container-fluid">
            <div class="navbar-header">
                <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#navbarMenu">
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                </button>
                <a class="navbar-brand" href="nexushome.py">
                    <img src="./image/logo.jpg" alt="Nexus Logo">
                    <span style="color: #1D373D; font-weight: 700; font-size: 24px;">Nexus</span>
                </a>
            </div>
            
            <div class="collapse navbar-collapse" id="navbarMenu">
                <ul class="nav navbar-nav">
                    <li><a href="#services"><i class="fa fa-briefcase"></i> Services</a></li>
                    <li><a href="#how-it-works"><i class="fa fa-cog"></i> How It Works</a></li>
                </ul>
                
                <ul class="nav navbar-nav navbar-right">
                    <li class="dropdown">
                        <a href="#" class="dropdown-toggle" data-toggle="dropdown">
                            <i class="fa fa-user-plus"></i> Register <span class="caret"></span>
                        </a>
                        <ul class="dropdown-menu">
                            <li><a href="userregister.py"><i class="fa fa-user"></i> As Worker</a></li>
                            <li><a href="EmpRegister.py"><i class="fa fa-briefcase"></i> As Employee</a></li>
                            <li class="divider"></li>
                            <li><a href="userregister.py"><i class="fa fa-building"></i> As Client</a></li>
                        </ul>
                    </li>
                    <li class="dropdown">
                        <a href="#" class="dropdown-toggle" data-toggle="dropdown">
                            <i class="fa fa-sign-in"></i> Login <span class="caret"></span>
                        </a>
                        <ul class="dropdown-menu">
                            <li><a href="userlogin.py"><i class="fa fa-user"></i> Client Login</a></li>
                            <li><a href="contracter_login.py"><i class="fa fa-user-tie"></i> Contractor Login</a></li>
                            <li><a href="Emplogin.py"><i class="fa fa-briefcase"></i> Employee Login</a></li>
                            <li class="divider"></li>
                            <li><a href="Adminlogin.py"><i class="fa fa-shield"></i> Admin Login</a></li>
                        </ul>
                    </li>
                </ul>
            </div>
        </div>
    </nav>

    <!-- Hero Section -->
    <section class="hero-section">
        <div class="container">
            <div class="hero-content">
                <h1 class="hero-title">
                    <i class="fa fa-handshake-o"></i> Nexus
                </h1>
                <p class="hero-subtitle">
                    Connect skilled workers with clients for seamless project engagement
                </p>
                <div style="margin-top: 40px;">
                    <a href="userregister.py" class="btn hero-btn btn-primary-hero">
                        <i class="fa fa-user-plus"></i> Find Workers
                    </a>
                    <a href="EmpRegister.py" class="btn hero-btn btn-secondary-hero">
                        <i class="fa fa-briefcase"></i> Offer Services
                    </a>
                </div>
            </div>
        </div>
    </section>

    <!-- Features Section -->
    <section id="services" class="mt-40 mb-40">
        <div class="container">
            <div style="text-align: center; margin-bottom: 50px;">
                <h2 style="color: #1D373D; font-size: 36px; font-weight: 700; margin-bottom: 10px;">
                    Why Choose Nexus?
                </h2>
                <p style="color: #7F8C8D; font-size: 16px;">
                    A comprehensive platform to connect and manage professional services
                </p>
            </div>

            <div class="row">
                <div class="col-md-4 col-sm-6">
                    <div class="feature-card">
                        <div class="card-icon">
                            <i class="fa fa-search"></i>
                        </div>
                        <h3 class="card-title">Find Perfect Workers</h3>
                        <p class="card-text">
                            Browse through a vetted list of skilled workers across various professions. Check ratings, reviews, and experience.
                        </p>
                    </div>
                </div>

                <div class="col-md-4 col-sm-6">
                    <div class="feature-card">
                        <div class="card-icon">
                            <i class="fa fa-calendar-check-o"></i>
                        </div>
                        <h3 class="card-title">Easy Booking</h3>
                        <p class="card-text">
                            Simple and transparent booking process. Schedule jobs, track progress, and manage payments all in one place.
                        </p>
                    </div>
                </div>

                <div class="col-md-4 col-sm-6">
                    <div class="feature-card">
                        <div class="card-icon">
                            <i class="fa fa-star"></i>
                        </div>
                        <h3 class="card-title">Trust & Safety</h3>
                        <p class="card-text">
                            Verified profiles, secure transactions, and customer feedback system. Your satisfaction is our priority.
                        </p>
                    </div>
                </div>

                <div class="col-md-4 col-sm-6">
                    <div class="feature-card">
                        <div class="card-icon">
                            <i class="fa fa-comments"></i>
                        </div>
                        <h3 class="card-title">Direct Communication</h3>
                        <p class="card-text">
                            Communicate directly with workers/clients. Share details, updates, and feedback throughout the service.
                        </p>
                    </div>
                </div>

                <div class="col-md-4 col-sm-6">
                    <div class="feature-card">
                        <div class="card-icon">
                            <i class="fa fa-shield"></i>
                        </div>
                        <h3 class="card-title">Secure Payments</h3>
                        <p class="card-text">
                            Safe payment processing with protection for both clients and workers. Release funds after job completion.
                        </p>
                    </div>
                </div>

                <div class="col-md-4 col-sm-6">
                    <div class="feature-card">
                        <div class="card-icon">
                            <i class="fa fa-bar-chart"></i>
                        </div>
                        <h3 class="card-title">Track & Manage</h3>
                        <p class="card-text">
                            Real-time updates, work history, and performance metrics. Everything you need to manage jobs efficiently.
                        </p>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Services Section -->
    <section class="mt-40 mb-40" style="background-color: white; padding: 40px 0;">
        <div class="container">
            <div style="text-align: center; margin-bottom: 50px;">
                <h2 style="color: #1D373D; font-size: 36px; font-weight: 700; margin-bottom: 10px;">
                    Our Services
                </h2>
                <p style="color: #7F8C8D; font-size: 16px;">
                    From construction to cleaning, find professionals for any job
                </p>
            </div>

            <div class="row">
                <div class="col-md-3 col-sm-6">
                    <div class="service-card">
                        <img src="./image/car.jpeg" alt="Carpenter">
                        <h3 class="card-title"><i class="fa fa-hammer"></i> Carpentry</h3>
                        <p class="card-text">Expert carpenters for construction, furniture, and renovations.</p>
                    </div>
                </div>

                <div class="col-md-3 col-sm-6">
                    <div class="service-card">
                        <img src="./image/elec.jpg" alt="Electrician">
                        <h3 class="card-title"><i class="fa fa-lightbulb-o"></i> Electrical</h3>
                        <p class="card-text">Professional electricians for installations and repairs.</p>
                    </div>
                </div>

                <div class="col-md-3 col-sm-6">
                    <div class="service-card">
                        <img src="./image/pain.jpeg" alt="Painter">
                        <h3 class="card-title"><i class="fa fa-paint-brush"></i> Painting</h3>
                        <p class="card-text">Skilled painters for interior and exterior painting projects.</p>
                    </div>
                </div>

                <div class="col-md-3 col-sm-6">
                    <div class="service-card">
                        <img src="./image/clean.jpeg" alt="Cleaning">
                        <h3 class="card-title"><i class="fa fa-home"></i> Cleaning</h3>
                        <p class="card-text">Professional cleaning services for homes and offices.</p>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- How It Works Section -->
    <section id="how-it-works" class="mt-40 mb-40">
        <div class="container">
            <div style="text-align: center; margin-bottom: 50px;">
                <h2 style="color: #1D373D; font-size: 36px; font-weight: 700; margin-bottom: 10px;">
                    How It Works
                </h2>
            </div>

            <div class="row">
                <div class="col-md-4">
                    <div style="text-align: center; margin-bottom: 30px;">
                        <div style="background-color: #1D373D; color: white; width: 60px; height: 60px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 24px; margin: 0 auto 20px; font-weight: 700;">
                            1
                        </div>
                        <h3 style="color: #1D373D; font-weight: 600;">Create Account</h3>
                        <p style="color: #7F8C8D;">
                            Sign up as a client or worker. Complete your profile with relevant details and qualifications.
                        </p>
                    </div>
                </div>

                <div class="col-md-4">
                    <div style="text-align: center; margin-bottom: 30px;">
                        <div style="background-color: #00897B; color: white; width: 60px; height: 60px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 24px; margin: 0 auto 20px; font-weight: 700;">
                            2
                        </div>
                        <h3 style="color: #1D373D; font-weight: 600;">Browse & Connect</h3>
                        <p style="color: #7F8C8D;">
                            Search for professionals or list your services. Connect with potential clients or workers.
                        </p>
                    </div>
                </div>

                <div class="col-md-4">
                    <div style="text-align: center; margin-bottom: 30px;">
                        <div style="background-color: #FF6F61; color: white; width: 60px; height: 60px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 24px; margin: 0 auto 20px; font-weight: 700;">
                            3
                        </div>
                        <h3 style="color: #1D373D; font-weight: 600;">Book & Complete</h3>
                        <p style="color: #7F8C8D;">
                            Book services, track progress, and provide feedback. Pay securely after job completion.
                        </p>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- CTA Section -->
    <section style="background: linear-gradient(135deg, #1D373D 0%, #00897B 100%); color: white; padding: 60px 20px; text-align: center; margin-top: 40px;">
        <div class="container">
            <h2 style="font-size: 32px; font-weight: 700; margin-bottom: 20px;">
                Ready to Get Started?
            </h2>
            <p style="font-size: 18px; margin-bottom: 30px; opacity: 0.95;">
                Join thousands of satisfied clients and workers using Nexus
            </p>
            <a href="userregister.py" class="btn" style="background-color: #FF6F61; color: white; padding: 12px 30px; font-size: 16px; border-radius: 5px; margin-right: 10px;">
                <i class="fa fa-user-plus"></i> Register Now
            </a>
            <a href="userlogin.py" class="btn" style="background-color: white; color: #1D373D; padding: 12px 30px; font-size: 16px; border-radius: 5px;">
                <i class="fa fa-sign-in"></i> Login
            </a>
        </div>
    </section>

    <!-- Footer -->
    <footer style="background-color: #1D373D; color: white; padding: 40px 20px; margin-top: 40px;">
        <div class="container">
            <div class="row">
                <div class="col-md-4">
                    <h4 style="font-weight: 700; margin-bottom: 15px;">About Nexus</h4>
                    <p>Connecting skilled workers with clients for seamless project engagement and professional service delivery.</p>
                </div>
                <div class="col-md-4">
                    <h4 style="font-weight: 700; margin-bottom: 15px;">Quick Links</h4>
                    <ul style="list-style: none; padding: 0;">
                        <li><a href="userregister.py" style="color: #00897B; text-decoration: none;">Register as Worker</a></li>
                        <li><a href="userlogin.py" style="color: #00897B; text-decoration: none;">Find Workers</a></li>
                        <li><a href="Adminlogin.py" style="color: #00897B; text-decoration: none;">Admin</a></li>
                    </ul>
                </div>
                <div class="col-md-4">
                    <h4 style="font-weight: 700; margin-bottom: 15px;">Contact</h4>
                    <p>
                        <i class="fa fa-envelope"></i> support@nexus.com<br>
                        <i class="fa fa-phone"></i> 1-800-NEXUS-HQ<br>
                        <i class="fa fa-map-marker"></i> Globally Available
                    </p>
                </div>
            </div>
            <hr style="border-color: rgba(255,255,255,0.1); margin: 20px 0;">
            <div style="text-align: center; color: rgba(255,255,255,0.7);">
                <p>&copy; 2026 Nexus. All rights reserved. | Connecting Workers & Clients</p>
            </div>
        </div>
    </footer>

    <!-- Scripts -->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.7.1/jquery.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>
    
    <script>
        // Smooth scrolling for anchor links
        $('a[href^="#"]').on('click', function(e) {
            e.preventDefault();
            var target = $(this.getAttribute('href'));
            if(target.length) {
                $('html, body').stop().animate({
                    scrollTop: target.offset().top - 60
                }, 1000);
            }
        });

        // Add active class to nav items on scroll
        $(window).scroll(function() {
            var scrollPos = $(document).scrollTop();
            $('#navbarMenu a').each(function() {
                var target = $(this.getAttribute('href'));
                if(target.length && target.offset().top <= scrollPos + 100) {
                    $('#navbarMenu a').removeClass('active');
                    $(this).addClass('active');
                }
            });
        });

        // Navbar collapse on link click
        $('.navbar-nav a:not([data-toggle])').on('click', function() {
            $('.navbar-toggle').click();
        });
    </script>
</body>
</html>
""")

con.close()
