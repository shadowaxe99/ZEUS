import numpy as np
import pandas as pd


class AgentEnsemble:
    def __init__(self):
        self.agents = []

    def add_agent(self, agent):
        self.agents.append(agent)

    def predict(self, X):
        predictions = []
        for agent in self.agents:
            prediction = agent.predict(X)
            predictions.append(prediction)
        return predictions
