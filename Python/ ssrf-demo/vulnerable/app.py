from flask import Flask, request
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return '''
    <h2>Image Preview Tool (VULNERABLE)</h2>
    <form action="/fetch" method="GET">
        <input name="url" placeholder="Enter URL..." size="50">
        <button type="submit">Fetch</button>
    </form>
    '''

@app.route('/fetch')
def fetch():
    url = request.args.get('url', '')
    try:
        response = requests.get(url, timeout=3)
        return f'<pre>{response.text[:2000]}</pre>'
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True, port=5000)
