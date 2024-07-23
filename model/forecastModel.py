
from model.classificationModel import predictData

import pickle

forecast_data = pickle.load(open("model/ml/forecast/data.pkl", "rb"))

def forecastByLocation(location):
  for item in forecast_data:
    if item["location"] == location:
      return item
    
def weekOfDateForecastData(data):
  # Collect data by date index
  max_entries = max(len(param['forecasted_data']) for param in data['parameter'])
  result = [[] for _ in range(max_entries)]

  # Populate result list based on index
  for index in range(max_entries):
      for param in data['parameter']:
          if index < len(param['forecasted_data']):
              entry = param['forecasted_data'][index]
              result[index].append({
                  "date": entry['date'],
                  "parameter": param['name'],
                  "value": entry['value']
              })

  output = []
  for entry in result:
    # Find the parameter with the highest value
    highest_param = max(entry, key=lambda x: x["value"])

    values = [item["value"] for item in entry]
    values.append(highest_param["value"])

    # Add the 'polutan' key
    output.append({
        "data": entry,
        "polutan": {
           "date": highest_param["date"],
            "name": highest_param["parameter"],
            "value": highest_param["value"],
            "category": predictData(values)
        }
    })

  return output