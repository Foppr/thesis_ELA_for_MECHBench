import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute logistic map parameters with enhanced chaos
        self.r_values = np.linspace(3.9, 4.1, min(dim, 15))
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced logistic map chaos component
        chaos_term = 0.0
        for i in range(min(self.dim, 15)):
            if i == 0:
                x_prev = 0.5
            else:
                x_prev = x[i-1] / 5.0 + 0.5
            chaos_term += self.r_values[i] * x_prev * (1 - x_prev)
        
        # Modified radial basis function with more varied centers and weights
        rbfs = 0.0
        centers = np.linspace(-4.0, 4.0, 9)
        for i, center in enumerate(centers):
            for j in range(self.dim):
                sigma = 1.2 + 0.1 * np.sin(i * 0.7)
                rbfs += np.exp(-0.5 * ((x[j] - center) / sigma)**2) * \
                       np.cos(2.5 * np.pi * (x[j] - center) / (1.8 + 0.15 * i))
        
        # Stronger asymmetric saddle points with exponential nonlinearity
        saddle = 0.0
        for i in range(self.dim):
            saddle += (x[i]**5 - 5*x[i]**3 + 4*x[i]) * np.sin(0.8 * x[i]) + \
                     0.15 * (x[i] - np.mean(x))**6
        
        # Cross-dimensional interaction with sine-cosine coupling and adaptive weights
        cross_term = 0.0
        for i in range(self.dim):
            j = (i + 2) % self.dim
            weight = 1.1 + 0.25 * np.sin(i * 0.5)
            cross_term += weight * np.sin(3.5 * x[i]) * np.cos(2.5 * x[j]) * \
                         np.exp(-0.2 * (x[i]**2 + x[j]**2))
        
        # Combine all components with refined weights
        result = 0.35 * np.sum(x**2) + 0.45 * chaos_term + 0.25 * rbfs + 0.35 * saddle + 0.25 * cross_term
        
        return result