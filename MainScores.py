from flask import Flask
import os

app = Flask(__name__)

def initialize_scores_file():
    if not os.path.exists("Scores.txt"):
        with open("Scores.txt", "w") as file:
            file.write("0")

@app.route('/')
def score_server():
    initialize_scores_file()
    try:
        with open("Scores.txt", "r") as file:
            score = file.read()
            return f"""
            <html>
                <head>
                    <title>Scores Game</title>
                </head>
                <body>
                    <h1>The score is <div id="score">{score}</div></h1>
                </body>
            </html>
            """
    except Exception as e:
        return f"""
        <html>
            <head>
                <title>Scores Game</title>
            </head>
            <body>
                <h1><div id="score" style="color:red">{e}</div></h1>
            </body>
        </html>
        """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
