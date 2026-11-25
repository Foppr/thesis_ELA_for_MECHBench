import numpy as np

class RuggedValleyBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Gaussian valley terms with varying centers and widths
        valley_term = np.sum(np.exp(-0.5 * ((x - 2.0) / 1.5)**2) + np.exp(-0.5 * ((x + 2.0) / 1.2)**2))
        
        # Fractal-like gradient variations with multiple frequency components
        fractal_grad = np.sum(np.sin(4.0 * x) * np.cos(3.0 * x) * np.sin(2.0 * x) * np.cos(x))
        
        # Non-linear coupling with asymmetric interaction weights
        coupling_term = np.sum(0.8 * x[:-1]**3 * x[1:] + 0.6 * x[:-1] * x[1:]**3 + 0.4 * x[:-1]**2 * x[1:]**2)
        
        # Sharp directional change terms with hyperbolic tangent modulation
        sharp_term = np.sum(np.tanh(3.0 * x) * np.exp(-0.5 * x**2) * np.sin(5.0 * x))
        
        # Multi-scale oscillation with amplitude modulation
        oscillation_term = np.sum(np.sin(7.0 * x) * np.cos(6.0 * x) * (1.0 + 0.3 * np.sin(4.0 * x)) * np.exp(-0.2 * x**2))
        
        # Ruggedness enhancement through polynomial and exponential interactions
        rugged_term = np.sum(0.5 * x**5 - 0.3 * x**4 + 0.1 * x**3 + 0.2 * x**2 + 0.05 * x)
        
        # Combined function with optimized weights for ruggedness and multimodality
        return 0.25 * valley_term + 0.20 * fractal_grad + 0.18 * coupling_term + 0.15 * sharp_term + 0.12 * oscillation_term + 0.10 * rugged_term