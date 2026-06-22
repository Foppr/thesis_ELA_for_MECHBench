import pandas as pd
from models import RSM, RandomForestModel, XGBModel, GPModel, BayesianNetworkModel

def instantiate_models(problems, sizes, models_dict):
    for size in sizes:
        for problem  in problems:
            if problem == 1:
                targets = ['intrusion', 'specific_energy_absorbed']
            elif problem == 2:
                targets = ['intrusion', 'mass']
            elif problem == 3:
                targets = ['load_uniformity']

            models_dict['BN'][f'BN_p{problem}_{size}D'] = BayesianNetworkModel(problem, size, SEED)
            print("Instantiated Bayesian Network")
            # for target in targets:
                # models_dict['RSM'][f'RSM_{target}_p{problem}_{size}D'] = RSM(target, problem, size, SEED)
                # print("Instantiated RSM")
                # models_dict['RF'][f'RF_{target}_p{problem}_{size}D'] = RandomForestModel(target, problem, size, SEED)
                # print("Instantiated Random Forest")
                # models_dict['XGB'][f'XGB_{target}_p{problem}_{size}D'] = XGBModel(target, problem, size, SEED)
                # print("Instantiated XGBoost")
                # models_dict['GP'][f'GP_{target}_p{problem}_{size}D'] = GPModel(target, problem, size, SEED)
                # print("Instantiated Gaussian Process")

    return models_dict

def track_metrics(models, problems, sizes):
    #TODO: create csvs of model performance for each model at each size on each problem
    for problem in problems:
        problem_df = None

    pass 

def main():
    problems = [1,2,3]
    sizes = [30, 60, 125, 250, 500]
    models_init = {
        # 'RSM' : {},
        # 'RF' : {},
        # 'XGB' : {},
        # 'GP' : {},
        'BN' : {}
    }
    # for size in sizes:
    #     for problem  in problems:
    #         if problem == 1:
    #             targets = ['Intrusion', 'SEA']
    #         elif problem == 2:
    #             targets = ['Intrusion', 'Mass']
    #         elif problem == 3:
    #             targets = ['LU']

    #         models['BN'][f'BN_p{problem}_{size}D']
    #         for target in targets:
    #             models['RSM'][f'RSM_{target}_p{problem}_{size}D'] = RSM(target, problem, size, SEED)
    #             models['RF'][f'RF_{target}_p{problem}_{size}D'] = RandomForestModel(target, problem, size, SEED)
    #             models['XGB'][f'XGB_{target}_p{problem}_{size}D'] = XGBModel(target, problem, size, SEED)
    #             models['GP'][f'GP_{target}_p{problem}_{size}D'] = GPModel(target, problem, size, SEED)
    models = instantiate_models(problems, sizes, models_init)

    
    for model_class, model_class_dict in models.items():
        print(f"----- {model_class} models -----")
        for model_name, model_instance in model_class_dict.items():
            print(f"Start fitting {model_name}")
            model_instance.train()
            #track_metrics(models) <- to create csv  of performances
            if model_class == 'XGB':
                extension = 'ubj'
            elif model_class == 'GP':
                extension = 'pt'
            else:
                extension = 'pkl'
            model_instance.save(f'{model_name}.{extension}')
            print(f"{model_name} fitted and saved")


if __name__ == "__main__":
    SEED = 1312
    main()