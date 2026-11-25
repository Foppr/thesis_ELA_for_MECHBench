import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-5, 5] domain
        x = np.array(x)
        
        # Enhanced polynomial terms with higher degree
        poly_term = np.sum(0.1 * x**6 - 2.0 * x**4 + 10.0 * x**2 + 0.5 * x)
        
        # Complex sinusoidal oscillations with multiple frequencies
        sin_term = np.sum(np.sin(0.8 * x) * np.cos(0.4 * x) + 
                         np.sin(1.2 * x) * np.cos(0.6 * x) + 
                         np.sin(0.3 * x) * np.cos(1.5 * x))
        
        # Multiple exponential peaks with varying positions and widths
        multi_term = np.sum(np.exp(-0.2 * (x - 3)**2) + 
                           np.exp(-0.2 * (x + 3)**2) + 
                           np.exp(-0.1 * (x - 1)**2) + 
                           np.exp(-0.1 * (x + 1)**2) + 
                           np.exp(-0.3 * x**2))
        
        # Add noise component to increase difficulty
        noise = 0.05 * np.sum(np.random.randn(self.dim) * x)
        
        # Combine all terms with different weights
        result = 0.2 * poly_term + 0.6 * sin_term - 0.4 * multi_term + noise
        
        return result