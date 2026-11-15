import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Quadratic base with conditioning
        quadratic = np.sum(x_norm**2)
        
        # Multiple local minima with higher frequency trigonometric terms
        trigonometric = np.sum(np.sin(10 * np.pi * x_norm)**2)
        
        # Enhanced multimodal component with mixed polynomial and exponential terms
        polynomial_exp = np.sum((x_norm**6 - 3 * x_norm**4 + 3 * x_norm**2 - 1) * np.exp(-0.3 * x_norm**2))
        
        # Additional challenging landscape with asymmetric scaling
        asymmetric = np.sum(np.cos(3 * np.pi * x_norm) * np.exp(-0.1 * x_norm**2))
        
        # Combine all components with adjusted weights for better conditioning
        return 0.8 * quadratic + 0.2 * trigonometric + 0.05 * polynomial_exp + 0.1 * asymmetric