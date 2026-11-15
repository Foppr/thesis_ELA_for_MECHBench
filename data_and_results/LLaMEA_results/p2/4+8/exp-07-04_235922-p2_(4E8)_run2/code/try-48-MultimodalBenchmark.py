import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Add radial basis function terms with varying widths and heights
        for i in range(self.dim):
            xi = x[i]
            result += 2.0 * np.exp(-0.5 * (xi - 1.0)**2) + 1.5 * np.exp(-0.3 * (xi + 2.0)**2) + 0.8 * np.exp(-0.7 * xi**2)
        
        # Add quaternion-inspired coupling terms for rotational symmetry
        sum_squares = np.sum(x**2)
        if sum_squares > 0:
            # Add coupling based on angle between variables (simplified quaternion-like)
            for i in range(self.dim):
                for j in range(i+1, self.dim):
                    # Angle-like coupling term
                    coupling = np.sin(2.0 * np.arctan2(x[j], x[i])) * np.exp(-0.1 * (x[i]**2 + x[j]**2))
                    result += 0.3 * coupling
        
        # Add nested minima structure with exponential decay
        result += 0.5 * np.exp(-0.2 * sum_squares) * np.sin(3.0 * sum_squares)
        
        # Add noise to make it more challenging
        result += 0.02 * np.random.random()
        
        return result