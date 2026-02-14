# Nexus UI - Quick Reference Guide

## 🚀 Quick Start

### Access New Pages
- **Homepage:** `http://localhost:8000/nexushome_new.py`
- **Login:** `http://localhost:8000/userlogin_new.py`
- **Register:** `http://localhost:8000/userregister_new.py`
- **Dashboard:** `http://localhost:8000/userdashboard_new.py`

### CSS File
```
/workspaces/Nexus-worker-client-engagement/css/style.css
```

---

## 🎨 Color Quick Reference

```
Primary:    #1D373D    Dark Teal
Secondary:  #00897B    Teal
Accent:     #FF6F61    Coral Red
Light:      #F5F9FB    Light Blue
Dark Text:  #2C3E50    Dark Gray
Light Text: #7F8C8D    Medium Gray
Border:     #ECF0F1    Light Gray
Success:    #27AE60    Green
Warning:    #F39C12    Orange
Danger:     #E74C3C    Red
```

---

## 💻 HTML Classes Reference

### Layout
```html
<div class="container">Centered container</div>
<div class="row">Bootstrap row</div>
<div class="col-md-4">Bootstrap column</div>
```

### Cards
```html
<!-- Feature Card -->
<div class="feature-card">
    <div class="card-icon"><i class="fa fa-icon"></i></div>
    <h3 class="card-title">Title</h3>
    <p class="card-text">Text</p>
</div>

<!-- Service Card -->
<div class="service-card">
    <img src="image.jpg">
    <h3 class="card-title">Title</h3>
    <p class="card-text">Text</p>
</div>
```

### Buttons
```html
<button class="btn btn-primary">Primary</button>
<button class="btn btn-danger">Danger</button>
<button class="btn btn-success">Success</button>
<button class="btn btn-info">Info</button>
<button class="btn btn-warning">Warning</button>
```

### Forms
```html
<div class="form-group">
    <label>Label</label>
    <input type="text" class="form-control" placeholder="...">
</div>

<div class="form-group">
    <label>Textarea</label>
    <textarea class="form-control" rows="4"></textarea>
</div>

<div class="form-group">
    <label>Select</label>
    <select class="form-control">
        <option>Option 1</option>
    </select>
</div>
```

### Tables
```html
<table class="table">
    <thead>
        <tr>
            <th>Header 1</th>
            <th>Header 2</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Data 1</td>
            <td>Data 2</td>
        </tr>
    </tbody>
</table>
```

### Status Badges
```html
<span class="status-badge success">Completed</span>
<span class="status-badge pending">In Progress</span>
<span class="status-badge danger">Cancelled</span>
```

### Alerts
```html
<div class="alert alert-success">Success message</div>
<div class="alert alert-danger">Error message</div>
<div class="alert alert-warning">Warning message</div>
<div class="alert alert-info">Info message</div>
```

### Navigation
```html
<nav class="navbar navbar-default">
    <div class="navbar-header">
        <a class="navbar-brand" href="#">Brand</a>
    </div>
    <ul class="nav navbar-nav">
        <li><a href="#">Link</a></li>
    </ul>
</nav>
```

### Sidebar (Dashboard)
```html
<aside class="sidebar">
    <div class="sidebar-header">Header</div>
    <ul class="sidebar-nav">
        <li><a href="#" class="active"><i class="fa fa-icon"></i> Menu</a></li>
        <li><a href="#"><i class="fa fa-icon"></i> Menu</a></li>
    </ul>
</aside>

<main class="main-content">
    <div class="top-navbar">
        <h2 class="page-title">Title</h2>
        <div class="top-actions">
            <button class="btn btn-primary">Action</button>
        </div>
    </div>
    <!-- Content -->
</main>
```

### Dashboard Stats
```html
<div class="dashboard-grid">
    <div class="stat-card">
        <div class="stat-icon"><i class="fa fa-icon"></i></div>
        <div class="stat-label">Label</div>
        <div class="stat-value">123</div>
        <div class="stat-change">+5% this month</div>
    </div>
</div>
```

---

## 🔄 Common Patterns

### Hero Section
```html
<section class="hero-section">
    <div class="container">
        <div class="hero-content">
            <h1 class="hero-title">Title</h1>
            <p class="hero-subtitle">Subtitle</p>
            <button class="btn hero-btn btn-primary-hero">CTA 1</button>
            <button class="btn hero-btn btn-secondary-hero">CTA 2</button>
        </div>
    </div>
</section>
```

### Feature Section
```html
<section>
    <div class="container">
        <h2>Section Title</h2>
        <div class="row">
            <div class="col-md-4">
                <div class="feature-card">
                    <!-- content -->
                </div>
            </div>
        </div>
    </div>
</section>
```

### Login Form
```html
<div class="auth-container">
    <div class="auth-header">
        <h2>Login</h2>
        <p>Subtitle</p>
    </div>
    <form method="POST">
        <div class="form-group">
            <label><i class="fa fa-user"></i> Email</label>
            <input type="email" class="form-control" required>
        </div>
        <div class="form-group">
            <label><i class="fa fa-lock"></i> Password</label>
            <input type="password" class="form-control" required>
        </div>
        <button type="submit" class="btn btn-primary" style="width: 100%;">Login</button>
    </form>
</div>
```

---

## 🎯 CSS Variables

Defined at the top of `style.css`:

```css
:root {
    --primary-color: #1D373D;
    --secondary-color: #00897B;
    --accent-color: #FF6F61;
    --light-bg: #F5F9FB;
    --text-dark: #2C3E50;
    --text-light: #7F8C8D;
    --border-color: #ECF0F1;
    --success: #27AE60;
    --warning: #F39C12;
    --danger: #E74C3C;
}
```

Use in CSS:
```css
background-color: var(--primary-color);
color: var(--text-dark);
```

---

## 📱 Responsive Classes

```html
<!-- Columns (Bootstrap) -->
<div class="col-xs-12">Mobile</div>
<div class="col-sm-6">Tablet</div>
<div class="col-md-4">Desktop</div>
<div class="col-lg-3">Large Desktop</div>

<!-- Display -->
<div class="d-flex">Flex container</div>
<div class="justify-content-between">Space between</div>
<div class="align-items-center">Center items</div>
<div class="gap-20">20px gap</div>
```

---

## 🎨 Utility Classes

```html
<!-- Text Colors -->
<p class="text-primary">Primary color</p>
<p class="text-secondary">Secondary color</p>
<p class="text-danger">Danger color</p>
<p class="text-muted">Muted color</p>

<!-- Background Colors -->
<div class="bg-primary">Primary bg</div>
<div class="bg-secondary">Secondary bg</div>

<!-- Spacing -->
<div class="mt-40">Margin top 40px</div>
<div class="mb-40">Margin bottom 40px</div>

<!-- Shadows -->
<div class="shadow">Light shadow</div>
<div class="shadow-lg">Large shadow</div>

<!-- Rounded -->
<div class="rounded">Rounded corners</div>
```

---

## 📦 Responsive Grid

```html
<div class="row">
    <div class="col-md-4 col-sm-6">Card 1</div>
    <div class="col-md-4 col-sm-6">Card 2</div>
    <div class="col-md-4 col-sm-6">Card 3</div>
</div>
```

Auto-responsive grid:
```css
display: grid;
grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
gap: 20px;
```

---

## 🔗 Icon Library

Font Awesome 4.7. Examples:

```html
<i class="fa fa-home"></i>        Home
<i class="fa fa-user"></i>        User
<i class="fa fa-envelope"></i>    Email
<i class="fa fa-phone"></i>       Phone
<i class="fa fa-lock"></i>        Lock
<i class="fa fa-calendar"></i>    Calendar
<i class="fa fa-star"></i>        Star
<i class="fa fa-briefcase"></i>   Briefcase
<i class="fa fa-search"></i>      Search
<i class="fa fa-cog"></i>         Settings
<i class="fa fa-sign-out"></i>    Sign Out
<i class="fa fa-shield"></i>      Shield
<i class="fa fa-users"></i>       Users
<i class="fa fa-dollar"></i>      Dollar
<i class="fa fa-arrow-up"></i>    Arrow Up
<i class="fa fa-check"></i>       Check
<i class="fa fa-times"></i>       Close
<i class="fa fa-comments"></i>    Comments
<i class="fa fa-file-text"></i>   File
```

See more: https://fontawesome.io/icons/

---

## ✅ Implementation Checklist

- [ ] Link CSS file: `<link rel="stylesheet" href="./css/style.css">`
- [ ] Include jQuery: `<script src="...jquery.min.js"></script>`
- [ ] Include Bootstrap JS: `<script src="...bootstrap.min.js"></script>`
- [ ] Include Font Awesome: `<link rel="stylesheet" href="...font-awesome.css">`
- [ ] Add viewport meta: `<meta name="viewport" content="width=device-width, initial-scale=1.0">`
- [ ] Test responsive design (F12)
- [ ] Test on mobile device
- [ ] Verify all links work
- [ ] Check color contrast
- [ ] Validate HTML

---

## 🐛 Troubleshooting

**Styles not applying?**
- Check file path to `style.css`
- Clear browser cache (Ctrl+Shift+Delete)
- Check CSS is loaded (F12 → Network tab)

**Layout broken?**
- Add viewport meta tag
- Check grid classes
- Verify Bootstrap is loaded
- Test media queries

**Buttons not styled?**
- Use `class="btn btn-primary"`
- Check CSS is loaded
- Verify no inline styles override

**Icons not showing?**
- Check Font Awesome CDN
- Verify icon class names
- Check network in DevTools

---

## 📚 File Structure

```
/workspaces/Nexus-worker-client-engagement/
├── css/
│   └── style.css                 Main stylesheet
├── image/                        Service images
├── media/                        Profile images
├── nexushome_new.py             New homepage
├── userlogin_new.py             New login
├── userregister_new.py          New registration
├── userdashboard_new.py         New dashboard
├── UI_GUIDE.md                  Full documentation
└── UI_PREVIEW.md                Preview guide
```

---

## 🎓 Learning Resources

1. **CSS Reference:** `css/style.css` (inline comments)
2. **HTML Examples:** Open `*_new.py` files
3. **Bootstrap Docs:** https://getbootstrap.com/docs/3.4/
4. **Font Awesome:** https://fontawesome.io/icons/

---

## 💬 Quick Tips

1. Always include the CSS file
2. Use Bootstrap grid for layout
3. Apply classes for styling
4. Test on mobile (F12 toggle)
5. Use semantic HTML
6. Follow color scheme
7. Maintain consistency
8. Document changes

---

## 🎯 Next Steps

1. **Explore** the new pages
2. **Review** the CSS
3. **Customize** colors if needed
4. **Update** other pages with new components
5. **Deploy** when ready

---

**Happy coding! 🚀**

Last Updated: February 14, 2026
