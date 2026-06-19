from scipy.stats import qmc
from tqdm import tqdm
import pandas as pd


def sampler(size=500, dim=15, seed=1312):
    sobol = qmc.Sobol(d=dim, scramble=True, seed=seed)
    
    points = sobol.random(size*dim)*10-5
    datapoints = []
    for i, x in enumerate(tqdm(points, desc="generating datapoints"), start=1):
        # print (f"datapoint {i}")
        datapoints.append([i])
        datapoints[i-1] = datapoints[i-1] + x.tolist()

    df = pd.DataFrame(datapoints, columns=["id", "x0", "x1", "x2", "x3", "x4", "x5", "x6", "x7", "x8", "x9", "x10", "x11", "x12", "x13", "x14"])
    return df


points = sampler(seed=1312)
print(points.to_string())
path = "C:/Users/foppe/Documents/DSAI-3/Thesis/thesis_code/point_4780.csv"
points.to_csv(path, index=False, sep=' ')
