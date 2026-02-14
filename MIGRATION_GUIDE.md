# Nexus UI - Migration Guide

## 📋 Overview

This guide walks you through migrating from the original pages to the new modern UI pages.

---

## 🎯 Step-by-Step Migration

### Step 1: Backup Original Pages

Before making any changes, back up all original pages:

```bash
# Backup all original Python files
for file in nexushome.py userlogin.py userregister.py userdashboard.py; do
    cp "$file" "${file%.py}_backup.py"
done

# Or use git
git add -A
git commit -m "Backup original pages before UI migration"
```

### Step 2: Deploy New Homepage

**Current:** `nexushome_new.py` (new version)  
**Target:** `nexushome.py` (replace original)

Option A - Rename file:
```bash
cp nexushome.py nexushome_old.py
cp nexushome_new.py nexushome.py
```

Option B - Update original:
```bash
# Copy new file's content to original location
cat nexushome_new.py > nexushome.py
```

**Test:**
```bash
curl -s http://localhost:8000/nexushome.py | head -20
```

---

### Step 3: Deploy New Login Page

**Current:** `userlogin_new.py`  
**Target:** `userlogin.py`

```bash
cp userlogin.py userlogin_old.py
cp userlogin_new.py userlogin.py
```

**Test:**
```bash
curl -s http://localhost:8000/userlogin.py | grep "Login"
```

---

### Step 4: Deploy New Registration Page

**Current:** `userregister_new.py`  
**Target:** `userregister.py`

```bash
cp userregister.py userregister_old.py
cp userregister_new.py userregister.py
```

**Test:**
```bash
curl -s http://localhost:8000/userregister.py | grep "Registration"
```

---

### Step 5: Deploy New Dashboard

**Current:** `userdashboard_new.py`  
**Target:** `userdashboard.py`

```bash
cp userdashboard.py userdashboard_old.py
cp userdashboard_new.py userdashboard.py
```

**Test:**
```bash
curl -s http://localhost:8000/userdashboard.py | grep "Dashboard"
```

---

### Step 6: Update All Other Pages

Add CSS link to remaining pages. Open each file and add this line in the `<head>` section:

```html
<link rel="stylesheet" href="./css/style.css">
```

**Pages to update:**
1. ✅ `nexushome.py` - Done (new file has it)
2. ✅ `userlogin.py` - Done (new file has it)
3. ✅ `userregister.py` - Done (new file has it)
4. ✅ `userdashboard.py` - Done (new file has it)
5. `Admindashboard.py` - Add CSS link
6. `Adminlogin.py` - Add CSS link
7. `admin_contracter.py` - Add CSS link
8. `admin_emp_exis.py` - Add CSS link
9. `admin_emp_new.py` - Add CSS link
10. `admin_feedback.py` - Add CSS link
11. `admin_user.py` - Add CSS link
12. `admin_work.py` - Add CSS link
13. `booking_existing.py` - Add CSS link
14. `booking_new.py` - Add CSS link
15. `contrac_book_exis.py` - Add CSS link
16. `contrac_book_new.py` - Add CSS link
17. `contrac_dash_wrk.py` - Add CSS link
18. `contrac_emp_feedback.py` - Add CSS link
19. `contrac_emp_feedback1.py` - Add CSS link
20. `contrac_feedback_exis.py` - Add CSS link
21. `contrac_feedback_new.py` - Add CSS link
22. `contract_dash_submit.py` - Add CSS link
23. `contracter_dashboard.py` - Add CSS link
24. `contracter_login.py` - Add CSS link
25. `emp_c_exis.py` - Add CSS link
26. `emp_c_new.py` - Add CSS link
27. `emp_feedback_table.py` - Add CSS link
28. `emp_work_new.py` - Add CSS link
29. `emp_working_history.py` - Add CSS link
30. `emp_wrk_exs.py` - Add CSS link
31. `Empdashboard.py` - Add CSS link
32. `Emplogin.py` - Add CSS link
33. `EmpRegister.py` - Add CSS link
34. `feedback_existing.py` - Add CSS link
35. `feedback_form.py` - Add CSS link
36. `user_dsh_wrk.py` - Add CSS link
37. `user_emp_feedback.py` - Add CSS link
38. `user_emp_feedback1.py` - Add CSS link
39. `user_workers.py` - Add CSS link

---

### Step 7: Verify Migration

Test all pages load correctly:

```bash
#!/bin/bash
echo "Testing migration..."

pages=(
    "nexushome.py"
    "userlogin.py"
    "userregister.py"
    "userdashboard.py"
)

for page in "${pages[@]}"; do
    status=$(curl -s -o /dev/null -w "%{http_code}" "http://localhost:8000/$page")
    if [ "$status" -eq 200 ]; then
        echo "✅ $page - OK"
    else
        echo "❌ $page - Error ($status)"
    fi
done
```

---

### Step 8: Cross-Browser Testing

Test new pages on multiple browsers:

**Desktop:**
- [ ] Chrome (latest)
- [ ] Firefox (latest)
- [ ] Safari (if available)
- [ ] Edge (if available)

**Mobile:**
- [ ] iOS Safari
- [ ] Chrome Mobile
- [ ] Firefox Mobile

**Testing Checklist:**
- [ ] All text readable
- [ ] Images load correctly
- [ ] Forms functional
- [ ] Buttons clickable
- [ ] Colors consistent
- [ ] No horizontal scroll
- [ ] Navigation works
- [ ] Database saves data

---

### Step 9: Performance Testing

Check page load times:

```bash
# Using curl timing
curl -w "@curl-format.txt" -o /dev/null -s http://localhost:8000/nexushome.py

# Using browser DevTools
# F12 → Network tab → View timing breakdown
```

---

### Step 10: Rollback (If Needed)

If issues arise, restore original pages:

```bash
# Restore individual file
cp nexushome_old.py nexushome.py

# Or restore all
for file in *_old.py; do
    cp "$file" "${file%_old.py}.py"
done
```

---

## 🎨 Customization During Migration

### Change Color Scheme

Edit `/css/style.css` root variables:

```css
:root {
    --primary-color: #1D373D;      /* Change this */
    --secondary-color: #00897B;    /* Change this */
    --accent-color: #FF6F61;       /* Change this */
}
```

### Modify Logo

Update image source in page files:

```python
# Original
print('<img src="/image/logo.jpg" class="logo">')

# Change to your logo
print('<img src="/image/your-logo.jpg" class="logo">')
```

### Adjust Layout

Modify sidebar width in CSS:

```css
.sidebar {
    width: 280px;  /* Change width here */
}
```

---

## ✅ Post-Migration Checklist

- [ ] All pages load without errors
- [ ] CSS file served correctly (check HTTP headers)
- [ ] Images display properly
- [ ] Forms submit data to database
- [ ] User workflows complete (login → register → dashboard)
- [ ] No console errors (F12)
- [ ] Responsive design works on mobile
- [ ] Color scheme matches design
- [ ] Navigation consistent across pages
- [ ] Performance acceptable (<3s load time)
- [ ] Accessibility criteria met
- [ ] All database operations working
- [ ] Backup files preserved safely
- [ ] Documentation updated
- [ ] Team informed of changes

---

## 🚨 Common Issues & Solutions

### Issue 1: CSS Not Applied

**Symptom:** Page loads but no styling

**Solution:**
```bash
# Check if CSS file exists
ls -la css/style.css

# Verify file permissions
chmod 644 css/style.css

# Check in browser DevTools
# F12 → Network tab → look for style.css
# Should show 200 status
```

### Issue 2: Images Not Loading

**Symptom:** Broken image icons appear

**Solution:**
```bash
# Check image directory
ls -la image/

# Verify permissions
chmod 755 image/
chmod 644 image/*

# Test image serving
curl -I http://localhost:8000/image/logo.jpg
# Should return HTTP 200
```

### Issue 3: Database Not Connected

**Symptom:** No data displays, connection errors

**Solution:**
```bash
# Check MariaDB running
sudo systemctl status mysql

# Test connection
mysql -u root -h localhost nexus -e "SELECT COUNT(*) FROM userregister;"

# Verify port in Python files
grep "port=" *.py
# Should all show port=3306
```

### Issue 4: Forms Not Submitting

**Symptom:** Form submit button doesn't work

**Solution:**
```bash
# Check form method and action
# F12 → Elements → inspect form tag

# Verify processing script exists
# Form should POST to same file or specific handler

# Check for JavaScript errors
# F12 → Console tab
```

### Issue 5: Mobile Layout Broken

**Symptom:** Page unusable on phone/tablet

**Solution:**
```html
<!-- Check viewport meta tag -->
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<!-- Test responsive design -->
<!-- F12 → Toggle Device Toolbar (Ctrl+Shift+M) -->

<!-- Check Bootstrap grid classes -->
<!-- Should have col-xs-*, col-sm-*, col-md-* -->
```

---

## 📞 Reference Files

**New Page Locations:**
- Homepage: `nexushome_new.py`
- Login: `userlogin_new.py`
- Registration: `userregister_new.py`
- Dashboard: `userdashboard_new.py`

**Backup Files:**
- Homepage: `nexushome_old.py` (if migrated)
- Login: `userlogin_old.py` (if migrated)
- Registration: `userregister_old.py` (if migrated)
- Dashboard: `userdashboard_old.py` (if migrated)

**Documentation:**
- Full Guide: `UI_GUIDE.md`
- Quick Reference: `UI_QUICK_REFERENCE.md`
- Preview: `UI_PREVIEW.md`

**CSS:**
- Main Stylesheet: `css/style.css`

---

## 🔄 Script: Automated Migration

Save as `migrate.sh`:

```bash
#!/bin/bash

echo "🚀 Starting Nexus UI Migration..."

# Step 1: Backup
echo "📦 Backing up original files..."
for file in nexushome.py userlogin.py userregister.py userdashboard.py; do
    if [ -f "$file" ]; then
        cp "$file" "${file%.py}_backup.py"
        echo "✅ Backed up $file"
    fi
done

# Step 2: Deploy new files
echo "🎨 Deploying new UI pages..."
cp nexushome_new.py nexushome.py && echo "✅ Deployed nexushome.py"
cp userlogin_new.py userlogin.py && echo "✅ Deployed userlogin.py"
cp userregister_new.py userregister.py && echo "✅ Deployed userregister.py"
cp userdashboard_new.py userdashboard.py && echo "✅ Deployed userdashboard.py"

# Step 3: Verify
echo "🧪 Verifying migration..."
for page in nexushome.py userlogin.py userregister.py userdashboard.py; do
    status=$(curl -s -o /dev/null -w "%{http_code}" "http://localhost:8000/$page" 2>/dev/null || echo "000")
    if [ "$status" -eq 200 ]; then
        echo "✅ $page - OK"
    else
        echo "❌ $page - Error (Status: $status)"
    fi
done

echo "✨ Migration complete!"
```

**Run migration:**
```bash
chmod +x migrate.sh
./migrate.sh
```

---

## 📚 Next Steps

After successful migration:

1. **Monitor** - Watch for issues in the wild
2. **Gather Feedback** - Talk to users about new design
3. **Iterate** - Make adjustments based on feedback
4. **Document** - Update internal documentation
5. **Train** - Train team on new interface

---

**Need Help?**

1. Check `UI_GUIDE.md` for detailed documentation
2. Review `UI_QUICK_REFERENCE.md` for code examples
3. View `UI_PREVIEW.md` for live page tours
4. Check browser console (F12) for errors
5. Review server logs for backend issues

---

**Good luck with your migration! 🎉**

Last Updated: February 14, 2026
