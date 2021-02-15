from django_pandas.io import read_frame
import numpy as np
import tensorflow as tf
from tensorflow import keras
from sklearn.preprocessing import MinMaxScaler
import pandas as pd
import datetime
from pathlib import Path
import os

RANDOM_SEED = 42

np.random.seed(RANDOM_SEED)
tf.random.set_seed(RANDOM_SEED)

n_steps_in, n_steps_out = 36, 12

CURRENT_DIR = Path(__file__).resolve(strict=True).parent

PREDICTION_MODEL_NAME = 'WaterConsumptionPredictionModel'


def predict_domestic_water_consumption(house, consumption_details):
    df = read_frame(consumption_details, fieldnames=[
                    'date', 'water_consumption'], index_col=['date'])

    df = df.tail(n_steps_in)

    scaled_data = df

    f_columns = ['water_consumption']

    scaler = MinMaxScaler(feature_range=(0, 1))

    scaled_data.loc[:, f_columns] = scaler.fit_transform(
        scaled_data[f_columns].to_numpy())

    scaled_data = scaled_data.values

    n_features = 1

    model = keras.models.load_model(
        os.path.join(CURRENT_DIR, PREDICTION_MODEL_NAME))

    x_input = scaled_data.reshape((1, n_steps_in, n_features))
    predicted_values = np.array(model.predict(x_input))

    predicted_values = scaler.inverse_transform(predicted_values[0])

    start_date = df.iloc[-1].name

    months_array = [(start_date+i)
                    for i in range(1, predicted_values.shape[0]+1)]

    final_output = pd.DataFrame(predicted_values)
    final_output['Date'] = months_array
    final_output = final_output.set_index('Date')
    final_output.columns = f_columns

    df.loc[:, f_columns] = scaler.inverse_transform(
        df[f_columns].to_numpy())

    print(df)

    print(final_output)

    real_list = []

    for index, row in df.iterrows():
        real_list.append({
            'date': datetime.date(index.year, index.month, 1),
            'water_consumption': row['water_consumption'],
        })

    predicted_list = []

    for index, row in final_output.iterrows():
        predicted_list.append({
            'date': datetime.date(index.year, index.month, 1),
            'water_consumption': row['water_consumption'],
        })

    data = {
        'home': house,
        'real': real_list,
        'predicted': predicted_list,
    }

    return real_list, predicted_list, data
