import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term for conditioning
        result = np.sum(x**2)
        
        # Add chaotic exponential interactions between variables
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.3 * np.exp(-0.5 * (x[i] - x[j])**2) * np.sin(3 * x[i]) * np.cos(2 * x[j])
        
        # Introduce trigonometric forcing with varying frequencies
        for i in range(self.dim):
            result += 0.25 * np.sin(5 * x[i]) * np.cos(3 * x[i]) * np.tan(0.5 * x[i])
            
        # Add a radial chaotic component with multiple peaks
        r = np.sqrt(np.sum(x**2))
        result += 0.4 * np.exp(-0.1 * r) * np.sin(8 * r) * np.cos(4 * r)
        
        # Include a non-smooth, piecewise component to increase complexity
        for i in range(self.dim):
            result += 0.1 * np.abs(x[i]) * np.sin(10 * x[i])
            
        return result