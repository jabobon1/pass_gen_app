from flask import Flask
from flask_cors import CORS


app = Flask(__name__, template_folder='templates')
app.config['FLASK_ENV'] = 'development'
app.config['SECRET_KEY'] = 'fsdfsd_5#y2L"F4Q8zsfsdfdo$%#@fpfmFLmpP)())]/'
CORS(app)


