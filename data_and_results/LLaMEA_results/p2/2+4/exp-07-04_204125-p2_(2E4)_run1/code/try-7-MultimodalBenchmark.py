import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic component
        f1 = np.sum(x**2)
        
        # Chaotic-like multimodal component with nested structure
        f2 = 0.2 * np.sum(np.sin(10.0 * x) * np.cos(5.0 * x) * np.sin(2.0 * x))
        
        # Nested local minima using exponential decay
        f3 = 0.15 * np.sum(np.exp(-np.abs(x)) * np.sin(8.0 * x))
        
        # Add a complex, non-separable interaction term
        f4 = 0.1 * np.sum(np.sin(x[:-1] + x[1:]) * np.cos(x[:-1] - x[1:]) * np.sin(3.0 * x[:-1]))
        
        # Add a "chaotic" component with varying frequency
        f5 = 0.08 * np.sum(np.sin(15.0 * x + np.sin(7.0 * x)) * np.cos(4.0 * x + np.sin(9.0 * x)))
        
        # Combine all components
        return f1 + f2 + f3 + f4 + f5