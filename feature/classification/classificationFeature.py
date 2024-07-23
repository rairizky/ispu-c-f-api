from flask import Blueprint, request, jsonify

from model.classificationModel import predictData

routes = Blueprint("classification", __name__)

@routes.route("/predict", methods=["POST"])
def predict():
  body = request.json

  pm10, pm25, so2, co, o3, no2 = body["pm10"], body["pm25"], body["so2"], body["co"], body["o3"], body["no2"]

  values = {
    "pm10": pm10,
    "pm25": pm25,
    "so2": so2,
    "co": co,
    "o3": o3,
    "no2": no2
  }

  highest_key = max(values, key=values.get)
  highest_value = values[highest_key]

  predict_data = predictData([pm10, pm25, so2, co, o3, no2, highest_value])

  return jsonify({ 
    "category": predict_data, 
    "polutan": {
      "name": highest_key,
      "value": highest_value
    } 
  })