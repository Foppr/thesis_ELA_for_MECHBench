import numpy as np

class MultimodalAdaptiveBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute adaptive conditioning parameters
        self.conditioning = np.array([1.0 + 0.5 * np.sin(i * 0.5) for i in range(dim)])
        self.frequency = np.array([1.0 + 0.3 * np.cos(i * 0.8) for i in range(dim)])
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Exponential decay component with adaptive conditioning
        for i in range(self.dim):
            exp_term = self.conditioning[i] * np.exp(-0.1 * np.abs(x[i])) * np.cos(self.frequency[i] * x[i])
            result += exp_term
            
        # Trigonometric coupling between dimensions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = np.sin(0.5 * (x[i]**2 + x[j]**2)) * np.cos(0.3 * x[i] * x[j])
                result += 0.2 * coupling
                
        # Add polynomial interaction with varying exponents
        poly_sum = 0.0
        for i in range(self.dim):
            poly_sum += (x[i]**3) * np.sin(0.4 * x[i]) * self.conditioning[i]
        result += 0.1 * poly_sum
        
        # Add radial component with dynamic scaling
        dist_squared = np.sum(x**2)
        radial_component = 0.5 * np.exp(-0.02 * dist_squared) * np.sin(0.2 * dist_squared)
        result += radial_component
        
        # Introduce chaotic-like behavior through recursive modulation
        modulated_result = 0.0
        for i in range(self.dim):
            mod_val = x[i] * np.sin(x[i]**2 + 1.0)
            modulated_result += mod_val * np.cos(0.3 * mod_val)
        result += 0.05 * modulated_result
        
        # Add noise to increase irregularity
        noise = 0.02 * np.sum(np.random.randn(self.dim) * np.sin(x))
        result += noise
        
        return result