import pandas as pd
import numpy as np
from pgmpy.estimators import HillClimbSearch, BayesianEstimator, MaximumLikelihoodEstimator, BICGauss, ExpertKnowledge
# from pgmpy.structure_score import 
from pgmpy.models import BayesianNetwork, LinearGaussianBayesianNetwork #, DiscreteBayesianNetwork<-uncomment and replace
from pgmpy.inference import VariableElimination
from pgmpy.factors.continuous import LinearGaussianCPD
from sklearn.preprocessing import KBinsDiscretizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

import pickle
from pathlib import Path
from ._utils import get_save_path, get_data_path


class BayesianNetworkModel():

    def __init__(self, problem=2, dset_size=250, seed=1312):
        self.problem = problem
        self.size = dset_size
        self.seed = seed

        if self.problem==1:
            self.features = ['x0', 'x1', 'x2', 'x3', 'x4']
            self.targets = ["intrusion", "specific_energy_absorbed",]# "penalized_sea"]
            # self.targets = ["Intrusion", "SEA"]#, "Penalized SEA"]
            self.dim = 5
        elif self.problem == 2:
            self.features = ['x0', 'x1', 'x2', 'x3', 'x4']
            self.targets = ["intrusion", "mass"]#, "penalized_mass"]
            # self.targets = ["Intrusion", "Mass"]#, "Penalized Mass"]
            self.dim = 5
        elif self.problem == 3:
            self.features = ['x0', 'x1', 'x2', 'x3', 'x4', 'x5', 'x6', 'x7', 'x8', 'x9', 'x10', 'x11', 'x12', 'x13', 'x14']
            # self.targets = ["LU"]
            self.targets = ['load_uniformity']
            self.dim = 15

        self.feature_discretizer = KBinsDiscretizer(n_bins=20, encode="ordinal", strategy='quantile')
        self.target_discretizer = KBinsDiscretizer(n_bins=20, encode='ordinal', strategy='quantile')
        self.train_data, self.test_data = self.get_data()

        feature_to_target = [(x, target) for x in self.features for target in self.targets]
        target_to_feature_or_target = []
        for target in self.targets:
            for x in self.features:
                target_to_feature_or_target.append((target,x))

        if self.problem == 1:
            target_to_feature_or_target.append(("intrusion", "specific_energy_absorbed"))
            target_to_feature_or_target.append(("specific_energy_absorbed", "intrusion"))
        elif self.problem == 2:
            target_to_feature_or_target.append(("mass", "intrusion"))
            target_to_feature_or_target.append(('intrusion', 'mass'))

        expert_knowledge = ExpertKnowledge(forbidden_edges=target_to_feature_or_target)


        hc = HillClimbSearch(self.train_data)
        estimated_model = hc.estimate(
            # white_list=feature_to_target,
            # black_list=target_to_feature_or_target,
            # scoring_method=BIC(self.train_data)
            # scoring_method = BicScore(self.train_data) #<- replace
            scoring_method = BICGauss(self.train_data),
            expert_knowledge=expert_knowledge
        )

        # self.model = DiscreteBayesianNetwork(estimated_model.edges())
        # self.model = BayesianNetwork(estimated_model.edges())
        self.model = LinearGaussianBayesianNetwork(estimated_model.edges())


        for target in self.targets:
            if target not in self.model.nodes():
                self.model.add_node(target)


    def get_data(self):
        path = get_data_path(self.problem, self.size, self.dim, self.seed)
        # get csv
        # data= pd.read_csv(f"data_p{self.problem}/{self.size}D/{self.size}d{self.dim}_p{self.problem}_seed{self.seed}.csv")
        data = pd.read_csv(path)
        X = data[self.features]
        y = data[self.targets]

        train_data, test_data = train_test_split(pd.concat([X, y], axis=1), test_size=0.2, random_state=self.seed)

        # data 
        # discritize
        # discretizer = KBinsDiscretizer(n_bins=5, encode='ordinal')
        # discretized_X_train = pd.DataFrame(self.feature_discretizer.fit_transform(X_train), columns=self.features).astype(int)
        # discretized_y_train = pd.DataFrame(self.target_discretizer.fit_transform(y_train), columns=self.targets).astype(int)

        # discretized_X_test = pd.DataFrame(self.feature_discretizer.transform(X_test), columns=self.features).astype(int)
        # discretized_y_test = pd.DataFrame(self.feature_discretizer.transform(y_test), columns=self.features).astype(int)
        # return train_test_split(pd.concat([discretized_X, discretized_y], axis=1), test_size=0.2, random_state=self.seed)
        # return X_train, X_test, y_train, y_test 

        # train_data = pd.concat([X_train, y_train],axis=1)
        # test_data = pd.concat([X_test, y_test], axis=1)

        return train_data, test_data


    def train(self):
        
        # self.model.fit(self.train_data, estimator=BayesianEstimator)
        # self.infer = VariableElimination(self.model)

        # estimator = BayesianEstimator(model=self.model, data=self.train_data, prior_type='BDeu', equivalent_sample_size=10) #bic instead?
        # estimator = BayesianEstimator
        # estimator = BayesianEstimator(
        #     model=self.model,
        #     data=self.train_data,        # <-- add this
        #     # prior_type='BDeu',
        #     # equivalent_sample_size=10
        # )
        self.model.fit(self.train_data)
        # self.infer = VariableElimination(self.model)

    def predict_row(self, row):
        values = {col: float(row[col]) for col in self.features}# if col in self.model.nodes()}

        for target in self.targets:
            cpd = self.model.get_cpds(target)

            mean = float(cpd.beta[0])

            for i, parent in enumerate(cpd.evidence):
                if parent in values:
                    mean += float(cpd.beta[i + 1]) * values[parent]
    
            values[target] = mean

        return {target: values[target] for target in self.targets}

    
    def pred(self):

        nodes = set(self.model.nodes())
        features_in_graph = [feature for feature in self.features if feature in nodes]

        predictions = {target: [] for target in self.targets}

        for _, row in self.test_data.iterrows():
            # evidence = {feature: row[feature] for feature in features_in_graph}
            row_preds = self.predict_row(row)
            for target in self.targets:
                predictions[target].append(row_preds[target])
                # query = self.infer.query([target], evidence = evidence)
                # bin_id = int(np.argmax(query.values))
                
                # predictions[target].append(int(np.argmax(query.values)))
                # predictions[target].append(query.mean)

                # continuous = self.value_from_bin(target, bin_id)
                # predictions[target].append(continuous)


        self.predictions_df = pd.DataFrame(predictions, index=self.test_data.index)

        return self.predictions_df
    
    def predict(self, X):
        X = pd.DataFrame(X, columns=self.features)
        # discretizer = KBinsDiscretizer(n_bins=5, encode='ordinal')
        # X_discretized = pd.DataFrame(
        #     self.discretizer.transform(X),
        #     columns = self.features
        # ).astype(int)

        # nodes = set(self.model.nodes())
        # features_in_graph = [feature for feature in self.features if feature in nodes]

        predictions = {target: [] for target in self.targets}

        for _, row in X.iterrows():
            # evidence = {feature: row[feature] for feature in features_in_graph}
            row_preds = self.predict_row(row)
            for target in self.targets:
                # query = self.infer.query([target], evidence=evidence)
                # bin_id = int(np.argmax(query.values))
                # # predictions[target].append(int(np.argmax(query.values)))
                # predictions[target].append(query.mean)
                # continuous = self.value_from_bin(target, bin_id)
                # predictions[target].append(continuous)
                predictions[target].append(row_preds[target])

        predictions_df = pd.DataFrame(predictions)

        return predictions_df

    def value_from_bin(self, target, bin_id):
        col_id = self.targets.index(target)
        edges = self.target_discretizer.bin_edges_[col_id]

        return (edges[bin_id] + edges[bin_id+1]) / 2.0

    def metrics(self, predictions):
        self.metrics_dict = {}
        for target in self.targets:
            # self.metrics_dict[target] = {
            #     "MSE" : [],
            #     "r-squared" : []
            # }
            self.metrics_dict[target] = {
                "MSE" : mean_squared_error(self.test_data[target], predictions[target]),#self.predictions_df[target]),
                "r-squared" : r2_score(self.test_data[target], predictions[target])# self.predictions_df[target])
            }

        return self.metrics_dict

        

    def save(self, filename):
        path = get_save_path(filename)
        checkpoint = {
            "model": self.model,
            # "discretizer": self.discretizer,
            "train_data": self.train_data,
            "test_data": self.test_data,
            "problem": self.problem,
            "size": self.size,
            "seed": self.seed,
            "features": self.features,
            "targets": self.targets,
            "dim": self.dim
        }       
        with open(path, "wb") as model_file:
            pickle.dump(checkpoint, model_file)

    
    @classmethod
    def load(cls, filename, problem=1, dset_size=250, seed=1312):
        path = get_save_path(filename)
        # instance = cls.__new__(cls)
        # instance.problem  = problem
        # if problem==1:
        #     instance.features = ['x0', 'x1', 'x2', 'x3', 'x4']
        #     instance.targets = ['intrusion', 'specific_energy_absorbed']
        #     instance.dim = 5
        # elif problem==2:
        #     instance.features = ['x0', 'x1', 'x2', 'x3', 'x4']
        #     instance.targets = ['intrusion', 'mass']
        #     instance.dim = 5
        # elif problem == 3:
        #     instance.features = ['x0', 'x1', 'x2', 'x3', 'x4', 'x5', 'x6', 'x7', 'x8', 'x9', 'x10', 'x11', 'x12', 'x13', 'x14']
        #     instance.targets = ['intrusion', 'load_uniformity']
        #     instance.dim = 15

        
        # instance.size = dset_size
        # instance.seed=seed
        # instance.train_data, instance.test_data = instance.get_data()

        with open(path, "rb") as model_file:
            checkpoint = pickle.load(model_file)

        instance = cls.__new__(cls)
        instance.problem = checkpoint["problem"]
        instance.size = checkpoint["size"]
        instance.seed = checkpoint["seed"]
        instance.features = checkpoint["features"]
        instance.targets = checkpoint["targets"]
        instance.dim = checkpoint["dim"]
        instance.model = checkpoint["model"]
        # instance.discretizer = checkpoint["discretizer"]
        instance.train_data = checkpoint["train_data"]
        instance.test_data = checkpoint["test_data"]

        # instance.model = pickle.load(model_file)

        # instance.infer = VariableElimination(instance.model)
        
        return instance