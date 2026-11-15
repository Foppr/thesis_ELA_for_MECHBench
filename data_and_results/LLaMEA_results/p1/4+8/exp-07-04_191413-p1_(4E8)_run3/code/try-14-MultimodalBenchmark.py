import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Global minimum at origin
        result = np.sum(x**2)
        
        # Add exponentially decaying sinusoidal components
        for i in range(self.dim):
            # Radial component with exponential decay
            r = np.sqrt(np.sum(x**2))
            result += np.exp(-r) * np.sin(2 * np.pi * x[i]) * np.cos(3 * np.pi * x[i])
        
        # Add cross-dimensional interactions with varying frequencies
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Interaction term with exponential decay based on distance
                dist = np.sqrt((x[i] - x[j])**2 + (x[i] + x[j])**2)
                result += 0.1 * np.exp(-dist/2) * np.sin(4 * x[i]) * np.cos(5 * x[j])
        
        # Add a radial symmetry component with multiple peaks
        r = np.sqrt(np.sum(x**2))
        result += 0.5 * np.exp(-r/3) * np.sin(10 * r) * np.cos(8 * r)
        
        # Add a small noise-like component to increase complexity
        result += 0.02 * np.sum(np.sin(15 * x) + np.cos(12 * x))
        
        return result