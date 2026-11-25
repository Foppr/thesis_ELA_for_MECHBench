import numpy as np

class MultimodalRidgeBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        result = 0.1 * np.sum(x**2)
        
        # Add sinusoidal wells with varying frequencies and amplitudes
        for i in range(self.dim):
            # Create periodic wells along each dimension
            well_depth = 2.0 * np.sin(0.5 * x[i]) + 1.5 * np.cos(0.3 * x[i])
            result += 0.5 * (x[i] - well_depth)**2
        
        # Add Gaussian ridges that create high-dimensional valleys and peaks
        ridge_amplitude = 1.0
        for i in range(0, self.dim, 2):
            if i + 1 < self.dim:
                # Create 2D Gaussian ridges
                x1, x2 = x[i], x[i+1]
                ridge_x = 2.0 * np.sin(0.4 * x1) * np.cos(0.3 * x2)
                ridge_y = 2.0 * np.cos(0.4 * x1) * np.sin(0.3 * x2)
                dist = np.sqrt((x1 - ridge_x)**2 + (x2 - ridge_y)**2)
                result += ridge_amplitude * np.exp(-dist**2 / (2 * 0.5**2))
        
        # Add higher-order polynomial terms for increased complexity
        for i in range(self.dim):
            result += 0.2 * x[i]**6 - 1.2 * x[i]**4 + 1.8 * x[i]**2
        
        # Add noise component to increase ruggedness
        noise = 0.1 * np.sum(np.sin(5 * x) * np.cos(3 * x))
        
        return result + noise