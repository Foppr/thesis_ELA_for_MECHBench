import numpy as np

class FractalMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Fractal component with self-similarity across scales
        for i in range(self.dim):
            # Create fractal-like behavior using nested trigonometric functions
            fractal_term = np.sin(x[i]) + 0.5 * np.sin(2 * x[i]) + 0.3 * np.sin(3 * x[i])
            result += fractal_term**2
        
        # Frequency modulation component creating multi-scale structure
        for i in range(self.dim):
            freq_mod = np.sin(10 * np.sin(x[i])) * np.cos(7 * np.cos(x[i]))
            result += 0.8 * freq_mod
        
        # Cross-dimensional interaction with nested coupling
        for i in range(self.dim - 1):
            # Create nested structure with varying coupling strength
            coupling = np.exp(-0.1 * (x[i]**2 + x[i+1]**2)) * np.sin(5 * x[i] * x[i+1])
            result += 0.4 * coupling
        
        # Polynomial fractal component for additional complexity
        for i in range(self.dim):
            # Higher-order polynomial with fractal-like behavior
            poly_term = 0.1 * x[i]**6 - 0.5 * x[i]**4 + 0.8 * x[i]**2
            result += poly_term
        
        # Add chaotic element through recursive-like structure
        for i in range(self.dim):
            # Recursive-like behavior with exponential decay
            recursive = np.exp(-0.05 * x[i]**2) * np.sin(15 * x[i])
            result += 0.3 * recursive
        
        # Normalize by dimension to keep scale reasonable
        result /= self.dim
        
        return result