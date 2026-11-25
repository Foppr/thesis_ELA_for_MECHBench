import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute logistic map parameters with enhanced chaos
        self.r_values = np.linspace(3.8, 4.2, min(dim, 15))
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced logistic map chaos component with feedback coupling
        chaos_term = 0.0
        for i in range(min(self.dim, 15)):
            if i == 0:
                x_prev = 0.5
            else:
                x_prev = x[i-1] / 5.0 + 0.5
            chaos_term += self.r_values[i] * x_prev * (1 - x_prev)
        
        # Modified radial basis function with dynamic centers and adaptive sigmas
        rbfs = 0.0
        num_centers = min(7, self.dim)
        centers = np.linspace(-4.5, 4.5, num_centers)
        for i, center in enumerate(centers):
            for j in range(self.dim):
                sigma = 1.2 + 0.3 * np.sin(i * 0.7 + x[j] * 0.1)
                rbfs += np.exp(-0.5 * ((x[j] - center) / sigma)**2) * \
                       np.cos(4.0 * np.pi * (x[j] - center) / (2.5 + 0.2 * i))
        
        # Stronger asymmetric saddle points with higher-order polynomial and trigonometric mixing
        saddle = 0.0
        for i in range(self.dim):
            saddle += (x[i]**7 - 7*x[i]**5 + 15*x[i]**3 - 9*x[i]) * np.sin(0.8 * x[i]) + \
                     0.15 * (x[i] - np.mean(x))**7
        
        # Cross-dimensional interaction with multi-scale coupling and dynamic weights
        cross_term = 0.0
        for i in range(self.dim):
            j = (i + 2) % self.dim
            k = (i + 5) % self.dim
            weight = 1.0 + 0.4 * np.sin(i * 0.5 + x[j] * 0.2)
            cross_term += weight * np.sin(3.0 * x[i]) * np.cos(2.0 * x[j]) * \
                         np.exp(-0.2 * (x[i]**2 + x[j]**2)) * \
                         np.tanh(0.5 * (x[k] - x[i]))
        
        # Combine all components with refined weights
        result = 0.3 * np.sum(x**2) + 0.4 * chaos_term + 0.3 * rbfs + 0.3 * saddle + 0.2 * cross_term
        
        return result