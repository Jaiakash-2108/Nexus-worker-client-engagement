# Nexus UI - Troubleshooting & FAQ

## 🔍 Troubleshooting Guide

### CSS & Styling Issues

#### Problem: Styles not applying to pages
```
Symptom: Page loads but looks plain, no colors or formatting
Likelihood: HIGH (common during initial setup)
```

**Diagnosis:**
```bash
# Check if CSS file exists
ls -la css/style.css

# Check CSS file size (should be ~15KB)
du -h css/style.css

# Verify CSS is accessible
curl -I http://localhost:8000/css/style.css
# Should show: HTTP/1.1 200 OK
# And: Content-Type: text/css
```

**Solutions:**

1. **Check HTML for CSS link:**
   ```html
   <!-- Required in <head> section -->
   <link rel="stylesheet" href="./css/style.css">
   ```
   - Verify path is correct (use `./css/style.css` not `/css/style.css`)
   - Check for typos in filename

2. **Clear browser cache:**
   - Chrome/Edge: `Ctrl+Shift+Delete` → Select "All time"
   - Firefox: `Ctrl+Shift+Delete` → Select "Everything"
   - Safari: Develop → Clear Caches

3. **Hard refresh page:**
   - Windows/Linux: `Ctrl+F5`
   - Mac: `Cmd+Shift+R`

4. **Check CSS file integrity:**
   ```bash
   # View first 10 lines
   head -10 css/style.css
   
   # Count lines (should be ~1000+)
   wc -l css/style.css
   
   # Check for syntax errors
   grep -n "ERROR\|INVALID\|PARSE" css/style.css
   ```

5. **Check DevTools:**
   - Open F12
   - Go to Network tab
   - Reload page (F5)
   - Look for `style.css` in list
   - Should show 200 status
   - If 404: file doesn't exist
   - If 403: permission denied

---

#### Problem: Colors not matching design
```
Symptom: Colors look different from expected
Likelihood: MEDIUM
```

**Solutions:**

1. **Verify color definitions:**
   ```bash
   # Check CSS variables
   grep "color:" css/style.css | head -20
   
   # Expected primary color should be #1D373D
   grep "primary-color" css/style.css
   ```

2. **Check color in browser:**
   - F12 → Elements → inspect element
   - Find computed color in Styles panel
   - Compare with expected hex code

3. **Common color reference:**
   ```
   Primary:    #1D373D    Dark Teal
   Secondary:  #00897B    Teal
   Accent:     #FF6F61    Coral Red
   Success:    #27AE60    Green
   Danger:     #E74C3C    Red
   ```

---

#### Problem: Layout broken/misaligned
```
Symptom: Elements overlapping, off-screen, or stacked wrong
Likelihood: MEDIUM
```

**Solutions:**

1. **Check viewport meta tag:**
   ```html
   <!-- Must be in <head> -->
   <meta name="viewport" content="width=device-width, initial-scale=1.0">
   ```

2. **Check Bootstrap inclusion:**
   ```html
   <!-- Required in <head> -->
   <link rel="stylesheet" href="...bootstrap.css">
   ```

3. **Test responsive design:**
   - F12 → Toggle Device Toolbar (Ctrl+Shift+M)
   - Try different screen sizes
   - Should adjust properly

4. **Check grid classes:**
   ```bash
   # Verify Bootstrap structure
   grep "col-" css/style.css | head -10
   ```

---

### Image Problems

#### Problem: Images not loading
```
Symptom: Broken image icon or blank spaces
Likelihood: HIGH (common in new deployments)
```

**Diagnosis:**
```bash
# Check image directory exists
ls -la image/

# Check file permissions
ls -l image/logo.jpg

# Test image serving
curl -I http://localhost:8000/image/logo.jpg
# Should show HTTP/1.1 200 OK
```

**Solutions:**

1. **Verify image directory exists:**
   ```bash
   mkdir -p image
   mkdir -p media
   chmod 755 image media
   ```

2. **Check image file permissions:**
   ```bash
   chmod 644 image/*
   chmod 644 media/*
   ```

3. **Verify image paths in code:**
   ```bash
   # Check for image references
   grep -r "src=" *.py | grep -i image
   
   # Should show relative paths like:
   # src="./image/logo.jpg"
   # src="/image/car.jpeg"
   ```

4. **Test individual image:**
   ```bash
   curl -I http://localhost:8000/image/logo.jpg
   # Check HTTP status (should be 200)
   # Check Content-Type (should be image/jpeg)
   ```

5. **Check image format:**
   ```bash
   # List all images
   file image/*
   
   # Should show JPEG/PNG format
   ```

---

### Database Issues

#### Problem: "Database connection failed" error
```
Symptom: Yellow error page, database error in output
Likelihood: HIGH
```

**Diagnosis:**
```bash
# Check MariaDB is running
sudo systemctl status mysql

# Test connection
mysql -h localhost -u root -e "SELECT VERSION();"

# Test database exists
mysql -h localhost -u root -e "USE nexus; SHOW TABLES;"
```

**Solutions:**

1. **Start MariaDB if stopped:**
   ```bash
   sudo systemctl start mysql
   sudo systemctl enable mysql  # Auto-start on boot
   ```

2. **Verify port configuration:**
   ```bash
   # Check all Python files for correct port
   grep "port=" *.py | sort | uniq
   
   # Should all show port=3306
   # If any show port=3307, update them:
   sed -i 's/port=3307/port=3306/g' *.py
   ```

3. **Test connection manually:**
   ```bash
   # This should work:
   mysql -h localhost -u root -e "SELECT 1;"
   
   # If fails, check if server is listening:
   sudo netstat -tulpn | grep 3306
   ```

4. **Check credentials in code:**
   ```bash
   # Look for connection strings
   grep -n "pymysql.connect" *.py
   
   # Should show:
   # host="localhost", user="root", password="", database="nexus", port=3306
   ```

5. **Verify database exists:**
   ```bash
   mysql -h localhost -u root -e "SHOW DATABASES;" | grep nexus
   ```

---

#### Problem: "Table not found" error
```
Symptom: SQL error mentioning missing table
Likelihood: MEDIUM
```

**Solutions:**

1. **Check what tables exist:**
   ```bash
   mysql -h localhost -u root -D nexus -e "SHOW TABLES;"
   
   # Should show:
   # admin
   # booking_details
   # emypregister
   # feedback_form
   # userregister
   ```

2. **Check table structure:**
   ```bash
   mysql -h localhost -u root -D nexus -e "DESC userregister;"
   ```

3. **Reimport database if corrupted:**
   ```bash
   # First backup current data
   mysqldump -u root nexus > backup.sql
   
   # Then drop and recreate
   mysql -u root -e "DROP DATABASE nexus;"
   mysql -u root < nexus.sql
   ```

---

### Server Issues

#### Problem: "Connection refused" error
```
Symptom: Cannot access localhost:8000
Likelihood: MEDIUM
```

**Solutions:**

1. **Check if server is running:**
   ```bash
   curl http://localhost:8000/
   
   # If fails, server is down
   ```

2. **Check what's listening on port 8000:**
   ```bash
   sudo lsof -i :8000
   
   # Should show python process
   ```

3. **Restart the server:**
   ```bash
   # First kill existing process
   pkill -f cgi_server.py
   
   # Then restart
   cd /workspaces/Nexus-worker-client-engagement
   python cgi_server.py &
   ```

4. **Check for port conflicts:**
   ```bash
   # See all listening ports
   sudo netstat -tulpn
   
   # If port 8000 in use, kill process or use different port
   ```

---

#### Problem: Server crashes/exits
```
Symptom: Server was running but suddenly stops
Likelihood: MEDIUM
```

**Solutions:**

1. **Check error logs:**
   ```bash
   # Look for recent errors
   tail -100 /var/log/syslog | grep -i python
   
   # Or check with dmesg
   dmesg | tail -20
   ```

2. **Run server in foreground to see errors:**
   ```bash
   cd /workspaces/Nexus-worker-client-engagement
   python cgi_server.py
   # Now you'll see errors in terminal
   ```

3. **Check disk space:**
   ```bash
   df -h /
   # If < 1GB free, may cause issues
   ```

4. **Check memory:**
   ```bash
   free -h
   # If very low, may cause issues
   ```

---

### Browser & Performance

#### Problem: Page loads very slowly
```
Symptom: Takes >5 seconds to display page
Likelihood: LOW-MEDIUM
```

**Solutions:**

1. **Check load times:**
   ```bash
   time curl http://localhost:8000/nexushome.py > /dev/null
   ```

2. **Monitor server resources:**
   ```bash
   top
   # Check CPU and memory usage
   ```

3. **Optimize images:**
   ```bash
   # Check image file sizes
   ls -lh image/
   
   # Large images slow load time
   # Consider compressing
   ```

4. **Check network:**
   ```bash
   # Ping server
   ping localhost
   
   # Should be < 1ms response time
   ```

---

#### Problem: Page looks different in different browsers
```
Symptom: Chrome looks good but Firefox/Safari looks wrong
Likelihood: LOW
```

**Solutions:**

1. **Test in all browsers:**
   - Chrome
   - Firefox
   - Safari (if Mac)
   - Edge

2. **Check CSS compatibility:**
   ```bash
   # CSS used should be standard (CSS3)
   grep -i "webkit\|moz\|ms" css/style.css
   
   # Some vendor prefixes may be needed
   ```

3. **Use browser DevTools:**
   - F12 in each browser
   - Check Console for errors
   - Check Styles for applied CSS
   - Note any differences

---

## ❓ Frequently Asked Questions

### Q1: How do I change the primary color?

**A:**
```css
/* Open /css/style.css */
:root {
    --primary-color: #1D373D;  /* Change this hex code */
}
```

Then save and refresh browser. All elements using `var(--primary-color)` will update automatically.

**Example colors:**
- Dark Blue: `#1A1F3A`
- Navy: `#003366`
- Teal: `#008080`
- Green: `#2E7D32`

---

### Q2: How do I change the logo?

**A:**
Replace the logo image in the page:

```python
# In nexushome.py, find:
print('<img src="./image/logo.jpg" class="logo">')

# Change to your logo path:
print('<img src="./image/my-logo.png" class="logo">')

# Place your logo file in /image/ directory
```

---

### Q3: How do I make the sidebar narrower?

**A:**
```css
/* In /css/style.css, find: */
.sidebar {
    width: 280px;  /* Change this value */
}

/* Change to smaller width, e.g.: */
.sidebar {
    width: 200px;  /* New width */
}
```

Also update main content margin:
```css
.main-content {
    margin-left: 280px;  /* Should match new sidebar width */
}
```

---

### Q4: How do I change the font?

**A:**
```css
/* In /css/style.css, find: */
body {
    font-family: 'Segoe UI', ...;
}

/* Change to your font: */
body {
    font-family: 'Arial', sans-serif;
    /* Or use Google Fonts */
    /* @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;700&display=swap'); */
}
```

---

### Q5: How do I add a new navbar item?

**A:**
In the page HTML, find the navbar section:

```html
<ul class="nav navbar-nav">
    <li><a href="#home">Home</a></li>
    <li><a href="#services">Services</a></li>
    <!-- Add new item here: -->
    <li><a href="#new-page">New Page</a></li>
</ul>
```

---

### Q6: How do I change button colors?

**A:**
```css
/* In /css/style.css, find: */
.btn-primary {
    background-color: var(--primary-color);
}

/* Change background color: */
.btn-primary {
    background-color: #2E7D32;  /* New color */
}
```

---

### Q7: How do I make cards wider or narrower?

**A:**
```css
/* For feature/service cards: */
.feature-card {
    max-width: 350px;  /* Change this */
}

/* For grid layout: */
.row {
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    /* Change 250px to larger/smaller value */
}
```

---

### Q8: How do I test on my phone?

**A:**

1. **Get your computer's IP:**
   ```bash
   ifconfig | grep "inet "
   # Look for something like 192.168.x.x
   ```

2. **Access from phone:**
   - Connect phone to same network as computer
   - Open browser
   - Go to: `http://<YOUR_IP>:8000/nexushome.py`

3. **Or use tunnel:**
   ```bash
   # Install ngrok: https://ngrok.com/
   ngrok http 8000
   # Get the public URL and access from phone
   ```

---

### Q9: How do I add animations?

**A:**
```css
/* Define animation in /css/style.css: */
@keyframes slideUp {
    from {
        opacity: 0;
        transform: translateY(20px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

/* Apply to element: */
.my-element {
    animation: slideUp 0.5s ease-in-out;
}
```

---

### Q10: How do I modify form styling?

**A:**
```css
/* In /css/style.css, find: */
.form-control {
    border: 1px solid var(--border-color);
    padding: 10px;
    font-size: 14px;
}

/* Customize: */
.form-control {
    border: 2px solid var(--primary-color);  /* Bold border */
    padding: 12px;  /* More padding */
    border-radius: 8px;  /* Round corners */
}

/* Add focus effect: */
.form-control:focus {
    border-color: var(--accent-color);
    box-shadow: 0 0 5px var(--accent-color);
}
```

---

### Q11: How do I hide an element?

**A:**
```css
/* Option 1: Hide completely */
.element-to-hide {
    display: none;
}

/* Option 2: Hide but keep space */
.element-to-hide {
    visibility: hidden;
}

/* Option 3: Make transparent */
.element-to-hide {
    opacity: 0;
}
```

Or in HTML:
```html
<!--
<div>Hidden element</div>
-->
```

---

### Q12: How do I center content?

**A:**
```css
/* Horizontally: */
.center-horizontal {
    margin: 0 auto;
    text-align: center;
}

/* Vertically with flexbox: */
.center-vertical {
    display: flex;
    align-items: center;
    justify-content: center;
    height: 100px;
}

/* Both: */
.center-both {
    display: flex;
    align-items: center;
    justify-content: center;
    height: 100vh;
}
```

---

### Q13: How do I make something full width?

**A:**
```css
.full-width {
    width: 100%;
    max-width: 100%;
    margin: 0;
    padding: 0;
}
```

---

### Q14: How do I add a border?

**A:**
```css
.bordered {
    border: 1px solid #ccc;
    /* border: [width] [style] [color]; */
    
    /* Also available: */
    border-top: 1px solid #ccc;
    border-bottom: 1px solid #ccc;
    border-left: 1px solid #ccc;
    border-right: 1px solid #ccc;
    
    /* Or shorthand: */
    border: 1px solid #ccc !important;
}
```

---

### Q15: How do I add shadow to elements?

**A:**
```css
.shadow {
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

.shadow-lg {
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
}

/* Text shadow: */
.text-shadow {
    text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
}
```

---

## 🆘 Getting Help

### If you encounter an issue:

1. **Check this guide first** ← You're already doing this! ✅

2. **Review the code:**
   - Open F12 in browser
   - Check Console tab for error messages
   - Check Network tab to see what failed

3. **Check file permissions:**
   ```bash
   ls -la css/
   ls -la image/
   ls -la media/
   ```

4. **Review logs:**
   ```bash
   tail -50 /var/log/syslog | grep -E "ERROR|CGI"
   ```

5. **Verify server status:**
   ```bash
   curl -I http://localhost:8000/
   ```

---

## 📊 Quick Health Check

Run this to verify everything:

```bash
#!/bin/bash
echo "🔍 Nexus Health Check"
echo "===================="

# 1. Check CSS
echo "✓ CSS File:"
ls -lh css/style.css 2>/dev/null && echo "  ✅ Exists" || echo "  ❌ Missing"

# 2. Check images
echo "✓ Images:"
[ -d image ] && echo "  ✅ Directory exists ($(ls image/ | wc -l) files)" || echo "  ❌ Directory missing"

# 3. Check database
echo "✓ Database:"
mysql -u root -e "SELECT COUNT(*) as tables FROM information_schema.tables WHERE table_schema = 'nexus';" 2>/dev/null || echo "  ❌ not running"

# 4. Check server
echo "✓ Web Server:"
curl -s -o /dev/null -w "  HTTP %{http_code}\n" http://localhost:8000/nexushome.py

# 5. Check pages
echo "✓ Pages:"
for page in nexushome userlogin userregister userdashboard; do
    status=$(curl -s -o /dev/null -w "%{http_code}" "http://localhost:8000/${page}.py" 2>/dev/null || echo "000")
    [ "$status" -eq 200 ] && echo "  ✅ ${page}.py" || echo "  ❌ ${page}.py (HTTP $status)"
done

echo ""
echo "✨ Check complete!"
```

---

**Remember: Most issues have simple solutions. Check the basics first!**

Last Updated: February 14, 2026
Version: 1.0
