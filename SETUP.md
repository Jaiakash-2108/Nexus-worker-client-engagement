# Nexus Worker Client Engagement - Setup Guide

## Server Status ✓

The **CGI Development Server** is now running on: **http://localhost:8000**

### Access Points:
- **Home**: http://localhost:8000/
- **Admin Login**: http://localhost:8000/Adminlogin.py
- **Employee Login**: http://localhost:8000/Emplogin.py  
- **User Login**: http://localhost:8000/userlogin.py
- **Contractor Login**: http://localhost:8000/contracter_login.py

---

## Database Setup Required

The application requires MySQL/MariaDB. Follow these steps to set up the database:

### Option 1: Using Docker (Recommended)

```bash
# Start a MySQL container
docker run -d --name nexus-mysql \
  -e MYSQL_ROOT_PASSWORD="" \
  -e MYSQL_DATABASE="nexus" \
  -p 3307:3306 \
  mysql:8.0

# Wait for MySQL to start (30 seconds)
sleep 30

# Import the database schema
docker exec -i nexus-mysql mysql -u root nexus < nexus.sql
```

### Option 2: Manual MySQL Installation

```bash
# Install MySQL Server
sudo apt-get update
sudo apt-get install -y mysql-server

# Start MySQL service
sudo service mysql start

# Create the database and import schema
mysql -u root -e "CREATE DATABASE IF NOT EXISTS nexus;"
mysql -u root nexus < nexus.sql
```

### Option 3: Using MariaDB (Lightweight Alternative)

```bash
# Install MariaDB
sudo apt-get update
sudo apt-get install -y mariadb-server

# Start MariaDB service
sudo service mariadb start

# Create the database and import schema
sudo mysql -u root -e "CREATE DATABASE IF NOT EXISTS nexus;"
sudo mysql -u root nexus < nexus.sql
```

---

## Database Configuration

The application expects:
- **Host**: localhost
- **Port**: 3307
- **User**: root
- **Password**: (empty)
- **Database**: nexus

If your MySQL is on a different port, update the port in all Python files:
- Search for `port=3307` in all `.py` files
- Replace with your actual MySQL port (default is 3306)

---

## Testing the Setup

Once the database is running:

```bash
# Test MySQL connection
mysql -u root -h localhost -P 3307 -e "SELECT 1"

# Access the application
curl http://localhost:8000/
```

---

## Important Notes

⚠️ **Security Warning**: The application uses hardcoded database credentials with no password. This is suitable for development only.

🔧 **Server Status**: The server is currently running in the background. To stop it:
```bash
lsof -i :8000 | grep -v COMMAND | awk '{print $2}' | xargs kill -9
```

---

## Project Structure

```
.
├── cgi_server.py           # Development server (running)
├── nexus.sql              # Database schema
├── *login.py              # Login pages (Admin, Employee, User, Contractor)
├── *dashboard.py          # Dashboard pages
├── admin_*.py             # Admin management modules
├── emp_*.py               # Employee modules
├── user_*.py              # User modules
├── contrac_*.py           # Contractor modules
└── README.md              # This file
```

---

## Available Logins

Test these credentials (after database setup):
- **Admin**: username=`admin`, password=`12345`
- **Employee**: Register via Employee Register page
- **User**: Register via User Register page
- **Contractor**: Register via system

---

## Troubleshooting

**Q: Port 8000 already in use?**
```bash
lsof -i :8000 | grep -v COMMAND | awk '{print $2}' | xargs kill -9
```

**Q: MySQL connection refused?**
- Ensure MySQL is running on port 3307 (or update the port in the `.py` files)
- Check MySQL is listening: `sudo netstat -tlnp | grep mysql`

**Q: Database schema errors?**
- Verify nexus.sql file exists
- Check MySQL user permissions: `mysql -u root -e "SHOW DATABASES;"`

---
