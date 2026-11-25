import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_normalized = x / 5.0
        
        # Quadratic term for conditioning
        quadratic_term = np.sum(x_normalized**2)
        
        # Multiple sinusoidal terms with different frequencies and amplitudes
        sinusoidal_term = np.sum(np.sin(10 * np.pi * x_normalized)**2 + 
                                0.5 * np.sin(20 * np.pi * x_normalized)**2)
        
        # Higher-order polynomial interactions to increase complexity
        interaction_term = np.sum((x_normalized**4 + 0.1 * x_normalized**3 + 
                                 0.01 * x_normalized**2) ** 2)
        
        # Product of all dimensions with sinusoidal modulation
        product_term = np.prod(np.sin(np.pi * x_normalized))
        
        # Combine terms with adaptive weights based on dimensionality
        weight1, weight2, weight3, weight4 = 1.0, 0.3, 0.1, 0.05
        
        return weight1 * quadratic_term + weight2 * sinusoidal_term + \
               weight3 * interaction_term + weight4 * product_term