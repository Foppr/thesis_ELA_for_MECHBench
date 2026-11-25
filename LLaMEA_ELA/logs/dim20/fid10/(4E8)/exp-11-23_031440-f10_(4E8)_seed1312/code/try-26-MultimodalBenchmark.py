import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range for better conditioning
        x_normalized = x / 5.0
        
        # Quadratic base term
        f1 = np.sum(x_normalized**2)
        
        # Cosine terms with multiple frequencies to create multiple local minima
        f2 = np.sum(np.cos(2 * np.pi * x_normalized) + 0.5 * np.cos(4 * np.pi * x_normalized))
        
        # Higher-order polynomial terms for increased complexity
        f3 = 0.1 * np.sum(x_normalized**4)
        f4 = 0.05 * np.sum(x_normalized**6)
        
        # Interaction terms between dimensions to increase conditioning difficulty
        interaction = 0.01 * np.sum(x_normalized[:-1] * x_normalized[1:])
        
        # Combine all terms with carefully chosen weights
        return f1 + 0.8 * f2 + f3 + f4 + interaction