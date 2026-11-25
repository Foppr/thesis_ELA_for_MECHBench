import numpy as np

class AsymmetricSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute cluster centers for penalty regions
        self.centers = np.random.uniform(-3, 3, (5, dim))
        
    def f(self, x):
        x = np.array(x)
        
        # Periodic sinusoidal components with varying frequencies and amplitudes
        periodic = np.sum(np.sin(2 * np.pi * x) * np.cos(3 * np.pi * x) + 
                          np.sin(5 * np.pi * x) * np.cos(7 * np.pi * x))
        
        # Asymmetric saddle points with different curvatures in each dimension
        saddles = 0
        for i in range(self.dim):
            saddles += (x[i]**4 - 2 * x[i]**2 + 0.5 * x[i]) * (1 + 0.3 * np.sin(2 * np.pi * x[i]))
            
        # Cross-dimensional coupling with asymmetric interaction terms
        cross_coupling = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Asymmetric coupling: stronger influence from dimension i to j
                cross_coupling += (x[i]**2 * x[j] + x[i] * x[j]**2) * np.exp(-0.1 * (x[i] - x[j])**2)
                
        # Adaptive penalty regions that change based on proximity to cluster centers
        penalty = 0
        for i in range(self.dim):
            dists = np.sqrt(np.sum((self.centers - x)**2, axis=1))
            min_dist = np.min(dists)
            penalty += 10 * (1 - np.exp(-0.5 * min_dist**2)) * np.sin(4 * np.pi * min_dist)**2
            
        # Combine all components with different weights
        return 0.7 * periodic + 0.8 * saddles + 0.6 * cross_coupling + penalty