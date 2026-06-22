import gpytorch
import torch
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler

from pathlib import Path
from ._utils import get_save_path, get_data_path

class GPRegressionModel(gpytorch.models.ExactGP):
    def __init__(self, train_x, train_y, likelihood):
        super(GPRegressionModel, self).__init__(train_x, train_y, likelihood)
        self.mean_module = gpytorch.means.ConstantMean()
        self.covar_module = gpytorch.kernels.ScaleKernel(gpytorch.kernels.RBFKernel())

    def forward(self, x):
        mean_x = self.mean_module(x)
        covar_x = self.covar_module(x)
        return gpytorch.distributions.MultivariateNormal(mean_x, covar_x)
    

class GPModel():

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

        self.scaler = StandardScaler()

        self.target = target
        self.X_train, self.X_test, self.y_train, self.y_test = self.get_data()
        
        self.likelihood = gpytorch.likelihoods.GaussianLikelihood()
        self.model = GPRegressionModel(self.X_train, self.y_train, self.likelihood)

    def get_data(self):

        path = get_data_path(self.problem, self.size, self.dim, self.seed)
        # data = pd.read_csv(f"data_p{self.problem}/{self.size}D/{self.size}d{self.dim}_p{self.problem}_seed{self.seed}.csv")
        data = pd.read_csv(path)

        X = data[self.features]
        y = data[self.target]

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=self.seed)

        # self.scaler = StandardScaler() #maybe minmax scaler instead?

        X_train_scaled = self.scaler.fit_transform(X_train)
        X_test_scaled = self.scaler.transform(X_test)

        X_train_scaled = torch.tensor(X_train_scaled, dtype=torch.float32)
        X_test_scaled = torch.tensor(X_test_scaled, dtype=torch.float32)
        y_train = torch.tensor(y_train.values, dtype=torch.float32)
        y_test = torch.tensor(y_test.values, dtype=torch.float32)

        return X_train_scaled, X_test_scaled, y_train, y_test


    def train(self):
        self.model.train()
        self.likelihood.train()

        optimizer = torch.optim.Adam(self.model.parameters(), lr=0.01)
        mll = gpytorch.mlls.ExactMarginalLogLikelihood(self.likelihood, self.model)

        for i in range(1000):
            optimizer.zero_grad()
            output = self.model(self.X_train)
            loss = -mll(output, self.y_train)
            loss.backward()
            optimizer.step()

        

    def pred(self):
        self.model.eval()
        self.likelihood.eval()
        
        with torch.no_grad():#, gpytorch.settings.fast_pred_var():
            predictions = self.likelihood(self.model(self.X_test))
            model_predictions = predictions.mean

        return model_predictions

    def predict(self, points):

        points_scaled = self.scaler.transform(points)
        points_scaled_tensor = torch.tensor(points_scaled, dtype=torch.float32)
        self.model.eval()
        self.likelihood.eval()

        with torch.no_grad():#, gpytorch.settings.fast_pred_var():
            prediction = self.likelihood(self.model(points_scaled_tensor))
            model_prediction = prediction.mean

        return model_prediction.detach().numpy()

    def metrics(self, predictions):
        self.metrics_dict = {}
        # for target in self.targets:
            # self.metrics_dict[target] = {
            #     "MSE" : [],
            #     "r-squared" : []
            # }
        self.metrics_dict = {
            "MSE" : mean_squared_error(self.y_test, predictions),
            "r-squared" : r2_score(self.y_test, predictions)
        }

        return self.metrics_dict
    
    def save(self, filename):
        path = get_save_path(filename) # should end in .pt
        checkpoint = {
            "model_state_dict":      self.model.state_dict(),
            "likelihood_state_dict": self.likelihood.state_dict(),
            "features": self.features,
            "dim" : self.dim,
            "scaler" : self.scaler,
            # "scaler_mean" : self.scaler.mean_, # do i need this?
            # "scaler_scale" : self.scaler.scale_, # do i need this?
            # "X_train" : self.X_train,
            # "X_test" : self.X_test,
            # "y_train" : self.y_train,
            # "y_test" : self.y_test,
            "init_kwargs": {
                "target":    self.target,
                "problem":   self.problem,
                "dset_size": self.size,
                "seed":      self.seed
            }
        }
        torch.save(checkpoint, path)
        return path

    @classmethod
    def load(cls, filename):
        path = get_save_path(filename)

        checkpoint = torch.load(path, weights_only=False)
        instance = cls(**checkpoint["init_kwargs"])
        instance.model.load_state_dict(checkpoint["model_state_dict"])
        instance.likelihood.load_state_dict(checkpoint["likelihood_state_dict"])
        # instance.X_train, instance.X_test, instance.y_train, instance.y_test = instance.get_data()
        instance.scaler = checkpoint["scaler"]
        instance.features = checkpoint["features"]
        instance.dim = checkpoint["dim"]


        instance.model.eval()
        instance.likelihood.eval()

        return instance
