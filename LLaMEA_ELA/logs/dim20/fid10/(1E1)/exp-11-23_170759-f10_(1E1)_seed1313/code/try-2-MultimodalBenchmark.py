import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-5, 5] domain
        x = np.array(x)
        
        # Global minimum at origin
        result = 0.0
        
        # Add multiple quadratic terms with different centers and scales
        centers = [
            [2.0, 2.0], 
            [-2.0, 2.0], 
            [2.0, -2.0], 
            [-2.0, -2.0]
        ]
        
        # Add 4 quadratic wells with different scales
        for i, center in enumerate(centers):
            if self.dim >= 2:
                # For higher dimensions, use first 2 dimensions for the wells
                dist = np.sum((x[:2] - center)**2)
                result += 0.3 * np.exp(-dist / 1.5) * (1.0 + 0.2 * i)
        
        # Add a central quadratic term that pulls towards origin
        result += 0.15 * np.sum(x**2)
        
        # Add some sinusoidal modulation to increase complexity
        if self.dim > 0:
            result += 0.08 * np.sin(4.0 * x[0]) * np.cos(4.0 * x[1]) if self.dim >= 2 else 0
        
        # Add a small noise term to make the landscape more challenging
        result += 0.02 * np.random.rand()
        
        return result