from flask import Flask
app = Flask(__name__)

@app.route('/')
def my_app():
    return 'I am a flask app in a container. You gotta pack me the right way'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
