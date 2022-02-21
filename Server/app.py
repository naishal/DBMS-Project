from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import (
    JWTManager
)
from flask_mail import Mail
from flask_migrate import Migrate
from werkzeug.middleware.proxy_fix import ProxyFix

from database import db

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_proto=1, x_port=1)

with app.app_context():
    from initializers.setup_config import SetupConfig
    SetupConfig(app)
    db.init_app(app)
    migrate = Migrate(app, db, compare_type=True)
    migrate.init_app(app, db)
    mail = Mail(app)
    CORS(app)
    jwt = JWTManager(app)
    app.config['JWT_TOKEN_LOCATION'] = ['headers']
    app.run(host="127.0.0.1", port=5000,)

    print("Server Running")
