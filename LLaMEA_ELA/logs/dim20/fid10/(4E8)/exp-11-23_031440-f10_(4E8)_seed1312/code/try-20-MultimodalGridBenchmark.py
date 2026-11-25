import numpy as np

class MultimodalGridBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Convert to numpy array and ensure correct shape
        x = np.array(x)
        
        # Robust quadratic basin term with exponential scaling
        basin_term = 0.01 * np.sum(np.exp(0.5 * x**2))
        
        # Enhanced grid of global minima with exponential interaction terms
        grid_minima = 0.0
        for i in range(self.dim):
            # Exponentially increasing frequency sinusoidal components
            freq1 = 2 ** (i % 3 + 1)
            freq2 = 3 ** (i % 2 + 1)
            grid_minima += np.sin(freq1 * np.pi * x[i] / 2.0) * np.cos(freq2 * np.pi * x[i] / 1.5)
            
        # Cross-dimensional interaction terms with exponential weights
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term += np.exp(-0.1 * (x[i] - x[j])**2) * np.sin(3 * np.pi * (x[i] + x[j]))
        
        # Add a deterministic noise term based on input magnitude
        noise = 0.05 * np.sum(np.sin(x)**2 + np.cos(x)**2)
        
        # Combine all terms with different scaling factors
        return basin_term + 2.0 * grid_minima + 0.5 * cross_term + noise