from src.app import create_flask_app
from src.infa.db.loggers.logger_default import LoggerDefault

logger = LoggerDefault()

if __name__ == "__main__":
    flask_app = create_flask_app(logger)
    flask_app.run(port=5000, debug=True)
