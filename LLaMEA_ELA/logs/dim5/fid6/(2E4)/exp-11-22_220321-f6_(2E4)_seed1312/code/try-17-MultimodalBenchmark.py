import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Global minimum at origin
        result = 0.0
        
        # Sum of quadratic terms with different scales
        for i in range(self.dim):
            result += (x[i] ** 2) * (i + 1)
            
        # Add multiple local minima using sine waves with exponentially increasing frequencies
        for i in range(self.dim):
            freq = 3 ** (i % 3)  # Changed from 2 to 3 for different frequency progression
            result += 0.3 * np.sin(freq * x[i]) * np.cos(freq * x[(i + 1) % self.dim])
            
        # Add a complex penalty term with multiple local optima
        penalty = 0.0
        for i in range(self.dim):
            # Increased polynomial order and changed coefficients
            penalty += (x[i] ** 8 + x[i] ** 5 + x[i] ** 3) * (i + 1)
            
        # Add enhanced cross-dimensional interactions
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Increased interaction strength and added a new nonlinear component
                cross_term += np.sin(x[i]) * np.cos(x[j]) * (i + j) * np.exp(-0.1 * abs(x[i] - x[j]))
                
        return result + 0.08 * penalty + 0.15 * cross_term