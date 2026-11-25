import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_normalized = x / 5.0
        
        # Quadratic basin term - central attraction to origin
        quadratic_term = np.sum(x_normalized**2)
        
        # Sinusoidal oscillations with exponential decay based on distance from origin
        distance_from_origin = np.sqrt(np.sum(x_normalized**2))
        oscillation_term = np.sum(np.sin(10 * np.pi * x_normalized) * np.exp(-distance_from_origin))
        
        # Additional higher-order polynomial term for increased complexity
        high_order_term = 0.1 * np.sum(x_normalized**6)
        
        # Combine all terms to create the final function value
        return quadratic_term + 0.3 * oscillation_term + high_order_term