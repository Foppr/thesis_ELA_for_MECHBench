import numpy as np
import pandas as pd
import xgboost as xgb
from xgboost import XGBClassifier, XGBRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

import pickle
from pathlib import Path
from ._utils import get_save_path, get_data_path


class XGBModel():
    def __init__(self, target='intrusion', problem=1, dset_size=250, seed=1312):
        self.problem = problem
        self.size = dset_size
        self.seed = seed

        if self.problem==1:
            self.features = ['x0', 'x1', 'x2', 'x3', 'x4']
            # self.targets = ["intrusion", "specific_energy_absorbed", "penalized_sea"]
            self.dim = 5
        elif self.problem == 2:
            self.features = ['x0', 'x1', 'x2', 'x3', 'x4']
            # self.targets = ["intrusion", "mass", "penalized_mass"]
            self.dim = 5
        elif self.problem == 3:
            self.features = ['x0', 'x1', 'x2', 'x3', 'x4', 'x5', 'x6', 'x7', 'x8', 'x9', 'x10', 'x11', 'x12', 'x13', 'x14']
            # self.targets = ["load_uniformity"]
            self.dim = 15

        self.target = target
        self.X_train, self.X_test, self.y_train, self.y_test = self.get_data()

        self.model = xgb.XGBRegressor(
            n_estimators=100,
            max_depth=5,
            random_state = self.seed,
            learning_rate = 0.1
        )

    def get_data(self):
        path = get_data_path(self.problem, self.size, self.dim, self.seed)
        # data = pd.read_csv(f"data_p{self.problem}/{self.size}D/{self.size}d{self.dim}_p{self.problem}_seed{self.seed}.csv")
        data = pd.read_csv(path)

        X = data[self.features]
        y = data[self.target]

        return train_test_split(X, y, test_size=0.2, random_state=self.seed)
    
    def train(self):
        self.model.fit(self.X_train, self.y_train)

    def pred(self):

        self.predictions = self.model.predict(self.X_test)
        
        return self.predictions
    
    def predict(self, point):
        
        return self.model.predict(point)
    
    def metrics(self, predictions):
        self.metrics_dict = {}
        # for target in self.targets:
        #     # self.metrics_dict[target] = {
        #     #     "MSE" : [],
        #     #     "r-squared" : []
        #     # }
        #     self.metrics_dict[target] = {
        #         "MSE" : mean_squared_error(self.y_test, predictions),
        #         "r-squared" : r2_score(self.y_test, predictions)
        #     }
        self.metrics_dict['MSE'] = mean_squared_error(self.y_test, predictions)
        self.metrics_dict['r-squared'] = r2_score(self.y_test, predictions)

        return self.metrics_dict
    
    def save(self, filename):
        # filename should end in .ubj
        path = get_save_path(filename)
        self.model.save_model(str(path))         
        return path

    @classmethod
    def load(cls, filename, problem=1, target='intrusion', dset_size=250, seed=1312):
        path = get_save_path(filename)

        instance = cls.__new__(cls)
        instance.problem = problem
        instance.target = target
        instance.size = dset_size
        instance.seed = seed

        if instance.problem==1:
            instance.features = ['x0', 'x1', 'x2', 'x3', 'x4']
            # self.targets = ["intrusion", "specific_energy_absorbed", "penalized_sea"]
            instance.dim = 5
        elif instance.problem == 2:
            instance.features = ['x0', 'x1', 'x2', 'x3', 'x4']
            # self.targets = ["intrusion", "mass", "penalized_mass"]
            instance.dim = 5
        elif instance.problem == 3:
            instance.features = ['x0', 'x1', 'x2', 'x3', 'x4', 'x5', 'x6', 'x7', 'x8', 'x9', 'x10', 'x11', 'x12', 'x13', 'x14']
            # self.targets = ["load_uniformity"]
            instance.dim = 15


        instance.X_train, instance.X_test, instance.y_train, instance.y_test = instance.get_data()


        # with open(path, "rb") as model_file:
        #     instance.model = pickle.load(model_file)

        instance.model = xgb.XGBRegressor()
        instance.model.load_model(str(path)) 

        return instance