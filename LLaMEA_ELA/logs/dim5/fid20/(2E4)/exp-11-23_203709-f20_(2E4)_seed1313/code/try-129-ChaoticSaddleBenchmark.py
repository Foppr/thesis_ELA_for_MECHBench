import numpy as np

class ChaoticSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic parameters for each dimension with altered frequencies and amplitudes
        self.chaos_params = [np.sin(i * 0.7 + 1.3) * 3.0 + 2.0 for i in range(dim)]
        self.saddle_params = [np.cos(i * 0.5 + 1.1) * 0.8 + 1.5 for i in range(dim)]
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced polynomial chaos expansion component with varying degrees (modified)
        chaos = 0.0
        for i in range(self.dim):
            degree = int(4 + 2 * np.sin(i * 0.3 + 1.0))  # Increased base and frequency
            coeff = self.chaos_params[i]
            chaos += coeff * (x[i] ** degree)
        
        # Enhanced saddle-point structure with dynamic orientation (modified coefficients)
        saddle = 0.0
        for i in range(self.dim):
            orient = self.saddle_params[i]
            saddle += x[i] ** 2 * np.sin(orient * x[i]) + x[i] ** 4 * np.cos(orient * x[i]) + x[i] ** 6 * np.sin(orient * x[i] / 2.0)  # Added higher-order terms
        
        # Cross-dimensional coupling with enhanced chaotic modulation (modified interaction)
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                mod_i = 0.5 + 0.5 * np.sin(0.3 * (i + j) + 1.4)  # Changed modulation
                mod_j = 0.3 + 0.7 * np.cos(0.3 * (i - j) + 1.0)  # Changed modulation
                coupling += (x[i] ** 4 + x[j] ** 4) * mod_i * mod_j  # Changed to x^4
        
        # Enhanced noise injection with time-varying amplitude (modified)
        noise = 0.0
        for i in range(self.dim):
            amp = 0.3 + 0.2 * np.sin(0.6 * i + 1.9)  # Changed amplitude formula
            noise += amp * np.random.normal(0, 1)
        
        # Combined function with dynamic scaling (modified weights)
        total = 1.0 * chaos + 1.2 * saddle + 0.8 * coupling + 0.15 * noise
        
        return total