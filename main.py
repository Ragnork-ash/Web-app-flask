from website import create_app
from flask import Flask
#chk call Flask app

app = create_app()

if __name__ == '__main__':
   # app.run(debug=True)
    app.run()