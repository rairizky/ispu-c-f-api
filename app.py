from flask import Flask
from flask_cors import CORS

from feature.classification.classificationFeature import routes as fClassification
from feature.forecast.forecastFeature import routes as fForecast

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})

# routes
app.register_blueprint(fClassification, url_prefix="/api/classification")
app.register_blueprint(fForecast, url_prefix="/api/forecast")

if __name__ == "__main__":
  app.run(debug=True)