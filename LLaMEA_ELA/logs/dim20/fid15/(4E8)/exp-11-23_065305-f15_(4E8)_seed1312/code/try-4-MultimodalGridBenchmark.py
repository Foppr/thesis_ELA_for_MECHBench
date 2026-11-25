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
            # Add sinusoidal terms with different frequencies and positions
            grid_terms += np.sin(0.5 * x[i]) * np.cos(0.3 * x[i])
            
        # Add some interaction terms between dimensions
        interaction = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interaction += 0.01 * x[i] * x[j]
                
        return basin + grid_terms + interaction