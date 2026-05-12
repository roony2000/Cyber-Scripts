from flask import Flask, request
import requests
import ipaddress
import socket
from urllib.parse import urlparse

app = Flask(__name__)

ALLOWED_DOMAINS = ['api.github.com', 'jsonplaceholder.typicode.com']

BLOCKED_IPS = [
    '127.0.0.0/8',
    '10.0.0.0/8',
    '172.16.0.0/12',
    '192.168.0.0/16',
    '169.254.0.0/16',
]

def is_ip_blocked(ip):
    try:
        ip_obj = ipaddress.ip_address(ip)
        for blocked in BLOCKED_IPS:
            if ip_obj in ipaddress.ip_network(blocked):
                return True
    except:
        return True
    return False

def is_url_safe(url):
    try:
        parsed = urlparse(url)
        if parsed.scheme not in ['http', 'https']:
            return False, "Only HTTP/HTTPS allowed"
        if parsed.hostname not in ALLOWED_DOMAINS:
            return False, "Domain not allowed"
        ip = socket.gethostbyname(parsed.hostname)
        if is_ip_blocked(ip):
            return False, "IP address is blocked"
        return True, "OK"
    except Exception as e:
        return False, str(e)

@app.route('/')
def index():
    return '''
    <h2>Image Preview Tool (SECURE)</h2>
    <form action="/fetch" method="GET">
        <input name="url" placeholder="Enter URL..." size="50">
        <button type="submit">Fetch</button>
    </form>
    <p>Allowed: api.github.com | jsonplaceholder.typicode.com</p>
    '''

@app.route('/fetch')
def fetch():
    url = request.args.get('url', '')
    is_safe, reason = is_url_safe(url)
    if not is_safe:
        return f'<h3>BLOCKED: {reason}</h3>', 403
    try:
        response = requests.get(url, timeout=3, allow_redirects=False)
        return f'<pre>{response.text[:2000]}</pre>'
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True, port=5001)
