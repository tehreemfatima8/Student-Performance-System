from flask import Flask
from flask_cors import CORS
from routes.prediction import prediction_bp
from config import Config


def create_app():
    """
    Create and configure the Flask application.
    """

    app = Flask(__name__)

    # Load configuration
    app.config["SECRET_KEY"] = Config.SECRET_KEY

    # Enable CORS so React can communicate with Flask
    CORS(app)

    # -------------------------
    # Home Route
    # -------------------------
    @app.route("/")
    def home():
        return {
            "project": "AI-Based Student Performance Prediction System",
            "status": "Backend Running Successfully",
            "version": "1.0"
        }

    # -------------------------
    # Register Routes
    # -------------------------
    app.register_blueprint(
    prediction_bp
)

    return app


app = create_app()

if __name__ == "__main__":
    app.run(debug=True)