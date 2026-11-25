import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range for better conditioning
        x_normalized = x / 5.0
        
        # Base quadratic term with modified scaling
        term1 = np.sum(x_normalized**2)
        
        # Enhanced sinusoidal components with multiple frequencies
        term2 = 0.2 * np.sum(np.sin(3 * np.pi * x_normalized) + 0.5 * np.sin(7 * np.pi * x_normalized))
        
        # Higher-order polynomial term to create sharper optima
        term3 = 0.02 * np.sum(x_normalized**6)
        
        # Additional sinusoidal component with varying amplitude
        term4 = 0.15 * np.sum(np.sin(9 * np.pi * x_normalized**2))
        
        # Combine all terms to create a challenging landscape
        return term1 + term2 + term3 + term4