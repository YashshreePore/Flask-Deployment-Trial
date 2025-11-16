from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    # इथून यूजर्सला एक साधे वेब पेज दिसेल
    return '<h1>Hello, Heroku! This is our deployment trial.</h1>'

if __name__ == '__main__':
    # पोर्ट ॲडजस्टमेंट Heroku स्वतः करते, पण लोकल टेस्टसाठी हे चांगले आहे.
    app.run(debug=True)