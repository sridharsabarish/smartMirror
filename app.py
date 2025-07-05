from flask import Flask, render_template_string
from smartMirror import smartMirror

app = Flask(__name__)

@app.route('/')
def serve_page():
    smartmirror = smartMirror()
    html = smartmirror.build_web_page()
    return render_template_string(html)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7000, debug=True)