import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_normalized = x / 5.0
        
        # Radial component with polynomial oscillations
        r = np.sqrt(np.sum(x_normalized**2))
        
        # Polynomial terms with varying degrees
        poly_term = np.sum((x_normalized**4 + 0.5 * x_normalized**3 + 0.1 * x_normalized**2) / self.dim)
        
        # Radial oscillation component
        radial_osc = np.sin(10 * np.pi * r) * np.cos(5 * np.pi * r)
        
        # Angular component with multiple local minima
        angular_term = 0.0
        for i in range(self.dim):
            angular_term += np.sin((i + 1) * np.arctan2(x_normalized[i], x_normalized[(i + 1) % self.dim]))
        
        # Combine components
        result = poly_term + 0.5 * radial_osc + 0.3 * angular_term
        
        # Add small noise for non-convexity
        noise = 0.01 * np.random.random()
        
        return result + noise