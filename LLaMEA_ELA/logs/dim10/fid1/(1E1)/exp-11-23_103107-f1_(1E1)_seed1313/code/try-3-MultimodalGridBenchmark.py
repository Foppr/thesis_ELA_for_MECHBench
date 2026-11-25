import numpy as np

class MultimodalGridBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-5, 5] domain
        x = np.array(x)
        
        # Quadratic basin term - global minimum at origin
        basin = 0.1 * np.sum(x**2)
        
        # Multimodal grid terms - multiple global minima arranged in a grid
        grid_terms = 0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    grid_terms += np.sin((x[i] - x[j])**2) * np.cos(x[i]**2 + x[j]**2)
        
        # Add some additional harmonic terms to increase complexity
        harmonic = 0
        for i in range(self.dim):
            harmonic += np.sin(3 * x[i]) * np.cos(2 * x[i])
            
        return basin + grid_terms + harmonic