from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    # תבנית HTML עם האלמנט score
    html_template = '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Test Page</title>
    </head>
    <body>
        <div id="score">500</div>
    </body>
    </html>
    '''
    return render_template_string(html_template)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8777)
