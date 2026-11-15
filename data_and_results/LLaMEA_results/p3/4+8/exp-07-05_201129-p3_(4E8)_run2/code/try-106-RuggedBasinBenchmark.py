import numpy as np

class RuggedBasinBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Polynomial base with high degree terms for non-separability
        poly_term = np.sum(x_norm**6) + 0.5 * np.sum(x_norm**4) + 0.1 * np.sum(x_norm**2)
        
        # Trigonometric modulation with multiple frequencies
        trig_term = 0.0
        for i in range(self.dim):
            trig_term += np.sin(10 * np.pi * x_norm[i]) * np.cos(7 * np.pi * x_norm[i])
        
        # Exponential interaction term between dimensions
        exp_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                exp_term += np.exp(-5 * (x_norm[i] - x_norm[j])**2)
        
        # Basin-forming potential wells with varying depths
        basin_term = 0.0
        for i in range(self.dim):
            basin_term += 0.5 * (x_norm[i] - 0.3)**2 * (x_norm[i] + 0.3)**2
        
        # Cross-term interactions creating complex ridges and valleys
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    cross_term += 0.1 * np.sin(3 * np.pi * x_norm[i]) * np.cos(2 * np.pi * x_norm[j])
        
        # Global optimum at origin with additional local optima
        return poly_term + 0.3 * trig_term + 0.2 * exp_term + 0.15 * basin_term + 0.25 * cross_term + 1.0