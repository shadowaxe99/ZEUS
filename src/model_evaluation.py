import numpy as np
import pandas as pd


def evaluate_model(model, X, y):
    # Evaluate the performance of the model
    predictions = model.predict(X)
    accuracy = accuracy_score(y, predictions)
    return accuracy
