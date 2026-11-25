import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': np.full(dim, -5.0), 'ub': np.full(dim, 5.0)})()
        
        # chaotic parameters for different dimensions
        self.a = 3.9
        self.b = 0.5
        self.c = 0.1
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Chaotic component using logistic map
        chaotic_term = 0.0
        for i in range(self.dim):
            if i == 0:
                x_prev = 0.5
            else:
                x_prev = x_norm[i-1]
            
            # Logistic map: x_n+1 = a * x_n * (1 - x_n)
            x_next = self.a * x_prev * (1 - x_prev)
            chaotic_term += np.sin(x_next * 10) * np.cos(x_next * 5)
        
        # Exponential decay interactions
        decay_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.abs(x_norm[i] - x_norm[j])
                decay_term += np.exp(-dist) * np.sin(2 * np.pi * dist)
        
        # Dynamic conditioning based on dimension
        cond_term = 0.0
        for i in range(self.dim):
            cond_term += (i + 1) * np.sin(x_norm[i]**2) * np.cos(x_norm[i])
        
        # Sinusoidal interference
        sine_term = 0.0
        for i in range(self.dim):
            sine_term += np.sin(5 * x_norm[i]) * np.cos(3 * x_norm[i])
            
        # Quadratic basin term
        basin_term = 0.5 * np.sum(x_norm**2)
        
        # Combine all terms
        result = basin_term + chaotic_term + decay_term + cond_term + sine_term
        
        return result