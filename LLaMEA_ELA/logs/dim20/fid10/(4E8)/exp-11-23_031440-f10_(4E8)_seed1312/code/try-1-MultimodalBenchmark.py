import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range for better conditioning
        x_normalized = x / 5.0
        
        # Sum of squared terms with different frequencies
        f1 = np.sum(x_normalized**2)
        
        # Sum of cosine terms with different frequencies to create multiple local minima
        f2 = np.sum(np.cos(2 * np.pi * x_normalized))
        
        # Additional quadratic term to make the landscape more complex
        f3 = 0.1 * np.sum(x_normalized**4)
        
        # Combine terms to create a challenging multimodal function
        return f1 + 0.5 * f2 + f3