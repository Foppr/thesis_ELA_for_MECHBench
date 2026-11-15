import numpy as np

class MultimodalSinusoidalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': -5.0, 'ub': 5.0})()
        
    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Input dimension mismatch")
        
        # Base quadratic term with condition number
        f = np.sum(x**2) * (1 + 0.1 * np.sum(np.abs(x)))
        
        # Add chaotic sinusoidal grid pattern with multiple global minima
        for i in range(self.dim):
            f += 0.2 * np.sin(7 * x[i]) * np.cos(4 * x[i]) * np.sin(2 * x[i]**2)
            
        # Add nested interaction terms between dimensions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f += 0.1 * np.sin(3 * x[i] + 2 * x[j]) * np.cos(5 * x[i] - x[j]) * np.exp(-0.1 * (x[i]**2 + x[j]**2))
                
        # Add fractal-like self-similar structure
        for i in range(self.dim):
            f += 0.05 * np.sin(10 * np.sin(3 * x[i])) * np.cos(7 * np.cos(2 * x[i]))
            
        # Add multiple nested global minima with varying scales
        for k in range(1, 4):
            f += 0.15 * np.exp(-0.5 * np.sum((x - k * np.pi/4)**2)) * np.sin(2 * k * np.pi * np.sum(x))
            
        # Add noise component to increase ruggedness
        f += 0.02 * np.sum(np.sin(100 * x) * np.cos(50 * x))
        
        return f