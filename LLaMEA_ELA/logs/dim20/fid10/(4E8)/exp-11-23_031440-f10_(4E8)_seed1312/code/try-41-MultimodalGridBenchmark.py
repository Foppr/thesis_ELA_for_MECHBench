import numpy as np

class MultimodalGridBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Convert to numpy array and ensure correct shape
        x = np.array(x)
        
        # Quadratic basin term - encourages convergence to origin
        basin_term = 0.1 * np.sum(x**2)
        
        # Grid of global minima terms with enhanced exponential decay and polynomial interactions
        grid_minima = 0.0
        for i in range(self.dim):
            # Enhanced multimodal term with exponential decay and polynomial interaction
            grid_minima += np.exp(-0.5 * x[i]**2) * (np.sin(3 * np.pi * x[i] / 2.5) * np.cos(3 * np.pi * x[i] / 1.2) + 
                                                     0.5 * np.sin(6 * np.pi * x[i] / 2.5) * np.cos(6 * np.pi * x[i] / 1.2))
            
        # Add a small random noise term to make it more challenging (deterministic for reproducibility)
        np.random.seed(hash(str(x)) % (2**32))  # Deterministic seed based on input
        noise = 0.01 * np.sum(np.random.rand() * x**2)
        
        return basin_term + grid_minima + noise