import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range for better conditioning
        x_normalized = x / 5.0
        
        # Sum of quadratic terms (central quadratic basin)
        quadratic_term = np.sum(x_normalized**2)
        
        # High-frequency sinusoidal oscillations with exponential growth
        sinusoidal_term = 0.0
        for i in range(self.dim):
            frequency = 2 ** (i + 1) * np.pi
            sinusoidal_term += np.sin(frequency * x_normalized[i]) ** 2
        
        # Product of all dimensions with exponentially increasing penalty
        product_term = 1.0
        for i in range(self.dim):
            product_term *= (x_normalized[i] ** 2 + 0.1 * (i + 1))
        
        # Chaotic cubic interaction terms with alternating signs
        cubic_term = 0.0
        for i in range(self.dim):
            cubic_term += ((-1) ** i) * x_normalized[i] ** 3
        
        # Additional chaotic barrier term based on sum of squared normalized values
        barrier_term = np.exp(0.5 * np.sum(x_normalized**2)) - 1.0
        
        # Combine all terms with carefully tuned weights
        return 10 * quadratic_term + 15 * sinusoidal_term + 0.2 * product_term + 0.7 * cubic_term + 2.0 * barrier_term