from website import create_app
from flask import Flask
from waitress import serve
#chk call Flask app

app = create_app()

#app = Flask(__name__)

if __name__ == "__main__":
   serve(app, host="0.0.0.0", port=8000)


    #if __name__ == '__main__':
   # app.run(debug=True)