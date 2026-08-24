import numpy as np

class ChaoticTrigonometricBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Exponential base with sinusoidal modulation
        for i in range(self.dim):
            result += np.exp(0.5 * np.abs(x[i])) * np.sin(3.0 * x[i]) * np.cos(2.0 * x[i])
            
        # Cross-dimensional trigonometric coupling with varying frequencies
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.3 * np.sin(2.5 * x[i] + 1.2 * x[j]) * np.cos(1.8 * x[i] - 0.9 * x[j])
                
        # Add fractional Brownian motion-like irregularities using sine and cosine combinations
        for i in range(self.dim):
            result += 0.1 * np.sin(10.0 * x[i]) * np.cos(7.0 * x[i]) + 0.05 * np.sin(15.0 * x[i]**2)
            
        # Add polynomial conditioning with chaotic scaling
        poly_term = 0.0
        for i in range(self.dim):
            poly_term += x[i]**2 + 0.1 * x[i]**4 + 0.01 * x[i]**6
            
        # Apply chaotic scaling factor based on sum of sinusoids
        scale_factor = 1.0 + 0.2 * np.sum(np.sin(5.0 * x))
        result = result * (1.0 + 0.5 * poly_term) * scale_factor
        
        # Add a stochastic-like perturbation term
        stochastic_perturbation = 0.0
        for i in range(self.dim):
            stochastic_perturbation += 0.02 * np.sin(20.0 * x[i]) * np.cos(13.0 * x[i]) * np.sin(8.0 * x[i])
            
        result += stochastic_perturbation
        
        return result