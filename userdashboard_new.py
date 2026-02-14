#!/usr/bin/env python3
print("content-type:text/html \r\n\r\n")
import pymysql
import cgi
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
    <title>Dashboard - Nexus</title>
    
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
    <link rel="stylesheet" href="./css/style.css">
    
    <style>
        .dashboard-wrapper {
            display: flex;
            height: 100vh;
        }
        
        .sidebar {
            width: 280px;
            background: #1D373D;
            color: white;
            padding: 0;
            position: fixed;
            height: 100vh;
            overflow-y: auto;
            box-shadow: 2px 0 8px rgba(0,0,0,0.1);
        }
        
        .sidebar-header {
            padding: 25px;
            border-bottom: 1px solid rgba(255,255,255,0.1);
            display: flex;
            align-items: center;
            gap: 15px;
        }
        
        .sidebar-header img {
            height: 40px;
            border-radius: 50%;
        }
        
        .sidebar-header-text h4 {
            margin: 0;
            font-size: 16px;
            font-weight: 700;
        }
        
        .sidebar-header-text p {
            margin: 3px 0 0 0;
            font-size: 12px;
            opacity: 0.8;
        }
        
        .sidebar-nav {
            padding: 20px 0;
            list-style: none;
            margin: 0;
        }
        
        .sidebar-nav li {
            margin: 0;
        }
        
        .sidebar-nav a {
            display: flex;
            align-items: center;
            padding: 15px 25px;
            color: rgba(255,255,255,0.8);
            text-decoration: none;
            transition: all 0.3s ease;
            border-left: 3px solid transparent;
            gap: 12px;
        }
        
        .sidebar-nav a:hover,
        .sidebar-nav a.active {
            background-color: rgba(255,255,255,0.1);
            color: white;
            border-left-color: #00897B;
            padding-left: 30px;
        }
        
        .sidebar-nav a i {
            width: 20px;
            text-align: center;
        }
        
        .sidebar-nav .badge {
            margin-left: auto;
            background-color: #FF6F61;
            padding: 4px 8px;
            border-radius: 12px;
            font-size: 11px;
        }
        
        .sidebar-section-title {
            padding: 15px 25px 8px;
            font-size: 12px;
            font-weight: 700;
            color: rgba(255,255,255,0.5);
            text-transform: uppercase;
            letter-spacing: 0.5px;
            margin-top: 10px;
        }
        
        .main-content {
            flex: 1;
            margin-left: 280px;
            padding: 30px;
            background-color: #F5F9FB;
            overflow-y: auto;
            height: 100vh;
        }
        
        .top-navbar {
            background: white;
            padding: 20px 30px;
            border-bottom: 2px solid #ECF0F1;
            margin: -30px -30px 30px -30px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            gap: 20px;
        }
        
        .page-title {
            font-size: 28px;
            font-weight: 700;
            color: #1D373D;
            margin: 0;
        }
        
        .top-actions {
            display: flex;
            gap: 15px;
            align-items: center;
        }
        
        .user-profile {
            display: flex;
            align-items: center;
            gap: 10px;
            cursor: pointer;
        }
        
        .user-profile img {
            height: 40px;
            width: 40px;
            border-radius: 50%;
        }
        
        .dashboard-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 20px;
            margin-bottom: 30px;
        }
        
        .stat-card {
            background: white;
            padding: 25px;
            border-radius: 8px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.08);
            border-top: 4px solid #00897B;
        }
        
        .stat-icon {
            font-size: 32px;
            color: #00897B;
            margin-bottom: 10px;
        }
        
        .stat-label {
            color: #7F8C8D;
            font-size: 14px;
            font-weight: 500;
        }
        
        .stat-value {
            font-size: 28px;
            font-weight: 700;
            color: #1D373D;
            margin: 5px 0;
        }
        
        .stat-change {
            color: #27AE60;
            font-size: 12px;
        }
        
        .dashboard-table {
            background: white;
            border-radius: 8px;
            overflow: hidden;
            box-shadow: 0 2px 8px rgba(0,0,0,0.08);
        }
        
        .table-header {
            background-color: #1D373D;
            color: white;
            padding: 20px 25px;
            margin: 0;
            border-bottom: none;
        }
        
        .dashboard-table table {
            margin: 0;
        }
        
        .dashboard-table table thead tr {
            background-color: #1D373D;
            color: white;
        }
        
        .dashboard-table table tbody tr:hover {
            background-color: #F5F9FB;
        }
        
        @media (max-width: 768px) {
            .sidebar {
                width: 100%;
                height: auto;
                position: relative;
            }
            
            .main-content {
                margin-left: 0;
                padding: 15px;
                height: auto;
            }
            
            .top-navbar {
                flex-direction: column;
                align-items: flex-start;
                margin: -15px -15px 20px -15px;
            }
            
            .top-actions {
                width: 100%;
                justify-content: flex-end;
            }
            
            .dashboard-grid {
                grid-template-columns: 1fr;
            }
        }
    </style>
</head>
<body>
    <div class="dashboard-wrapper">
        <!-- Sidebar Navigation -->
        <aside class="sidebar">
            <div class="sidebar-header">
                <img src="./image/logo.jpg" alt="Nexus">
                <div class="sidebar-header-text">
                    <h4>Nexus</h4>
                    <p>Client Dashboard</p>
                </div>
            </div>
            
            <ul class="sidebar-nav">
                <li><a href="#" class="active"><i class="fa fa-home"></i> Dashboard</a></li>
                <li><a href="#"><i class="fa fa-briefcase"></i> Browse Workers</a></li>
                <li><a href="#"><i class="fa fa-calendar"></i> My Bookings <span class="badge">3</span></a></li>
            </ul>
            
            <div class="sidebar-section-title">Management</div>
            <ul class="sidebar-nav">
                <li><a href="#"><i class="fa fa-file-text"></i> Projects</a></li>
                <li><a href="#"><i class="fa fa-star"></i> Reviews & Ratings</a></li>
                <li><a href="#"><i class="fa fa-envelope"></i> Messages</a></li>
                <li><a href="#"><i class="fa fa-credit-card"></i> Payments</a></li>
            </ul>
            
            <div class="sidebar-section-title">Account</div>
            <ul class="sidebar-nav">
                <li><a href="#"><i class="fa fa-user"></i> Profile</a></li>
                <li><a href="#"><i class="fa fa-cog"></i> Settings</a></li>
                <li><a href="#"><i class="fa fa-sign-out"></i> Logout</a></li>
            </ul>
        </aside>
        
        <!-- Main Content -->
        <main class="main-content">
            <!-- Top Navbar -->
            <div class="top-navbar">
                <h2 class="page-title">Dashboard</h2>
                <div class="top-actions">
                    <button class="btn btn-primary" style="background-color: #00897B; border: none;">
                        <i class="fa fa-plus"></i> New Booking
                    </button>
                    <div class="user-profile">
                        <img src="./image/logo.jpg" alt="User">
                        <div>
                            <strong>John Doe</strong><br>
                            <small style="color: #7F8C8D;">Client</small>
                        </div>
                    </div>
                </div>
            </div>
            
            <!-- Statistics -->
            <div class="dashboard-grid">
                <div class="stat-card">
                    <div class="stat-icon"><i class="fa fa-briefcase"></i></div>
                    <div class="stat-label">Active Projects</div>
                    <div class="stat-value">5</div>
                    <div class="stat-change"><i class="fa fa-arrow-up"></i> 2 more this month</div>
                </div>
                
                <div class="stat-card">
                    <div class="stat-icon"><i class="fa fa-users"></i></div>
                    <div class="stat-label">Connected Workers</div>
                    <div class="stat-value">12</div>
                    <div class="stat-change"><i class="fa fa-arrow-up"></i> 4 new this month</div>
                </div>
                
                <div class="stat-card">
                    <div class="stat-icon"><i class="fa fa-calendar-check-o"></i></div>
                    <div class="stat-label">Completed Jobs</div>
                    <div class="stat-value">28</div>
                    <div class="stat-change"><i class="fa fa-arrow-up"></i> 100% satisfaction</div>
                </div>
                
                <div class="stat-card">
                    <div class="stat-icon"><i class="fa fa-dollar"></i></div>
                    <div class="stat-label">Total Spent</div>
                    <div class="stat-value">$4,250</div>
                    <div class="stat-change"><i class="fa fa-arrow-up"></i> +$850 this month</div>
                </div>
            </div>
            
            <!-- Recent Bookings Table -->
            <div class="dashboard-table">
                <div class="table-header">
                    <h4 style="margin: 0;">Recent Bookings</h4>
                </div>
                <table class="table table-hover">
                    <thead>
                        <tr>
                            <th>Worker</th>
                            <th>Service</th>
                            <th>Date</th>
                            <th>Status</th>
                            <th>Amount</th>
                            <th>Action</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>
                                <div style="display: flex; align-items: center; gap: 10px;">
                                    <img src="./image/logo.jpg" alt="User" style="height: 30px; border-radius: 50%;">
                                    <strong>Mike Johnson</strong>
                                </div>
                            </td>
                            <td>Carpentry</td>
                            <td>Feb 10, 2026</td>
                            <td><span class="status-badge success">Completed</span></td>
                            <td>$350</td>
                            <td>
                                <button class="btn btn-xs btn-primary" style="background-color: #00897B; border: none;">
                                    <i class="fa fa-eye"></i> View
                                </button>
                            </td>
                        </tr>
                        <tr>
                            <td>
                                <div style="display: flex; align-items: center; gap: 10px;">
                                    <img src="./image/logo.jpg" alt="User" style="height: 30px; border-radius: 50%;">
                                    <strong>Sarah Williams</strong>
                                </div>
                            </td>
                            <td>Electrical Work</td>
                            <td>Feb 08, 2026</td>
                            <td><span class="status-badge success">Completed</span></td>
                            <td>$280</td>
                            <td>
                                <button class="btn btn-xs btn-primary" style="background-color: #00897B; border: none;">
                                    <i class="fa fa-eye"></i> View
                                </button>
                            </td>
                        </tr>
                        <tr>
                            <td>
                                <div style="display: flex; align-items: center; gap: 10px;">
                                    <img src="./image/logo.jpg" alt="User" style="height: 30px; border-radius: 50%;">
                                    <strong>Robert Brown</strong>
                                </div>
                            </td>
                            <td>Painting</td>
                            <td>Feb 06, 2026</td>
                            <td><span class="status-badge pending">In Progress</span></td>
                            <td>$425</td>
                            <td>
                                <button class="btn btn-xs btn-primary" style="background-color: #00897B; border: none;">
                                    <i class="fa fa-eye"></i> View
                                </button>
                            </td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </main>
    </div>
    
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.7.1/jquery.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>
</body>
</html>
""")

con.close()
