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
            # Use different frequencies and add phase shift for complexity
            freq1 = 2 * np.pi * (x[i] + 0.5) / 2.0
            freq2 = 2 * np.pi * (x[i] - 0.3) / 1.5
            grid_minima += np.sin(freq1) * np.cos(freq2)
            
        # Add interaction terms between dimensions
        interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interaction += 0.05 * np.sin(0.5 * x[i]) * np.cos(0.3 * x[j])
        
        # Add noise term to make it more challenging
        noise = 0.02 * np.sum(np.random.rand(self.dim) * (x**2 + 1))
        
        return basin_term + grid_minima + interaction + noise