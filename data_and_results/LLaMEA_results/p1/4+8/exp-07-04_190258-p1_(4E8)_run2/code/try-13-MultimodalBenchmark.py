import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Main quadratic term
        f_val = np.sum(x**2)
        
        # Add multiple local minima using rotated sinusoidal terms
        for i in range(self.dim):
            # Use a rotation matrix to create directional dependencies
            rotated_x = x[i] * np.cos(0.5 * i) - x[(i+1) % self.dim] * np.sin(0.5 * i)
            f_val += 0.2 * np.sin(3 * rotated_x) * np.cos(2 * rotated_x)
            
        # Add additional local minima with different scales and phases
        for i in range(self.dim):
            f_val += 0.1 * np.sin(7 * x[i]) * np.sin(4 * x[i]) * np.cos(2 * x[i])
            
        # Add a more complex deceptive basin term
        basin_term = 0.05 * np.sum(np.sin(0.3 * x)**4)
        f_val += basin_term
        
        # Add a small noise term to make it more challenging
        f_val += 0.005 * np.random.random()
        
        return f_val