import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute logistic map parameters for chaos generation
        self.r_values = np.linspace(3.5, 4.0, dim)
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Logistic map chaos component
        chaos_term = 0.0
        for i in range(min(self.dim, 10)):  # Limit to first 10 dimensions for chaos
            if i == 0:
                x_prev = 0.5
            else:
                x_prev = x[i-1] / 5.0 + 0.5  # Normalize to [0,1]
            chaos_term += self.r_values[i] * x_prev * (1 - x_prev)
        
        # Radial basis function component with asymmetric peaks
        rbfs = 0.0
        centers = np.linspace(-4, 4, 5)
        for i, center in enumerate(centers):
            for j in range(self.dim):
                rbfs += np.exp(-0.5 * ((x[j] - center) / (1.5 + 0.5 * (i % 2)))**2) * \
                       np.sin(2 * np.pi * (x[j] - center) / (2.0 + 0.3 * (i % 3)))
        
        # Asymmetric saddle points
        saddle = 0.0
        for i in range(self.dim):
            saddle += (x[i]**3 - 3*x[i]) * np.cos(0.5 * x[i]) + \
                     0.1 * (x[i] - np.mean(x))**4
        
        # Cross-dimensional interaction with periodic terms
        cross_term = 0.0
        for i in range(self.dim):
            j = (i + 1) % self.dim
            cross_term += np.sin(3 * x[i]) * np.cos(2 * x[j]) * \
                         np.exp(-0.1 * (x[i]**2 + x[j]**2))
        
        # Combine all components with different weights
        result = 0.5 * np.sum(x**2) + 0.3 * chaos_term + 0.4 * rbfs + 0.2 * saddle + 0.1 * cross_term
        
        return result