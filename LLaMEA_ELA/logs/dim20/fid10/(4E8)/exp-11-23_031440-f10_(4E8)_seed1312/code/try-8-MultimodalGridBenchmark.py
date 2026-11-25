import numpy as np

class MultimodalGridBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-5, 5] domain
        x = np.array(x)
        
        # Quadratic basin term - encourages convergence to origin
        basin_term = 0.1 * np.sum(x**2)
        
        # Grid of global minima terms with modified frequencies and phase shifts
        grid_minima = 0.0
        for i in range(self.dim):
            # Create periodic pattern with multiple local minima using different frequencies
            grid_minima += (np.sin(3 * np.pi * x[i] / 5.0) * np.cos(2 * np.pi * x[i] / 2.0) + 
                           0.5 * np.sin(4 * np.pi * x[i] / 3.0))
            
        # Add interaction terms between dimensions
        interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interaction += 0.05 * np.sin(np.pi * (x[i] + x[j]) / 4.0) * np.cos(np.pi * (x[i] - x[j]) / 3.0)
        
        # Add noise term to make it more challenging
        noise = 0.01 * np.sum(np.random.rand(self.dim) * x**2)
        
        return basin_term + grid_minima + interaction + noise