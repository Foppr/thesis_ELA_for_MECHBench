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
        
        # Exponential growth components with trigonometric modulation
        for i in range(self.dim):
            result += np.exp(0.1 * x[i]) * np.sin(2.0 * x[i]) + 0.5 * np.exp(-0.05 * x[i]**2) * np.cos(1.5 * x[i])
            
        # Cross-dimensional exponential coupling with chaotic interaction
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited coupling for complexity control
                coupling = np.exp(-0.1 * (x[i] - x[j])**2) * np.sin(3.0 * (x[i] + x[j]))
                result += 0.3 * coupling
                
        # Fractal-like perturbations using chaotic sine-cosine combinations
        fractal_perturbation = 0.0
        for i in range(self.dim):
            fractal_perturbation += 0.02 * np.sin(10.0 * np.sin(5.0 * x[i])) * np.cos(7.0 * np.cos(3.0 * x[i]))
            
        # Add global scaling with polynomial terms
        poly_term = 1.0 + 0.2 * np.sum(x**2) + 0.05 * np.sum(x**4) + 0.01 * np.sum(x**6)
        
        result = result * poly_term + fractal_perturbation
        
        return result