import numpy as np

class MultimodalGridBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_minima = []
        # Generate grid of global minima
        for i in range(-2, 3):
            for j in range(-2, 3):
                if i != 0 or j != 0:  # Exclude center point
                    self.global_minima.append([i, j])
        
    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Dimension mismatch")
        
        # Base quadratic term
        result = np.sum(x**2)
        
        # Add multiple global minima with different scales
        for i in range(0, min(self.dim, 10)):
            xi = x[i] if i < len(x) else 0
            # Add periodic terms that create multiple local minima
            result += 0.1 * np.sin(5 * xi) * np.cos(3 * xi)
            
        # Add grid of global minima
        for i in range(0, min(self.dim, 10), 2):
            if i + 1 < len(x):
                xi = x[i]
                yi = x[i + 1]
                # Create attractive points at grid locations
                grid_term = 0.5 * ((xi - np.round(xi))**2 + (yi - np.round(yi))**2)
                result += grid_term
                
        return result