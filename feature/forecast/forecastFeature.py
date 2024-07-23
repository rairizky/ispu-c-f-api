from flask import Blueprint, request, jsonify

from model.forecastModel import forecastByLocation, weekOfDateForecastData

routes = Blueprint("forecast", __name__)

@routes.route("/list", methods=["GET"])
def list():
  body = request.json

  location = body["location"]

  data_forecasted = forecastByLocation(location)

  to_week_data = weekOfDateForecastData(data_forecasted)

  return to_week_data