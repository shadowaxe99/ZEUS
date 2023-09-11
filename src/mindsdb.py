import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier


class MindsDB:
    def __init__(self):
        self.model = None

    def learn(self, X, y):
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        self.model = DecisionTreeClassifier()
        self.model.fit(X_train, y_train)

    def predict(self, X):
        return self.model.predict(X)
