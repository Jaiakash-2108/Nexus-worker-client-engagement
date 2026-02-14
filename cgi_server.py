#!/usr/bin/env python3
"""
CGI Development Server for Nexus Worker Client Engagement
This server handles CGI scripts and serves the application
"""

import http.server
import socketserver
import os
import sys
import subprocess
from pathlib import Path
from urllib.parse import parse_qs, urlparse

# Add the project directory to the Python path
project_dir = Path(__file__).parent
sys.path.insert(0, str(project_dir))

class CGIRequestHandler(http.server.BaseHTTPRequestHandler):
    """Custom request handler for CGI and static files"""
    
    def do_GET(self):
        """Handle GET requests"""
        self.handle_request('GET')
    
    def do_POST(self):
        """Handle POST requests"""
        self.handle_request('POST')
    
    def handle_request(self, method):
        """Handle both GET and POST requests"""
        # Parse the path
        parsed_path = urlparse(self.path)
        file_path = parsed_path.path.lstrip('/')
        
        # Default to home page
        if file_path == '' or file_path == '/':
            file_path = 'nexushome.py'
        
        full_path = project_dir / file_path
        
        # Check if it's a Python script (CGI)
        if file_path.endswith('.py'):
            self.execute_cgi(full_path, method, parsed_path.query)
        # Check if it's a static file (media, images, css, js)
        elif full_path.exists() and full_path.is_file():
            # Serve static files
            self.serve_file(full_path)
        # Try with .py extension if the file doesn't exist
        elif not file_path.endswith('.py') and (project_dir / (file_path + '.py')).exists():
            self.execute_cgi(project_dir / (file_path + '.py'), method, parsed_path.query)
        else:
            # Log the requested path for debugging
            print(f"⚠ 404 Not Found: {file_path} (Full: {full_path})", file=sys.stderr)
            self.send_error(404, f"File not found: {file_path}")
    
    def execute_cgi(self, script_path, method, query_string):
        """Execute a Python script as CGI"""
        if not script_path.exists():
            self.send_error(404, f"Script not found: {script_path.name}")
            return
        
        try:
            # Prepare environment
            env = os.environ.copy()
            env['REQUEST_METHOD'] = method
            env['SCRIPT_NAME'] = f'/{script_path.name}'
            env['QUERY_STRING'] = query_string or ''
            
            if method == 'POST':
                content_length = int(self.headers.get('Content-Length', 0))
                env['CONTENT_LENGTH'] = str(content_length)
                env['CONTENT_TYPE'] = self.headers.get('Content-Type', 'application/x-www-form-urlencoded')
            
            # Read POST data if present
            post_data = b''
            if method == 'POST':
                content_length = int(self.headers.get('Content-Length', 0))
                if content_length > 0:
                    post_data = self.rfile.read(content_length)
            
            # Execute the Python script
            result = subprocess.run(
                [sys.executable, str(script_path)],
                env=env,
                input=post_data,
                capture_output=True,
                timeout=30,
                cwd=str(project_dir)
            )
            
            output = result.stdout.decode('utf-8', errors='ignore')
            error = result.stderr.decode('utf-8', errors='ignore')
            
            # Parse headers and body
            if '\r\n\r\n' in output:
                headers_part, body = output.split('\r\n\r\n', 1)
            elif '\n\n' in output:
                headers_part, body = output.split('\n\n', 1)
            else:
                headers_part = "content-type: text/html"
                body = output
            
            # Send response
            self.send_response(200)
            
            # Parse and send headers
            for header_line in headers_part.split('\n'):
                header_line = header_line.strip().rstrip('\r')
                if ':' in header_line:
                    key, value = header_line.split(':', 1)
                    self.send_header(key.strip(), value.strip())
            
            if 'content-type' not in headers_part.lower():
                self.send_header('Content-Type', 'text/html')
            
            self.end_headers()
            
            # Send body
            self.wfile.write(body.encode('utf-8', errors='ignore'))
            
            # Log any errors
            if error:
                print(f"⚠ Error in {script_path.name}: {error}", file=sys.stderr)
        
        except subprocess.TimeoutExpired:
            self.send_error(500, "Script execution timeout")
        except Exception as e:
            self.send_error(500, f"Error executing script: {str(e)}")
    
    def serve_file(self, file_path):
        """Serve a static file"""
        try:
            with open(file_path, 'rb') as f:
                content = f.read()
            
            # Determine content type based on file extension
            suffix = file_path.suffix.lower()
            content_types = {
                '.html': 'text/html',
                '.css': 'text/css',
                '.js': 'application/javascript',
                '.json': 'application/json',
                '.jpg': 'image/jpeg',
                '.jpeg': 'image/jpeg',
                '.png': 'image/png',
                '.gif': 'image/gif',
                '.svg': 'image/svg+xml',
                '.ico': 'image/x-icon',
                '.webp': 'image/webp',
                '.pdf': 'application/pdf',
                '.txt': 'text/plain',
                '.csv': 'text/csv',
            }
            content_type = content_types.get(suffix, 'application/octet-stream')
            
            self.send_response(200)
            self.send_header('Content-Type', content_type)
            self.send_header('Content-Length', len(content))
            self.send_header('Cache-Control', 'public, max-age=3600')
            self.end_headers()
            self.wfile.write(content)
            
            # Log successful file serve
            print(f"✓ Served: {file_path.relative_to(project_dir)} ({len(content)} bytes)", file=sys.stderr)
        
        except FileNotFoundError:
            self.send_error(404, "File not found")
        except PermissionError:
            self.send_error(403, "Permission denied")
        except Exception as e:
            print(f"✗ Error serving {file_path}: {str(e)}", file=sys.stderr)
            self.send_error(500, f"Error serving file: {str(e)}")
    
    def log_message(self, format, *args):
        """Custom logging"""
        # Suppress default logging - we'll do our own
        pass

def main():
    """Start the CGI server"""
    os.chdir(str(project_dir))
    
    PORT = 8000
    Handler = CGIRequestHandler
    
    try:
        # Use SO_REUSEADDR to allow quick restart
        socketserver.TCPServer.allow_reuse_address = True
        httpd = socketserver.TCPServer(("", PORT), Handler)
        
        print(f"""
╔════════════════════════════════════════════════════════════╗
║          Nexus Worker Client Engagement Server             ║
║                   CGI Development Server                   ║
╚════════════════════════════════════════════════════════════╝

✓ Server started on http://localhost:{PORT}
✓ Home page: http://localhost:{PORT}/nexushome.py
✓ Admin login: http://localhost:{PORT}/Adminlogin.py
✓ Employee login: http://localhost:{PORT}/Emplogin.py
✓ User login: http://localhost:{PORT}/userlogin.py

Database: nexus (localhost, port 3307)
         User: root (no password)

Press Ctrl+C to stop the server
════════════════════════════════════════════════════════════
""")
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n✓ Server stopped.")
        sys.exit(0)
    except OSError as e:
        if e.errno == 48 or e.errno == 98:  # Address already in use
            print(f"\n✗ Error: Port {PORT} is already in use.")
            print("Try: lsof -i :{PORT} and kill the process")
        else:
            print(f"\n✗ Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
