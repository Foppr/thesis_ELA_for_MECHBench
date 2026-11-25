import numpy as np

class ChaoticSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic parameters for each dimension with modified frequencies
        self.chaos_params = [np.sin(i * 0.9 + 1.5) * 2.5 + 1.5 for i in range(dim)]
        self.saddle_params = [np.cos(i * 0.6 + 0.9) * 0.7 + 1.2 for i in range(dim)]
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial chaos expansion component with varying degrees (modified)
        chaos = 0.0
        for i in range(self.dim):
            degree = int(3 + 3 * np.sin(i * 0.4 + 1.2))  # Increased base and frequency
            coeff = self.chaos_params[i]
            chaos += coeff * (x[i] ** degree)
        
        # Saddle-point structure with dynamic orientation (modified coefficients)
        saddle = 0.0
        for i in range(self.dim):
            orient = self.saddle_params[i]
            saddle += x[i] ** 2 * np.sin(orient * x[i]) + x[i] ** 4 * np.cos(orient * x[i])  # Added x^4 term
        
        # Cross-dimensional coupling with chaotic modulation (modified interaction)
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                mod_i = 0.6 + 0.4 * np.sin(0.4 * (i + j) + 1.2)  # Changed modulation
                mod_j = 0.4 + 0.6 * np.cos(0.2 * (i - j) + 1.1)  # Changed modulation
                coupling += (x[i] ** 3 + x[j] ** 3) * mod_i * mod_j  # Changed to x^3
        
        # Adaptive noise injection with time-varying amplitude (modified)
        noise = 0.0
        for i in range(self.dim):
            amp = 0.2 + 0.3 * np.sin(0.5 * i + 1.8)  # Changed amplitude formula
            noise += amp * np.random.normal(0, 1)
        
        # Combined function with dynamic scaling (modified weights)
        total = 0.9 * chaos + 1.1 * saddle + 0.7 * coupling + 0.2 * noise
        
        return total