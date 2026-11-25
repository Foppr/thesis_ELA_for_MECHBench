import numpy as np

class ExponentialTrigonometricBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base exponential decay term
        result = np.sum(np.exp(-0.5 * x**2))
        
        # Trigonometric sine-cosine interaction terms with varying frequencies
        for i in range(self.dim):
            result += 0.5 * np.sin(2 * np.pi * x[i]) * np.cos(3 * np.pi * x[i])
            
        # Multi-scale exponential potentials with varying decay rates
        for i in range(self.dim):
            result += 0.3 * np.exp(-0.1 * np.abs(x[i])) * np.sin(5 * x[i])**2
            
        # Gradient-based attraction fields with multiple local minima
        for i in range(self.dim):
            result += 0.2 * (x[i] - np.sin(x[i]))**2 + 0.1 * np.cos(4 * x[i])
            
        # Cross-dimensional coupling with exponential decay and trigonometric modulation
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.abs(x[i] - x[j])
                result += 0.15 * np.exp(-dist) * np.sin(2 * np.pi * (x[i] + x[j]))
                
        # Non-linear transformation with piecewise polynomial components
        poly_term = 0.05 * np.sum(np.abs(x)**3 + 0.5 * x**4)
        result += poly_term
        
        # Add noise with fractal-like characteristics using fractional Brownian motion approximation
        noise = 0.03 * np.sum(np.sin(7 * x) + np.cos(11 * x) + np.tan(4 * x))
        result += noise
        
        # Scale the function to control overall difficulty
        result *= 1.5
        
        return result