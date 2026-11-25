import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_normalized = x / 5.0
        
        # Sum of quadratic terms with different scales
        f1 = np.sum(x_normalized**2)
        
        # Add sinusoidal perturbations to create multiple local minima
        f2 = 0.2 * np.sum(np.sin(8 * np.pi * x_normalized) ** 2)
        
        # Add a global scaling factor to control the function landscape
        f3 = 0.03 * np.sum(x_normalized**4)
        
        # Add higher-order nonlinear terms for increased complexity
        f4 = 0.06 * np.sum(np.cos(4 * np.pi * x_normalized) ** 2)
        
        # Add interaction term between dimensions to increase complexity
        f5 = 0.01 * np.sum(x_normalized[:-1] * x_normalized[1:])
        
        return f1 + f2 + f3 + f4 + f5