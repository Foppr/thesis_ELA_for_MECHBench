import numpy as np

class MultiModalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial base with mixed degrees
        polynomial = np.sum(x**4 + 2*x**3 + 3*x**2 + x)
        
        # Trigonometric components creating oscillatory behavior
        trigonometric = np.sum(np.sin(3*x) * np.cos(2*x) + 0.5*np.sin(5*x))
        
        # Radial basis function component with multiple centers
        rbf = 0
        centers = np.linspace(-4, 4, min(5, self.dim))
        for i in range(self.dim):
            if i < len(centers):
                rbf += np.exp(-0.5 * (x[i] - centers[i])**2) * np.sin(2*x[i])
                
        # Cross-terms creating interaction between dimensions
        cross_terms = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_terms += (x[i]**2 + x[j]**2) * np.sin(0.3 * x[i] * x[j])
                
        # High-frequency oscillations to increase gradient complexity
        high_freq = 0
        for i in range(self.dim):
            high_freq += np.sin(10*x[i]) * np.cos(7*x[i]) + 0.3*np.sin(15*x[i])
            
        # Saddle-like structure with exponential scaling
        saddle = 0
        for i in range(self.dim):
            saddle += (x[i]**2 - 1) * np.exp(-0.2 * x[i]**2)
            
        # Multi-modal component with varying local minima depths
        multimodal = 0
        for i in range(self.dim):
            multimodal += (np.sin(4*x[i]) + 0.5*np.sin(8*x[i])) * np.exp(-0.1 * x[i]**2)
            
        # Combine all components with different weights
        return (0.2 * polynomial + 
                0.3 * trigonometric + 
                0.15 * rbf + 
                0.2 * cross_terms + 
                0.1 * high_freq + 
                0.1 * saddle + 
                0.05 * multimodal)