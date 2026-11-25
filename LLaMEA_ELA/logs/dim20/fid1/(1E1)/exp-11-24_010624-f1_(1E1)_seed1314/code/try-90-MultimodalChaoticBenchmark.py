import numpy as np

class MultimodalChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute adaptive conditioning parameters
        self.conditioning = np.array([1.0 + 0.5 * np.sin(i * 0.5) for i in range(dim)])
        self.frequency = np.array([2.0 + 0.3 * np.cos(i * 0.8) for i in range(dim)])
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Exponential decay component with adaptive conditioning
        for i in range(self.dim):
            exp_term = self.conditioning[i] * np.exp(-0.1 * x[i]**2) * np.cos(self.frequency[i] * x[i])
            result += exp_term
            
        # Trigonometric coupling between dimensions
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited coupling
                coupling = np.sin(x[i] * x[j]) * np.cos(0.5 * (x[i] + x[j]))
                result += 0.3 * coupling * (1 + 0.1 * np.abs(x[i] - x[j]))
                
        # Adaptive polynomial terms with varying degrees
        for i in range(self.dim):
            poly_degree = 3 + int(i % 4)
            poly_term = 0.1 * x[i]**poly_degree * np.sin(0.2 * x[i])
            result += poly_term
            
        # Global sinusoidal modulation with adaptive frequency
        global_mod = np.sum(np.sin(x * 0.3)) * np.cos(np.sum(x * 0.1))
        result += 0.5 * global_mod
        
        # Add noise with dimension-dependent amplitude
        noise = 0.02 * np.sum(np.sin(x * 15) * self.conditioning)
        result += noise
        
        return result