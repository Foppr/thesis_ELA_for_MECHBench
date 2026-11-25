import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute logistic map parameters for chaos generation with slight modification
        self.r_values = np.linspace(3.7, 4.2, dim)
    
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
        centers = np.linspace(-3.8, 3.8, 7)  # Slightly more shifted centers
        for i, center in enumerate(centers):
            for j in range(self.dim):
                rbfs += np.exp(-0.5 * ((x[j] - center) / (1.3 + 0.4 * (i % 2)))**2) * \
                       np.sin(3.0 * np.pi * (x[j] - center) / (2.0 + 0.3 * (i % 3)))
        
        # Asymmetric saddle points with increased nonlinearity
        saddle = 0.0
        for i in range(self.dim):
            saddle += (x[i]**5 - 5*x[i]**3) * np.cos(0.7 * x[i]) + \
                     0.2 * (x[i] - np.mean(x))**6  # Increased power for more complexity
        
        # Cross-dimensional interaction with altered periodic terms
        cross_term = 0.0
        for i in range(self.dim):
            j = (i + 3) % self.dim  # Changed coupling shift
            cross_term += np.sin(4.0 * x[i]) * np.cos(3.0 * x[j]) * \
                         np.exp(-0.15 * (x[i]**2 + x[j]**2))
        
        # Combine all components with modified weights
        result = 0.5 * np.sum(x**2) + 0.4 * chaos_term + 0.5 * rbfs + 0.3 * saddle + 0.2 * cross_term
        
        return result