import numpy as np
import pandas as pd


class EnsembleModel:
    def __init__(self):
        self.models = []

    def add_model(self, model):
        self.models.append(model)

    def predict(self, X):
        predictions = []
        for model in self.models:
            prediction = model.predict(X)
            predictions.append(prediction)
        return predictions
