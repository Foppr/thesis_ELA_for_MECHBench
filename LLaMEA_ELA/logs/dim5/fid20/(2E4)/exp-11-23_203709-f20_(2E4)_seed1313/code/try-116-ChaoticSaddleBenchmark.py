import numpy as np

class ChaoticSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic parameters for each dimension
        self.chaos_params = [np.sin(i * 0.7 + 1.2) * 3.0 + 2.0 for i in range(dim)]
        self.saddle_params = [np.cos(i * 0.5 + 0.8) * 0.5 + 1.0 for i in range(dim)]
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial chaos expansion component with varying degrees
        chaos = 0.0
        for i in range(self.dim):
            degree = int(2 + 2 * np.sin(i * 0.3 + 1.0))
            coeff = self.chaos_params[i]
            chaos += coeff * (x[i] ** degree)
        
        # Saddle-point structure with dynamic orientation
        saddle = 0.0
        for i in range(self.dim):
            orient = self.saddle_params[i]
            saddle += x[i] ** 2 * np.sin(orient * x[i]) + x[i] ** 3 * np.cos(orient * x[i])
        
        # Cross-dimensional coupling with chaotic modulation
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                mod_i = 0.5 + 0.5 * np.sin(0.3 * (i + j) + 1.0)
                mod_j = 0.5 + 0.5 * np.cos(0.3 * (i - j) + 1.0)
                coupling += (x[i] ** 2 + x[j] ** 2) * mod_i * mod_j
        
        # Adaptive noise injection with time-varying amplitude
        noise = 0.0
        for i in range(self.dim):
            amp = 0.3 + 0.2 * np.sin(0.4 * i + 2.0)
            noise += amp * np.random.normal(0, 1)
        
        # Combined function with dynamic scaling
        total = 0.8 * chaos + 1.2 * saddle + 0.6 * coupling + 0.3 * noise
        
        return total