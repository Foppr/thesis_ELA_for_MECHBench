import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute logistic map parameters for chaos generation with slight modification
        self.r_values = np.linspace(3.6, 4.1, dim)
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Logistic map chaos component with modified recurrence
        chaos_term = 0.0
        for i in range(min(self.dim, 10)):  # Limit to first 10 dimensions for chaos
            if i == 0:
                x_prev = 0.5
            else:
                x_prev = x[i-1] / 5.0 + 0.5  # Normalize to [0,1]
            chaos_term += self.r_values[i] * x_prev * (1 - x_prev)
        
        # Radial basis function component with shifted centers and modified weights
        rbfs = 0.0
        centers = np.linspace(-3.5, 3.5, 7)  # Shifted centers
        for i, center in enumerate(centers):
            for j in range(self.dim):
                rbfs += np.exp(-0.5 * ((x[j] - center) / (1.2 + 0.3 * (i % 2)))**2) * \
                       np.sin(2.5 * np.pi * (x[j] - center) / (1.8 + 0.2 * (i % 3)))
        
        # Asymmetric saddle points with increased nonlinearity
        saddle = 0.0
        for i in range(self.dim):
            saddle += (x[i]**4 - 4*x[i]**2) * np.cos(0.6 * x[i]) + \
                     0.15 * (x[i] - np.mean(x))**5  # Increased power for more complexity
        
        # Cross-dimensional interaction with altered periodic terms
        cross_term = 0.0
        for i in range(self.dim):
            j = (i + 2) % self.dim  # Shifted coupling
            cross_term += np.sin(3.5 * x[i]) * np.cos(2.5 * x[j]) * \
                         np.exp(-0.12 * (x[i]**2 + x[j]**2))
        
        # Combine all components with modified weights
        result = 0.5 * np.sum(x**2) + 0.35 * chaos_term + 0.45 * rbfs + 0.25 * saddle + 0.15 * cross_term
        
        return result