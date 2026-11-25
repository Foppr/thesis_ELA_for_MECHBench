import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        result = np.sum(x**2)
        
        # Add multiple sinusoidal oscillations with varying frequencies and amplitudes
        for i in range(self.dim):
            result += 2.5 * np.sin(3.0 * x[i]) * np.cos(5.0 * x[i]) + 1.8 * np.sin(7.0 * x[i])
            
        # Add radial basis function components with adaptive widths
        for i in range(self.dim):
            result += 0.9 * np.exp(-0.5 * (x[i] - 2.0)**2) + 0.7 * np.exp(-0.3 * (x[i] + 3.0)**2)
            
        # Add a multi-modal component with polynomial interactions
        for i in range(self.dim):
            result += 0.5 * x[i]**4 - 0.9 * x[i]**3 + 0.4 * x[i]**2
            
        # Add cross-dimensional coupling with trigonometric functions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.4 * np.sin(x[i] * x[j]) * np.cos(0.6 * (x[i]**2 + x[j]**2))
                
        # Add a conditioning component that scales with dimensionality
        condition_factor = 1.0 + 0.3 * self.dim
        result *= condition_factor
        
        # Add chaotic behavior through nested trigonometric functions
        for i in range(self.dim):
            result += 0.6 * np.sin(np.pi * np.sin(2.5 * x[i])) * np.cos(np.pi * np.cos(1.8 * x[i]))
            
        # Add a fractal-like component with recursive sine terms
        for i in range(self.dim):
            recursive_term = 0.0
            for k in range(1, 5):
                recursive_term += 0.25**k * np.sin(2**(k) * x[i])
            result += recursive_term
            
        # Add penalty for large values with exponential scaling
        result += 0.15 * np.sum(np.exp(np.abs(x)) - 1)
        
        return result