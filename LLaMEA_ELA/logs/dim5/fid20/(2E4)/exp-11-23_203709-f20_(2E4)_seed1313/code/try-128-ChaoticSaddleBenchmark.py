import numpy as np

class ChaoticSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic parameters for each dimension with enhanced frequencies
        self.chaos_params = [np.sin(i * 1.2 + 2.0) * 3.0 + 2.0 for i in range(dim)]
        self.saddle_params = [np.cos(i * 0.8 + 1.1) * 0.9 + 1.5 for i in range(dim)]
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced polynomial chaos expansion component with varying degrees
        chaos = 0.0
        for i in range(self.dim):
            degree = int(4 + 4 * np.sin(i * 0.5 + 1.5))  # Increased base and frequency
            coeff = self.chaos_params[i]
            chaos += coeff * (x[i] ** degree)
        
        # Enhanced saddle-point structure with dynamic orientation
        saddle = 0.0
        for i in range(self.dim):
            orient = self.saddle_params[i]
            saddle += x[i] ** 2 * np.sin(orient * x[i]) + x[i] ** 4 * np.cos(orient * x[i]) + x[i] ** 6 * np.sin(0.5 * orient * x[i])
        
        # Enhanced cross-dimensional coupling with chaotic modulation
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                mod_i = 0.7 + 0.3 * np.sin(0.5 * (i + j) + 1.5)
                mod_j = 0.5 + 0.5 * np.cos(0.3 * (i - j) + 1.3)
                coupling += (x[i] ** 4 + x[j] ** 4) * mod_i * mod_j
        
        # Enhanced adaptive noise injection with time-varying amplitude
        noise = 0.0
        for i in range(self.dim):
            amp = 0.3 + 0.4 * np.sin(0.6 * i + 2.0)
            noise += amp * np.random.normal(0, 1)
        
        # Combined function with dynamic scaling
        total = 1.0 * chaos + 1.2 * saddle + 0.8 * coupling + 0.3 * noise
        
        return total