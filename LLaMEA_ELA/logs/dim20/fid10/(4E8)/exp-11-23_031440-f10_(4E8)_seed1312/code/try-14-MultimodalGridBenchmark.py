import numpy as np

class MultimodalGridBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Convert to numpy array and ensure correct shape
        x = np.array(x)
        
        # Quadratic basin term - encourages convergence to origin
        basin_term = 0.1 * np.sum(x**2)
        
        # Grid of global minima terms with consistent dimension handling
        grid_minima = 0.0
        for i in range(self.dim):
            # Create periodic pattern with multiple local minima using sin and cos
            grid_minima += np.sin(3 * np.pi * x[i] / 5.0) * np.cos(2 * np.pi * x[i] / 5.0)
            
        # Add a small noise term to make it more challenging (deterministic for reproducibility)
        noise = 0.01 * np.sum(np.sin(x) * np.cos(x))
        
        return basin_term + grid_minima + noise