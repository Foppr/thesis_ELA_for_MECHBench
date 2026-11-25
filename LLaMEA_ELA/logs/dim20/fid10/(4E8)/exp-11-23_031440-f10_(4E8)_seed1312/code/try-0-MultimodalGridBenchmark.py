import numpy as np

class MultimodalGridBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-5, 5] domain
        x = np.array(x)
        
        # Quadratic basin term - encourages convergence to origin
        basin_term = 0.1 * np.sum(x**2)
        
        # Grid of global minima terms
        grid_minima = 0.0
        for i in range(self.dim):
            # Create periodic pattern with multiple local minima
            grid_minima += np.sin(2 * np.pi * x[i] / 2.5) * np.cos(2 * np.pi * x[i] / 1.2)
            
        # Add noise term to make it more challenging
        noise = 0.01 * np.sum(np.random.rand(self.dim) * x**2)
        
        return basin_term + grid_minima + noise