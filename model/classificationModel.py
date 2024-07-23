import pandas as pd
import pickle

model = pickle.load(open("model/ml/classification/model.pkl", "rb"))

train = pickle.load(open("model/ml/classification/train.pkl", "rb"))

def predictData(classification):
  inputData = { train.columns[i] : [classification[i]] for i in range(train.shape[1]) }
  dfs = pd.DataFrame(inputData)

  return model.predict(dfs)[-1]