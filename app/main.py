from app import app
from api.home import blueprint as home
from api.api import blueprint as password

app.register_blueprint(home)
app.register_blueprint(password)

if __name__ == '__main__':
    app.run()
