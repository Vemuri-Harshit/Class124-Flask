from flask import Flask;
app = Flask(__name__);

@app.route('/')
def router():
    return 'Namaste Ham hai Harshit'

if __name__ == '__main__':
    app.run();