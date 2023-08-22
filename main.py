from flask import Flask
from scripts.services import search_service
from scripts.services import home_service
from scripts.services import data_exploration_service

app = Flask(__name__)

# Register routes
app.register_blueprint(home_service.home)
app.register_blueprint(search_service.search_service_bp)
app.register_blueprint(data_exploration_service.data_exploration_bp)


if __name__ == '__main__':
    app.run(port=8005, debug=True)

