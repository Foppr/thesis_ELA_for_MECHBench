import pandas as pd
from pyDOE3 import ccdesign
from sklearn.preprocessing import PolynomialFeatures, MinMaxScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

import pickle
from pathlib import Path
from ._utils import get_save_path, get_data_path

class RSM():
    def __init__(self, target="intrusion", problem=1, dset_size=250, seed=1312):
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

        self.scaler = MinMaxScaler()

        self.X_train, self.X_test, self.y_train, self.y_test = self.get_data()

        self.pf = PolynomialFeatures(degree=2)
        # X_pf = pf.fit_transform(self.X)
        
        self.X_train_poly = self.pf.fit_transform(self.X_train_scaled)
        self.X_test_poly = self.pf.transform(self.X_test_scaled)

        self.model = LinearRegression()

    def get_data(self):
        path = get_data_path(self.problem, self.size, self.dim, self.seed)
        # data  = pd.read_csv(f"data_p{self.problem}/{self.size}D/{self.size}d{self.dim}_p{self.problem}_seed{self.seed}.csv")
        data = pd.read_csv(path)

        X = data[self.features]
        y = data[self.target]

        # X_scaled = 2*((X-X.min())/(X.max()-X.min()))

        # y = {}
        # if self.problem == 1:
        #     y_intrusion = data['Intrusion']
        #     y_sea = data['SEA']
        #     y_penalized_sea= data['Penalized SEA']
        # elif self.problem == 2:
        #     y_intrusion = data['Intrusion']
        #     y_mass = data['Mass']
        #     y_penalized_mass = data['Penalized Mass']

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=self.seed)

        # self.scaler = MinMaxScaler()
        self.X_train_scaled = self.scaler.fit_transform(X_train)
        self.X_test_scaled = self.scaler.transform(X_test)

        return X_train, X_test, y_train, y_test
    
    def train(self):
        self.model.fit(self.X_train_poly, self.y_train)

    def pred(self):
        self.predictions = self.model.predict(self.X_test_poly)

        return self.predictions
    
    def predict(self, point_to_predict):
        point_to_predict_scaled = self.scaler.transform(point_to_predict) 
        # pf = PolynomialFeatures(degree=2)
        point_poly = self.pf.transform(point_to_predict_scaled)

        return self.model.predict(point_poly)
    
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
        path = get_save_path(filename)
        checkpoint = {
            "model" : self.model,
            "scaler" : self.scaler,
            "problem" : self.problem,
            "size" : self.size,
            "seed" : self.seed,
            "features" : self.features,
            "dim" : self.dim,
            "target" : self.target,
            "X_train_poly" : self.X_train_poly,
            "X_test_poly" : self.X_test_poly,
            "y_train" : self.y_train,
            "y_test" : self.y_test,
            "pf" : self.pf
        }
        with open(path, "wb") as model_file:
            pickle.dump(checkpoint, model_file)

    @classmethod
    def load(cls, filename, target='intrusion', problem=1, dset_size=250, seed=1312):
        path = get_save_path(filename)
        # instance = cls.__new__(cls)
        # instance.problem = int(problem)
        # instance.target = target
        # instance.size = dset_size
        # instance.seed = seed

        # if instance.problem==1:
        #     instance.features = ['x0', 'x1', 'x2', 'x3', 'x4']
        #     # self.targets = ["intrusion", "specific_energy_absorbed", "penalized_sea"]
        #     instance.dim = 5
        # elif instance.problem == 2:
        #     instance.features = ['x0', 'x1', 'x2', 'x3', 'x4']
        #     # self.targets = ["intrusion", "mass", "penalized_mass"]
        #     instance.dim = 5
        # elif instance.problem == 3:
        #     instance.features = ['x0', 'x1', 'x2', 'x3', 'x4', 'x5', 'x6', 'x7', 'x8', 'x9', 'x10', 'x11', 'x12', 'x13', 'x14']
        #     # self.targets = ["load_uniformity"]
        #     instance.dim = 15        

        # if instance.dim is None:
        #     instance.dim = len(instance.features)

        # instance.X_train, instance.X_test, instance.y_train, instance.y_test = instance.get_data()
        
        # pf = PolynomialFeatures(degree=2)

        # instance.X_train_poly = pf.fit_transform(instance.X_train_scaled)
        # instance.X_test_poly = pf.transform(instance.X_test_scaled)

        with open(path, "rb") as model_file:
            checkpoint = pickle.load(model_file)

        instance = cls.__new__(cls)
        instance.problem = checkpoint["problem"]
        instance.size = checkpoint["size"]
        instance.seed = checkpoint["seed"]
        instance.features = checkpoint["features"]
        instance.target = checkpoint["target"]
        instance.dim = checkpoint["dim"]
        instance.model = checkpoint["model"]
        instance.scaler = checkpoint["scaler"]
        instance.X_train_poly = checkpoint["X_train_poly"]
        instance.X_test_poly = checkpoint["X_test_poly"]
        instance.y_train = checkpoint["y_train"]
        instance.y_test = checkpoint["y_test"]
        instance.pf = checkpoint["pf"]


        return instance