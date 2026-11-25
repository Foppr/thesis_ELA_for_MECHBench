import numpy as np

class MultimodalGridBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Convert to numpy array and ensure correct shape
        x = np.array(x)
        
        # Quadratic basin term - encourages convergence to origin
        basin_term = 0.1 * np.sum(x**2)
        
        # Grid of global minima terms with proper dimension handling
        grid_minima = 0.0
        for i in range(self.dim):
            # Create periodic pattern with multiple local minima using sine and cosine
            grid_minima += np.sin(3 * np.pi * x[i] / 2.0) * np.cos(3 * np.pi * x[i] / 1.5)
            
        # Add a small random noise term to make it more challenging (deterministic for reproducibility)
        np.random.seed(hash(str(x)) % (2**32))  # Deterministic seed based on input
        noise = 0.01 * np.sum(np.random.rand() * x**2)
        
        return basin_term + grid_minima + noise